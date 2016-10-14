#!/usr/bin/python
#
# Script to delete all FbW ACC accounts that start with agentId of I######## or I#########
# So that we don't have cruft in production.
#
from dlkit_runtime import PROXY_SESSION, RUNTIME
from dlkit_runtime.primitives import Id
from dlkit_runtime.proxy_example import TestRequest

FBW_ACC_SCHOOL_NODE = 'assessment.Bank%3A57279fc2e7dde08807231e61%40bazzim.MIT.EDU'

TERM_GENUS = 'assessment-bank-genus%3Afbw-term%40ODL.MIT.EDU'

# -------------


class RemoveINumbers(object):
    def __init__(self):
        test_request = TestRequest(username='cjshaw@mit.edu', authenticated=True)
        condition = PROXY_SESSION.get_proxy_condition()
        condition.set_http_request(test_request)
        proxy = PROXY_SESSION.get_proxy(condition)
        self.am = RUNTIME.get_service_manager('ASSESSMENT', proxy=proxy)

    @staticmethod
    def _agent_id_is_i_number(taking_agent_id):
        identifier = taking_agent_id.identifier
        if '@' in identifier:
            identifier = identifier.split('@')[0]
        return identifier[0].lower() == 'i' and (len(identifier) == 9 or len(identifier) == 10)

    def _extract_terms(self, node):
        terms = []
        for child_node in node.get_child_bank_nodes():
            bank = child_node.get_bank()
            if str(bank.genus_type) == TERM_GENUS:
                terms.append(bank)
            terms += self._extract_terms(child_node)
        return terms

    def _is_i_number_taken(self, taken):
        return self._agent_id_is_i_number(taken.get_taking_agent_id())

    def execute(self):
        # first, find all the children "terms" of the school node
        # should be 3 levels deep: school -> department -> subject -> term
        node = self.am.get_bank_nodes(Id(FBW_ACC_SCHOOL_NODE), 0, 3, False)
        terms = self._extract_terms(node)
        num_deleted = 0
        # second, for each term, find all of its assessments
        for term in terms:
            # we want the "services" version of the bank
            bank = self.am.get_bank(term.ident)
            for assessment in bank.get_assessments():
                # third, for each assessment, find all takens
                for taken in bank.get_assessments_taken_for_assessment(assessment.ident):
                    # if the agentId is an I-number, delete the taken
                    if self._is_i_number_taken(taken):
                        print "Deleting taken for I-number {0} in assessment {1}".format(taken.get_taking_agent_id().identifier,
                                                                                         assessment.display_name.text)
                        bank.delete_assessment_taken(taken.ident)
                        num_deleted += 1
        return num_deleted

#-----------------------------------------------------------------------------

if __name__=='__main__':
    try:
        cleaner = RemoveINumbers()
        num_deleted = cleaner.execute()
    except:
        # http://stackoverflow.com/questions/1000900/how-to-keep-a-python-script-output-window-open#1000968
        import sys, traceback
        print sys.exc_info()[0]
        print traceback.format_exc()
    finally:
        print "Done! Deleted {0} records.".format(num_deleted)

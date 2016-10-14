def impl_key_dict(value, priority=1):
    """to reduce duplicate code in configs.py and handcar_configs.py"""
    return {
        'syntax': 'STRING',
        'displayName': 'Implementation Key',
        'description': 'Implementation key used by Runtime for class loading',
        'values': [
            {'value': value, 'priority': priority}
        ]
    }

###################################################
# PRODUCTION SETTINGS
###################################################

MONGO_1 = {
    'id': 'mongo_configuration_1',
    'displayName': 'Mongo Configuration',
    'description': 'Configuration for Mongo Implementation',
    'parameters': {
        'implKey': impl_key_dict('mongo'),
        'mongoDBNamePrefix': {
            'syntax': 'STRING',
            'displayName': 'Mongo DB Name Prefix',
            'description': 'Prefix for naming mongo databases.',
            'values': [
                {'value': '', 'priority': 1}
            ]
        },
        'authority': {
            'syntax': 'STRING',
            'displayName': 'Mongo Authority',
            'description': 'Authority.',
            'values': [
                {'value': 'bazzim.MIT.EDU', 'priority': 1}
            ]
        },
        'indexes': {
            'syntax': 'OBJECT',
            'displayName': 'Mongo DB Indexes',
            'description': 'Indexes to set in MongoDB',
            'values': [
                {'value': {}, 'priority': 1}
            ]
        },
        'keywordFields': {
            'syntax': 'OBJECT',
            'displayName': 'Keyword Fields',
            'description': 'Text fields to include in keyword queries',
            'values': [
                {'value': {}, 'priority': 1}
            ]
        },
        'localImpl': {
            'syntax': 'STRING',
            'displayName': 'Implementation identifier for local service provider',
            'description': 'Implementation identifier for local service provider.  Typically the same identifier as the Mongo configuration',
            'values': [
                {'value': 'MONGO_1', 'priority': 1}
            ]
        },
        'recordsRegistry': {
            'syntax': 'STRING',
            'displayName': 'Python path to the extension records registry file',
            'description': 'dot-separated path to the extension records registry file',
            'values': [
                {'value': 'records.registry', 'priority': 1}
            ]
        },
    }
}

SERVICE = {
    'id': 'dlkit_runtime_bootstrap_configuration',
    'displayName': 'DLKit Runtime Bootstrap Configuration',
    'description': 'Bootstrap Configuration for DLKit Runtime',
    'parameters': {
        'implKey': impl_key_dict('service'),
        'assessmentProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Provider Implementation',
            'description': 'Implementation for assessment service provider',
            'values': [
                {'value': 'MONGO_1', 'priority': 1}
            ]
        },
        'assessment_authoringProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Assessment Authoring Provider Implementation',
            'description': 'Implementation for assessment authoring service provider',
            'values': [
                {'value': 'MONGO_1', 'priority': 1}
            ]
        },
        'authorizationProviderImpl': {
            'syntax': 'STRING',
            'displayName': 'Authorization Provider Implementation',
            'description': 'Implementation for authorization service provider',
            'values': [
                {'value': 'MONGO_1', 'priority': 1}
            ]
        },
    }
}

BOOTSTRAP = {
    'id': 'bootstrap_configuration',
    'displayName': 'BootStrap Configuration',
    'description': 'Configuration for Bootstrapping',
    'parameters': {
        'implKey': impl_key_dict('service'),
    }
}

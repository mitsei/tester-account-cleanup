
MANAGER_PATHS = {

    'service': {
        'ASSESSMENT': ('dlkit.services.assessment.AssessmentManager',
                       'dlkit.services.assessment.AssessmentManager'),
        'ASSESSMENT_AUTHORING': ('dlkit.services.assessment_authoring.AssessmentAuthoringManager',
                                 'dlkit.services.assessment_authoring.AssessmentAuthoringManager'),
        'AUTHORIZATION': ('dlkit.services.authorization.AuthorizationManager',
                          'dlkit.services.authorization.AuthorizationManager'),
        'REPOSITORY': ('dlkit.services.repository.RepositoryManager',
                       'dlkit.services.repository.RepositoryManager'),
        'LEARNING': ('dlkit.services.learning.LearningManager',
                     'dlkit.services.learning.LearningManager'),
        'LOGGING': ('dlkit.services.logging_.LoggingManager',
                    'dlkit.services.logging_.LoggingManager'),
        'COMMENTING': ('dlkit.services.commenting.CommentingManager',
                       'dlkit.services.commenting.CommentingManager'),
        'RESOURCE': ('dlkit.services.resource.ResourceManager',
                     'dlkit.services.resource.ResourceManager'),
        'GRADING': ('dlkit.services.grading.GradingManager',
                    'dlkit.services.grading.GradingManager')
    },
    'mongo': {
        'ASSESSMENT': ('dlkit.mongo.assessment.managers.AssessmentManager',
                       'dlkit.mongo.assessment.managers.AssessmentProxyManager'),
        'ASSESSMENT_AUTHORING': ('dlkit.mongo.assessment_authoring.managers.AssessmentAuthoringManager',
                                 'dlkit.mongo.assessment_authoring.managers.AssessmentAuthoringProxyManager'),
        'AUTHORIZATION': ('dlkit.mongo.authorization.managers.AuthorizationManager',
                          'dlkit.mongo.authorization.managers.AuthorizationProxyManager'),
        'REPOSITORY': ('dlkit.mongo.repository.managers.RepositoryManager',
                       'dlkit.mongo.repository.managers.RepositoryProxyManager'),
        'LEARNING': ('dlkit.mongo.learning.managers.LearningManager',
                     'dlkit.mongo.learning.managers.LearningProxyManager'),
        'LOGGING': ('dlkit.mongo.logging_.managers.LoggingManager',
                    'dlkit.mongo.logging_.managers.LoggingProxyManager'),
        'COMMENTING': ('dlkit.mongo.commenting.managers.CommentingManager',
                       'dlkit.mongo.commenting.managers.CommentingProxyManager'),
        'RESOURCE': ('dlkit.mongo.resource.managers.ResourceManager',
                     'dlkit.mongo.resource.managers.ResourceProxyManager'),
        'GRADING': ('dlkit.mongo.grading.managers.GradingManager',
                     'dlkit.mongo.grading.managers.GradingProxyManager')
    },
}


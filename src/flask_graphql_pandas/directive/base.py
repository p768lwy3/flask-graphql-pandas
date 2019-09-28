

class BaseDirective():
    """Base class of directive to be called in the initialization step of GraphQLView,
    which make the directive is allowed in queries of GraphQL.
    """
    def __init__(self, directive: str = "_pandas"):
        pass

        
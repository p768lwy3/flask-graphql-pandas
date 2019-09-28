from .base import BaseBeforeware
from flask_graphql_pandas.language.parser import get_schema


class SchemaBeforeware(BaseBeforeware):
    def __init__(self, 
                 directive: str = "_pandas"):
                 
        self.directive = directive

    def set_schema(self, query):
        """Extract and save schema from GraphQL queries.
        
        Args:
            schema ([type]): [description]
        """
        self.schema = get_schema(query, self.directive)
    
    def get_schema(self) -> dict:
        """Get schema extracted from directive.
        
        Returns:
            dict: A json object of schema to transform the response.
        """
        return self.schema
    
    def resolve(self, **kwargs):
        self.get_schema()
    

from .base import BaseAfterware
from flask_graphql_pandas.execution.beforeware import SchemaBeforeware
from flask_graphql_pandas.utilities import transform

class TransformationAfterware(BaseAfterware):
    def __init__(self,
                 schema_beforeware: SchemaBeforeware):
        self.schema_beforeware = schema_beforeware
    
    def apply(self, 
              response: dict) -> dict:
        return transform(response, self.schema_beforeware.get_schema())

    def resolve(self, **kwargs):
        pass
    
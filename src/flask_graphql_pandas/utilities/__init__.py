"""Utilities of flask-graphql-pandas for transforming data in response.
"""


def transform(response : dict,
              schema   : dict) -> dict:
    """Apply transformation to the object of response with the given schema.
    
    Args:
        response (dict): A nested json object of response of GraphQL.
        schema (dict): A json object of schema to transform the response.
    
    Returns:
        dict: A json object of transformed object.
    """
    transformed = response
    return transformed

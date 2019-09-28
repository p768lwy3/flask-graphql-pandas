import sys
sys.path.append("..")

from flask import Flask
from src.flask_graphql_lodash.graphqlodashview import GraphQLodashView
from graphene import Field, Schema, String, ObjectType

data = {
    "hello": "world",
    "haha" : "wow"
}

class Template(ObjectType):
    key = String()
    value = String()

class Query(ObjectType):
    template = Field(lambda: Template, key = String(required = True))

    def resolve_template(parent, info, **kwargs):
        value = data.get(kwargs.get("key"))
        return Template(
            key = kwargs.get("key"),
            value = value
        )


schema = Schema(
    query = Query
)

app = Flask(__name__)
app.add_url_rule(
    "/graphqlodash", 
    view_func=GraphQLodashView.as_view(
        "graphql", 
        graphiql = True,
        schema   = schema))

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=False)
from flask import Flask
from flask_graphql import GraphQLView
from flask_grpahql_pandas import graphql_pandas
from graphql.type.definition import GraphQLArgument, GraphQLField, GraphQLNonNull, GraphQLObjectType
from graphql.type.scalars import GraphQLString
from graphql.type.schema import GraphQLSchema

def resolve_raises(*_):
    raise Exception("Throws!")

QueryRootType = GraphQLObjectType(
    name = "QueryRoot",
    fields = {
        "thrower": GraphQLField(GraphQLNonNull(GraphQLString), resolver=resolve_raises),
        'request': GraphQLField(GraphQLNonNull(GraphQLString),
                                resolver=lambda obj, info: info.context.args.get('q')),
        'context': GraphQLField(GraphQLNonNull(GraphQLString),
                                resolver=lambda obj, info: info.context),
        'test': GraphQLField(
            type=GraphQLString,
            args={
                'who': GraphQLArgument(GraphQLString)
            },
            resolver=lambda obj, info, who='World': 'Hello %s' % who
        )
    }
)

MutationRootType = GraphQLObjectType(
    name='MutationRoot',
    fields={
        'writeTest': GraphQLField(
            type=QueryRootType,
            resolver=lambda *_: QueryRootType
        )
    }
)

schema = GraphQLSchema(QueryRootType, MutationRootType)

def create_app(schema, path="/graphql", **kwargs):
    backend = None
    app = Flask(__name__)
    app.debug = True
    view_func = GraphQLView("graphql", schema=schema, backend=backend, **kwargs)
    app.add_url_rule(path, view_func=view_func)
    return app


if __name__ == "__main__":
    app = create_app(graphiql=True)
    app.run()

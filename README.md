# flask-graphql-pandas

Apply [pandas](https://pandas.pydata.org/pandas-docs/stable/) in GraphQL queries

## Table of contents

- [About Flask-GraphQL-Pandas](#about-flask-graphql-pandas)
- [Idea and Concept in Flask-GraphQL-Pandas](#idea-and-concept-in-flask-graphql-pandas)
- [API](#api)
- [Quickstart](#quickstart)
- [Example queries](#example-queries)

## About Flask-GraphQL-Pandas

GraphQL allows to get what you want exactly, but a complicated nested json.  

[`pandas`](https://pandas.pydata.org/pandas-docs/stable/) is the most famous data transformation framework in the world, with a rich and powerful api, and easy to use syntax.

So, what we can have if we can combine these two excited things?

## Idea and Concept in Flask-GraphQL-Pandas

Instead of modifying source code of [graphql-core](https://github.com/graphql-python/graphql-core), [graphene](https://github.com/graphql-python/graphene) and [flask-graphql](https://github.com/graphql-python/flask-graphql), I am planning to develop a decorator on [GraphQLView](https://github.com/graphql-python/flask-graphql/blob/master/flask_graphql/graphqlview.py) in `flask-graphql`, which will capture the schema of transformation from directive (default with `@_pandas`) of queries in GraphQL, and apply the changing of response after the queries return. These steps are called by `Beforeware` and `Afterware` respectively.

You can see what the process actually did in the below image:

## API

So, there will be several parts in Flask-GraphQL-Pandas:

1. `graphql_pandas`: Decorator on GraphQLView in `flask-graphql`, which will be initialized with arguments:
    1. beforeware (list, default by [SchemaBeforeware].): a list of beforeware.
    2. afterware (list, default by [TransformationAfterware].): a list of afterware.

2. `beforeware`: Class of beforeware, which is called before queries are executed by GraphQL Engine.

3. `afterware`: Class of afterware, which is called after responses of queries are returned.

## Quickstart

## Example queries

### _.groupby(level = 0).count()

```graphql
{
    genderStats: allPeople @_pandas(get: "people") {
        people @_(gropyBy: "gender", level: 0, operation: "count" )  {
            gender
        }
    }
}
```

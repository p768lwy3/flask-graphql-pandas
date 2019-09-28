# flask-graphql-pandas

Apply [pandas](https://pandas.pydata.org/pandas-docs/stable/) in GraphQL queries

## Table of contents

- [About Flask-GraphQL-Pandas](#about-flask-graphql-pandas)
- [Example queries](#example-queries)
- [API](#api)

## About Flask-GraphQL-Pandas

GraphQL allows to get what you want exactly, but a complicated nested json.  

[`pandas`](https://pandas.pydata.org/pandas-docs/stable/) is the most famous data transformation framework in the world, with a rich and powerful api, and easy to use syntax.

So, what we can have if we can combine these two excited things?

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

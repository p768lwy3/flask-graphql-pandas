from flask import Response, request
from flask_graphql import GraphQLView
from functools import partial
from graphql_server import (HttpQueryError, default_format_error,
                            encode_execution_results, json_encode,
                            load_json_body, run_http_query)

"""

#. Idea:

##. develop a decorator `@graphql_pandas`, which is used at `GraphQLView` to initialize 
    flask-graphql-pandas features, instead of build a new class `GraphQLPandasView`.

"""


class GraphQPandasView(GraphQLView):
    afterware  = None
    beforeware = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key in ["afterware"]:
                setattr(self, key, value)

        super(GraphQPandasView, self).__init__(**kwargs)
    
    def dispatch_request(self):
        try:
            request_method = request.method.lower()
            data = self.parse_body()

            """

            #. Add beforeware here to parse the data into schema-like
            -> Extract a dictionary from directive `@pandasOp(...)`.

            """

            # print("data: ", data)
            # data:  {'query': '{\n  template(key: "hello"){\n    key\n    value\n  }\n}', 'variables': None, 'operationName': None}


            # parse data from the afterware directive 
            # to a query object and a schema to apply the afterware transformation

            show_graphiql = request_method == 'get' and self.should_display_graphiql()
            catch = show_graphiql

            pretty = self.pretty or show_graphiql or request.args.get('pretty')

            extra_options = {}
            executor = self.get_executor()
            if executor:
                # We only include it optionally since
                # executor is not a valid argument in all backends
                extra_options['executor'] = executor

            execution_results, all_params = run_http_query(
                self.schema,
                request_method,
                data,
                query_data=request.args,
                batch_enabled=self.batch,
                catch=catch,
                backend=self.get_backend(),

                # Execute options
                root=self.get_root_value(),
                context=self.get_context(),
                middleware=self.get_middleware(),
                **extra_options
            )

            result, status_code = encode_execution_results(
                execution_results,
                is_batch=isinstance(data, list),
                format_error=self.format_error,
                encode=partial(self.encode, pretty=pretty)
            )

            """
            
            #. Add a list of afterware here to apply the schema on the result
            
            """
            
            # print("result: ", result)
            # result:  {"data":{"template":null}}

            # then apply the transformation of afterware to the result of the schema

            if show_graphiql:
                return self.render_graphiql(
                    params=all_params[0],
                    result=result
                )

            return Response(
                result,
                status=status_code,
                content_type='application/json'
            )

        except HttpQueryError as e:
            return Response(
                self.encode({
                    'errors': [self.format_error(e)]
                }),
                status=e.status_code,
                headers=e.headers,
                content_type='application/json'
            )
            
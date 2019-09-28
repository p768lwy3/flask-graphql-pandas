r"""Parser to parse directives from GraphQL query at the beginning of request,
and extract the transformation of response from the directives, which would be appied 
on the data of response at the end after query from data source.
"""

from graphql.language import source
from graphql.language import parser


class DirectiveParser(object):
    """Parser to parse directive from graphQL query to a transformation schema, 
    which is a python dictionary (planning).
    """
    def _parse_recursive(self, field):
        if field.selection_set is not None:
            for f in field.selection_set.selections:
                yield from self._parse_recursive(f)
        if len(field.directives) > 0:
            yield field
    
    def parse(self, field, afterware_directive):
        parsed_object = dict()
        for f in self._parse_recursive(field):
            for d in f.directives:
                if d.name.value == afterware_directive:
                    parsed_object[f.name.value] = d.arguments
        return parsed_object


# string = '{\n  template(key: "hello") @_(keyBy: "values") {\n    key @format(as :".4f") @_(to: "float")\n    value\n  }\n}'
# s = source.Source(body=string)
# p = parser.parse(s)
# d = p.definitions

# parser = DirectiveParser()
# for doc in d:
#     parsed_object = parser.parse(doc, "_")
#     print(parsed_object)

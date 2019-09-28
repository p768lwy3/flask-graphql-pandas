"""

# In Lodash,
# 
# var object = { 'a': [{ 'b': { 'c': 3 } }] };
# 
# _.get(object, 'a[0].b.c');
# // => 3
# 
# _.get(object, ['a', '0', 'b', 'c']);
# // => 3
# 
# _.get(object, 'a.b.c', 'default');
# // => 'default'


#. json => any type

#. _.get("(Index String)")(
    {"(String)":  <value>, "(String)": <value>, ...}
) =>  <indiced value>

"""
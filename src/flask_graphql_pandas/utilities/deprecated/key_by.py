"""
In lodash,

#. List of json => json of json

#. _.keyBy("(Key-String)")([
    {"(Key-String)": <key-value>, "(String)": <value>, "(String)": <value>, ...},
    {"(Key-String)": <key-value>, "(String)": <value>, "(String)": <value>, ...},
    ...
]) => {
    <key-value>: {"(String)": <value>, "(String)": <value>, ...}, 
    <key-value>: {"(String)": <value>, "(String)": <value>, ...}, 
    ...
}

#. _.keyBy("(Key-String)").mapValue("(Map-String)")([
    {"(Key-String)": <key-value>, "(Map-String)": <map-value>, ...},
    {"(Key-String)": <key-value>, "(Map-String)": <map-value>, ...},
    ...
]) =>  {
    <key-value>: <map-value>, 
    <key-value>: <map-value>,
    ...
}

"""


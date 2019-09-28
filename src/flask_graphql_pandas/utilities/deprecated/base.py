from copy import deepcopy
from typing import Dict, List, Tuple, Union

def key_delimiter(key_string : str, 
                  delimiter  : str =".") -> List[str]:
    return key_string.split(delimiter)

def nest_json_pop(json_obj  : dict, 
                  key_string: str) -> Tuple[str, dict]:
    # deepcopy input to prevent any changing of input
    json_obj = deepcopy(json_obj)

    # copy location of input to return
    pop_json_obj = json_obj
    
    # delimite key string into a list of key
    keys = key_delimiter(key_string)
    
    for key in keys[:-1]:
        json_obj = json_obj[key]
    
    pop_val = json_obj.pop(keys[-1])
    return pop_val, pop_json_obj

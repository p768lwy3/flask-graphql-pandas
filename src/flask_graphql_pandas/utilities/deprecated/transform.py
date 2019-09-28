"""

# In Lodash,
# 
# _.transform([2, 3, 4], function(result, n) {
#   result.push(n *= n);
#   return n % 2 == 0;
# }, []);
# // => [4, 9]
# 
# _.transform({ 'a': 1, 'b': 2, 'c': 1 }, function(result, value, key) {
#   (result[value] || (result[value] = [])).push(key);
# }, {});
# // => { '1': ['a', 'c'], '2': ['b'] }

# >> x = eval("lambda k, v: (str(v), str(k))")
# >> y = {"a": 1, "b": 2}
# >> y2 = dict(x(e) for e in y.items())
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 1, in <genexpr>
# TypeError: <lambda>() missing 1 required positional argument: 'v'
# >> y2 = dict(x(*e) for e in y.items())
# >> y2
# {'1': 'a', '2': 'b'}
# >> 
# x = eval("lambda k: str(k)")


"""
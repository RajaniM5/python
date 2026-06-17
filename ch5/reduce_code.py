# reduce() = apply a function to an iterable and reduce
#           performs function on first two elements

import functools
letters = ["H", "E", "L", "L", "O"]


word = functools.reduce(lambda x, y, :x + y, letters)
print(word)


import numpy as np

rng = np.random.default_rng()

single_int = rng.integers(low=0, high=10)
arr_1d = rng.integers(0, 10, size=5)
matrix_2d = rng.integers(0, 10, size=(3,4))

print(single_int)
print(arr_1d)
print(matrix_2d)

items = np.array(['apple', 'banana', 'cherry', 'date'])

pick_one = rng.choice(items)

print(pick_one)


def move_zeros(arr):
    return [i for i in arr if i != 0] + [0] * arr.count(0)


array = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]
print(move_zeros(array))

"""
First i tried with the sorted function, but then I got an error in the test, because other values has to be in the same order, 
So i came up with this solution
"""
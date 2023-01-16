import numpy as np
def rowwise_max(a):
    b = []
    for i in a:
        b.append(max(i))
    return b
def is_matrix(a):
    nasol = 0
    for i in range(len(a)-1):
        if len(a[i])!=len(a[i+1]):
            nasol = 1
    if nasol == 0:
        return True
    return False

def transpose(a):
    if is_matrix(a) == False:
        return ValueError
    b = np.array(a)
    transpusa = b.transpose()
    #print(transpusa)
    return transpusa
def columnwise_max(a):
    b = transpose(a)
    return rowwise_max(b)

def l2_distance(a,b):
    aa = np.array(a)
    bb = np.array(b)
    dist = np.linalg.norm(aa-bb)
    return dist


assert is_matrix([]) is True
assert is_matrix([[], []]) is True
assert is_matrix([[1, 2], [2, 1]]) is True
assert is_matrix([[1], [2, 1]]) is False
assert is_matrix([[1, 2], [2, 1], [3, 4]]) is True
assert is_matrix([[1, 2], [2, 1], [3, 4, 5]]) is False

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[1, 4], [2, 5], [3, 6]]

assert rowwise_max(
            [
                        [1, 2, 3],
                                [1, 4, 3],
                                        [1, 5, 3],
                                            ]
            ) == [3, 4, 5]

assert rowwise_max([list(range(1000))]) == [999]
assert rowwise_max(transpose([list(range(1000))])) == list(range(1000))


assert columnwise_max(
            [
                        [1, 2, 3],
                                [1, 4, 3],
                                        [1, 5, 3],
                                            ]
            ) == [1, 5, 3]

assert columnwise_max([list(range(1000))]) == list(range(1000))
assert columnwise_max(transpose([list(range(1000))])) == [999]
assert abs(l2_distance([1, 0], [1, 0]) - 0) < 1e-5
assert abs(l2_distance([1, 0], [0, 1]) - 2**0.5) < 1e-5

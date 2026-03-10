# import numpy as np

# #coefficient of matrix

# A = np.array([[1,1],
#                [2,3]], dtype=float)

# #Right hand side
# b = np.array([5,13], dtype=float)

# #Gauss elimination using numpy
# x=np.linalg.solve(A,b)

# print("Solution",x)


import numpy as np

#coefficient of matrix

A = np.array([[2,3,1],
               [4,1,2],
             [3,-2,1]], dtype=float)

#Right hand side
b = np.array([5,6,4], dtype=float)

#Gauss elimination using numpy
x=np.linalg.solve(A,b)

print("Solution",x)
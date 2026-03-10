# import numpy as np
# #coefficient matrix
# A=np.array([[-5,2],
#  [3,-4]], dtype=float)
# #right-hand side
# b=np.array([7,-8], dtype=float)
# import sympy as sp
# #create augmented matrix
# aug= sp.Matrix(np.hstack((A,b.reshape(-1,1))))
# #reduce to RREF
# rref_matrix, _ = aug.rref()
# print("RREF form:\n", rref_matrix)
# #extract solution
# solution = [rref_matrix[i, -1] for i in range(rref_matrix.rows)]
# print("Solution:", solution)





# import numpy as np
# #coefficient matrix
# A=np.array([[2,-3,1],
#  [-1,5,-2],
#  [3,1,4]], dtype=float)
# #right-hand side
# b=np.array([4,-3,10], dtype=float)
# import sympy as sp
# #create augmented matrix
# aug= sp.Matrix(np.hstack((A,b.reshape(-1,1))))
# #reduce to RREF
# rref_matrix, _ = aug.rref()
# print("RREF form:\n", rref_matrix)
# #extract solution
# solution = [rref_matrix[i, -1] for i in range(rref_matrix.rows)]
# print("Solution:", solution)




import numpy as np
#coefficient matrix
A=np.array([[2,-1,3,-1],
 [4,2,-1,2],
 [-2,1,5,-3],
 [3,-4,2,1]], dtype=float)
#right-hand side
b=np.array([5,6,-4,7], dtype=float)
import sympy as sp
#create augmented matrix
aug= sp.Matrix(np.hstack((A,b.reshape(-1,1))))
#reduce to RREF
rref_matrix, _ = aug.rref()
print("RREF form:\n", rref_matrix)
#extract solution
solution = [rref_matrix[i, -1] for i in range(rref_matrix.rows)]
print("Solution:", solution)

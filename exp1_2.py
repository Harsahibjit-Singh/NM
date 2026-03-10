# a=0.1
# b=0.2
# c=0.3
# result=(a+b)-c
# print(result)

# handling rounding off error - reducing round-off Error using Decimal

# from decimal import Decimal

# a=Decimal('0.1')
# b=Decimal('0.2')
# c=Decimal('0.3')

# result=(a+b)-c
# print(result)



# Propagation / Accumulation of Round-off Error

# sum_value=0.0
# for i in range(10):
#     sum_value+=0.1;
# print('Sum after adding 0.1 10 times= ',sum_value)
# print("Expected value = ",1.0)
# print ("Error =",sum_value-1.0)


# truncation error

# import math

# print("Truncation Error Demonstration")

# x=math.pi/6
# true_value=math.sin(x)

# print(true_value)


# #Taylor Series

# approx_value=x-(x**3)/math.factorial(3) + (x**5)/math.factorial(5) - (x**7)/math.factorial(7)


# print(f"Actual sin({x}) = {true_value}")
# print(f"Approximation with 4 terms: {approx_value}")
# print(f"Truncation error: {abs(true_value-approx_value)}")



# import math

# x=1;
# true_value=math.exp(x)

# approx_value=1 + x/1 + (x**2)/math.factorial(2) + (x**3)/math.factorial(3) + (x**4)/math.factorial(4)+ (x**5)/math.factorial(5)

# print(f"Actual exp({x}) = {true_value}")
# print(f"Approximation with 4 terms: {approx_value}")
# print(f"Truncation error: {abs(true_value-approx_value)}")




# to compute absolute error and relative error
# true_value = 3.14159
# approx_value = 3.14
# absolute_error = abs(true_value - approx_value)
# relative_error = absolute_error / abs(true_value)
# print(f"Absolute Error: {absolute_error}")
# print(f"Relative Error: {relative_error}")



# implementing bisection method to find root of a function

# def f(x):
#     return x**2 - 4
# def bisection_method(a, b, tol):
#     if f(a) * f(b) >= 0:
#         print("Bisection method fails.")
#         return None
    
#     iteration =1

#     print("Iter\t    a\t    b\t    c\t f(c)\t Error")
#     print("-"*80)

#     while (b - a) / 2.0 > tol:
#         c = (a + b) / 2.0
#         error = (b-a)/2.0
#         print(f"{iteration}\t {a:.6f}\t {b:.6f}\t {c:.6f}\t {f(c):.6f}\t {error:.6f}")
#         iteration += 1

#         if f(c) == 0:
#             return c
#         elif f(a) * f(c) < 0:
#             b = c
#         else:
#             a = c


#     return (a + b) / 2.0

# root = bisection_method(0, 3, 1e-3)
# print(f"Approximate root: {root}")


# find the root of f(x) = x^3 - x - 2 in the interval [1, 2] using the bisection method

def f(x):
    return x**3 - x - 2
def bisection_method(a, b, tol):
    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        return None
    
    iteration =1

    print("Iter\t    a\t            b\t            c\t            f(c)\t  Error")
    print("-"*85)

    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0
        error = (b-a)/2.0
        print(f"{iteration}\t {a:.6f}\t {b:.6f}\t {c:.6f}\t {f(c):.6f}\t {error:.6f}")
        iteration += 1

        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c


    return (a + b) / 2.0

root = bisection_method(1, 2, 1e-3)
print(f"Approximate root: {root}")


# # find the root of f(x) = e^{-x} - x  in the interval [0,1] using the bisection method

# import math
# def f(x):
#     return math.exp(-x) - x
# def bisection_method(a, b, tol):
#     if f(a) * f(b) >= 0:
#         print("Bisection method fails.")
#         return None
    
#     iteration =1

#     print("Iter\t a\t b\t c\t f(c)\t Error")
#     print("-"*75)

#     while (b - a) / 2.0 > tol:
#         c = (a + b) / 2.0
#         error = (b-a)/2.0
#         print(f"{iteration}\t {a:.6f}\t {b:.6f}\t {c:.6f}\t {f(c):.6f}\t {error:.6f}")
#         iteration += 1

#         if f(c) == 0:
#             return c
#         elif f(a) * f(c) < 0:
#             b = c
#         else:
#             a = c


#     return (a + b) / 2.0
# root = bisection_method(0, 1, 1e-3)
# print(f"Approximate root: {root}")
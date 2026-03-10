# #define function
# def f(x):
#   return x**3+x**2+3*x+4
# #define derivative
# def df(x):
#   return 3*x**2+2*x+3
# #newton raphson method with iteration table
# def newton_raphson(x0,tol,max_iter=100):
#   x=x0
#   print("Iter\t x_n\t\t f(x_n)\t\t Error ")
#   print("-"*50)
#   for i in range(1,max_iter+1):
#     x_new=x - f(x)/df(x)
#     error=abs(x_new - x)
#     print(f"{i}\t {x:.6f}\t {f(x):.6f}\t {error:.10f}")
#     if error<tol:
#       return x_new
#     x=x_new
#   return x
# root=newton_raphson(1,1e-5)
# print("\nApproximate root:",root)












# define function
def f(x):
    return x**3 - x - 1

# define derivative
def df(x):
    return 3*x**2 - 1

# Newton Raphson method with iteration table
def newton_raphson(x0, tol, max_iter=100):
    x = x0
    print("Iter\t x_n\t\t f(x_n)\t\t Error ")
    print("-" * 50)

    for i in range(1, max_iter + 1):
        x_new = x - f(x) / df(x)
        error = abs(x_new - x)

        print(f"{i}\t {x:.6f}\t {f(x):.6f}\t {error:.10f}")

        if error < tol:
            return x_new

        x = x_new

    return x

# initial guess and tolerance
root = newton_raphson(1, 1e-5)

print("\nApproximate root:", root)

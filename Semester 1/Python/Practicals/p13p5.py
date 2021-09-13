def f(x):
    """Function that adds 1 to its argument and prints it out"""
    print("In function f:")
    x += 1

    # y and p are locals, they do not affect
    # the global variables of the same name
    y = 1
    p = q + r

    # q and r, though, since they do not exist locally
    # are global references.

    # The result is that p is different in the function
    #  but unchanged outside it.
    
    print("x is", x)
    print("y is", y)
    print("z is", z)
    print("pqr", p, q, r)

    # Same with x, though that will be returned
    # and its value set to z
    return x

x, y, z = 5, 10, 15
p, q, r = 1, 2, 3

print("Before function f:")
print("x is", x)
print("y is", y)
print("z is", z)

print("pqr: ", p, q, r)

z = f(x)

print("After function f:")
print("x is", x)
print("y is", y)
print("z is", z)

print("pqr", p, q, r)
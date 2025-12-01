'''x = 98
print(x)
def fun():

    y = 99
    print(y)
    print(x)
    print(globals())
    print(locals())


fun()
print(x)'''

'''x = 88
print(x)
def fun():
    global x

    x = 84
    print(x)

fun()
print(x)'''

# def fact(n):
#     if n == 1:
#         return n
#     else:
#         return  n*fact(n-1)
# res = int(input("Enter your number\n"))
# print(fact(res))

# x = 10
# print(x)
# def fun():
#     global x
#     x = 20
#     print(x)

# fun()

# print(x)


# x = 10
# print(x)
# def fun():
#     global x
#     x = 20

#     print("Inner:", x)

# fun()
# print("Outer:",x)

# x = 5

# def fun():
#     print(globals())
#     print(locals())

#     x = 100
#     print("Inner:", x)

# fun()
# print("Outer:", x)


'''def outer():
    a = 50

    def inner():
        print(a)

    inner()

outer()'''


# def outer():
#     a = 30

#     def inner():
#         nonlocal a
#         a = 20
#         print(a)
#     inner()
#     print(a)

# outer()
 
# def outer():
#     x = 40

#     def inner():
#         nonlocal x
#         x = 20

#         print(x)
#     inner()

#     print(x)
# outer()

# x = lambda x : x*x
# print(x(5))
# x = (lambda x,y : x+y)(2,5)
# print(x)


# fun = (lambda x,y: x**y)
# res = fun(3,5)
# print(res)

# fun1 = fun(5,5)
# print(fun1)

# iranna = fun(10,2)
# print(iranna)

# from functools import reduce
lst = [2,3,4,5,6,7,89,10]
# def fun(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
# res = list(filter(fun,lst))
# print(res)

# fun = list(filter(lambda x : x % 2 != 0,lst))
# print(fun)

# def fun(a,b):
#     return a+b

# res = reduce(fun,lst)
# print(res)

# fun = reduce(lambda x,y : x*y,lst)
# print(fun)

# fun = reduce(lambda x,y : a+b, lst)
# print(fun)

# def fun(a):
#     return a*a

# res = list(map(fun,lst))
# print(res)


# fun = list(map(lambda x : x*x,lst))
# print(fun)

# def fun(num):
    # return lambda x : x*num

# res = fun(2)(5)
# print(res)

# fun2 = fun(5)
# res = fun2(4)
# print(res)

def fun(num):
    return lambda x : x*num

res = int(input("Enter your number\n"))

print(res)


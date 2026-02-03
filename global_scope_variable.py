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

# x = 99
# print(x)
# def fun():
    # print(globals())
    # global y
    # y = 999

    # print(x)
    # print(locals())

# fun()
# print(x)
# print(y)
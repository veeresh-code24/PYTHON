# def mul():
#     a = 10
#     b = 20
#     c = a*b
#     print(c)
# mul()

# def power_of(a, b):
#     c = a**b
#     print(c)
# power_of(2,5)
# power_of(2, 10)
# power_of(2)

# def add(a, b):
#     print(a+b)
# add(5,3)

# def mul(a, b):
#     b = a *b
#     return b
# print(mul(5,8))
# print(mul(2,8))
# print(mul(5,8))


# def info(name, age= 18, height= 7.2):
#     print(name)
#     print(age)
#     print(height)
# info("pacchu")

# def tea(abcd,cccc, *tea):
#     print(abcd)
#     print(tea)
#     print(cccc)
# tea("black", "lemon", "white")

# def info(**student):
#     a = sum(student.values())
#     return a
# x = info(b= 2,c= 3,d= 4,e= 5,f= 6,g= 7)
# print(x)

# def mui_action(a,b):
#     return a+b, a-b, a*b
# x, y,z = mui_action(2,5)
# print(x,y,z)


# def outer():
#     print("Outer function")

#     def inner():
#         print("inner function")

#     return inner

# s = outer()
# print(s)

# a = 10
# b = 20
# c = a+b
# print(c)
# print(id(c))

# def chech(a):
#     if a % 2 == 0:
#         print("even number")
# (chech(2))
# (chech(3))

def fun():
    a = 10
    b = 20 
    c = 30
    return a, b , c
print(fun())
# res1,res2, res3= fun()
# print(res1)
# print(res2)
# print(res3)





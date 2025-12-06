# def power_of(num,p):
#     return num ** p

# res = power_of(2,5)
# print(res)
# res1 = power_of(3,2)
# print(res1)

# Instead of using a def function we have to use lambda function in a short
 

# res = (lambda a,b : a**b)(3,3)
# print(res)

# fun = lambda  a,b : a*b
# res = fun(5*5)
# print(res)

# res1 = fun(5*10)
# print(res1)

# res = (lambda num,pow : num ** pow)(2,5)
# print(res)

# You can reuse the lamde function

# lbd= lambda a,b : a-b
# fun = lbd(2,5)
# print(fun)

# fun = lbd(10,2)
# print(fun)

# Filter(function, sequence)

# lst = [2,3,4,5,6,7,8,9,10]

# def fun(x):
#     if x%2 == 0:
#         return True
#     else:
#         return False
# even_lst = list(filter(fun, lst))
# print(even_lst)

# lst = [2,3,4,5,6,7,12,3,4]

# def fun(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
# res1 = list(filter(fun,lst))
# print(res1)

# result = list(filter(lambda x : x % 2 == 0, lst))
# print(result)

# Reduce funtion

# from functools import reduce
# lst = [12,3,4,5,6,7,8,9,10]

# def fun(x,y):
#     return x+y
# res = reduce(fun,lst)
# print(res)

# res = reduce(lambda x,y : x + y, lst)
# print(res)

# lst = [1,2,3,4,5,6,7,8,9,10]
# def fun(x):
#     return x ** 2
# res = list(map(fun, lst))
# print(res)

# res1 = set(map(lambda x : x**2 , lst))
# print(res1)

# how can i use lamda function in functions


# def mul(num):
#     return lambda x : num * x

# res = mul(5)(10)
# print(res)

# res1 = mul(6)
# res2 = res1(5)
# print(res2)

# x = (lambda x : x*x)(5)
# print(x)

# res1 = x(6)
# print(res1)

# def mul(num):
#     return lambda x : num * x
# result = mul(5)(5)
# print(result)

# result2 = mul(10)
# print(result2(10))


# def fun(num):
#     return lambda x : num * x
# math_table = fun(5)

# for i in range(1,11):
#     print("5 X" , i , "=", math_table((i)) )

# a = (lambda a,b : a+b)(2,5)
# print(a)

# fun = (lambda  a,b:a+b)
# res = fun(10,2)
# print(res)

# res1 = fun(100,2)
# print(res1)

# res2 = fun(100,100)
# print(res2)


# lst = [10,20,12,3,7,17,19,28]

# def call(x):
#     if x % 2 != 0:
#         return True
#     else:
#         return False
# even_lst = list(filter(call,lst))
# print(even_lst)

# even_lst = list(filter(lambda x : x%2!=0,lst))
# print(even_lst)

# from functools import reduce
lst = [10,20,12,3,7,17,19,28]


# def call(a,b):
#     return a+b

# res = reduce(call,lst)
# print(res)

# x = reduce(lambda x,y : x+y,lst)
# print(x)

def call(a):
    if a % 2 == 0:
        return True
    else:
        return False

res = list(map(call,lst))
print(res)
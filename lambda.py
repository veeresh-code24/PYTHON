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
# lst = [10,20,12,3,7,17,19,28]


# def call(a,b):
#     return a+b

# res = reduce(call,lst)
# print(res)

# x = reduce(lambda x,y : x+y,lst)
# print(x)

# fun = (lambda a,b : a**b)(2,3)
# print(fun)

# fun1 = (lambda x,y : x+y)(10,2)
# print(fun1)

'''fun = lambda x,y : x**y
res = fun(100,2)
print(res)

res1 = fun(10,2)
print(res1)

fun = lambda x,y : x/y
res2 = fun(100,50)
print(res2) 

res3 = fun(10,2)
print(res3)

lam = (lambda x,y : x**y)(2,10)
print(lam)'''


# lst = [10,2,2,3,1,23,77,32]

# def main(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
# evn_lst = list(filter(main,lst))
# print(evn_lst)

# evn_lst = list(filter(lambda x : x % 2 != 0, lst))
# print(evn_lst)

# age = [10,20,30,40,12,2,4,76,54,12,14,17,18]

# def main(x):
#     if x <= 18:
#         return True
#     else:
#         return False
# res = list(filter(main, age))
# print(res)

# res = list(filter(lambda x : True if x >= 18 else False , [2,4,6,8,98,76,54]))
# print(res)

# from functools import reduce
# lst = [1,1,3,1,5]
# def fun(x,y):
#     return x*y 

# res = reduce(fun, lst)
# print(res)

# res = reduce(lambda x,y : x * y, lst)
# print(res)

# lst = [1,2,3,4,5]
# def fun(x):
#     return x**2

# res = list(map(fun, lst))
# print(res)
# sq_lst = set(map(lambda x : x+2 , lst))
# print(sq_lst)


# students = [("Ram", 85), ("John", 90), ("Alex", 78)]

# names = list(map(lambda x: x[0], students))
# print(names)


# lst = [65, 45, 78]
# res  = list(map(lambda x : x + 5 , lst))
# print(res)

# lst1 = ['1','2','3','4']
# lst2 = [1,10,3,4]


# res = list(map(lambda x ,y : x +y , lst1 , lst2))
# print(res)

def main(num):
    return lambda x : x*num 

res1 = main(2)(5)
print(res1)

res2 = main(3)
print(res2(10))

res3 = main(100)
print(res3(10))




'''def fun1():
    print("inside fun1()")
fun1()
print(fun1)
fun2 = fun1
print(fun2)'''

# def alpha(ref):
#     print("Inside alpha")
#     ref()

# def beta():
#     print("Inside beta")
# alpha(beta)


# def iranna(pacchu):
#     print("inside a iranna")
#     pacchu()

# def veeresh():
#     print("inside veeresh")
# iranna(veeresh)

# def iranna():
#     print("hii")

# x = iranna
# x()

'''def get_sum(lst):
    print(sum(lst))

def sum_product(lst):
    p = 1
    for i in lst:
        p *= i
    print(p)

def fun(choice):
    if choice == "sum":
        return get_sum
    else:
        return sum_product
    
fun1 = fun("sum")
fun1([1,2,3,4,5])
fun2 = fun("kjdfk")
fun2([1,2,3,4,5,6])'''

# def get_sum(lst):
#     print(sum(lst))

# def get_product(lst):
#     p = 1
#     for i in lst:
#         p *= i
#     print(p)

# def fun(choice):
#     if choice == "sum":
#         return get_sum
#     else:
#         return get_product
# fun1 = fun("sum")
# fun1([10,20,30,40,50])

# def get_sum(lst):
#     print(sum(lst))

# def sum_product(lst):
#     p = 1
#     for i in lst:
#         p *= i
#     print(p)

# def fun(choice):
#     if choice == "sum":
#         return get_sum
#     else:
#         return sum_product
    
# fun1 = fun("sum")
# fun1([1,2,3,4,5])


# def outer():
#     print("inside outer")

#     def inner():
#         print("inside inner")
    
#     return inner()

# ine_ref = outer()

# def get_product(lst):
#     p = 1
#     for i in lst:
#         p *= i
#     print(p)
# get_product([10,20,30])
# get_product([10,0,30])

# def outer(ref):

#     def inner(lst):
#         if 0 in lst:
#             print('0 is present')
#         else:
#             ref(lst)
#     return inner

# def get_product(lst):
#     p = 1
#     for i in lst:
#         p *= i
#     print(p)

# modified_get_product = outer(get_product)
# modified_get_product([10,20,30])
# modified_get_product([10,0,30])

# def outer(ref):

#     def inner(lst):
#         if 0 in lst:
#             print("0 is present")
#         else:
#             ref(lst)

#     return inner
# @outer

# def get_product(lst):
#     p = 1
#     for i in lst:
#         p *= i
#     print(p)

# get_product([10,20,30])
# get_product([10,0,30])

# modi_iner = outer(get_product)
# modi_iner([10,20,30])
# modi_iner([10,0,30])

# def outer(ref):
    
#     def inner(a,b):
#         if b == 0:
#             print("Please provide a non zero number")
#         else:
#             ref(a,b)

#     return inner

# def div(a,b):
#     print(a/b)

# modi_inne = outer(div)
# modi_inne(10,5)
# modi_inne(10,0)

# def fun1():
#     print("inside fun1")

# fun1()
# print(fun1)
# fun2 = fun1
# print(fun2)

# def outer(ref):
#     print("inside outer")

#     ref()
#     return outer

# def inner():
#             print("inside inner")
# modi_outer = outer(inner)

'''def get_sum(lst):
    print(sum(lst))


def get_product(lst):
    p = 1
    for i in lst:
        p *= i
    print(p)

def fun(choice):
    if choice == 'sum':
        return get_sum
    else:
        return get_product
    
modi_fun = fun('sum')
modi_fun([1,2,3,4,5])

modi_fun = fun("egiud")
modi_fun([1,2,3,4,5,6,7,8,9])'''

# def outer(ref):

#     def wrapper(lst):
#         lst = list(map(lambda x : x**2, lst))
#         ref(lst)
#     return wrapper

# @outer

# def get_product(lst):
#     p = 1
#     for i in lst:
#         p *= i

#     print(p)

# get_product([1,2,3,4,5])

# mod_get_prod = outer(get_product)
# mod_get_prod([1,2,3,4,5])

# def decorator(num):

#     def power_of(ref):

#         def wrapper(lst):
#             lst = list(map(lambda x:x**num, lst))
#             ref(lst)

#         return wrapper
    
#     return power_of

# @decorator(3)

# def get_product(lst):
#     p = 1
#     for i in lst:
#         p *= i
#     print(p)

# get_product([1,2,3,4,5])

# mod_pow = decorator(3)
# mod_get_product = mod_pow(get_product)
# mod_get_product([1,2,3,4,5])

# a = 3 
# b = 4
# print(a+b)

# def outer():
#     x = 99

#     def inner():
#         print(x)

#     inner()

# outer()


# def decorators(num):

#     def power_of(ref):

#         def wrapper(lst):
#             lst = list(map(lambda x: x*num,lst))
#             ref(lst)

#         return wrapper

#     return power_of

# @decorators(3)

# def get_product(lst):
#     p = 1
#     for i in lst:
#         p *= i
#     print(p)

# get_product([1,2,3,4,5])

# mod_get_po = decorators(2)
# wrapp = mod_get_po(get_product)
# wrapp([1,2,3,4,5])

# def decorators(num):

#     def outer(ref):

#         def wrapper(lst):
#             lst = list(map(lambda x : x**num , lst))
#             ref(lst)

#         return wrapper
#     return outer

# @decorators(2)


# def get_product(lst):
#     p = 1
#     for i in lst:
#         p *= i
#     print(p)

# get_product([1,2,3,4,5])

# modifi_outer = decorators(3)
# modifieret_wrapper = modifi_outer (get_product)
# modifieret_wrapper([1,2,3,4,5])

# def outer():
#     x = 99

#     def inner():
#         print(x)

#     return inner

# x = outer()
# del outer
# x()

# def outer():
#     x = 99

#     def inner1():
#         y = 92

#         def inner2():
#             print(x)
#             print(y)

#         return inner2
#     return inner1

# mod_ret1 = outer()
# mod_ret2 = mod_ret1()
# mod_ret2()

# def outer():
#     x = 99

#     def inner1():
#         y = 88

#         def inner2():
#             print(x)
#             print(y)

#         return inner2
#     return inner1

# mod_inne1 = outer()
# mod_ret2 = mod_inne1()
# mod_ret2()
# del outer
# del mod_inne1
# mod_ret2()




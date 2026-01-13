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

def get_sum(lst):
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
modi_fun([1,2,3,4,5,6,7,8,9])




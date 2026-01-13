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


def outer():
    print("inside outer")

    def inner():
        print("inside inner")
    
    return inner()

ine_ref = outer()





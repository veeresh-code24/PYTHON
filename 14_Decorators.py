# def fun1():
#     print('Inside fun1()')

# fun1()
# print(fun1)
# fun2 = fun1
# print(fun2)


def alpha(ref):
    print('Inside alpha()')
    ref()

def beta():
    print('inside beta')

alpha(beta)

def beta(a, b):
    print(a + b)

def alpha(ref):
    ref(5, 3)

alpha(beta)

a = 10
b = 20
c =a+b
print(c)







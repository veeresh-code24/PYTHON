'''def mul():
    a = 10
    b = 20
    c = a+b
    print(c)
mul()

def mul(a,b):
    c = a*b
    print(c)
mul(10,20)

def mul():
    a = 10
    b = 20
    c = a*b
    return c
res = mul()
print(res)

# positional argument

def add(a,b):
    c = a*b
    return c
res = add(10,20)
print(res)'''

# default argument
'''def fun(a,b=2):
    d = a**b
    return d
res = fun(5,5)
print(res)'''

# keyword argument

'''def main(a,b):
    print(a,b)

main(b=10,a = 20)'''

# variable length argument 

'''def cricket(best,*name,extra_player):
    print(name)
    print(extra_player)
    print(best)

cricket('virat','dhoni','gill',extra_player='iranna')'''

# variable length keyword argument
'''def student_info(pacchu,**data):
    print(type(data))
    print(data)
    print(pacchu)

student_info('name',Name='iranna',age=21,weight= 58,iranna=24)'''

# def main(n):
#     if n % 2 == 0:
#         print('even number')
#     else:
#         print('odd number')

# main(10)
# main(7)

# def ret_mul(a,b):
#     c = a*b, a+b, a-b
#     return c

# a, b, c = ret_mul(10,20)
# print(a,b,c)

# def outer():
#     print('outer function')

#     def inner():
#         print('inner function')

#     inner()
# outer()

def fun3():
    print('ytre')
    fun2()

def fun2():
    print('gfhgjhk')
    fun1()

def fun1():
    print('dhfj')

fun3()

















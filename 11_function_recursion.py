# def mul():
#     a = 10
#     b = 20
#     c = a*b
#     print(c)
# mul()

# def add(a,b):
#     c = a+b
#     print(c)
# add(10,5)

# def quo():
#     a = 175
#     b = 500
#     c = a%b
#     return c
# res = quo()
# print(res)

# def pow(a):
#     c = a**a
#     return c
# res = pow(2)
# print(res)

# Defult argument

# def power_of(a,b=2):
#     c = a**b
#     print(c)
# x = (power_of(2,))
# print(x)

# Keyword argument

# def add(name, city,age):
#     print(name)
#     print(city)
#     print(age)
# add(city = "Bagalkot",name = "veeresh",age = 21)

'''def name(age,*name,nam="har"):
    print(type(name))
    print(age)
    print(name)
    print(nam)

name( 21,"iranna","pacchu","veeresh",nam="harish")

# last argument as anon defult is allow is not there


def stu_info(year,**data):
    print(type(data))
    print(year)
    print(data)

stu_info(2025,name= "iranna",age=21, city= "vijayapura",branch="engineering")'''


# def add(a,b):
#     c = a+b
#     return c
# a = add(5,4)
# print(a)

# def add():
#     print("Hello")
# add()

# def square(a):
#     c = a*a
#     print(c)
# square(5)

# def add(a,b=6):
#     c = a**b
#     return c
# print(add(2))

# def add(b=22,*a,c):
#     print(a)
#     print(b)
#     print(c)

# a = add(24,2,3,4,5,6,c=6)

def sud_info(name,*details,add="aaa"):
    print(details)
    print(name)
    print(add)

sud_info("iranna",21,"veeresh","iranna","aaa")




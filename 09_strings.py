# s = ""
# print(s)

# s = 'P'
# print(s)

# s = "Python"
# print(s)

# s = '''PYTHON makes perfect'''
# print(s)

# s = '''"Python" makes \'perfect\' '''
# print(s)

# s = "Python"
# print(s[2])
# s[2] = "P"
# print(s)

# s = "Python"
# for i in s:
#     print(i)

# for i in "PYTHON":
    # print(i)

# s1 = "Hello"
# s2 = "world"

# print(s1)
# print(s2)

# print(id(s1))
# print(id(s2))

# print(id(s1[4]))
# print(id(s2[1]))

# s1 = "P"
# s2 = "P"
# print(id(s1))
# print(id(s2))

# print(s1 is s2)

# s1 = [1,2,3]
# s2 = [1,2,3]
# print(s1 is s2)

# s1 = "hello"
# s2 = "world"
# print(s1)
# print(s2)

# print(s1[2], s1[3], s1[3])
# print(id(s1[2]), id(s1[3]), id(s2[3]))

# s = "Guido Van Rossum"
# print(s[0:14])
# print(s[0:17])

# print(s[15:9:-1])

# print(s[-1:9:])
# print(s[::-1])
# print(s[::-2])

# s1 = "python"
# s2 = "python"

# if s1 == s2:
#     print("String referene are equal")

# else:
#     print("string reference are unequal")

# s1 = "hello" + "world"
# print(s1)

# s1 = "hello"
# print(s1)
# s1 + "world"
# print(s1)

# s1 = "hello"
# print(s1)
# s2 = s1 + "world"
# print(s2)

# s1 = "hello"
# print(s1)
# s1 = s1 + "world"
# print(s1)


# c = "a"
# print(chr(ord(c)-32))

# c = "b"
# print(chr(ord(c)-32))

# n = input("Enter the string\n ")
# u_case = ""

# for i in n:
#     if ord(n)>=97 and ord(n)<=122:
#         u_case += chr(ord(i)-32)
#     else:
#         u_case += ord(i)

# print(u_case)

# c = ['Python', 'Java', 'c++', 'Django', 'c']
# new_str = "\n".join(c)
# print(new_str)

# for i in c:
    # new_str += i

# print(new_str)

# a = 10
# b = 20
# c = 30
# print(a,b,c)
# print(a,b,c,sep="manya ",end="ibbani")

url = ["http/iranna.com", "http/veeresh.com","http.pacchu/n.com/",
       "htt.preetu/.org"]

# for i in url:
    # if i[0:4] == "http":
    # if i[len(i)-3::] == "com" or i[len(i)-4::] == "com/":
        # print(i)

# for i in url:
    # if i.startswith("http") or i.endswith("com") or i.endswith("com/"):
        # print(i)

# u_case, lower_case, digi, spe_car = "","","",""

# n = input("Enetr the string\n")

# for i in n:
#     if ord(i) >= 65 and ord(i) <= 90:
#         u_case += i
#     elif ord(i)>= 97 and ord(i) <=122:
#         lower_case += i
#     elif ord(i) >= 48 and ord(i)<= 57:
#         digi += i
#     else:
#         spe_car += i

# print(u_case)
# print(lower_case)
# print(digi)
# print(spe_car)

# n = input("Enter the string\n")
# s = n.capitalize()
# print(s)

# n = input("Enter the string\n")
# table = n.maketrans("aeiou", "AEIOU", "1234567890")
# s_table = n.translate(table)
# print(s_table)

# name = input("Enter your name\n")
# place = input("Enter your place\n")
# s = "my name is {}, I am from {}".format(name, place)

# print(s)

# s = "{2} {0} {1} ".format(10,20,30)
# print(s)

# s = "{0:^10}".format(999)
# print(s)

# import math

# s = "{0:>10.4f}".format(math.pi)
# print(s)

# s = 597820000000000000000

# n = "{0:!>20.3e}".format(s)
# print(n)

# s = "{} ".format(*[10,20,30])
# print(s)

# from functools import reduce
# n = input("Enter the number\n").split()

# l = list(map(int, n))

# res = reduce(lambda x,y : x+y,l)
# avg = res/len(l)
# exp = "{0:*>10.4f}".format(avg)
# print(exp)

# import math

# res = "{0:!>10.5f}".format(math.pi)
# print(res)

# res = 5483578300000000000000

# print("{0:*>50.10e}".format(res))

'''u_case, low_case, dig, spe_chr = "","","",""
n = input("Enter your character\n")

for i in n:
    if i.isupper():
        u_case += i

    elif i.islower():
        low_case += i

    elif i.isnumeric():
        dig += i

    else:
        spe_chr += i

print("upper case", u_case)
print("lower case", low_case)
print("digit", dig)
print("Special character", spe_chr)'''

# n = list(map(int,input("Enter the numbers\n").split()))

# total = 0

# for i in n:

#     total = total + i

# avg = total/len(n)
# print(avg)

# s = "python"
# s1 = str(24)
# print(s + s1)

# n = input("Enter the number\n").split()

# total = 0

# for i in n:
#     total += int(i)

# avg = total/len(n)
# print(avg)


















        





    









 


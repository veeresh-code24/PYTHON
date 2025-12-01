# for i in range(1, 11):
    # print(i)

# i = 10
# while i >= 1:
    # print(i)
    # i -= 1

# for i in range(2, 11, 2):
    # print("Even number:", i)

# i = 2
# while i <= 10:
    # print(i)
    # i += 2

# sum = 0
# for i in range(1, 11):
#     sum += i
# print("Sum Numer:", sum)

# i = 1
# sum = 0
# while i < 100:
#     sum += i
#     i += 1
# print(sum)




# for i in range(1, 11):
    # print(f" {5} X {i} = {5 * i}")

# i = 1
# while i < 11:
    # print(f"{5} X {i} = {5 * i}")
    # i += 1

# fruits = ["apple", "banana", "cherry", "grapes"]
# for index, fruit in enumerate(fruits):
    # print(f"{index + 1} :" ,fruit)

# fruits = ["apple", "banana", "cherry", "grapes"]
# i = 1
# while i <len(fruits):
#     i += 1
#     print(i)
#     # i += 1

# name = "iranna"
# for i in name:
    # print(i,end =" ")

# name = "iranna"
# i = 1
# while i < len(name):
    # print(name)
    # i += 1  

# for i in range(1, 51):
#     if i % 5 == 0:
#         print("It's skip")
#         continue
#     print(i)

# i = 1
# while i <51:
#     if i % 5 == 0:
#         i += 1
#         continue
#     print(i)
#     i += 1


# i = 1
# while i <= 10:
#     if i == 7:
#         break
#     print(i)
#     i += 1

# for i in range(1, 11):
#     if i == 7:
#         break
#     print(i)

# i = 1
# while i < 51:
#     if i % 5 == 0:
#         print("It's skip")
#         i += 1
#         continue
#     print(i)
#     i += 1

# for i in range(1, 51):
#     if i % 5 == 0:
#         print("It's skip")
#         continue
#     print(i)

# name = "iranna"
# for i in name:
#     print(i)


# total = 0

# i = 1
# while i < 51:
#     total += i
#     i += 1
# print(total)

# total = 0
# i = 1
# while i < 51:
#     total += i
#     i += 1
# print(total)

# lst = [10,20,30,40,50]

# i= 0
# while i<5:
#     print(lst[i])
#     i += 1

# print(list(range(5)))
# print(list(range(5,15,5)))

# balance = 15000
# min_balance = 500

# print("Before balance:", balance)

# while min_balance < balance:
#     balance = balance - 1000

# print("After balance:", balance)

# n = int(input("Enter your number: "))

# for i in range(2, n+1):
#     if n % i == 0:
#         break
# if n == i:
#     print("It's prime")
# else:
#     print("It's not prime")

# n = int(input("Enter your number\n: "))

# for i in range(2, n+1):
#     if n % i == 0:
#         break
# if n == i:
#     print("It's a prime")s
# else:
#     print("It's not a prime ")

# even_number, odd_number = 0,0

# n = int(input("Enter your number\n"))

# for i in range(1, n+1):
#     if i % 2 == 0:
#         even_number += i
#         continue
#     odd_number += i

# print(even_number, "is a even number")
# print(odd_number, "is a odd number")

# s1 = 3
# s2 = 3

# if id(s1) == id(s2):
#     print("True")
# else:
#     print('false')

# s = "hello" + "world"
# print(s)

'''s1 = "hello"
print(s1)

s1+"world"
print(s1)'''

'''s1 = "hello"
print(s1)

s2 = s1 + "world"
print(s2)

s1 = "hello"
print(id(s1))

s1 = s1 + "hello"
print(id(s1))'''


# a = ""
# c = chr(ord(a)-32)
# print(c)

# a = "a"
# print(chr(ord(a)-32))

# n = input("Enter your string\n")

# s = n.upper()
# print(s)

# upper_str = ""

# for i in n:
#     if ord(i)>=97 and ord(i)<=127:
#         upper_str += chr(ord(i)-32)
#     else:
#         upper_str += i
# print(n)
# print(upper_str)

'''lst = ["iranna", "manya","ibbani","pacchu"]

s = ""

for i in lst:
    s += i
print(s)

lst = ["iranna", "manya","ibbani","pacchu"]
s = "\n".join(lst)
print(s)'''

'''s = ["http.com","http,com/","http.com"]

for i in s:
    if i.startswith("http"):
        print(i)


s = ["http.com","http,com/","http.com"]
s1 = s.startswith("http")
print(s1)'''


# s = ["http.com","http,com/","http.com"]

# for i in s:
#     if i.endswith(("com","com/")):
#         print(i)



'''n = input("Enter your string\n")
low_count,upp_cou,num_cou,spe_cou = 0,0,0,0

for i in n:
    if 'a'  <= i <= 'z':
        low_count += 1
    elif 'A' <= i <= 'Z':
        upp_cou += 1
    elif '0' <= i <= '9':
        num_cou += 1       
    else:
        spe_cou += 1
    
print("lower count",low_count)
print("upper count",upp_cou)
print("numeric count", num_cou)
print("speciial count",spe_cou)'''

'''s = "iRANNA you ARE good boy"
s1 = s.swapcase()
print(s1)

print(s.title())
print(s.capitalize())'''

# a = "I am good boy little 1234 bit bad boy"
# s1 = a.maketrans("aeiou", "AEIOU","1234567890")
# b = a.translate(s1)
# print(a)
# print(b)
    
import sys

print(sys.argv)

s = int(sys.argv[1]) + int(sys.argv[2])
print(s)
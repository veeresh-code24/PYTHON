# d = {2:36,1:32,3:45,4:57,5:73}
# print(d)
# print(d[2])
# print(d[3])
# print(d["two"])

'''d = {1:"c",2:"java",3:'python'}
print(d)

# Adiing one element
d[4] = "c++"
print(d)

# Adding two element in two ways
d.update({'python':'PHP',6:'javascript'})
print(d)


d.update(seven='JS',eight='Bootcamp')
print(d)

# Modifying a element
d[2] = "Python"
print(d)'''

# d = {1:22, 2:33, 3:44, 4:55, 5:66}
# print(d)

# d.pop(99,999)
# print(d)

# d.popitem()
# print(d)

# print(d.pop(1))

# del d[6]
# print(d)

# print(d.clear())

# print(d.pop(2, "python"))
# d.clear()
# print(d)

# d.popitem()
# print(d)

# d = {1:'a',2:[10,20,30] }
# print(d[1])

# x = "a"
# print(x)
# print(d[1])

# x = "b"
# print(x)
# print(d[1])
# print(x)

# print(d[1])

# print(d[2])

# l = d[2]
# print(l)

# l = d[2]
# print(l)

# print(d[2])

# d = {1:'c', 2:'java',3:'python'}
# print(list(d.items()))

# for i,j in d:
#     print(i,j)


# s = input("Enter your word\n")
# d = {}

# for i in s:
#     if i not in d:
#         d[i] = 1 
#     else:
#         d[i] += 1
# for i in d.keys():
#     if d[i] >= 3:
#         print(i)

# s = input("enter a word").upper()

# d = {}

# for i in s:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# for i in d.keys():
#     if d[i] >= 3:
#         print(i) 

# s = list(map(int, input("Enter a number").split()))
# d = {}

# for i in s:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# print(d)


# n = int(input())
# d = {}

# for i in range(n):
#     l = input().split()
#     d[l[0]] = l[1]

# s = int(input())

# for i in range(s):
#     name = input()
#     if name in d:
#         print("mob:", d[name])
#     else:
#         print("No contact found")


# s = int(input("Enter how much contact u to store\n"))
# d = {}
# for i in range(s):
#     n = input("enter your name and contact\n").split()
#     d[n[0]] = n[1]

# m = int(input("How many times to serch\n"))

# for i in range(m):
#     name = input("Enter the which name u want to search")
#     if name in d:
#         print("mob:", d[name])
#     else:
#         print("contact not found")

# n = int(input())
# d = {}

# for i in range(n):
#     l = input().split()
#     d[l[0].lower()] = l[1]

# s = int(input())

# for i in range(s):
#     name = input().lower()
#     if name in d:
#         print("mob:", d[name])
#     else:
#         print("No contact found")

'''n = input("Enter your letter\n")
k = int(input("Enter pisition u want that letter"))
d = {}

for i in n:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

count = 0
for i in d:
    if d[i] == 1:
        count += 1
        if k == count:
            print(i)
            break

        # iranna'''

# str1 = "123"
# str1 = "c"
# print(str1)

# import re
# s = input("Enter a sentence\n")
# s = re.sub(r'[.,?!]', '', s)
# lst = s.split()

# d = {}
# for i in lst:
#     if i in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# for i in d:
#     if d[i] >= 3:
#         print(i)
# import re
# s = input().upper()
# s = re.sub(r"[.,?!]", "", s)
# lst = s.split()
# d = {}

# for i in lst:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# for i in d:
#     if d[i] >= 3:
#         print(i)


s = input().split(',')
d = {}
for i in s:
    t = i.split()
    if t[0] not in d:
        d[t[0]] = t[1]
    else:
        if t[1] > t[0]:
            d[t[0]] = t[1]
print(d)


a = 10
b = 20
print(a+b)


















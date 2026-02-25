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


# s = input().split(',')
# d = {}
# for i in s:
#     t = i.split()
#     if t[0] not in d:
#         d[t[0]] = t[1]
#     else:
#         if t[1] > t[0]:
#             d[t[0]] = t[1]
# print(d)

# s = input("Enter the string\n").upper()
# d = {}

# for i in s:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
    
# for i in d:
#     if d[i] > 3:
#         print(i)

# from collections import Counter

# s = input("Enter the string\n").upper()
# d = Counter(s)

# for i,j in d.items():
#     if j>3:
#         print(f"if {i} appears ,{d[i]} times")

# s = input("Enter the string\n").upper()
# d = {}

# for i in s:
#     d[i] = d.get(i, 0) + 1

# for i,j in d.items():
#     if j > 3:
#         print(i)

# from collections import Counter
# s = input("Enter the string\n").upper()
# d = Counter(s)

# for i , j in d.items():
#     if j >= 3:
#         print(i, d[i])

# lst = list(map(int, input("Enter the number").split()))
# d = {}

# for i in lst:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1 

# count = 0
# for i in d.values():
#     count += i//2

# print(count)

# n = int(input("Enter how much number can store\n"))
# d = {}

# for i in range(n+1):
#     l = input("Enter the name and number\n").split()
#     d[l[0]] = l[1]

# s = int(input("Enter the number of times of searching\n"))
# for i in range(s+1):
#     name = input("Enter the name u want to search\n")
#     if name in d.keys():
#         print("mob", d[name])

#     else:
#         print('Contact not found')

# n = int(input("Enter the how many numbers can store\n"))
# d = {}

# for i in range(n):
#     l = input("enter the name and number u can store\n").upper().split()
#     d[l[0]] = l[1]

# s = int(input("Enter the number of times searching"))

# for  i in range(s):
#     name = input("Enter the which contact u want to search\n").upper()
#     if name in d.keys():
#         print("mob", d[name])

#     else:
#         print("Contact not found")

# s = input("Enter the string\n")
# k = int(input("Enter kth value non-repeating string\n"))
# d = {}

# for i in s:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1

# count = 0
# for i in s:
#     if d[i] == 1:
#         count += 1
#         if k == count:
#             print(i)
#             break

# import re
# s = input("Enter the string\n").upper()
# s = re.sub('[?,!]','',s)
# lst = s.split()
# d = {}

# for i in lst:
#     if i not in d:
#         d[i] = 1

#     else:
#         d[i] += 1

# for i in d:
#     if d[i] > 3:
#         print(i, d[i])

# lst = input("enter the name and marks\n").split(',')
# d = {}

# for i in lst:
#     t = i.split()
#     if t[0] not in d:
#         d[t[0]] = t[1]
#     else:
#         if  int(t[1]) > int(d[t[0]]):
#             d[t[0]] = t[1]

# print(d)    
# data=sorted(d.items(),key=lambda x:x[0],reverse=True)



#     print(data[i])

# d = {1:'A', 2:'B', 3:'A',4:'A', 5:'C',6:'A'}
# s = {}

# for i in d:
#     if d[i] not in s:
#         s[d[i]] = []
#         s[d[i]].append(i)
#     else:
#         s[d[i]].append(i)
# print(s)

# lst = input("Enter the string\n").upper().split()
# d = {}

# for i in lst:
#     if len(i) not in d:
#         d[len(i)] = []
#         d[len(i)].append(i)

# s_d = sorted(d.keys(), reverse=True)

# for i in s_d:
#     for j in sorted(d[i]):
#         print(j)

# lst = input("Enter the string\n").split()
# d = {i : len(i) for i in lst}
# print(d)

# for i in lst:
    # d[i] = len(i)

# print(d)

lst = [1,2,3,4,5,6,7,8,9,10]
d = {i : i **2 if i % 2 == 0 else i**10 for i in lst}

# for i in lst:
#     if i%2 == 0:
#         d[i] = i**2
print(d)


        

        






































# lst = [10,20,30,40,50]
# print(lst)

# lst = ["iranna", 3, 3.333,False, "apple"]
# print(lst)

# lst1 = [10, [10,20,30],(40,50,60),{70,80,90},{"name":"iranna","age":21}]
# print(lst1)

# print(lst1[0])
# print(lst1[1][2])
# print(lst1[2][1])
# # print(lst1[3][1])
# print(lst1[4]["name"])
# print(lst1[4]["age"])

# lst1 = [10,20,30]
# lst2 = [40,50,60]
# lst3 = lst2 + lst1
# print(lst3)

# lst = [1]*10
# print(lst)

# lst4 = [1,2,3,4]*4
# print(lst4)

'''lst = [10,20,30,40,50,60,70,80]
print(lst)
print(lst[0])
print(lst[::])
print(lst[::-1])
print(lst[::2])
print(lst[-2::-2])
print(lst[-2:-8:-1])
print(lst[7:1:-1])'''


# lst = [10,20,30,40,50,60,70,80]

# for i in range(0,8):
#     print(lst[i])

# lst = [10,20,30,40,50]
# print(lst)

# lst.append(40)
# print(lst)

# lst.append([10,20,30])
# print(lst)

# lst = lst + [10,20,30]
# print(lst)

'''lst.extend([10,20,30])
print(lst)

lst.insert(2,99)
print(lst)

lst.extend([10,20,30])
print(lst)

lst[2] = 300
print(lst)

lst = lst + [1,2,3]
print(lst)'''

# lst = [10,20,30,40,50]
# lst[1:4] = [90]
# print(lst)

# lst[1:4] = [99,99,99,99,99,99,99]
# print(lst)

# lst[::2] = [22,22,22]
# print(lst)

# lst  = [10,20,30,40,50,30,40]
# print(lst)
# lst.remove(30)
# print(lst)

# while 30 in lst:
#     lst.remove(30)
# print(lst)

# print(30 in lst)
# print(30 not in lst)

# print(lst.pop())
# print(lst)
# print(lst)


# lst  = [10,20,30,40,50,30,40]
# lst.pop(0)
# print(lst)
# del lst[-1:-7:-1]

# del lst[::3]

# print(lst)

# lst[2:6] = [4]
# print(lst)



# lst  = [10,20,30,40,50]
# lst1 = lst[:]
# print(lst)
# print(lst1)
# print(lst is lst1)

# lst = [10,20,30,40,50]
# lst1 = list(lst)
# print(lst)
# print(lst1)
# print(lst is lst1)

#  Shallow copy 

'''lst = [[10,20],[30,40,50]]
lst1 = list(lst)
print(lst)
print(lst1)
print(lst is lst1)

lst.append([60,70])
print(lst)
print(lst1)
print(lst is lst1)

lst[1][0] = 300
print(lst)
print(lst1)
print(lst is lst1)'''

# Deep copy
'''import copy
lst =  [10,[20,30],[40,50]]
lst1 = copy.deepcopy(lst)
print(lst)
print(lst1)
print(lst is lst1)

lst.append([60,70])
print(lst)
print(lst1)

lst[1][0] = 300
print(lst)
print(lst1)'''

# lst = [10,20,30,40,50]
# print(len(lst))
# print(max(lst))
# print(min(lst))
# print(sum(lst))


# for i,j in enumerate(lst,start=00):
    # print(i,j) 

# Built in methoda

# lst = [10,20,30,40,50,20]
# print(lst.count(20))
# print(lst.index(20,2,6))
# print(lst.index(20))
# lst.clear()
# print(lst)

# lst = [12,88,2,101,950,20]
# lst = sorted(lst,reverse=True)
# print(lst)
# lst.sort(reverse=True)
# print(lst)

# lst = list(reversed(lst))
# print(lst)
# lst.reverse()
# print(lst)

# lst = sorted(lst, reverse=True)
# print(lst)

# PROGRAM TO FIND THE THE SUBLIST

'''lst = input("Enter a list between[]\n")
lst = eval(lst)

start = int(input("Enter your starting index\n "))
stop = int(input("Enter your ending index\n "))

print(sum(lst[start:stop+1]))'''

# lst = [10,20,30,40,50]
# lst1 = [10,20,30,80,88,28,38]

# for i in lst1:
#     if i not in lst:
#         lst.append(i)
# print(lst)

lst2 = [10,20,30,40,50]
lst1 = [50,40,30,20,10,8]

# for i in lst1:
#     if i not in lst2:
#         lst2.append(i)
# print(lst2)

# for i in lst2:
#     if i not in lst1:
#         lst1.append(i)
# print(lst1)
# print(lst2)

# lst = eval("Enter a sorted list between []\n")
# n = int("Enter your value to be inserted\n")

# for i in range(len(lst)):
#     if n<lst(i):
#         lst.insert(i,n)
#         break
# print(lst)

# lst = eval(input("Enter your sorted list between[]\n" ))
# n = int(input("Enter your value to be inserted\n"))

# for i in range(len(lst)):
#     if n < lst[i]:
#         lst.insert(i,n)
#         break
# print(lst)


# lst = [1,2,3,4,5,6,7]

# print(sum(lst)-min(lst), sum(lst)-max(lst))

# s = input("Enter your expression brackets\n")

# lst = []

# for i in s:
#     if i == "[" or i == "{" or i == "(":
#         lst.append(i)

#     elif i == "]" and lst[-1] == "[":
#         lst.pop()

#     elif i == "}" and lst[-1] == "{":
#         lst.pop()

#     elif i == ")" and lst[-1] == "(":
#         lst.pop()

#     else:
#         break
# if len(lst) == 0:
#     print(s,"It's a balnance expression")
# else:
#     print(s,"It's not a balance")

# s = input("Enter your expression brackets\n")
# lst = []
# balance = True

# for i in s:
#     if i == "{" or i == "[" or i == "(":
#         lst.append(i)

#     elif i == "}":
#         if lst and lst[-1] == "{":
#             lst.pop()
#         else:
#             balance = False
#             break
#     elif i == "]":
#         if lst and lst[-1] == "[":
#             lst.pop()
#         else:
#             balance = False
#             break
#     elif i == ")":
#         if lst and lst[-1] == "(":
#             lst.pop()
#         else:
#             balance = False
#             break

# if balance and len(lst) == 0:
#     print("It's balance")
# else:
#     print("It's not  balance")

# s = input("Enter your expression between\n")

# lst = []

# for i in s:
#     if i == "{" or i == "(" or i == "[":
#         lst.append(i)

#     elif i == "}" and lst[-1] == "{":
#         lst.pop()
    
#     elif i == ")" and lst[-1] == "(":
#         lst.pop()
    
#     elif i == "]" and lst[-1] == "[":
#         lst.pop()
    
#     else:
#         break

# if len(lst) == 0:
#     print("it's balance")
# else:
#     print("it's not a balance")

# lst1 = [1,3,1,5]
# lst2 = [4,]
# print(lst1 < lst2)

lst = [2,4,6,8,10,2,4,81,3,7,9]

# s_lst = []

# for i in lst:
    # s_lst.append(i**2)
# print(lst)
# print(s_lst)

# s = dict(map(lambda x : x**2,lst))
# print(s)

# sq_lst = [i**2 for i in lst]
# print(sq_lst)

# sq_lst = [i**2 for i in lst if i%2 == 0]
# print(sq_lst)

# lst1 = ["name","age","Branch"]
# lst2 = ["iranna",21,"Enginee"]
# print(list(zip(lst1,lst2)))
# print(list(zip(lst1,lst2)))

# for i,j in enumerate(lst1,start=1):
#     print(i,j) 


# lst1 = ["A","app","","da","kee","t","doc","a"]
# lst2 = ["n","le","a","y","ps","he","tor","way"]

# res = []
# for i,j in zip(lst1,lst2):
#     res.append(i+j)
# print(" ".join(res))

# print(" ".join([i+j for i,j in zip(lst1,lst2)]))

# print(" ".join([i+j for i,j in zip(lst1,lst2)]))

# s = input("Enter your string\n")

# lst = s.split()

# res = []
# for i in range(len(lst)):
#     if len(lst[i]) > 5:
#         res.append(lst[i].lower())
#     else:
#         res.append(lst[i].upper())
# print(' '.join(res))

# print(''.join([lst[i].lower() if len(lst[i]) > 5 else lst[i].upper() for i in range(len(lst))]))

# s = input("Enter your string\n")
# lst = s.split()

# res = []
# for i in range(len(lst)):
#     if len(lst[i]) > 5:
#         res.append(lst[i].lower())
#     else:
#         res.append(lst[i].upper())
# print(' '.join(res))

# print(' '.join([lst[i].lower() if len(lst[i]) > 5 else lst[i].upper() for i in range(len(lst))]))

'''lst = [10,20,30,40,50]
print(lst)

lst = ["python", 23,False, 1.222,1+3j]
print(lst)'''

# lst = [10,[10,20,30],(10,20,30),{1,2,3},{1:"x",2:"y"}]
# print(lst)

# print(lst[4][2])

# lst = [1,2,3] * 101
# print(lst)

# lst = [1,2,3]
# lst1 = [4,5,6]
# print(lst1+lst) 

# lst = [10,20,30,40,50,60]
# print(lst[0:6:-1]

# for i in range(len(lst)):
    # print(lst[i])

# lst = [10,20,30,40,50,30]
'''lst.append([60,70,80])
print(lst)
lst = lst + [60,70,80]
print(lst)
lst.extend([10,20,30])
print(lst)'''

# lst.insert(2,999)
# print(lst)
# lst.insert(2,299)
# print(lst)

# lst[4] = 300
# print(lst)

# lst[::2] = [100,100,100]
# print(lst)

# lst[::] = [22]
# print(lst)


lst = [10,20,30,40,50,30]
print(lst)
lst.remove(30)
print(lst)

# while 30 in lst:
#     lst.remove(30)
# print(lst)

print(30 in lst)
print(30 not in lst)
print(60 not in lst)







     

    



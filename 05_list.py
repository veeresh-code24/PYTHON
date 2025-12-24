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

# lst = input("Enter a lst between[]\n")
# lst = eval(lst)

# start = int(input("Enter the start index"))
# stop = int(input("Enter the stop index"))

# print(sum(lst[start:stop+1]))

# lst = list(map(int,input("Enter your list between \n").split()))

# start = int(input("Enter the start index"))
# stop = int(input("Enter the stop index"))

# print(sum(lst[start:stop+1]))

# lst1 = [1,2,3,4]
# lst2 = [2,3,4,5]

# for i in lst2:
#     if i not in lst1:
#         lst1.append(i)
# print(lst1)

'''lst1 = input("Enter a lst 1 numbers)")
lst1 = eval(lst1)
lst2 = input("Enter a lst 1 numbers")
lst2 = eval(lst2)

for i in lst2:
    if i not in lst1 :
        lst1.append(i)
print(lst1)'''

# lst = input("Enter the list number between []")
# lst = eval(lst)

# lst2 = int(input("entrer the insert number"))

# for i in range(len(lst)):
#     if lst2 < lst[i]:
#         lst.insert(i,lst2)
#         break
# print(lst)


# lst = eval(input("Enter your lst between []"))
# n = int(input("Enter your value to be inserted"))

# for i in range(len(lst)):
#     if n < lst[i]:
#         lst.insert(i,n)
#         break
# print(lst)

# lst1 = eval(input("Enter your list between []"))

# print(sum(lst1)-max(lst1),sum(lst1)-min(lst1))

'''lst1 = input("Enter your parenthesis\n")
lst = []

for i in lst1:
    if i == "[" or i == "{" or i == "(":
        lst.append(i)
    elif i == "]" and lst[-1] == "[":
        lst.pop()
    elif i == "}" and lst[-1] == "{":
        lst.pop()
    elif i == ")" and lst[-1] == "(":
        lst.pop()

if len(lst) == 0:
    print("Parenthesis are are equal")
else:
    print("Parenthesis are not equal")'''

# lst1 = [11,2,3,4]
# lst2 = [12]
# print(lst1 < lst2)

# lst = [1,2,3,4,5,6,7,8]

# sq_lst = []

# for i in lst:
#     if i%2 == 0:
#         sq_lst.append(i**2)
# print(lst)
# print(sq_lst)

# lst = [1,2,3,4,5,6,7,8]
# sq_lst = [i**2 for i in lst]
# print(sq_lst)

# sq_lst = [i**2 for i in lst if i%2 ==0]
# print(sq_lst)

# lst1  = [1,2,3,4,5]
# lst2 = [1,1,1,1,1]

# print(list(zip(lst1,lst2)))

# for i,j in zip(lst1,lst2):
#     print(i,j)

# lst1 = ["i","am","go","bo"]
# lst2 = ["","","od","y"]

# res = []
# for i,j in zip(lst1,lst2):
#     res.append(i+j)
# print(" ".join(res))

# print(" ".join([i+j for i,j in zip(lst1,lst2)]))

# print(" ".join([i+j for i,j in zip(lst1,lst2)]))

str = input("Enter your string\n").split()

# res = []
# for i in range(len(str)):
#     if len(str[i]) > 5:
#         res.append(str[i].lower())
#     else:
#         res.append(str[i].upper())
# print(' '.join(res))

print(' '.join([str[i].lower() if len(str[i]) > 5 else str[i].upper() for i in range(len(str))]))

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


lst = [1,2,3,4,5,6,7]

print(sum(lst)-min(lst), sum(lst)-max(lst))

    



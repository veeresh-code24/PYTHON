# l = [10,20,30,40,50]
# print(l)

# l = ["python", 10,20, [10,20,30],4+3j, {10,20,30},{1:"x", 2:"y"}]
# print(l)


# l = [[10,20], {1,2,3}, "python", 3+4j]
# print(l)

# l1 = [10,20,30]
# l2 = [40,50,60]
# print(l1*3)

# l = [0] * 10
# print(l)

# l = [10,20,30,40,50,60,70,80]
# print(l[0])
# print(l[::])
# print(l[::-1])
# print(l[-1:-5:-1])

# for i in range(0,8):
    # print(i)

# lst = [10,20,30,40,50,30]
# print(lst)

# lst.append([300,40,50,])
# print(lst)

# lst = lst + [10,20,30]
# print(lst)

# lst.extend([10,20,30,40,50])
# print(lst)

# lst.remove(30)
# print(lst)

# while 30 in lst:
#     lst.remove(30)

# print(lst)

# for i in lst:
#     lst.remove(30)
# print(i)
# print(lst)

# lst = [10,20,30,40,50,30,20,30]

# lst = [i for i in lst if i != 30]
# print(lst)

# lst[::2] = [99,99,99,99]
# print(lst)

# for i in lst[:]:
#     if i == 30 or i == 20:
#         lst.remove(i)

# print(lst)

# while 30 in lst:
#     lst.remove(30)
# print(lst)

# lst = [10,20,30,40,50,60]
# print(lst)

# print(lst.pop(3))
# print(lst)

# del lst[::2]
# print(lst)

# lst.insert(2, 24)
# print(lst)

# lst = [10,20,30,40,50,60,10]

# print(lst)
# print(len(lst))
# print(max(lst))
# print(min(lst))
# print(sum(lst))

# print(lst.count(10))
# print(lst.index(20))
# print(lst.index(10,2,7))


# print(sorted(lst, reverse=False))

# lst.sort(reverse=True)
# print(lst)

# lst = list(reversed(lst))
# print(lst)

# lst.reverse()
# print(lst)

# lst = [10,20,30,40,50]

# for i,j in enumerate(lst,start=0):
#     print(i,j)

# for i in lst:
#     print(i)

# for i in range(0,5):
#     print(i,lst[i])

# lst = input("Enter the sum of sub list[]\n")
# lst = eval(lst)


# start = int(input("Enter the atarting index\n"))
# end = int(input("Enter the ending index\n"))

# res = sum(lst[start:end+1])
# print(res)

# lst = input("Enter the input[]/")
# lst = eval(lst)
# total = 0
# for i in lst:
#     total += i
# print(total)

# lst = [[10,20,30],[1,2,3],[12,1,21]]
# total = 0

# for i in lst:
    # print(sum(i))

# for i in lst:
    # for num in i:
        # total += num

# print(total)

# lst = input("Enter the strng\n")
# lst = eval(lst)

# start = int(input("Enter the strig\t"))
# stop = int(input("Enter the stop index\t"))

# res = sum(lst[start:stop+1])
# print(res)

# lst1 = [10,20,30,40,50]
# lst2 = [600,700,30,440,50]

# for i in lst1:
#     if i not in lst2:
#         lst2.append(i)
# print(lst2)
# print(lst1)

# lst1 = [[10,20,30],[10,20,10],10,20]
# total = 0
# for i in lst1:

#     for j in i:
#         total += j
# print(total)

# lst = [1,2,3,5,6] 

# sqa_lst = []

# for i in lst:
    # sqa_lst.append(i**2)

# print(lst)
# print(sqa_lst)

# sqa_lst = [i**2 for i in lst]
# print(sqa_lst)

# sqa_lst = [i**2 for i in lst if i%2==0]
# print(sqa_lst)

# lst1 = [10,30,50,70,90]
# lst2 = [20,40,60,80,100]
# print(list(zip(lst1,lst2)))

# for i,j in zip(lst1, lst2):
    # print(i,j)

# lst1 = ["M","i","ira","stud","SDIT",]
# lst2 = ["y","is","nna","ing","college"]

# res = []

# for i,j in zip(lst1,lst2):
#     res.append(i+j)

# print(" ".join(res))

# for i ,j in zip(lst1, lst2):
#     if i == j:
#         print("matching",i,j)

# a = [1,2,3]
# b = [1,2,4]
# count = 0

# for x, y in zip(a, b):
#     if x != y:
#         count += 1
#         print("Mismatch:", x, y)

# print(count)


# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]

# trans = list(zip(*matrix))
# print(trans)

# for i,j,k in trans:
#     print(i,j,k)

# lst = [i + j for i,j in zip(lst1, lst2)]
# print(lst)

# s = input("Enter the string\n")
# lst = s.split()
# res = []

# for i in range(len(lst)):
#     if len(lst[i]) > 5:
#         res.append(lst[i].lower())
#     else:
#         res.append(lst[i].upper())
# print(res)
# print(' '.join(res))

# print(" ".join([lst[i].lower() if len(lst[i]) > 5 else lst[i].upper() for i in range(len(lst))]))

# nums =[1,2,3,4,5]

# lst = [i**2 for i in nums]
# print(lst)

# nums = [10,15,20,25,30,35]


# for i in nums:
    # if i % 2 == 0:
        # print(i)

# lst = [i%2==0 for i in nums]
# print(lst)

# words = ["python","java","c","go"]
# res = []

# for i in words:
#     res.append(i.upper())
# print(" ".join(res))

# lst = [i.upper() for i in words]
# print(lst)

# nums = [5,12,7,18,3,20]

# lst = [i > 10 for i in nums]
# print(lst)































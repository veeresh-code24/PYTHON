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

lst = [10,20,30,40,50]
print(lst)

# lst.append(40)
# print(lst)

# lst.append([10,20,30])
# print(lst)

# lst = lst + [10,20,30]
# print(lst)

lst.extend([10,20,30])
print(lst)

lst.insert(2,99)
print(lst)

lst.extend([10,20,30])
print(lst)

lst[2] = 300
print(lst)

lst = lst + [1,2,3]
print(lst)





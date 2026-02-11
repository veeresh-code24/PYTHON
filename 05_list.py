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

lst = [10,20,30,40,50,30,20,30]

# lst = [i for i in lst if i != 30]
# print(lst)

# lst[::2] = [99,99,99,99]
# print(lst)

for i in lst[:]:
    # if i == 30 or i == 20:
        # lst.remove(i)

        lst.remove(30)

print(lst)
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

d = {1:'a',2:[10,20,30] }
print(d[1])

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

s = list(map(int, input("Enter a number").split()))
d = {}

for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)








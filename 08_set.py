# set = set()
# print(set,type(set))

# s = {1,2,3,2,1,23,32,1,23,2,1,333,2,12}
# print(s)

# s = {1,3.333,False,'Python',(1,2,3)}
# print(s)

# s = {{1,2,3},[1,2,3],{1:"x",2:"y"}}
# print(s)

# s= {(1,2,3),"python"}
# print(s)

'''s = {21,23,12,12,1,21,23,44,56,54,45,32,999}
print(s)
s.add(999)
print(s)
s.add(999)
print(s)
s.remove(32)
print(s)
s.discard(999)
print(s)
s.discard(111)
print(s)
s.pop()
print(s)
print(s.pop())
s.update({1,2,3,4,5,6,7,8,8,66,5,3,3,2,21,34,67,89,0,8,7})
print(s)
print(hash(999))'''

# s = {"python"}
# print(s)
# print(hash("python"))

# print(hash(99999))


# s1 = {1,2,3,4,5,6,7,8}
# s2 = {6,7,8,9,0,10,20,30}
# s3 = s1 | s2
# print(s3)
# s3 = s1.union(s2)
# print(s3)

# s4 = s1 & s2
# print(s4)
# s3 = s1.intersection(s2)
# print(s3)

# s4 = s2 - s1
# print(s4)
# s3 = s1.difference(s2)
# print(s3)

# s3 = s1 ^ s2
# print(s3)
# s3 = s1.symmetric_difference(s2)
# print(s3)
# print(s1)
# print(s1.intersection(s2))
# print(s1)

# print(s1)
# s1.intersection_update(s2)
# print(s1)

# print(s1)
# print(s1.difference(s2))
# print(s1)

# print(s1)
# s1.difference_update(s2)
# print(s1)

# print(s1)
# print(s1.symmetric_difference(s2))
# print(s1)

# print(s1)
# s1.symmetric_difference_update(s2)
# print(s1)

# s1 = {1,2,3,4,99}
# s2 = {1,2,3,4,5,6,78,9,10,11,12}
# print(s1.issubset(s2))
# print(s2 <= s1)

# print(s2.issuperset(s1))
# print(s2 >= s1)
# print(s1 <= s2)


# print(s1.isdisjoint(s2))

# print(s2.issuperset(s1))
# print(s1 <= s2)

# lst = input("Enter your string\n").split()

# lst2 = set(lst)
# print(lst2)

# lst = list(map(int,input("Enter your list number").split() ))

# s = set(lst)
# print(len(lst)-len(s))

# lst = list(map(int,input("Enter your list number").split() ))

# s = set(lst)
# print(len(lst)-len(s))


# List comprehension

# s = {1,2,3,4,5,6,7,8,9}
# res = set()

# for i in s:
#     if i % 2 == 0:
#         res.add(i**2)

# print(res)

# res = {i**2 for i in s if i % 2 == 0}
# print(res)

# res = {i**2 for i in s}
# print(res)

# s = {2,3,4,5,6,7,8,9,10}
# res = set()
# for i in s:
#     if i % 2 == 0:
#         res.add(i**2)
#     else:
#         res.add(i+i)
# print(res)

# res = {i**2 if i%2==0 else i+i for i in s}
# print(res)

# set  = set()
# print(set)
# print(type(set))

# set1 = {10,20,30,40,50,60,70,80,90,10,20,30,40}
# print(set1)

# set2 = {"python",(10,"apple"),10,3+4j,3.333,True}
# print(set2)

# print(hash(3.3333))


'''s = {12,32,12,34,23,56,67,45,23}
print(s)
s.add(99)
print(s)
s.pop()
print(s)
# s.remove(100)
# print(s)
s.discard(23)
print(s)

s.update({1,2,3,4})
print(s)'''

# s = {1,2,3}
# s1 = {4,5,6}
# print(s | s1)

s1 = {1,2,3,4,5,6,7,8,9,10}
s2 = {8,9,10,22,11,12,13,14}
# s3 = s1.union(s2)
# print(s3)

# s3 = s1.intersection(s2)
# print(s3)

# s3 = s2.difference(s1)
# print(s3)

# s3 = s1.symmetric_difference(s2)
# print(s3)

# print(s1)
# print(s1.intersection(s2))
# print(s1)

# s1.intersection_update(s2)
# print(s1)

# s1.difference_update(s2)
# print(s1)
# print(s1)
# print(s1.difference(s2))
# print(s1)

# print(s1)
# print(s1.symmetric_difference(s2))
# print(s1)

# s1.symmetric_difference_update(s2)
# print(s1)

# s1 = {1,2,3,4,5,6,78,9,10}
# s2 = {1,2,3,4}
# print(s1.issubset(s2))
# print(s2 <= s1)

# s1 = {1,2,3,4,5,6,7,8,9,10}
# s2 = {1,2,3,4}
# print(s1.issuperset(s2))
# print(s2 >= s1)

# s1 = {1,2,3,4,5,6,7,8}
# s2 = {9,10,11,12}

# print(s1.isdisjoint(s2))

parent = input("Enter the parenthesis\n")
lst = []

for i in parent:
    if i == "[" or i == "{" or i == "(":
        lst.append(i)
    elif i == "}" and lst[-1] == "{":
        lst.pop()

    elif i == "]" and lst[-1] == "[":
        lst.pop()

    elif i == ")" and  lst[-1] == "(":
        lst.pop()
        break

if len(lst) == 0:
    print("parenthesis are balanced")
else:
    print("It's not imbalanced")
    

















# a = 10
# b = 20
# a,b = b,a
# print(a)
# print(b)
# a = a+b
# b = a-b
# a= a-b
# print(a)
# print(b)

# student = {"name": "Veeresh", "age": 21, "city": "Bengaluru"}
# lst = list(student)
# print(lst)

# l = [1, 2, 2, 3, 3, 4]
# unique = []
# for i in l:
#     if i not in unique:
#         i.append()
#     print(unique)

# d = {"a": 1, "b": 2, "c": 3}
# c = ("b" in d)
# print(c)

# keys = ["name", "age", "city"]
# values = ["Veeresh", 21, "Bengaluru"]
# print(f"{keys : values}")

# l = [1, 2.5, 3, 4.7, 5]
# int_sum = 0
# float_sum = 0

# for x in l:
#     if type(x) == int:
#         int_sum += x
#     elif type(x) == float:
#         float_sum += x
# print("Sum of integer=", int_sum)
# print("Sum of float=", float+sum)

# l = [1, 2.5, 3, 4.7, 5]

# int_sum = 0
# float_sum = 0
# for x in l:
#     if type(x) == int:
#         int_sum += 1
#     elif type(x) == float:
#         float_sum += 1
# print("integer= ", int_sum)
# print("Float number=", float_sum)


# l = [1, "hello", 3.14, "python", 10, 4.5]

# int_count = 0
# string_count = 0
# float_count = 0

# for x in l:
#     if type(x) == int:
#         int_count += 1
    
#     elif type(x) == float:
#         float_count += 1
    
#     elif type(x) == str:
#         string_count += 1

# print("int=", int_count)
# print("float=", float_count)
# print("str=", string_count)

# student = {"name": "Veeresh", "age": 21, "city": "Bengaluru"}
# for key, value in student.items():

# place = "Bengaluru"
# wheather = "cold"
# sentence = f"The wheather in {place} is {wheather} today."
# print(sentence)

# l = [1, "a", 3, "b", 4, "python", 7]

# extract_number = []
# for i in l:
#     if type(i) == str or type(i) == int: 


#         extract_number.append(i)
# print(extract_number) 

# l = [1, 2, 2, 3, 3, 4]

# unique = []
# for x in l:
#     if x not in unique:
#         unique.append(x)
# print(unique)

# l = [1, "a", 3, "b", 4, "python", 7]

# result = []

# for x in l:
#     if isinstance(x, (int, str)):   # checks for both
#         result.append(x)

# print(result)

# num = int(input("Enter ypur number \n: "))
# den = int(input("Enter your number \n: "))
# res = num/den
# print("Your divide number is: ", res)

# exp = input("Enter your expression")
# res = eval(exp)
# print(res)

# l = [1, "a", 3, "b", 4, "python", 7]

# unique = []
# for i in l:
#     if type(i) == int:
#         unique.append(i)
# print(unique)

# keys = ["name", "age", "city"]
# values = ["Veeresh", 21, "Bengaluru"]
# for keys, values in

# keys = ["name", "age", "city"]
# values = ["Veeresh", 21, "Bengaluru"]
# result = dict(zip(keys,values))
# print(result)

# l = [1, 2, 2, 3, 3, 4]
# lst = []
# for i in l:
#     if i not in lst:
#         lst.append(i)
# print(lst)


# d = {"a": 1, "b": 2, "c": 3}
# res = "b" in d
# print(res)

# l = [10, 25, 7, 99, 3]
# largest = l[3]
# for i in l:
#     if i > largest:
#         largest = i
# print(largest)

# l = [1, 2, 2, 3, 3, 4]
# largest = l[0]
# for i in l:
#     if i > largest:
#         largest = i
# print(largest)

# keys = ["name", "age", "city"]
# values = ["Veeresh", 21, "Bengaluru"]

# res = dict(zip(keys,values))
# print(res)

# l = [1, "a", 3, "b", 4, "python", 7]
# int_number = []
# for i in l:
#     if type(i) == int:
#         int_number.append(i)
# print(int_number)

# l = [1, "a", 2.5, 3, "hello"]
# int_num = 0
# str_num = 0
# flo_num = 0

# for x in l:
#     if type(x) == int:
#         int_num += 1
#     if type(x) == str:
#         str_num += 1
#     if type(x) == float:
#         flo_num += 1
# print("Integer number=", int_num)
# print("String number=", str_num
# print("Float number=", flo_num)


# a = "ab12cd34"

# str_lett = []
# for i in a:
#     if type(i) == str:
#         str_lett.append(i)
# print(str_lett)

# a = "python"

# a = "iranna"
# vowels = "asHHYGtwsdsanna"
# count = 0

# for s in a:
#     if s in vowels:
#         count += 1
# print(count)


# balance = 15000
# min_balance = 500

# print("Before balance:", balance)

# while min_balance < balance:
# # for i in range(5):
#     balance = balance - 1000



# print("After balance:", balance)

s = input("Enter your string:\n")

if s == s[ ::-1]:
    print(s, "It's a palimdrome")
else:
    print(s,"It's not a palindrome")
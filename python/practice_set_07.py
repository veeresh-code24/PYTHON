# Table
# n = int(input("Enter your number"))

# for i in range(1, 11):
#     print(f" {n} X {i} = {n * i}")

# l = ["iranna", "veeresh", "iraa", "irappa"]

# for name in l:
#     if (name.endswith("h")):
#         print(name)

# n = int(input("Enter your number: "))

# i = 1
# while i < 11:
#     print(f"{n} X {i} = {n * i}")
#     i += 1
    
#  Prime number

# n = int(input("Enter your number: "))

# Prime

# n = int(input("Emter your number: "))s

# for i in range(2, n):
#     if n % i == 0:
#         print("This is not prime")
#         break
# else:
#     print("This is prime")


# n = int(input("Enter your number: "))
# i = 1
# sum = 0
# while (i <= n):
#     sum += i
#     i += 1
# print(sum)


# for i in range(5):
#     print()
#     for j in range(5):
#         print("*",end =" ")

# n = int(input("Enter your number: "))
# total = 0
# for i in range(1, n + 1):
#     total += i
# print(total)

# n = int(input("Enter ypur number: "))
# i = 1
# total = 0
# while (i <= n):
#     total += i
#     i += 1
# print(total)

# pass

# n = int(input("Enter ypur number: "))
# total = 0
# for i in range(1, n +1):
#     total += i
# print(total)

# for i in range(5, 11):
#     print(i)

n = [8, 4, 6, 9, 4]

for number in n:
    if number % 2 == 1:
        print(f"First even: {number}")
        break
else:
    print("NO even found number")
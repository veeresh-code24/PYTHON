# lst = [10,20,30,40,50]

# for i in range(len(lst)):
#     print(lst)

# print(list(range(2,10)))

# print(list(range(10)))

# balance = 15000
# min_balance = 500
# print("Before valance:",balance)

# while balance > min_balance:
#     balance -= 1000

# print(balance)


# balance = 15000
# min_balance = 500
# print("Before valance:", balance)

# while balance > min_balance:
#     balance -= 1000
#     print("After subtract:", balance)

# print("Final:", balance)


n = int(input("Enter your number\n"))

for i in range(2,n+1):
    if n % i == 0:
        break
if i == n:
    print("it's a prime")
else:
    print("It;s not a prime")



even_sum,odd_sum = 0,0
n = int(input("Enter your number\n"))

for i in range(1,n+1):
    if i % 2 == 0:
        even_sum+= i
        continue

    odd_sum += i

print(even_sum,"even_number")
print(odd_sum,"Odd number")
# print("Bank server established securely")
# try:
#     s = int(input("Enter your loan amount"))
#     t = int(input("Enter time duration "))
#     i = 10

# except:
#     print("Something went wrong")
# else:
#     si = (s*t*i)/100
#     print("Simple interest", si)
# print("Bank server securely must be closed")


print("Execution started normally")

lst = [10,20,30,40,50,0]
l = {1:'c', 2:'java',3:'python',4:'c++'}

try:
    rank = int(input("Enter the rank of language "))
    print(l[rank])

    num = int(input("Enter the index of numerator"))
    den = int(input("Enter the index of denominator"))
    print(lst[num]/lst[den])
except:
    print("Hey something went")

print("Execution terminated normally")

a = 10
b = 20
print(a+b)


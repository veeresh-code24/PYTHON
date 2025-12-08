# def power_of(a,b):
#     '''this functioon is showm the power a of b'''
#     res = a**b
#     print(res)


# def divide(numerator,denominator):
#     '''this function is divided into num/deno'''
#     res = numerator/denominator
#     print(res)

# if __name__ == '__main__':
#     power_of(2,5)
# divide(20,40)
# import sys

# print(sys.argv[0])
# print(sys.argv[1])
# print(sys.argv[2])

# res = int(sys.argv[1])/int(sys.argv[2])
# print(res)

# import sys
# print(sys.argv[0])
# print(sys.argv[1])
# print(sys.argv[2])

# res = int(sys.argv[1]) / int(sys.argv[2])

# a = int(input("Enter upo 1st number\n"))
# b = int(input("Enter upo 2st number\n"))
# c = int(input("Enter upo 3st number\n"))

# if a>b and a>c:
#     print("A is the largest")
# elif b>c and b>a:
#     print("B is the largest")
# else:
#     print("C is the largest")

# n = int(int(input("Enter your numbe\n")))

# if n % 3 == 0 or n % 8 == 0:
#     print("It is dividible by either 3 or 8")
# else:
#     print("It is not dividible by either 3 or 8")

# if {}:
#     print("It's a True")
# else:
#     print("It's a False")


# Store the voters who already voted
voted_list = set()  

def cast_vote(voter_id):
    # Check if voter already voted
    if voter_id in voted_list:
        print("❌ You have already voted! Duplicate vote detected.")
    else:
        print("✔ Vote submitted successfully.")
        voted_list.add(voter_id)

# -------------------------------
# Testing the program
# -------------------------------

# First time voting
cast_vote("1001")  
# Output: ✔ Vote submitted successfully.

# Same voter tries again
cast_vote("1001")  
# Output: ❌ You have already voted! Duplicate vote detected.

# Another voter
cast_vote("1002")
# Output: ✔ Vote submitted successfully.


def fun(num):
    return lambda x : x*num

res = int(input("Enter your number\n"))

print(res)


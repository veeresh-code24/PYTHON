# name = input("Enter tour name: ")
# print("Hello", name)

# height =  float(input("Enter your height: "))
# weight = int(input("Enter your weight"))
# print("your height is", height)


# a = int(input("Enter your number 1: "))
# b = int(input("Enter your number 2: "))
# print("Sum is a", a-b)

# age = int(input("Enter your age: "))
# print(age + 5)

# username = input("Username: ")
# password = int(input("Password: "))
# print("usernwme is ", username)
# print("password is ", password)

# answer = input("you are playing a cricket? (YES/NO): ").upper()
# if  answer == "YES":
#     print("That'a a great!")
# else:
#     print("i will play later")

# while True:
#     print("\nMenu:")
#     print("1. Say Hello")
#     print("2. Add Numbers")
#     print("3. Exit")
    
#     choice = input("Enter your choice: ")
    

#     if choice == "1":
#         name = input("Enter your name: ")
#         print(f"hello, good afternoon {name}")

#     elif choice == "2":
#         a = int(input("Enter your number 1:  "))
#         b = int(input("Enter your number 2: "))
#         result = a + b
#         print("Sum is ", result)

#     elif choice == "3":
#         print("Good Bye")
#         break
#     else:
#         print("your choice is invalid")    


# while True:
#     print("\nMenu:")
#     print("1. Say Hello")
#     print("2. Add Numbers")
#     print("3. Exit")
    
#     choice = input("Enter your choice: ")

#     if choice == "1":
#         name = input("Enter your name: ")
#         print(f"Hello, good afternoon {name}")

#     elif choice == "2":
#         try:
#             a = int(input("Enter your number 1: "))
#             b = int(input("Enter your number 2: "))
#             result = a + b
#             print("Sum is", result)
#         except ValueError:
#             print("Please enter valid numbers.")

#     elif choice == "3":
#         print("Good Bye")
#         break

#     else:
#         print("Your choice is invalid. Please try again.")


# a = input("Enter your number 1: ")
# b = input("Enter your number 2: ")
# x = int(a)
# y = int(b)
# sum = a + b
# print("Sum is", a+b)

# a, b = input("Enter two numbers : ").split()
# print("You entered:", a+b)

# boy = input("Enter your name: ")
# age = int(input("Enter your age: "))
# girl = input("Enter your name: ")
# age1 = int(input("Enter uour age: "))

# age_difference = abs(age-age1)

# print(boy + " loves " + girl + " Age difference is: " + str(age_difference))
# print(f"{boy} loves {girl}. Age difference is {age_difference}")

# age = int(input("Enter your age: "))
# print(age +10)

# price = float(input("Enter your number: "))
# print("Final price", price * 1.99)

# a = "Python is fun"
# b = a.split()
# print(b)

# s = "Python is fun"
# words = s.split()
# print(words)

# a, b = input("Enter your number: ").split()
# print(a,b)

# a, b = int(input("Enter two numbers: ").split())
# print(a + b)

# for i in range(3):
#     a = input("Enter your name: ")
#     print("Hii", a)

while True:
    txt = input("Enter your text(or type 'exit'):")
    if txt == "exit":
        print("Your typed is correct", txt)
        break
    print("You typed: ", txt)

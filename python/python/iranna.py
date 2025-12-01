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


while True:
    print("\nMenu:")
    print("1. Say Hello")
    print("2. Add Numbers")
    print("3. Exit")
    
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        name = input("Enter your name: ")
        print(f"Hello, good afternoon {name}")

    elif choice == "2":
        try:
            a = int(input("Enter your number 1: "))
            b = int(input("Enter your number 2: "))
            result = a + b
            print("Sum is", result)
        except ValueError:
            print("Please enter valid numbers.")

    elif choice == "3":
        print("GoodBye")
        break

    else:
        print("Your choice is invalid. Please try again.")

# a1 = int(input("Enter number 1: "))
# a2 = int(input("Enter number 2: "))
# a3 = int(input("Enter number 3: "))
# a4 = int(input("Enter number 4: "))

# if(a1>a2 and a1>a3 and a1>a4):
#     print("Greatest number is a1:", a1)
    
# elif(a2>a1 and a2>a3 and a2>a4):
#     print("Greatest number is a2:", a2)

# elif(a3>a1 and a3>a2 and a3>a4):
#     print("Greatest number is a3:", a3)

# elif(a4>a1 and a4>a2 and a4>a3):
#     print("Greatest number is a4:", a4)

# greatest = max(a1,a2,a3,a4)
# print("Greatest:",greatest )

# smallest = min(a1, a2, a3, a4)
# print("Smallest:", smallest)

# marks1 = int(input("Enter your marks 1:"))
# marks2 = int(input("Enter your marks 2:"))
# marks3 = int(input("Enter your marks 3:"))

# total_percentage = (100 * (marks1 + marks2 +marks3)) / 3002

# if (total_percentage>=40):
#     print("you passed:", total_percentage)
# else:
#     print("You are failed:", total_percentage)

# # Take input from user
# marks1 = int(input("Enter marks for Subject 1: "))
# marks2 = int(input("Enter marks for Subject 2: "))
# marks3 = int(input("Enter marks for Subject 3: "))

# # Calculate total and percentage
# total_marks = marks1 + marks2 + marks3
# percentage = (total2marks / 300) * 100

# # Display results
# print("\n--- Result ---")
# print("Total Marks:", total_marks)
# print("Percentage:", round(percentage, 2), "%")

# # Check pass or fail
# if percentage >= 40:
#     print("Status: Passed ")
# else:
#     print("Status: Failed ")

# # Optional: assign grade
# if percentage >= 90:
#     grade = "A+"
# elif percentage >= 75:
#     grade = "A"
# elif percentage >= 60:
#     grade = "B"
# elif percentage >= 40:
#     grade = "C"
# else:
#     grade = "F"

# print("Grade:", grade)


# marks1 = int(input("Enter your marks1: "))
# marks2 = int(input("Enter your marks2: "))
# marks3 = int(input("Enter your marks3: "))

# total_marks = marks1 + marks2 +marks3
# total_percentage = (total_marks / 300) * 100

# if total_percentage>=40:
#     print("You are passed", total_percentage)
# else:
#     print("You are failed", total_percentage)

# p1 = "you are geted big jackpot"
# p2 = "click here"
# p3 = "you are account is blocked"
# p4 = "buy now"

# message = input("Enter your comment: ")

# if ((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
#     print("This message is spam")
# else:
#     print("This comment is not in a spam")


# username = input("Enter your comment: ")

# if (len(username)<10):
#     print("Your message is less than 10 character")
# else:
#     print("It's ok")
 

name = input("Enter your name: ")

l = ["iranna", "veeresh", "venkatesh", "anand"]


if (name in l):
    print("Your name in the list")
else:
    print("Your name is not in the list")


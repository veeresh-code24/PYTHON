# age = int(input("Enter your age: "))

# if (age>18):
#     if (age==18):
#         print("Age are equal")

#     print("Your age is above the consent")
#     print("Congratualations this is good for you")

# elif (age<0):
#     print("You are entering a inavalid negative age")

# elif (age==0):
#     print("Your are entering a invalid age ")


# else:
#     print("Your age is below the consent")

# print("End the program")

# age = int(input("Enter your age: ")) 

# if(age%2 == 0):
#     print("Age is even") 

# if age>18:
#     print("Your age is greater than above")

# elif age==18:
#     print("your age is equal to above")
    
# else:
#     print("Your age is below above")

# age = 21
# b = "Adult" if age>21 else "Minor"
# print(b)


# age = 21
# b = "Minor" if age>=22 else "minor"
# print(b)

# marks = 65
# a = "A" if marks>=75 else "B" if marks>=75 else "c"
# print(a)


# marks = input("Enter your marks: ")
# marks = 85

# if marks>=86:
#     print("Grade A")
# elif marks>=75:
#     print("Grade B")
# else:
#     print("Grade c")

# x = 6
# print("Even" if x % 2 == 0  else "odd")


# x = 8
# print("Even" if x % 3 == 2 else "odd")

# age = 21
# if age>=22:
#     print("Adult")
# else:
#     print("Minor")

# age = 21
# print("Adult" if age>=77 else "MINOR")

# score = 99
# if score>=98:
#     Grade = "A"
# elif score>=94:
#     Grade = "B"
# else:
#     Grade = "C"
# # print(Grade)

# Grade = ("A" if score>=98 else
#          "B" if score>=94 else
#          "C")
# print(f"Score : {score} : {Grade}")

# score = 85

# # Traditional
# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# else:
#     grade = "C"

# # With conditional expressions (nested)
# grade = ("A" if score >= 90 else 
#          "B" if score >= 80 else 
#          "C")
# print(f"Score {score}: {grade}")  # Output: Score 85: B

# total = 150
# discount = 20 if total > 160 else 0
# final_price = total - discount
# print(f"Final price: {final_price}")

# total = 150
# if total > 160:
#     discount = 20
# else:
#     discount = 0
# final_price = total - discount
# print(final_price)

# a = int(input("Enter your age: "))
# a =20
# if a>18:
#     print("Your age is greater than above")
# elif a==20:
#     print("your age is invalid" )
# else:
#     print("your age is below")
 

# age = int(input("Enter your age: "))


# if age % 2 == 0:
#     print("number is even")
# if age >= 18:
#     print("Your age above the consent")
# # elif age < :
#     # print("your age is below the consenr")
# elif age == 8:
#     print("Your age is not matching")
# else:
#     print("your age is not matching the above" )

# age = 16

# if age >= 18:
#     print("Adult")
# else:
#     print("Minor")


# age = 21
# print("Adult" if age > 22 else "Minor")

# marks = 95
# grade = "A" if marks >= 92 else "B" if marks >= 98 else "C"
# print(grade)

# a = int(input("Enter your number: "))
# result = "Even" if a % 2 == 0 else "Odd"
# print(result)

# total = 160
# result = 80 if total >= 160 else 0
# final_price = total - result
# print(final_price)

# number = 16
# if number % 2 == 0 :
#     result = "Even"
# else:
#     result = "Odd"
# print(result)

# total = 120
# discount = 25 if total < 130 else 5
# final_price = total-discount
# print(f"Discount: {final_price}%")

# a = 25
# b = 30
# max_value = a if a // b else b
# print(f"Maximum: {max_value}")

# text = ""
# print("empty" if not text else "not empty")

# marks = 85
# result = "A" if marks >= 95 else "B" if marks >=97 else "C"
# print(f"Marks: {result}")

# i = 1
# while (i<=10):
#     if (i == 5):
#         break
#     print(i)
#     i += 1

# n = int(input("Enter tour number\n"))

# if n%2 == 0:
#     print(n, "is even number")

# else:
#    print(n, "odd number")

# if False:
#     print("Condition true")
# else:
#     print("Condition False")

# n = int(input("Enter your number\n"))

# if n%2 == 0:
#     print("Even number")
# else:

#     print("Odd number")

# a = int(input("Enter your number of a \n"))
# b = int(input("Enter your number of b\n"))
# c = int(input("Enter your number of c\n"))

# if a>b and a>c:
#     print("A is the largest number")
# elif b>a and b>c:
#     print("Bis the largest number")
# else:
#     print("C is the largest number")

# n = int(input("Enter youe number"))

# if n %2 == 0 or n % 5 == 0:
#     print("It is divisible by 2 neither 5")
# else:
#     print("It's a not divisible neither 3 or 5")

n = int(input("Enter your number\n:"))

if not n % 2 == 0:
    print("even number")
else:
    print("odd number")

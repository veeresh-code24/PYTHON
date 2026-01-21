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


# print("Execution started normally")

# lst = [10,20,30,40,50,0]
# l = {1:'c', 2:'java',3:'python',4:'c++'}

# try:
#     rank = int(input("Enter the rank of language "))
#     print(l[rank])

#     num = int(input("Enter the index of numerator"))
#     den = int(input("Enter the index of denominator"))
#     print(lst[num]/lst[den])
# except:
#     print("Hey something went")

# print("Execution terminated normally")

# a = 10
# b = 20
# print(a+b)

'''print("Execution started normally")

try:

    lst = [10,20,30,40,0,50]
    l = {1:"java", 2:"python", 3:"c++", 4:"c"}

    r = int(input("Enter the rank of language "))
    print(l[r])

    num = int(input("Enter your numerator "))
    den = int(input("Enter your denominator "))
    print(lst[num]/lst[den])



except KeyError as a:
    print(a)

except IndexError as a:
    print(a)

except ZeroDivisionError as e:
    print(e)

except ValueError as e:
    print(e)

except:
    print("Hey something went wrong")

print("Execution terminated normally")'''

'''def fun2():
    # try:


    print('fun2() execution started')

    num = int(input("Enter your numerator"))
    den = int(input("Enter your numerator"))
    print(num/den)
    # except ZeroDivisionError:
    # print("fun2() exception handled here")
    print('fun2 terminated normally')

def fun1():

    print("Fun1 started execution")
    # try:

    fun2()
    # except:
        # print("fun1() Exception handled here")

    print("Fun1 terminated normally")

def main():
    print("main() xecution started")
    try:


        fun1()
    except ZeroDivisionError:
        print("main() Exception handled here")

    print('main() terminated normally')

main()'''

# print("Bank server secure connection established here")
# try:

#     loan = int(input("Enter your loan amount\n"))
#     t_d = int(input("Enter your time duration loan\n"))
#     inte = 10
#     res = (loan*t_d*inte)/100
#     print("Your loan amount is ",res)
# except:
#     print("Something went wrong")

# print("Bank connection securely closed here")

'''def validate(mob):
    if len(mob) == 10:
        print("Mob number is validate")
    else:
        raise ValueError

def main():
    mob = input("Enter your mobile number")
    validate(mob)

main()'''

def menu(item):
    if item == 'pizza':
        print('Enjoy your pizza')
    elif item == 'Burger':
        print('Enjoy your burger')
    elif item == 'idli':
        print("Enjoy your tiffian")
    else:
        raise NameError
    
def main():
    item = input("Enter your food")
    menu(item)

main()








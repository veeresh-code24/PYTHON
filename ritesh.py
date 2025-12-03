
# def power_of(a,b):
#     '''This function is calculates the 
#     result of raise to the power of b'''
#     c = a**b
#     print(c)


# def get_quotient(numerator,denominator):
#     '''this function calculates the quptient of
#       numerator divided by denominator'''
#     quotient = numerator/denominator
#     print(quotient)

# def main():
#     power_of(2,5)
#     get_quotient(100,2)


# if __name__ == '__main__':
#     main()

# def add():

#     '''this will do two numbers to substitution'''
#     a = 10
#     b = 20
#     c = a+b
#     print(c)






# def sub():
#     '''this will do two numbers to substitution'''
#     a = 10
#     b = 20
#     c = a-b
#     print(c)






# def mul():
#     '''this will do two numbers to substitution'''
#     a = 10
#     b = 20
#     c = a*b
#     print(c)

# def main():
#     mul()
#     sub()
#     add()



# if __name__ == '__main__':
#     main()

import re
text = "Python is the best language"
regu = r"\b[a-zA-Z]\b"
lst = re.findall(regu,text)
print(lst)
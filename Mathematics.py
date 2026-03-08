# Factorial of n number

'''def factorial(n):
    res = 1

    for i in range(1,n+1):
        res *= i
    return res

def main():
    n = int(input())
    print(factorial(n))

if __name__ == '__main__':
    main()'''

# count of digit

'''def count(n):
    count = 0

    while n > 0:
        n = n//10
        count += 1
    return count

def main():
    n = int(input())
    print(count(n))

if __name__ == '__main__':
    main()'''

# trailing zero

'''def trailinig_zero(n):
    res = 0
    power_of5 = 5

    while n >= power_of5:
        res = res + (n//power_of5)
        power_of5 = power_of5 * 5
    return res

def main():
    n = int(input("Enter facto"))
    print(trailinig_zero(n))

if __name__ == '__main__':
    main()

def trailing_zero(n):
    return n//5 + n//25 + n//125 

n = int(input())
print(trailing_zero(n))'''

# gcd and hcf

'''def gcd(a,b):
    min = 0
    if a>b:
        min = a
    else:
        min = b

    for i in range(min, 0, -1):
        if (a % i == 0 and  b % i == 0):
            return i
        
def main():
    a = int(input())
    b = int(input())
    print(gcd(a,b))

if __name__ == '__main__':
    main()'''


# def gcd_euclid(a,b):

#     while (a!=b):
#         if a>b:
#             a = a-b
#         else:
#             b = b-a

#     return a
        
# def main():

#     a = int(input())
#     b = int(input())
#     print(gcd_euclid(a,b))

# if __name__ == '__main__':
    # main()

'''def euclid_gcd(a,b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    if a != 0:
        return a
    else:
        return b
    
def main():
    a = int(input())
    b = int(input())
    print(euclid_gcd(a,b))

if __name__ == '__main__':
    main()'''

# LCM

'''def lcm(a,b):
    res = max(a,b)

    while (True):
        if res % a == 0 and res % b == 0:
            break
        res += 1

    return res

def main():
    a = int(input())
    b = int(input())
    print(lcm(a,b))

if __name__ == '__main__':
    main()'''

# LCM and GCD more efficient code

'''def lcm(a,b):
    return (a*b)/euclid_gcd(a, b)

def euclid_gcd(a,b):

    while a!= 0 and b!= 0:
        if a>b:
            a = a%b
        else:
            b = b%a

    if a!=0:
        return a
    else:
        return b
    
def main():
    a = int(input())
    b = int(input())
    print(euclid_gcd(a,b))

if __name__ == '__main__':
    main()

def factor(n):
    i = 2

    while n > 1:
        while n % i == 0:
            print(i)
            n = n//i

        i += 1

def main():
    n = int(input())
    factor(n)

if __name__ == '__main__':
    main()'''

# # Factor
# import math

# def factor(n):
#     for i in range(1,int(math.sqrt(n)) +1):
#         if n % i == 0:
#             print(i)

#             if i != i//n:
#                 print(n//i)

# def main():
#     n = int(input())
#     factor(n)

# if __name__ == '__main__':
#     main()


# import math

# def factor(n):

#     for i in range(1, int(math.sqrt(n)) +1):
#         if n % i == 0:
#             print(i)
#             # if i != n//i:
#                 # print(n//i)

#     for i in range(int(math.sqrt(n)),0,-1):
#         if n % i == 0 and i != n//i :
#             # if n // i:
#             print(n//i)


# def main():
#     n = int(input())
#     factor(n)

# if __name__ == '__main__':
#     main()

# import math
# def factor(n):

#     for i in range(1,int(math.sqrt(n))+1 ):
#         if n % i == 0:
#             print(i)

#     for i in range(int(math.sqrt(n)), 0, -1):

#         if i != n//i and n % i == 0:
#             print(n//i)

# n = int(input())
# factor(n)



















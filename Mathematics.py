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


def gcd_euclid(a,b):

    while (a!=b):
        if a>b:
            a = a-b
        else:
            b = b-a

    return a
        
def main():

    a = int(input())
    b = int(input())
    print(gcd_euclid(a,b))

if __name__ == '__main__':
    main()










def power_of(a,b):
    '''this function will gives
    result of power of a power of b'''
    c = a**b
    return c


f = power_of(2,5)
print(f)


def quotient_of(num,deno):
    '''this will caluculate the the
      divided the numerator and denominator'''
    c = num/deno
    return c
r = quotient_of(5,200)
print(r)


s = input("Enter your expression\n")
s = eval(s)
print(s)
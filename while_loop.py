'''s = input("Enter the string\n").upper()

for i in range(0, len(s)-3):
    print(s[i:i+4])

s = input("Enter the string\n")

for i in range(1,len(s)-1):
    print(s[1:len(s)-1])
    break

s = input("Enter the string\n").upper()
print(s[len(s)-2:0:-1])

s = input("Enter the string\n").upper()

if s == s[::-1]:
    print(s,"it's a palindrome")
else:
    print(s,"it's not a palindrome")

s = input("Enter the string\n").lower()
pal_str = []

for i in s:
    pal_str = i + pal_str

if s == pal_str:
    print(s, "it's a palindrome")

else:
    print(s,"it's not a palindrome")

s = input("Enter the string\n").upper()
print(s[0:len(s)//2:] + s[len(s)-1:(len(s)//2)-1:-1])

s = input("Enter the string\n")
uppe_str = ""

for i in s:
    if ord(i) >= 65 and ord(i) <= 95:
        uppe_str += chr(ord(i)+32)
    else:
        uppe_str += i

print(uppe_str)

s = input("Enter the string\n")
print(s.lower())

url = ["hhtps.com", 'https.www.youtube.com', "https.www.com/",'https.googl.com']

for i in url:
    if i[0:5:] == "https":
        print(i)

for i in url:
        i.append



    if i[len(i)-4::] == "com/" or i[len(i)-3::] == "com":
        print(i)

s = input("Enter the string\n")

low_case,upp_case,digits,spe_chr = 0,0,0,0

for i in s:
    if ord(i) >= 97 and ord(i) <= 122:
        low_case += 1

    elif ord(i) >= 65 and ord(i) <= 90:
        upp_case += 1

    elif ord(i) >= 48 and ord(i) <= 57:
        digits += 1

    else:
        spe_chr += 1

print(low_case,"is lower case")
print(upp_case,"is upper case")
print(digits,"is digits case")
print(spe_chr,"is special character")

from functools import reduce

nums = input("Enter the numbers\n").split()
print(nums)
l = list(map(int, nums))
print(l)

add_nums = reduce(lambda x,y : x+y, l)
print(add_nums)

res = add_nums/len(nums)
print(res)

nums = list(map(int, input("Enter thr numbers\n").split()))

res = 0

for i in nums:
    res += i
    print(res)
print(res/len(nums))'''

nums = list(map(int, input("Enter the numbers\n").split()))
res = 0

for i in nums:
    res += i

s = res/len(nums)
print(res)
print(s)








        





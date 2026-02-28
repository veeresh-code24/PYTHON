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

print(uppe_str)'''

s = input("Enter the string\n")
print(s.lower())
        





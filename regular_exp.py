'''import re
text = "Python is super easy"
regex = r"super"
match = re.search(regex, text)
print(match)
start, end = match.span()
print(start,end)
print(text[start:end])
print(text[match.start():match.end()])'''


#  .


# import re
# text = "Python is very easy."
# regex = r"."
# match = re.finditer(regex,text)
# # print(text[match.start():match.end()])
# for i in match:
#     print(text[i.start():i.end()])


# \. 

'''import re
text = "Python is very easy.#"
# regex = r"\."
match = re.findall(regex,text)
# print(text[match.start():match.end()])
print(match)'''

# \ OR
'''import re
text = "Python is very super"
regex = r"Python|very"
match = re.findall(regex,text)
print(match)'''

# * ? +
'''import re
text = " a whole hole is not a wwwhole. wholes"
regex = r"w+hole"
match = re.findall(regex,text)
print(match)'''

# {2,5} curly bracket
'''import re
text = ''
gogle
google
gooogle
gooooogle
gooooooogle''

regul = r"go{2,6}gle"
lst = re.findall(regul,text)
print(lst)
print(len(lst))'''

# ^ or $
'''import re
text = "Python is very easy to learn Python"
regul = r"Python$"
match = re.search(regul,text)
print(match)
print(text[match.start():match.end()])'''

#  serch for these elemnts [aeioub] or [] or [^aeioub] forgot these elements 

'''import re
text = "Iranna is a good boy but little bit bad boy"
regul = r"[aeioub]"
match = re.findall(regul,text)
print(match)
print("occurence=",len(match) )'''

#  select the all character \w or [a-zA-z]

'''import re
text = "Python is very easy"
regul = "\w"
lst = re.findall(regul,text)
print(lst)
print(len(lst))


#  select the all character \W or [^a-zA-Z]

import re
text = "Python is very easy"
regul = r"\W"
lst = re.findall(regul,text)
print(lst)
print(len(lst))'''

'''# select the only digit \d 0r \D
import re
text = "Python is very easy 1234467890"
regul = r"\D"
lst = re.findall(regul,text)
print(lst)
print(len(lst))'''

# select the white space \s or \S

import re
text = "Python is very easy 1234467890"
regul = r"[1234567890]+$"
lst = re.findall(regul,text)
print(lst)
print(len(lst))

#  repeating two times

'''import re
text = "If foot becomes feet tooth becomes teeth"
regul = r"[aeiou]{2}"
lst = re.findall(regul,text)
print(lst)'''

#  i want weak and week

'''import re
text = "Only the weak wait for the week to end"
regul = r"we[ae]k"
lst = re.findall(regul,text)
print(lst)'''

# \babc\b or \babc or abc\b or \Babc\B

'''import re
text = abcpqrxyz
pqrxyzabc
pqrabcxyz
abc
regula = r"\babc"
lst = re.search(regula,text)
print(text[lst.start():lst.end()])
print(lst)'''

# I wan tfirst character in the sentence

'''import re
text = "Python is the best language"
regu = r"^[a-zA-Z]"
lst = re.findall(regu,text)
print(lst)
# print(lst.group())
# print(text[lst.start():lst.end()])
# print(lst)
# print(lst.group())'''

# I want 4 length character.  r"\b[a-zA-Z]{4}\b"

'''import re
text = "Python is the best language four five"
regu = r"\b[a-zA-Z]{4}\b"
lst = re.findall(regu,text)
# print(lst.group())
print(lst)'''

# Find the valid gmail r"[a-zA-z0-9_$\-]+@gmail.com". or

# '''import re
# text = '''iranna@gmail.com
# rohit@@gmail.com
# rohit_xys@gmail.com
# roh?>@gmail.com
# rohit@yahoo.com
# rohit@outlook.com
# rohit@hotmail.com'''
# '''
# # regex = r"[a-zA-z0-9_$\-]+@[a-zA-Z]+.com"
# # regex = r"[a-zA-Z0-9$_\-]+@[a-zA-z0-9$_/-]+.com"
# # regex = r"[a-zA-Z0-9$_/-]+@gmail.com"

# # 2 group is there

# '''regu = r"([9a-zA-Z0-9$_/-]+)@([a-zA-Z0-9$_/-]+.com)"
# match = re.search(regu,text)
# print(match.group(0))
# print(match.group(1))
# print(match.group(2))'''

# # ITERable
# # regu = r"([9a-zA-Z0-9$_/-]+)@([a-zA-Z0-9$_/-]+.com)"
# # match = re.findall(regu,text)
# # print(match)

# # for i in match:
# #     print(i.group(0))
# #     print(i.group(1))
# #     print(i.group(2))

#all gmail are same  sub(pattern,"rep1",string) sub.subn

# import re
# text = '''iranna@gmail.com
# rohit@@gmail.com
# rohit_xys@gmail.com
# roh?>@gmail.com
# rohit@yahoo.com
# rohit@outlook.com
# rohit@hotmail.com'''

# regu = r"@[a-zA-z]+.com" 
# match = re.subn(regu,"@roomaan.com",text)
# print(match)

#Split numbers

'''import re
text = "2005:04:23"
lst = re.split(r"[-\:]", text)
print(lst)'''

# 1st Approach

# import re
# text = "9018880822 90198808"
# regular = r"\d{10}"
# list = re.search(regular,text)
# print(list.group())

# 2nd Approach

'''import re
text = "9018088221 87878787"
p = re.compile(r"\d{10}")
a = p.search(text)
print(a.group())
print(p.findall(text))'''

# import re
# text = ['9019880822',
# '9945324556',
# '9113571717',
# '8660655063']

# p = re.compile(r"\b\d{5}[02468]\d{4}\b")

# for i in text:
#     if p.search(i) != None:
#         print(i,"Valid")
#     else:
#         print(i,"Invalid")

# import re
# text = ['9019880822',
# '9945324556',
# '9113571717',
# '8660655063']

# regu = r"\b\d{5}[24680]\d{4}\b"
# match = re.match(regu,text)

# for i in match:
#     if i != None:
#         print(i,"Valid")
#     else:
#         print(i,"invalid")

# import re

# text = ['9019880822',
#         '9945324556',
#         '9113571717',
#         '8660655063']

# regu = r"\b\d{5}[24680]\d{4}\b"
# p = re.compile(regu)

# for number in text:
#     if p.fullmatch(number):
#         print(number, "Valid")
#     else:
#         print(number, "Invalid")


















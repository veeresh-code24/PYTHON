import re

# text = "Python is super easy"
# regex = r"Python"
# match = re.match(regex, text)
# print(match)
# start, end = match.span()
# print(text[match.start():match.end():])

# import re

# text = "Python is super easy"
# regex = r"Python"

# match = re.match(regex, text)

# if match:
#     print(match)
#     print(text[match.start():match.end()])

# import re
# text = "Python is super easy"
# regex = r"easy"

# match = re.search(regex, text)
# print(match)
# print(match.span())
# print(text[match.start():match.end()])

# import re
# text = "python is super easy."
# regex = r"\."

# match = re.findall(regex, text)
# print(match)
# print(text[match.start():match.end()])

# text = "Python is super easy"

# regex = r"Python|easy"

# match = re.match(regex, text)
# print(match)
# print(text[match.start():match.end()])

# text = "a whole hole is not a wwwhole"
# regex = r"w+hole"

# match = re.findall(regex, text)
# print(match)

# text = "I know that no one is there in the school now"
# regex = r"k?now?"

# match = re.findall(regex, text)
# print(match)

# print("Number of occurence", len(match))

# text = '''gogle
# ggggle
# gggggggle
# ggggggle
# gggggggle
# goooooogle
# '''

# regex = r"g{1}gle"
# match = re.findall(regex, text)
# print(match)

'''text = "Python has nothing to do with the Python"
regex = r"Python$"

match = re.findall(regex, text)
print(match)
# print(text[match.start():match.end()])'''

# text = "My name is iranna i am studying in a 7th sem"
# regex = r"[^aeiou]"

# match = re.findall(regex, text)
# print(len(match))
# print(match)

# text = "My name is iranna my phone number is : 9019880822"
# regex = r"M"

# match = re.findall(regex, text)
# print(len(match))
# print(match)

# regex = r"\D"
# match = re.findall(regex, text)
# print(match)
# print("Number of occurence", len(match))

# text = "Only the weak wait for the week to end"

# tegex = r"we[ae]k"

# match = re.findall(tegex, text)
# print(match)

# text = '''abcpqrxyz
# pqrxyzabc
# pqrabcxyz
# abc'''

# regex = r"abc"
# match = re.search(regex, text)
# print(match)
# print(text[match.start():match.end()])

# text = "Python is the best language"
# regex = r"\W"
# match = re.search(regex,text)
# print(match)

# print(match.group())

# text = "Python is the best language four"
# regex = r"\b[a-zA-Z]{4}\b"

# match = re.findall(regex, text)
# print(match)

text = '''iranna@gmail.com
iranna@@gmail.com
iranna_xyz@gmail.com
irann?>@gmail.com
iranna-123@gmail.com
iranna@yahoo.com
iranna@outlook.com
iranna@hotmail.com'''
regex = r"[a-zA-Z0-9_$\-]+@[a-zA-Z0-9]+.com"

match = re.findall(regex, text)
print(match)






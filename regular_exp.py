'''import re
text = "Python is very easy"
regex = r"Python"
match = re.match(regex,text)
# print(match)
print(match.span())
start,end = match.span()
print(text[start:end])
print(text[match.start():match.end()])'''

# import re
# text = "Iranna is a good boy"
# regex = r"Iranna"
# match = re.match(regex,text)
# print(match)
# print(match.span())
# start,end = match.span()
# print(text[match.start():match.end()]) #Match also cantains a position, regeular exp, string
# print(text[start:end])
# print(text[match.start():match.end()])

import re
text = "Python is very easy"
regu = r"very"
match = re.search(regu,text)
print(match)
print(text[match.start():match.end()])


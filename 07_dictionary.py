# a = {
#     "iranna": 98,
#     "manya": 67,
#     "pacchu": 76
# }
# print(a["iranna"])
# # # print(a.get("iranna"))

# print(a.keys())
# print(a.values())
# a.update({"iranna" : 78, "veeresh": 87})
# print(a)
# print(a.items())
# print(a.get("iranna"))
# print(a["iranna"])

# a["kalasha"] = 98
# print(a)


person = dict(name="iranna", age=20, manya=98)
# print(person.popitem())
# print(person.pop(0))
# print(person)
# person.clear()
# print(person)

# del person["name"]
person  ["name"] = "pacchu"

# del person ["age"]
print(person)
person["branch"] = "priya"
print(person)

# person = dict(name="iranna", age=20, manya=98)


# for key, value in person.items(): 
#     print(f"{key}:{value}")   


# for key in person:
#     print(key)
# for value in person.values():
#     print(person) 

# a = {
#     "s1" : {"name": "iranna", "age": 20},
#     "s2" : {"name": "chandu", "age": 21}
# }

# print(a["s2"])
# print(a["s1"])
# a.get("s1")
# print(a["s1"])


# marks = {
#     "harry": 98,
#     "iranna": 65,
#     "pacchu": 76
# }
# print(marks, type(marks))
# print(marks.keys())
# print(marks.values())
# print(marks.items())
# print(marks["harry"])
# print(marks.get("iranna"))
# marks.update({"iranna": 98, "manya": 87})
# marks["iranna"] = 84

# print(marks)
# marks["age"] = 21
# print(marks)

# a = {
#      "101": {"name": "iranna", "Age": 21, "branch": "Engineering"},
#      "102": {"name": "chandu", "Age": 22, "Branch": "BCA"}
# }

# print(a["101"]["name"])
# a["103"] = {"name": "akash", "Age": 22, "Branch": "bba"}
# print(a)

# a.pop("102")
# print(a)

# a = {
#     "102": {"name": "iranna", "age": 21, "branch": "Engineering"}
# }
# # print(a)
# print(a.popitem())
# del a ["name"]
# print(a)
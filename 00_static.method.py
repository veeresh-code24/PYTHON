'''class Cricket:

    def __init__(self,name,age,team):
        self.name = name
        self.age = age
        self.team = team

    def team_name(self):
        print(self.name,'is the RCB team')


    @staticmethod
    def km_miles(kms):
        print(kms * 1.6)


def main():

    virat = Cricket('Virat Kohli',37,'RCB')
    virat.team_name()


    Cricket.km_miles(2)

    virat.km_miles(2)







if __name__ == '__main__':
    main()'''

class Student:
    college = "ABC College"   # static variable

    def __init__(self, name):
        self.name = name      # instance variable

s1 = Student("Ravi")
s2 = Student("Asha")

print(s1.college)
print(s2.college)
print(s1.name)
print(s2.name)

a = 10
b = 20
print(a+b)

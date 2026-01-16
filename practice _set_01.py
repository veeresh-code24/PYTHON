'''class Car:
    def __init__(self):
        self.name = 'BMW'
        self.cc = 1000
        self.colour = 'Blue'

    def start_engine(self):
        print(self.name, 'engine is started...')

    def car_enigine(self):
        print(self.cc, 'BMW car engine of capacity')

    def car_colour(self):
        print(self.colour, 'is the BMW car')

    def display(self):
        print(self.name)
        print(self.cc)
        print(self.colour)

def main():
    c1 = Car()
    # print(c1.name)
    # print(c1.cc)
    # print(c1.colour)

    c1.display()

    c1.start_engine()
    c1.car_enigine()
    c1.car_colour()

    c2 = Car()
    c2.display()

    c2.start_engine()
    c2.car_enigine()
    c2.car_colour()


if __name__ == '__main__':
    main()'''

# class Cricket:
#     def __init__(self,name,team,score):
#         self.name = name
#         self.team = team
#         self.score = score

#     def scored(self):
#         print(self.name, 'scored well...')

#     def belongs(self):
#         print(self.team,'belongs to a team')

#     def batter(self):
#         print(self.name, "it's a good batter ")

#     def display(self):
#         print(self.name)
#         print(self.team)
#         print(self.score)
#         print(self.age)
#         print(self.jersay_no)

# def main():
#     virat = Cricket('Virat Kohli','RCB',130000)
    # virat.age = 37
    # virat.jersay_no = 18
    # setattr(virat,'age',22)
    # setattr(virat,'jersay_no',18)

    # print(getattr(virat,'name'))
    # print(virat.name)

    # print(hasattr(virat,'name'))
    # print(hasattr(virat,'gender'))

    # print(virat.__dict__)
    # print(virat.name)

    # print(virat.__dict__['name'])



    # virat.display()

    # virat.scored()
    # virat.belongs()
    # virat.batter()

    # dhoni = Cricket('Dhoni','CSK',11000)
    # dhoni.display()

    # dhoni.scored()
    # dhoni.belongs()
    # dhoni.batter()


# if __name__ == '__main__':
    # main()


'''class Citizen:

    nationality = 'India'

    def __init__(self,name,city,age,state):
        self.name = name
        self.city = city
        self.age = age
        self.state = state



    def display(self):
        print(self.name)
        print(self.city)
        print(self.age)
        print(self.state)
        print(self.nationality)

def main():
    c1 = Citizen('Iranna','bijapura',21,'karnataka',)
    # print(Citizen.__dict__['nationality'])
    # print(Citizen.nationality)

    # print(c1.__dict__)

    print(Citizen.nationality)
    print(Citizen.__dict__)


    c1.display()

    c2 = Citizen('Veeresh','bagalkot',20,'kerala')
    c2.display()


if __name__ == '__main__':
    main()'''

class Demo:
    a = 10
    b = 20

def main():

    print(Demo.a) #10
    print(Demo.b) #20

    Demo.a = 100 #100
    Demo.b = 200 #200
    print(Demo.a) #100
    print(Demo.b) #200

    d = Demo()

    print(d.a) #100 
    print(d.b) #200

    d.a = 1000 #1000
    d.a = 2000 #2000

    print(d.a) #1000
    print(d.b) #2000

    print(Demo.a) #100
    print(Demo.b) #200

if __name__ == "__main__":
    main()






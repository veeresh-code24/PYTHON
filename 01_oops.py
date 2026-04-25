# Creting a Object

'''class Car:

    def __init__(self):
        self.brand = 'BMW'
        self.cc = 1000
        self.colour = 'blue'

    def start_engine(self):
            print(self.brand, "starting the engine")

    def accelerate(self):
            print(self.brand,"accelerating the engine")

    def show_colour(self):
            print(self.colour,"is the car colour")


def main():
    c1 = Car()
    print(c1.brand)
    print(c1.cc)
    print(c1.colour)
    c1.start_engine()
    c1.accelerate()
    c1.car_colour()



if __name__ == '__main__':
    main()'''

# Differnt object with state, behaviour,property and 

class FootBaller:
    def __init__(self,name,team,goal):
        self.name = name
        self.team = team
        self.goal = goal

    def shooting(self):
        print(self.name, 'is a shooting')

    def passing(self):
        print(self.name, 'is passing the ball')

    def running(self):
        print(self.name, 'is a running')

    def display(self):
        print(self.name)
        print(self.team)
        print(self.goal)
        print(self.age)
        print(self.jersey_no)

def main():
    cr = FootBaller('critiano','juventu','749')
    # cr.display()

    setattr(cr,'age',37)
    setattr(cr,'jersey_no',7)
    # cr.age = 37
    # cr.jersey_no = 7
    cr.display()
    # print(getattr(cr,'name'))
    # print(cr.name)

    print(hasattr(cr,'name'))
    print(hasattr(cr,'iranna'))

    print(cr.__dict__)
    print(cr.__dict__['name'])
    print(cr.name)

    cr.shooting()
    cr.passing()
    cr.running()

    # messi = FootBaller('messi','portgu','856')
    # messi.display()
    # messi.running()
    # messi.shooting()
    # messi.passing()

if __name__ == '__main__':
    main()







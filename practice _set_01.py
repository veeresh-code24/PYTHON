class Car:
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
    main()



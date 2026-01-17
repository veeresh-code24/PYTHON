class BmwCar:
    def __init__(self,name,cc,colour):
        self.name = name
        self.cc = cc
        self.colour = colour
    @classmethod
    def ix(cls):
        return cls('x1',2100,'blue')
    
    @classmethod
    def super(cls):
        return cls('superx1',1998,'Red')
    
    
    @classmethod
    def x2(cls):
        return cls('x2',21000,'purple')
    
    @staticmethod
    def km_miles(kms):
        print(kms * 1.6)
    
    def display(self):
        print(self.name)
        print(self.cc)
        print(self.colour)
        # print(self.age)


def main():
    c1 = BmwCar.ix()
    c2 = BmwCar.super()
    c3 = BmwCar.x2()
    # c1.ix()
    # c1.age = 21
    # c2.age = 21
    # c3.age = 21
    # BmwCar.km_miles(2)

    # c2.km_miles(2)


    c1.display()
    c2.display()
    c3.display()


if __name__ == '__main__':
    main()




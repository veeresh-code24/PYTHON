
# __add__(int)

'''def main():
    a = 10
    print(a)
    # a = a + 5
    a = a.__add__(5)
    print(a)

if __name__ == '__main__':
    main()'''

# __add__(string)

'''def main():
    a = 'pyt'
    # a = a + 'hon'
    a = a.__add__('hon')
    print(a)

if __name__ == '__main__':
    main()'''

# using the int.__add__(int) // dunder method

class Point:
    def __init__(self,x, y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return  Point(self.x +other.y 
                ,self.y + other.y)

    # def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'{type(self)} {id(self)}'

    # def display(self):
        print(self.__dict__)


def main():
    p1 = Point(2,3)
    p2 = Point(1,1)
    # p1.display()
    # p2.display()
    # p3 = p1 + p2
    # p3 = p1.__add__(p2)

    # print(p1.__str__())
    # print(p2)
    # print(p3)

    print(p1)
    print(p2)
    print(p1.__repr__())
    print(p2.__repr__())



if __name__ == '__main__':
    main()
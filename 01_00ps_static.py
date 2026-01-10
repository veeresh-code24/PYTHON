# class Citizen:
    
#     nationality = 'India'

#     def __init__(self,name,age,gender,state):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.state = state


#     def display(self):
#         print(self.name)
#         print(self.age)
#         print(self.gender)
#         print(self.state)
#         print(self.nationality)

# def main():
#     iranna = Citizen('Iranna',20,'M','Karnataka')
#     veeresh = Citizen('pacchu',24,'M','Maharashtra')
#     ipacchu = Citizen('veeresh',34,'M','Kerala')

#     print(Citizen.__dict__['nationality'])
#     print(Citizen.nationality)
#     print(iranna.name)

#     # iranna.display()
#     # veeresh.display()
#     # ipacchu.display()

# if __name__ == '__main__':
    # main()

# class Demo:

#     a = 10
#     b = 20

# def main():

#     print(Demo.a)
#     print(Demo.b)
#     Demo.a = 100
#     Demo.b = 200
#     print(Demo.a)
#     print(Demo.b)

#     c = Demo()

#     c.a = 1000
#     c.b = 2000

#     print(c.a)
#     print(c.b)

#     print(Demo.a)
#     print(Demo.b)

# if __name__ == '__main__':
#     main()


class Demo:

    a = 100
    b = 200


def main():

    print(Demo.a)  #100
    print(Demo.b) #200
    Demo.a = 1000
    Demo.b = 2000
    print(Demo.a) #1000
    print(Demo.b) #2000


    c = Demo()
    print(c.a)  #10000

    print(c.b)   #20000

    c.a = 1000000
    c.b = 20000

    print(c.a)  #200000
    print(c.b)   #2000

    print(Demo.a) #1000
    print(Demo.b)  #2000

if __name__ == '__main__':
    main()

















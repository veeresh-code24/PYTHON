class Citizen:
    
    nationality = 'India'

    def __init__(self,name,age,gender,state):
        self.name = name
        self.age = age
        self.gender = gender
        self.state = state


    def display(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.state)
        print(self.nationality)

def main():
    iranna = Citizen('Iranna',20,'M','Karnataka')
    veeresh = Citizen('pacchu',24,'M','Maharashtra')
    ipacchu = Citizen('veeresh',34,'M','Kerala')

    print(Citizen.__dict__['nationality'])
    print(Citizen.nationality)
    print(iranna.name)

    # iranna.display()
    # veeresh.display()
    # ipacchu.display()

if __name__ == '__main__':
    main()



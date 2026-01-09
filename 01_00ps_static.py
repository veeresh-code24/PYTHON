class Citizen:
    def __init__(self,name,age,gender,state,nationality):
        self.name = name
        self.age = age
        self.gender = gender
        self.state = state
        self.nationality = nationality

    def display(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.state)
        print(self.nationality)

def main():
    iranna = Citizen('Iranna',20,'M','Karnataka','India')
    veeresh = Citizen('pacchu',24,'M','Maharashtra','India')
    ipacchu = Citizen('veeresh',34,'M','Kerala','India')

    iranna.display()
    veeresh.display()
    ipacchu.display()

if __name__ == '__main__':
    main()



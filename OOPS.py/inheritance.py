# Single inheritance

'''class Alpha:

    def fun(self):
        print("Alpha class fun()")

class Beta(Alpha):
    pass

b = Beta()
b.fun()'''

# Initially call the Object

'''class Alpha:

    def fun(self):
        print("Alpha class fun()")

print(dir(Alpha))'''

# Multilevel inheritance

'''class Alpha:

    def fun1(self):
        print("Inside the alpha fun1()")


class Beta(Alpha):

    def fun2(self):
        print("Inside the Beta fun2()")


class Gamma(Beta):
    pass

g = Gamma()
g.fun1()
g.fun2()
print(dir(Gamma))'''

# multiple inheritance

'''class Alpha:

    # def fun1(self):
        # print("Inside tha Alpha fun1()")
        pass

class Beta:

    def fun1(self):
        print("Inside the Beta fun1()")

class Gamma(Alpha, Beta):
    pass

g = Gamma()
g.fun1()

# help(Gamma)
# print(Gamma.__mro__)
print(Gamma.mro())
'''

'''class A:
    def fun(self):
        print('A')

class B:
    def fun(self):
        print('B')

class C:
    def fun(self):
        print('C')

class D:
    def fun(self):
        print('D')

class E(A,B):
    def fun(self):
        print('E')

class F(C,D):
    def fun(self):
        print('F')

class G(E,F):
    def fun(self):
        print('G')
        pass

g = G()
g.fun()

# help(G)
print(G.__mro__)
print(G.mro())


'''

# Inherited Method // Overridem Method // Spwcialized Method

'''class Messenger:
    def send_message(self):
        print("Text messaga is sent")

    def receive_message(self):
        print("Text message is sent")


class InternalMessegger(Messenger):
    pass

class WhatsappMessenger(Messenger):

    def send_message(self):
            print("Photo, Video, Text messaga is sent")


    def receive_message(self):
            print("Video, photo, Text message is sent")

    def set_dp(self):
         print("Set a DP")

    def set_status(self):
         print("Set a Staatus")

IM = InternalMessegger()
IM.send_message()
IM.receive_message()

WM = WhatsappMessenger()
WM.send_message()
WM.receive_message()'''

# super() method

'''class Customer:
    def __init__(self,name, ph, email):
        self.name = name
        self.ph = ph
        self.email = email

class PlatinumCustomer(Customer):

    def __init__(self, name, ph, email, plat_id):
        super().__init__(name,ph,email) # Call parent constructor
        # self.name = name
        # self.ph = ph
        # self.email = email
        self.plat_id = plat_id

    def display(self):
        print(self.__dict__)

def main():
    PC = PlatinumCustomer('Iranna',9019880821, 'veereshkanamadi@gmail.com',9)
    PC.display()

if __name__ == '__main__':
    main()
'''


'''class Customer:
    def __init__(self, name, ph, email):
        self.name = name
        self.ph = ph
        self.email = email


    def place_order(self,dish):
        cost = 0
        del_charge = 50

        if dish == 'pizza':
            cost = 500 + del_charge

        else:
            cost = 200 + del_charge

        return cost

class PlatinumCustomer(Customer):

    def __init__(self,name, ph, email, plat_id):
        super().__init__(name,ph,email)
        self.plat_id = plat_id

    def place_order(self, dish):
        del_charge = 50

        return (super().place_order(dish) - del_charge) * 0.95

def main():
    Pc = PlatinumCustomer('Iranna', 9029880822, 'veere@123', 10)
    print(Pc.place_order('banana'))

if __name__  == '__main__':
    main()'''

'''class A:
    def fun(self):
        print('A')

class B(A):
    def fun (self):
        print('B')

class C(B):
    def fun(self):
        super(B,self).fun() 
        print('C')

c = C()
c.fun()


class A:
    def fun(self):
        print('A')

class B:
    def fun(self):
        print('B')

class C(A,B):
    def test(self):
        super().fun()
        print('C')

c = C()
# help(c)
c.test()'''

# Extending 
# without using Extending built in python

'''class Contact:

    all_contact = []

    def __init__(self,name, email):
        self.name = name
        self.email = email
        Contact.all_contact.append(self)


    def display(self):
        print(self.__dict__)

def main():
    c1 = Contact('Iranna','Iranna!321')
    c2 = Contact('Preetam','Iranna@123')

    # c1.display()
    # c2.display()

    for i in Contact.all_contact:
        i.display()

    name = 'Iranna'
    for i in Contact.all_contact:
        if i.name == name:
            print('Contact Found')

if __name__ == '__main__':
    main()
'''
# using Extending built in python

class ContactList(list):

    def display_all_contacts(self):
        for i in self:
            i.display()

    def search_contact(self,name):
        for i in self:
            if i.name == name:
                return 'Contact Found'

        return 'Contact Not Found'

class Contact:

    all_contact = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contact.append(self)


    def display(self):
        print(self.__dict__)

def main():
    c1 = Contact('iranna','veera@gmail.com')
    c2 = Contact('veeresh','irann@gmail.com')

    Contact.all_contact.display_all_contacts()

    print(Contact.all_contact.search_contact('iranna'))

if __name__ == '__main__':
    main()




    

     








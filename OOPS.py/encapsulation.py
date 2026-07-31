'''It can calling directly someone misuse'''

'''class AccountHolder:
    def __init__(self):
        self.bal = 10000

ah = AccountHolder()
print(ah.bal)
ah.bal = -20000
print(ah.bal)'''

# We are not direct  Acess the instance knoe ex, ah.bal
'''class AccountHolder:
    def __init__(self):
        self.bal = 10000


    def get_bal(self):
        return self.bal

    def set_bal(self,amt):
        if amt > 0:
            self.bal = amt

        else:
            print("Invald Amount")

ah = AccountHolder()

# print(ah.bal)
print(ah.get_bal())
ah.set_bal(-20000)
print(ah.get_bal())'''


'''class AccountHolder:
    def __init__(self):
        self._bal = 10000

    def get_bal(self):
        return self._bal

    def set_bal(self, amt):
        if amt > 0:
            self._bal = 20000

        else:
            print("Invalid Amout")

ah = AccountHolder()'''

# We cannot Access Direct

# print(ah.bal)
# ah.bal = 20000
# print(ah.bal)


# print(ah._bal)
# ah_bal = 20000
# print(ah_bal)


# ah.set_bal(20000)
# print(ah.get_bal())
# print(ah.__dict__)

# Using the Mangling Concept

'''class AccountHolder:
    def __init__(self):
        self.__bal = 10000

    def get_bal(self):
        return self.__bal

    def set_bal(self,amt):
        if amt > 0:
            self.__bal = amt

        else:
            print("Invalid Amount")

ah = AccountHolder()
# print(ah.__bal)
print(ah.__dict__)
print(ah._AccountHolder__bal)
# ah.__bal = 20000
# print(ah.__dict__) ah.__dict__['__bal'] = 20000
ah.set_bal(20000)

print(ah.get_bal())'''

# Using the Property method

'''class AccountHolder:
    def __init__(self):
        self.__bal = 10000

    def get_bal(self):
        return self.__bal

    def set_bal(self,amt):
        if amt > 0:
            self.__bal = amt

        else:
            print("Invalid Amount")

    bal = property(get_bal,set_bal)

ah = AccountHolder()
print(ah.bal)'''

# using @Decorator

class AccountHolder:
    def __init__(self):
        self.__bal = 10000

    @property
    def bal(self):
        return self.__bal
    
    @bal.setter
    def bal(self,amt):
        if amt > 0:
            self.__bal = amt

        else:
            print("Invalid Amount")

    # bal = property(get_bal,set_bal)

ah = AccountHolder()
print(ah.bal)























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

class A:
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



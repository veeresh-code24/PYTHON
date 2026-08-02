# one to one Relation

'''class Messenger:

    def use_keyboard(self):
        print('Use Kerboard: ')

    def send_Message(self):
        print('Sent a message: ')

    def receice_message(self):
        print('receive a message: ')

class Whatsapp(Messenger):

    def send_Message(self):
            print('Sent a message WT: ')
    
    def receice_message(self):
        print('receive a message WT: ')


class FacebookMessenger(Messenger):

    def send_Message(self):
        print('Sent a message FM: ')
         
    def receice_message(self):
        print('receive a message FM: ')


class InstaMessenger(Messenger):

    def send_Message(self):
        print('Sent a message IM: ')
             
    def receice_message(self):
        print('receive a message IM: ')

wm =  Whatsapp()
fm = FacebookMessenger()
im = InstaMessenger()

wm.use_keyboard()
wm.send_Message()
wm.receice_message()

fm.use_keyboard()
fm.receice_message()
fm.send_Message()

im.use_keyboard()
im.send_Message()
im.receice_message()
'''


# Polymorphism one to many Realtion
# specialized not present in 


'''class Messenger:

    def use_keyboard(self):
        print('Use Kerboard: ')

    def send_Message(self):
        print('Sent a message: ')

    def receice_message(self):
        print('receive a message: ')

class Whatsapp(Messenger):

    def send_Message(self):
            print('Sent a message WT: ')
    
    def receice_message(self):
        print('receive a message WT: ')


class FacebookMessenger(Messenger):

    def send_Message(self):
        print('Sent a message FM: ')
         
    def receice_message(self):
        print('receive a message FM: ')


class InstaMessenger(Messenger):

    def send_Message(self):
        print('Sent a message IM: ')
             
    def receice_message(self):
        print('receive a message IM: ')

def use_message(ref):

    ref.use_keyboard()
    ref. send_Message()
    ref.receice_message()



wm =  Whatsapp()
fm = FacebookMessenger()
im = InstaMessenger()

use_message(wm)
use_message(fm)
use_message(im)'''

# specialized present in using a Duck Type overcom this solution

class Messenger:

    def use_keyboard(self):
        print('Use Kerboard: ')

    def send_Message(self):
        print('Sent a message: ')

    def receice_message(self):
        print('receive a message: ')

class Whatsapp(Messenger):

    def send_Message(self):
            print('Sent a message WT: ')
    
    def receice_message(self):
        print('receive a message WT: ')

    def sent_live_location(self):
        print('sent a live location: ')

class FacebookMessenger(Messenger):

    def send_Message(self):
        print('Sent a message FM: ')
         
    def receice_message(self):
        print('receive a message FM: ')

    def built_in_apps(self):
        print('Use builti in apps using the Fb')


class InstaMessenger(Messenger):

    def send_Message(self):
        print('Sent a message IM: ')
             
    def receice_message(self):
        print('receive a message IM: ')

    def add_filter(self):
        print('use the filter using the instagram: ')

def use_message(ref):

    ref.use_keyboard()
    ref. send_Message()
    ref.receice_message()
    if type(ref) == InstaMessenger:
        ref.add_filter()

    if type(ref) == FacebookMessenger:
        ref.built_in_apps()

    if type(ref) == Whatsapp:
        ref.sent_live_location()



wm =  Whatsapp()
fm = FacebookMessenger()
im = InstaMessenger()

use_message(wm)
use_message(fm)
use_message(im)








     






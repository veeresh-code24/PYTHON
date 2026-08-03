'''class VoiceAssistant:

    def activate_assisstant(self):
        print('VA')

    def perform_task(self):
        print('VA perform task')

    def use_built_in_apps(self):
        print('VA used built in apps')

class Siri(VoiceAssistant):

    def activate_assisstant(self):
            print('SI')
    
    def perform_task(self):
        print('siri perform task')
    
    def use_built_in_apps(self):
        print('siri used built in apps')


class Alexa(VoiceAssistant):

    def activate_assisstant(self):
        print('Alexa')
     
    def perform_task(self):
        print('alexa perform task')
     
    def use_built_in_apps(self):
        print('alexa used built in apps')

class GoogleAssistant(VoiceAssistant):

    def activate_assisstant(self):
        print('Google Assis')

    def perform_task(self):
        print('google perform task')

    def use_built_in_apps(self):
        print('google used built in apps')

def use_assistant(ref):

    ref.activate_assisstant()
    ref.perform_task()
    ref.use_built_in_apps()


s = Siri()
a = Alexa()
g = GoogleAssistant()

# s.activate_assisstant()
# s.perform_task()
# s.use_built_in_apps()

use_assistant(s)
use_assistant(a)
use_assistant(g)'''

'''from abc import ABC, abstractmethod
class VoiceAssistant(ABC):

    @abstractmethod
    def activate_assisstant(self):
        pass

    @abstractmethod
    def perform_task(self):
        pass
        
    @abstractmethod
    def use_built_in_apps(self):
        pass
        

class Siri(VoiceAssistant):

    def activate_assisstant(self):
            print('SI')
    
    def perform_task(self):
        print('siri perform task')
    
    def use_built_in_apps(self):
        print('siri used built in apps')


class Alexa(VoiceAssistant):

    def activate_assisstant(self):
        print('Alexa')
     
    def perform_task(self):
        print('alexa perform task')
     
    def use_built_in_apps(self):
        print('alexa used built in apps')

class GoogleAssistant(VoiceAssistant):

    def activate_assisstant(self):
        print('Google Assis')

    def perform_task(self):
        print('google perform task')

    def use_built_in_apps(self):
        print('google used built in apps')

def use_assistant(ref):

    ref.activate_assisstant()
    ref.perform_task()
    ref.use_built_in_apps()


s = Siri()
a = Alexa()
g = GoogleAssistant()

use_assistant(s)
use_assistant(a)
use_assistant(g)
'''

# we cannot create object when abstarct class can contain a abstarct method

'''from abc import ABC, abstractmethod
class VoiceAssistant(ABC):

    @abstractmethod
    def activate_assisstant(self):
        pass

    @abstractmethod
    def perform_task(self):
        pass
        
    @abstractmethod
    def use_built_in_apps(self):
        pass

    def fun(self):
        print('Hello')

va = VoiceAssistant()
va.fun()
va.use_built_in_apps()
'''

# But we can overriden from another class we can create a object

from abc import ABC, abstractmethod
class VoiceAssistant(ABC):

    @abstractmethod
    def activate_assisstant(self):
        pass

    @abstractmethod
    def perform_task(self):
        pass
        
    @abstractmethod
    def use_built_in_apps(self):
        pass
        

class Siri(VoiceAssistant):

    def activate_assisstant(self):
            print('SI')
    
    def perform_task(self):
        print('siri perform task')
    
    def use_built_in_apps(self):
        print('siri used built in apps')


siri = Siri()
siri.perform_task()
siri.activate_assisstant()
siri.use_built_in_apps()
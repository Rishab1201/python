class person :
    #constructor

    def __init__(self,name):
        self.name = name

    def say(self):
        print("my name is :",self.name)

p = person('Rishab')

p.say()
class leran:

    def __init__(self,name,std,profession):
        self.name = name
        self.std = std
        self.profession =profession

    def speak(self):
        print("My name is {}".format(self.name))
        print("My profession is {}".format(self.std))
        print("My profession is {}".format(self.profession))

obj = leran("Abhinay RAI","Working","Engineer")

obj.speak()
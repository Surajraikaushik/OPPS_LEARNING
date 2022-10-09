class my_details :
    #empty class

    #class attribute
    attr = "Abhinay"
    print("Class details")

    #Instance attribute
    def __init__(self,name):
        self.name =name



obj = my_details('Abhinay12')
obj2 = my_details('Vandana')

#Accessing class attribute
print("My name is {}".format(obj.__class__.attr))
#Accessing instance class attribute
print("My name is {}".format(obj2.name))
## classes and Objects 

#object has state(data) and behavior(code) and objects get their variables and functions from classes.
## objects are instances of classes
#classes are esentialy template to create your templates 

##Classes – the definitions for the data format and available procedures for a given type or class of object; may also contain data and procedures 
# (known as class methods) themselves, i.e. classes contain the data members and member functions
##Class variables – belong to the class as a whole; there is only one copy of each one
#Instance variables or attributes – data that belongs to individual objects; every object has its own copy of each one
#Member variables – refers to both the class and instance variables that are defined by a particular class
#Class methods – belong to the class as a whole and have access only to class variables and inputs from the procedure call
#Instance methods – belong to individual objects, and have access to instance variables for the specific object they are called on, inputs, and class variables

class my_class:
    variable = "blah"

    def funcname(self):
        print("This is the message inside the class")
#myobjectx = my_class()
#print(myobjectx.variable)

#myobjecty = my_class()
#myobjecty.variable = "abc"
#print(myobjecty.variable)


myobjectx = my_class()
myobjectx.funcname()
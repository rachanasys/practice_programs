#write a python program to Implement object oriented programming with a class and an object
#object-orientation: let us START SEEING everything as an object
#what is orientation?
#perspective, point of view, the way of look at something

#what is object-orientation?
#the process of CONSIDERING EVERYTHING AROUND US-as a collection of objects.

#{everything around is a collection of objects.}

#we now know what is orientation, and object orientation, what is object??
#object is a real-world entity which is having physical existence.
#object is a real-world entity which is having physical existence.
#object is a real-world entity which is having physical existence.
#object is a real-world entity which is having physical existence.
#object is a real-world entity which is having physical existence.
#object is a real-world entity which is having physical existence.
#object is a real-world entity which is having physical existence.
#object is a real-world entity which is having physical existence.

#object is also called as an instance of a class.

#ex: student object, teacher object, fan object, book object, pen object

#sometimes, an object is not fully unique, it is derived from another object..
#with one or more modifications.... that is what we call as inheritance...
#by modifying some properties, deleting some other properties, adding some other properties 
#to an existing object, we can and normally do create new objects

#semiconductor from silicon
#sugar water by adding sugar to water
#i feel like this is an excellent example of inheritance..
#we can inherit features, and keep them as it is, modify them, delete them?
class Water:
    color='colorless'
    state='liquid'

    def quantize(self,q):
        self.quantity=q

    def taste(self):
            print("i am tasteless!!")

    def flow(self):
        print("i am water, i flow")
class SugarWater(Water):
    color='light yellow'
    def taste(self):
        print("i am sweet!!")
w1=Water()
w1.flow()
w1.taste()
w2=SugarWater()
w2.flow()
w2.taste()
print(w2.color)    

#python is an object oriented programming language
#in python, everything is considered as an object

#in order to create an object, COMPULSORILY, CLASS is required!!!!!

#in order to create an object, COMPULSORILY, CLASS is required!!!!!

#in order to create an object, COMPULSORILY, CLASS is required!!!!!

#in order to create an object, COMPULSORILY, CLASS is required!!!!!

#in order to create an object, COMPULSORILY, CLASS is required!!!!!

#in order to create an object, COMPULSORILY, CLASS is required!!!!!

#in order to create an object, COMPULSORILY, CLASS is required!!!!!

#in order to create an object, COMPULSORILY, CLASS is required!!!!!

#in order to create an object, COMPULSORILY, CLASS is required!!!!!

#in order to create an object, COMPULSORILY, CLASS is required!!!!!

#in order to create an object, COMPULSORILY, CLASS is required!!!!!

#now you realise that, in order to create an object, a class is required
#don't you wanna know what is a class??

#what is a class?
#class is a blueprint/a template using which PVM would create an object.

#class does not have any existence, only an object would be having physical existence.

#without class, it is not possible to create an object

#python project is a collection of objects.
#in python, there is no useless object...all objects are useful..

#objects do not exist in isolation, Rather they would be constantly interacting..with each other

#every object in python BELONG to a particular category/classification(class)
#that category is called a class
#class does not have physical existence, whereas an object have physical existence...

#every object is having some properties and shows some behavior...

#has part is managed using variables/attributes.
#does part is managed using methods/functions.


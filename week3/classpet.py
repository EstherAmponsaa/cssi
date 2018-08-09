class Pet:

        '''_init_()is a method of the class pet .
        A method is a function that belongs to a class instance.
        All methods of a class first parameter is self'''

    def _init_(self,name,age):


'''self.name and self.age are instance attributes or
data members of the class Pet. instance attributes
are unique in every occurrance (instance) of a Pet
object'''

        self.name = name
        self.age = age
        self.animal = animal
        self.is_hunger = False
        self.mood = "happy"
    def eat(self):
        self.is_hungry = False

    def _str_(self):
        return "{0} {1}".format    


''' The pet class has the members age ,name,count,_init()_self.
To call the _init_() functionwe use the class name with the
respective parameters within parenthesis'''

def makeHunger(pet):
    pet.is_hungry = True

o = Pet("Dog",3)

t = Pet("Cat",4)

print "Before call to makeHunger() "
print o.name, o.age, o.is_hungry
print t.name, t.age, t.is_hungry

makeHunger(o)


print "Before call to makeHunger() and before call to eat()"
print o.name, o.age, o.is_hungry
print t.name, t.age, t.is_hungry

o.eat()

print "Before call to makeHunger() "
print o.name, o.age, o.is_hungry
print t.name, t.age, t.is_hungry

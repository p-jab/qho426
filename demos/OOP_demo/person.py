#The class Person is a blueprint for my objects to store info about people
class Person:

    #CLASS Attribute -> attribute/feature accessible to every object
    MAX_W = 150

    #Static Method -> Utility function that does NOT require
    #an object to work on
    def is_mature(age):
        if age >= 18:
            return "Person is mature"
        else:
            return "Person is immature"

    #Initialiser/Constructor - function automatically called when
    # object is instantiated (magic method)
    #Initialiser of ANY class has the same name
    #"self" - reference to specific object beijng instantiated
    #DUNDER - Double Underscore
    def __init__(self, name="Maria", age=0, job="None", w=MAX_W):
        #Instance Attributes -> Features of the object
        self.name = name
        self.age = age
        self.job = job
        if w > Person.MAX_W:
            self.weight = Person.MAX_W
        else:
            self.weight = w
        #str() magic method -> invoked automatically when print()
        # function is called [informal representation]
    def __str__(self):
        return f"{self.name} is {self.age} years old. They work as {self.job} and weight {self.weight}kg."
    #Magic Method repr provides "formal representation of an
    #object via string. How we wish to store object for later
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, job={self.job},weight={self.weight})"
    #Method - function attached to a specific data type (class)
    #Instance Method -> a method that applies to specific instance
    #of the class
    def eat(self, food, w):
        print(f"{self.name} has eaten {food}")
        self.weight += w
        print(f"{self.name} now weights {self.weight}kg")

    def exercise(self, burned):
        self.weight -= burned
        print(f"{self.name} now weights {self.weight}kg")

if __name__ == "__main__":
    p1 = Person("Mark", 20, "Accountant", 65)
    p2 = Person(age=75, w=120)
    p1.eat("Sandwich", 0.6)
    p1.eat("Apple", 0.2)
    p2.exercise(0.5)
    p2.eat("Pizza", 1.2)
    p2.exercise(0.9)
    print(Person.is_mature(50))
    print(Person.is_mature(p2.age))
    # print(p1)
    # print(repr(p1))
    # print(p2)
    # print(repr(p2))
    # print(f"We have {p1.name} and {p2.name} who altogether weight {p1.weight + p2.weight}kg")

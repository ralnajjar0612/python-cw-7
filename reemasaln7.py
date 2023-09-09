class Person:
    name= "Reemas"
    age= 17

    def is_adult():
            if Person>18:   
                print("You have too much responsibilities") 
            else:
                print("Lucky you")

first_person= Person()
print(first_person.name)
print(first_person.age)

print(first_person.is_adult)   

class Person2:
    def __init__(self, name, age):
        self.name= name
        self.age= age

    def __str__(self):
        return f"My name is {self.name} and I am {self.age} years old."
    

second_person= Person2("Anwar", 25)
print(second_person)
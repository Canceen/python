import pandas


class Person:
    def __init__(self, age, weight, height, first_name, last_name):
        self.age = age
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.last_name = last_name

    def walk(self):
        print("Walking..")
        
    def run(self):
        print("Running...")  

user = Person(34, "100KG", "6'2", "Tony", "Carter")

user.run()
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"CLASS OBJECT: {self.name}: {self.age}, {self.salary}"


# test = Employee("hong", 41, 9000)
# print(test)
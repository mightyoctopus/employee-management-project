class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"MyClass -- Name: {self.name}, Age: {self.age}, Salary: {self.salary}"




#
# arr = []
# test = Employee("Hong", 41, 8000)
#
# print(test)

# arr.append(test)

# print(arr)

# for item in arr:
#     print(item.age)

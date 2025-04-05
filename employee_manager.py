from employee import Employee

class EmployeeManager:
    def __init__(self):
        self.employee_list = []

    def add_employee(self):
        name = input("Enter the name: ")
        age = int(input("Enter the age: "))
        salary = int(input("Enter the salary: "))

        if not name:
            print("Please type in a valid name.")
        elif not age or not salary:
            print("Please type in valid number.")
        elif age <= 0 or salary <= 0 :
            print("Please type in valid number greater than 0.")
        else:
            self.employee_list.append(Employee(name, age, salary))
            print(self.employee_list)

    def list_employees(self):
        if len(self.employee_list) == 0:
            print("There are no employees.")
        for employee in self.employee_list:
            print(employee)

    def delete_employee_by_age_range(self):
        start_age = int(input("What's the starting age?"))
        end_age = int(input("What's the end age?"))

        if len(self.employee_list) == 0:
            print("There are no employees.")

        for employee in self.employee_list:
            if start_age <= employee.age <= end_age:
                self.employee_list.remove(employee)
                print("Employee successfully removed from the system.")

    def update_employee_salary(self):
        name = input("What's the name of the employee that you want to update on? ")
        salary = input("What's the new salary amount? ")
        if len(self.employee_list) == 0:
            print("There are no employees.")

        for employee in self.employee_list:
            if employee.name == name:
                employee.salary = salary
                print("Salary has been updated.")












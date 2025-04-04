from employee import Employee

class EmployeeManager:
    def __init__(self):
        self.employee_list = []

    def add_new_employee(self):
        print("Add a new employee. ")
        name = input("Enter employee name. ")
        age = input("Enter the age of the employee. ")
        salary = input("What's the salary of the employee? ")

        self.employee_list.append(Employee(name, age, salary))

    def list_employees(self):
        if len(self.employee_list) == 0:
            print("There's no employee!")
            return
        else:
            for emp in self.employee_list:
                print(emp)

    def delete_employees_by_age(self, age_from, age_to):

        if len(self.employee_list) == 0:
            print("No employee found.")
            return

        for emp in self.employee_list:
            if age_from <= int(emp.age) <= age_to:
                print(f"Deleting employee {emp.name}")
                self.employee_list.remove(emp)
                print(f"{emp} was removed successfully!")


    def find_employee_by_name(self, name):
        for emp in self.employee_list:
            if emp.name == name:
                return emp
        return None

    def update_salary_by_name(self, name, new_salary):

        emp = self.find_employee_by_name(name)

        if emp is None:
            print("Error: No employee found.")
        else:
            emp.salary = new_salary
            print("Salary modification was successfully done!")






# test_employee = EmployeeManager()
# print(test_employee.employee_list)









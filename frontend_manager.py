from employee import Employee
from employee_manager import EmployeeManager

class FrontendManager:
    def __init__(self):
        self.EmployeeManager = EmployeeManager()

    def print_menu(self):
        messages = [
            '1) Add a new employee',
            '2) List all employees',
            '3) Delete by age range',
            '4) Update salary given a name',
            '5) End the program',
        ]
        for message in messages:
            print(message)

    def run(self):
        while True:
            print("Choose what you want to process:")
            self.print_menu()
            choice = int(input("Your Selection: "))

            if choice == 1:
                self.EmployeeManager.add_new_employee()
            elif choice == 2:
                self.EmployeeManager.list_employees()
            elif choice == 3:
                start_age = int(input("What's the start age? "))
                end_age = int(input("What's the end age? "))
                self.EmployeeManager.delete_employees_by_age(start_age, end_age)
            elif choice == 4:
                name = input("What's the name of the employee for salary change? ")
                salary = int(input("What's the new salary amount? "))
                self.EmployeeManager.update_salary_by_name(name, salary)
            else:
                print("Goodbye...")
                break
            print("\n")

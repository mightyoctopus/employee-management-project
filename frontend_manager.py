from employee_manager import EmployeeManager

class FrontendManager:
    def __init__(self):
        self.EmployeeManager = EmployeeManager()

    def menu_ui(self):
        menu = [
            "1) Add Employee",
            "2) View Employee List",
            "3) Delete Employee By Age",
            "4) Update Employee Salary",
            "5) End The Program"
        ]

        for item in menu:
            print(item)


    def run(self):
        while True:
            print("Choose what you want to proceed to: ")
            self.menu_ui()
            choice = input("Enter your number: ")

            match choice:
                case "1":
                    self.EmployeeManager.add_employee()
                case "2":
                    self.EmployeeManager.list_employees()
                case "3":
                    self.EmployeeManager.delete_employee_by_age_range()
                case "4":
                    self.EmployeeManager.update_employee_salary()
                case "5":
                    print("Program ends...")
                    break
            print("\n")

            # self.EmployeeManager.add_employee()


from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def display_details(self):
        pass


class Manager(Employee):
    def __init__(self, emp_id, name, basic_salary, bonus):
        super().__init__(emp_id, name)
        self.basic_salary = basic_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.basic_salary + self.bonus

    def display_details(self):
        print(f"\nManager | ID:{self.emp_id} | Name:{self.name}")
        print(f"Basic Salary : {self.basic_salary}")
        print(f"Bonus        : {self.bonus}")
        print(f"Net Salary   : {self.calculate_salary()}")


class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary):
        super().__init__(emp_id, name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

    def display_details(self):
        print(f"\nFull Time | ID:{self.emp_id} | Name:{self.name}")
        print(f"Monthly Salary : {self.monthly_salary}")


class Intern(Employee):
    def __init__(self, emp_id, name, stipend):
        super().__init__(emp_id, name)
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend

    def display_details(self):
        print(f"\nIntern | ID:{self.emp_id} | Name:{self.name}")
        print(f"Stipend : {self.stipend}")


class PayrollSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self):
        emp_id = input("Employee ID: ")
        if emp_id in self.employees:
            print("Employee already exists.")
            return
        name = input("Name: ")
        print("1.Manager\n2.Full Time\n3.Intern")
        ch = input("Choice: ")

        try:
            if ch == "1":
                basic = float(input("Basic Salary: "))
                bonus = float(input("Bonus: "))
                emp = Manager(emp_id, name, basic, bonus)
            elif ch == "2":
                salary = float(input("Monthly Salary: "))
                emp = FullTimeEmployee(emp_id, name, salary)
            elif ch == "3":
                stipend = float(input("Stipend: "))
                emp = Intern(emp_id, name, stipend)
            else:
                print("Invalid choice")
                return
            self.employees[emp_id] = emp
            print("Employee Added Successfully.")
        except ValueError:
            print("Invalid salary value.")

    def remove_employee(self):
        emp_id = input("Employee ID: ")
        if emp_id in self.employees:
            del self.employees[emp_id]
            print("Employee Removed.")
        else:
            print("Employee Not Found.")

    def display_all(self):
        if not self.employees:
            print("No employees.")
            return
        for emp in self.employees.values():
            emp.display_details()

    def generate_payslip(self):
        emp_id = input("Employee ID: ")
        emp = self.employees.get(emp_id)
        if emp:
            print("\n------ PAYSLIP ------")
            emp.display_details()
            print(f"Payable Salary : {emp.calculate_salary()}")
            print("---------------------")
        else:
            print("Employee Not Found.")

    def total_payroll(self):
        total = sum(emp.calculate_salary() for emp in self.employees.values())
        print(f"Total Payroll = {total}")

    def menu(self):
        while True:
            print("\n===== Employee Payroll System =====")
            print("1. Add Employee")
            print("2. Remove Employee")
            print("3. Display All Employees")
            print("4. Generate Payslip")
            print("5. Calculate Total Payroll")
            print("6. Exit")

            choice = input("Enter Choice: ")

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.remove_employee()
            elif choice == "3":
                self.display_all()
            elif choice == "4":
                self.generate_payslip()
            elif choice == "5":
                self.total_payroll()
            elif choice == "6":
                print("Thank You!")
                break
            else:
                print("Invalid Choice")


if __name__ == "__main__":
    PayrollSystem().menu()

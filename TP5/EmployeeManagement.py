class Employee:
    company = "ITC"
    employee_count = 0

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        Employee.employee_count += 1

    def display_info(self):
        print(f"Company: {Employee.company}")
        print(f"Employee: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: {self.salary}")
        print()

    @classmethod
    def get_employee_count(cls):
        return cls.employee_count


emp1 = Employee("Nary", "Network Engineer", 1000)
emp2 = Employee("Somphors", "Data Analyst", 1100)
emp3 = Employee("Kakrona", "Teaching Assistant", 850)
emp4 = Employee("Mary", "System Administrator", 1200)

emp1.display_info()
emp2.display_info()
emp3.display_info()
emp4.display_info()

print(f"Total Employees: {Employee.get_employee_count()}")
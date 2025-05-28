class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def display_info(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}")

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  

    def show_department_details(self):
        print(f"Department: {self.dept_name}")
        self.employee.display_info()

emp1 = Employee(101, "Tanzeela")
dept1 = Department("HR", emp1)
dept1.show_department_details()

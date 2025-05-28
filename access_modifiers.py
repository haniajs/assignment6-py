class Employee:
    def __init__(self, name, salary, ssn):
        self.name  = name
        self._salary = salary
        self.__ssn = ssn

    def get_ssn(self):
        return self.__ssn
    
    def set_salary(self, new_salary):
        if new_salary > 0:
            self._salary = new_salary
        else:
            print("salary must be positive in number")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")

class Manager(Employee):
    def __init__(self, name, salary, ssn, department):
        super().__init__(name, salary, ssn)
        self.department = department

    def show_manager_info(self):
        print(f"Manager: {self.name}")
        print(f"Department: {self.department}")
        print(f"Protected Salary: {self._salary}")
        print(f"Acessing SSN via getter command: {self.get_ssn()}")

m = Manager("Afnan", "100000", "444-958-2025", "Information Technology")
m.show_manager_info()
m.set_salary(200000)
print("Update Salary:" , m._salary)

#print(m.__ssn)
print("private SSN via managed: ", m._Employee__ssn)

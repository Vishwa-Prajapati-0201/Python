# Create a class "Employee" with attributes name and salary. Implement overloaded operators +
# and - to combine and compare employees based on their salaries.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        return Employee(self.name + " & " + other.name, self.salary + other.salary)

    def __sub__(self, other):
        return abs(self.salary - other.salary)

    def __str__(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

if __name__ == "__main__":
    name1 = input("Enter first employee name: ")
    salary1 = float(input("Enter first employee salary: "))
    emp1 = Employee(name1, salary1)
    
    name2 = input("Enter second employee name: ")
    salary2 = float(input("Enter second employee salary: "))
    emp2 = Employee(name2, salary2)
    
    combined_employee = emp1 + emp2
    salary_difference = emp1 - emp2
    
    print("Combined Employee:", combined_employee)
    print("Salary Difference:", salary_difference)
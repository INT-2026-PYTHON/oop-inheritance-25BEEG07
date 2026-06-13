class Employee:
    company = "Acme Corp"
    raise_pct = 5
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def apply_raise(self):
        self.salary += self.salary * Employee.raise_pct / 100
    @classmethod
    def set_raise_percentage(cls, new_pct):
        cls.raise_pct = new_pct
    @classmethod
    def from_string(cls, csv_line):
        name, salary = csv_line.split(",")
        return cls(name, float(salary))
    @staticmethod
    def is_valid_salary(amount):
        return isinstance(amount, (int, float)) and amount > 0
e1 = Employee("Alice", 100000)
e2 = Employee("Bob", 80000)
e3 = Employee.from_string("Carol,75000")
e1.apply_raise()
e2.apply_raise()
e3.apply_raise()
print("After 5% raise:")
print(f"{e1.name} -> {e1.salary}")
print(f"{e2.name} -> {e2.salary}")
print(f"{e3.name} -> {e3.salary}")
Employee.set_raise_percentage(10)
e1.apply_raise()
e2.apply_raise()
e3.apply_raise()
print("\nAfter additional 10% raise:")
print(f"{e1.name} -> {e1.salary}")
print(f"{e2.name} -> {e2.salary}")
print(f"{e3.name} -> {e3.salary}")
print("\nSalary Validation:")
print("is_valid_salary(50000)  ->", Employee.is_valid_salary(50000))
print("is_valid_salary(-100)   ->", Employee.is_valid_salary(-100))
print('is_valid_salary("abc")  ->', Employee.is_valid_salary("abc"))
print("is_valid_salary(0)      ->", Employee.is_valid_salary(0))
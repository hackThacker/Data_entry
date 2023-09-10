import pandas as pd
from openpyxl import Workbook

# Define a class for an Employee
class Employee:
    def __init__(self, id, first_name, last_name, location, age, mobile):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.mobile = mobile
        self.operator_name = self.get_operator_name(mobile)

    def get_operator_name(self, mobile):
        prefixes = {
            '984': 'NTC',
            '985': 'NTC',
            '986': 'NTC',
            '976': 'NTC',
            '974': 'NTC',
            '975': 'NTC',
            '980': 'Ncell',
            '981': 'Ncell',
            '982': 'Ncell',
            '970': 'Ncell'
        }

        prefix = mobile[:3]
        return prefixes.get(prefix, 'Unknown')

    def display(self):
        print("Employee ID:", self.id)
        print("Employee Name:", self.first_name, self.last_name)
        print("Employee Location:", self.location)
        print("Employee Age:", self.age)
        print("Employee Mobile Number:", self.mobile)
        print("Operator Name:", self.operator_name)

# Create an empty list to store employees
employees = []
next_employee_id = 1  # Initialize the ID for the first employee

while True:
    print("\nMenu:")
    print("1. Create Employee")
    print("2. Read Employee Data")
    print("3. Save to CSV")
    print("4. Save to Excel")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        # Automatically increment the employee ID
        id = next_employee_id
        next_employee_id += 1

        first_name = input("Enter Employee First Name: ")
        last_name = input("Enter Employee Last Name: ")
        location = input("Enter Employee Location: ")
        age = int(input("Enter Employee Age: "))
        mobile = input("Enter Employee Mobile Number: ")

        # Validate mobile number length
        if len(mobile) == 10:
            emp = Employee(id, first_name, last_name, location, age, mobile)
            employees.append(emp)
            print("Employee created successfully.")
        else:
            print("Invalid mobile number. Mobile number should be 10 digits long.")

    elif choice == 2:
        if len(employees) > 0:
            search_id = int(input("Enter Employee ID to read data: "))
            found = False

            for emp in employees:
                if emp.id == search_id:
                    emp.display()
                    found = True
                    break

            if not found:
                print(f"Employee with ID {search_id} not found.")
        else:
            print("No employees to read.")

    elif choice == 3:
        if len(employees) > 0:
            # Save data to CSV
            data = []
            for emp in employees:
                data.append([emp.id, emp.first_name, emp.last_name, emp.location, emp.age, emp.mobile, emp.operator_name])

            df = pd.DataFrame(data, columns=['ID', 'First Name', 'Last Name', 'Location', 'Age', 'Mobile', 'Operator Name'])
            df.to_csv('employees.csv', index=False)
            print("Employee data saved to employees.csv.")
        else:
            print("No employees to save.")

    elif choice == 4:
        if len(employees) > 0:
            # Save data to Excel
            wb = Workbook()
            ws = wb.active

            # Add headers
            headers = ['ID', 'First Name', 'Last Name', 'Location', 'Age', 'Mobile', 'Operator Name']
            ws.append(headers)

            for emp in employees:
                row_data = [emp.id, emp.first_name, emp.last_name, emp.location, emp.age, emp.mobile, emp.operator_name]
                ws.append(row_data)

            wb.save('employees.xlsx')
            print("Employee data saved to employees.xlsx.")
        else:
            print("No employees to save.")

    elif choice == 5:
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please select a valid option.")

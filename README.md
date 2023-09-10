# Data_entry

Certainly! Here's a comprehensive README.md file for your GitHub repository that provides a detailed explanation of how the code works:

# Employee Data Management System

This Python program is a simple Data Management System that allows you to create, read, and store employee records. It also provides the option to save employee data to CSV and Excel files. The system automatically assigns employee IDs and includes functionality to validate mobile numbers and determine the operator name based on the number's prefix.

## Features

- Create employee records with automatically incremented employee IDs.
- Read and display employee data.
- Save employee data to CSV and Excel files.
- Validate mobile numbers and determine the operator name.

## Prerequisites

Before running the program, ensure that you have Python installed on your system. You'll also need to install the following Python libraries if you haven't already:

- pandas: Used for data manipulation and CSV handling.
- openpyxl: Used for Excel file handling.

You can install these libraries using pip:

```bash
pip install pandas openpyxl
```

## Usage

1. Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/employee-data-management.git
cd employee-data-management
```

2. Run the Python script:

```bash
python employee_management.py
```

3. Follow the on-screen menu to perform various actions:

   - **Create Employee:** Enter employee details, including first name, last name, location, age, and mobile number. The program will automatically assign an employee ID and determine the operator name based on the mobile number prefix.

   - **Read Employee Data:** Search for an employee by entering their ID and view their details.

   - **Save to CSV:** Save all employee data to a CSV file named "employees.csv."

   - **Save to Excel:** Save all employee data to an Excel file named "employees.xlsx."

   - **Exit:** Quit the program.

## Operator Name Determination

The program determines the operator name (NTC or Ncell) based on the starting digits of the mobile number as follows:

- NTC: Mobile numbers starting with 984, 985, 986, 976, 974, or 975.
- Ncell: Mobile numbers starting with 980, 981, 982, or 970.

## Data Validation

- Employee mobile numbers must be 10 digits long.
- The program validates mobile numbers to ensure they meet the required format.

## Sample Data

Sample data for employee records is included in the CSV file "employees.csv" as an example.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Make sure to replace the placeholders like `yourusername` with your actual GitHub username, and customize the repository and license information as needed. This README.md provides a clear and detailed explanation of the project's features, prerequisites, and usage instructions.

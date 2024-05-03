# Importing the FileHandler module to handle binary file operations.
from binary_file_handler import FileHandler

# Defining a class called Employee to manage employee data.
class Employee:
    # Constructor method to initialize employee attributes.
    def __init__(self, name, emp_id, department, job_title, basic_salary, age, dob, passport_details):
        # List to store employee data.
        self.employees = []
        # Assigning attributes with provided values.
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.dob = dob
        self.passport_details = passport_details

    # Method to add a new employee to the list and save to file.
    def add_employee(self, employee_data):
        # Appending employee data to the list.
        self.employees.append(employee_data)
        # Writing the updated list to a binary file.
        FileHandler.write_to_binary_file(self.employees, 'employees.pkl')

    # Method to read employee data from file.
    def read_employees_from_file(self):
        # Returning employee data read from the binary file.
        return FileHandler.read_from_binary_file('employees.pkl')

    # Method to delete an employee by their ID.
    def delete_employee_by_id(self, emp_id):
        # Reading employee data from the file.
        employees = self.read_employees_from_file()
        # If there are employees in the file:
        if employees:
            # Iterating through each employee.
            for employee in employees:
                # Checking if the employee ID matches the provided ID.
                if employee.get('Employee ID') == emp_id:
                    # Removing the employee from the list.
                    employees.remove(employee)
                    # Writing the updated list back to the file.
                    FileHandler.write_to_binary_file(employees, 'employees.pkl')
                    # Returning True indicating successful deletion.
                    return True
            # Returning False if the employee ID was not found.
            return False
        # Returning False if there are no employees in the file.
        else:
            return False
        
    # Method to update an employee's data by their ID.
    def update_employee_by_id(self, emp_id, updated_data):
        # Reading employee data from the file.
        employees = self.read_employees_from_file()
        # If there are employees in the file:
        if employees:
            # Iterating through each employee.
            for employee in employees:
                # Checking if the employee ID matches the provided ID.
                if employee.get('Employee ID') == emp_id:
                    # Updating the employee's data with the provided data.
                    employee.update(updated_data)
                    # Writing the updated list back to the file.
                    FileHandler.write_to_binary_file(employees, 'employees.pkl')
                    # Returning True indicating successful update.
                    return True
            # Returning False if the employee ID was not found.
            return False
        # Returning False if there are no employees in the file.
        else:
            return False

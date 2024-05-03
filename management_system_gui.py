# management_gui.py
# Importing necessary modules and classes.
import tkinter as tk
import datetime
from tkinter import ttk, messagebox
from employee import Employee
from client import Client
from venue import Venue
from event import Event
from guest import Guest
from supplier import Supplier
from binary_file_handler import FileHandler
 
# Defining a class called ManagementGUI to create the GUI for the event management system.
class ManagementGUI:
    # Constructor method to initialize the GUI.
    def __init__(self, master):
        # Initializing the Tkinter root window.
        self.master = master
        # Setting the title of the window.
        self.master.title("Event Management System")

        # Setting the size of the window.
        self.master.geometry("500x350")

        # Setting the background color of the window to light purple.
        self.master.configure(bg="#E6E6FA")
        
        # Creating instances of various classes for managing different aspects of the system.
        self.employee = Employee(
            name="", 
            emp_id="", 
            department="", 
            job_title="", 
            basic_salary="", 
            age="", 
            dob="", 
            passport_details=""
        )

        self.client = Client(
            name="",
            client_id="",
            address="",
            contact_details="",
            budget=""
        )
            
        self.venue = Venue(
            venue_id="",
            name="",
            address="",
            contact="",
            min_guests="",
            max_guests=""
        )
        self.event = Event("","","","","","","","","","","")

        self.guest = Guest("","","","")

        self.supplier = Supplier("","","","","","","")

        # Creating the login page.
        self.create_login_page()

    # Method to create the login page.
    def create_login_page(self):
        # Creating a frame for the login page.
        self.login_frame = tk.Frame(self.master, bg="#E6E6FA")
        self.login_frame.pack(pady=50)

        # Creating a label for the password entry.
        self.password_label = tk.Label(self.login_frame, text="Enter Password:", font=("Arial", 12), bg="#E6E6FA")
        self.password_label.grid(row=0, column=0, padx=5, pady=5)

        # Creating an entry widget for entering the password.
        self.password_entry = ttk.Entry(self.login_frame, show="*", font=("Arial", 12))
        self.password_entry.grid(row=0, column=1, padx=5, pady=5)

        # Creating a login button.
        self.login_button = ttk.Button(self.login_frame, text="Login", command=self.login, style="TButton")
        self.login_button.grid(row=1, columnspan=2, pady=10)

    # Method to handle the login process.
    def login(self):
        # Getting the password entered by the user.
        password = self.password_entry.get()
        # Checking if the password is correct.
        if password == "12345":
            # If correct, create the main menu and destroy the login frame.
            self.create_main_menu()
            self.login_frame.destroy()
        else:
            # If incorrect, show an error message.
            messagebox.showerror("Error", "Incorrect password!")


    def create_main_menu(self):
        self.menu_frame = tk.Frame(self.master, bg="#E6E6FA")
        self.menu_frame.pack(pady=50)

        style = ttk.Style()
        style.configure("TButton", font=("Arial", 12), padding=10, background="black", foreground="black")

        # Create buttons for different functionalities
        employee_button = ttk.Button(self.menu_frame, text="Employee", command=self.open_employee_menu, style="TButton")
        employee_button.grid(row=0, column=0, padx=10, pady=5)

        client_button = ttk.Button(self.menu_frame, text="Client", command=self.open_client_menu, style="TButton")
        client_button.grid(row=0, column=1, padx=10, pady=5)

        event_button = ttk.Button(self.menu_frame, text="Event", command=self.open_event_menu, style="TButton")
        event_button.grid(row=1, column=0, padx=10, pady=5)

        supplier_button = ttk.Button(self.menu_frame, text="Supplier", command=self.open_supplier_menu, style="TButton")
        supplier_button.grid(row=1, column=1, padx=10, pady=5)

        guest_button = ttk.Button(self.menu_frame, text="Guest", command=self.open_guest_menu, style="TButton")
        guest_button.grid(row=2, column=0, padx=10, pady=5)

        venue_button = ttk.Button(self.menu_frame, text="Venue", command=self.open_venue_menu, style="TButton")
        venue_button.grid(row=2, column=1, padx=10, pady=5)

        close_button = ttk.Button(self.menu_frame, text="Close", command=self.master.quit, style="TButton")
        close_button.grid(row=3, columnspan=2, pady=10)

    def open_employee_menu(self):
        
        self.clear_frame()
        
        employee_menu_frame = tk.Frame(self.master, bg="#E6E6FA")
        employee_menu_frame.pack(pady=20)

        add_button = ttk.Button(employee_menu_frame, text="Add Employee", command=self.add_employee, style="TButton", width=15)
        add_button.grid(row=0, column=0, padx=10, pady=5)

        edit_button = ttk.Button(employee_menu_frame, text="Edit Employee", command=self.edit_employee, style="TButton", width=15)
        edit_button.grid(row=0, column=1, padx=10, pady=5)

        delete_button = ttk.Button(employee_menu_frame, text="Delete Employee", command=self.delete_employee, style="TButton", width=15)
        delete_button.grid(row=1, column=0, padx=10, pady=5)

        display_button = ttk.Button(employee_menu_frame, text="Display Employee", command=self.display_employee, style="TButton", width=15)
        display_button.grid(row=1, column=1, padx=10, pady=5)

        close_button = ttk.Button(employee_menu_frame, text="Close", command=self.back_to_main_menu, style="TButton", width=15)
        close_button.grid(row=2, columnspan=2, pady=10)

    def open_supplier_menu(self):
        self.clear_frame()
        
        supplier_menu_frame = tk.Frame(self.master, bg="#E6E6FA")
        supplier_menu_frame.pack(pady=20)

        add_button = ttk.Button(supplier_menu_frame, text="Add Supplier", command=self.add_supplier, style="TButton", width=15)
        add_button.grid(row=0, column=0, padx=10, pady=5)

        edit_button = ttk.Button(supplier_menu_frame, text="Edit Supplier", command=self.edit_supplier, style="TButton", width=15)
        edit_button.grid(row=0, column=1, padx=10, pady=5)

        delete_button = ttk.Button(supplier_menu_frame, text="Delete Supplier", command=self.delete_supplier, style="TButton", width=15)
        delete_button.grid(row=1, column=0, padx=10, pady=5)

        display_button = ttk.Button(supplier_menu_frame, text="Display Supplier", command=self.display_supplier, style="TButton", width=15)
        display_button.grid(row=1, column=1, padx=10, pady=5)

        close_button = ttk.Button(supplier_menu_frame, text="Close", command=self.back_to_main_menu, style="TButton", width=15)
        close_button.grid(row=2, columnspan=2, pady=10)

    def open_guest_menu(self):
        self.clear_frame()
        
        guest_menu_frame = tk.Frame(self.master, bg="#E6E6FA")
        guest_menu_frame.pack(pady=20)

        add_button = ttk.Button(guest_menu_frame, text="Add Guest", command=self.add_guest, style="TButton", width=15)
        add_button.grid(row=0, column=0, padx=10, pady=5)

        edit_button = ttk.Button(guest_menu_frame, text="Edit Guest", command=self.edit_guest, style="TButton", width=15)
        edit_button.grid(row=0, column=1, padx=10, pady=5)

        delete_button = ttk.Button(guest_menu_frame, text="Delete Guest", command=self.delete_guest, style="TButton", width=15)
        delete_button.grid(row=1, column=0, padx=10, pady=5)

        display_button = ttk.Button(guest_menu_frame, text="Display Guest", command=self.display_guest, style="TButton", width=15)
        display_button.grid(row=1, column=1, padx=10, pady=5)
        
        close_button = ttk.Button(guest_menu_frame, text="Close", command=self.back_to_main_menu, style="TButton", width=15)
        close_button.grid(row=2, columnspan=2, pady=10)

    def open_event_menu(self):
        self.clear_frame()
        
        event_menu_frame = tk.Frame(self.master, bg="#E6E6FA")
        event_menu_frame.pack(pady=20)

        add_button = ttk.Button(event_menu_frame, text="Add Event", command=self.add_event, style="TButton", width=15)
        add_button.grid(row=0, column=0, padx=10, pady=5)

        edit_button = ttk.Button(event_menu_frame, text="Edit Event", command=self.edit_event, style="TButton", width=15)
        edit_button.grid(row=0, column=1, padx=10, pady=5)

        delete_button = ttk.Button(event_menu_frame, text="Delete Event", command=self.delete_event, style="TButton", width=15)
        delete_button.grid(row=1, column=0, padx=10, pady=5)

        display_button = ttk.Button(event_menu_frame, text="Display Event", command=self.display_event, style="TButton", width=15)
        display_button.grid(row=1, column=1, padx=10, pady=5)

        upcoming_button = ttk.Button(event_menu_frame, text="Upcoming Events", command=self.display_upcoming_events, style="TButton", width=15)
        upcoming_button.grid(row=2, column=0, padx=10, pady=5)

        close_button = ttk.Button(event_menu_frame, text="Close", command=self.back_to_main_menu, style="TButton", width=15)
        close_button.grid(row=3, columnspan=2, pady=10)

    def open_client_menu(self):
        self.clear_frame()
        
        client_menu_frame = tk.Frame(self.master, bg="#E6E6FA")
        client_menu_frame.pack(pady=20)

        add_button = ttk.Button(client_menu_frame, text="Add Client", command=self.add_client, style="TButton", width=15)
        add_button.grid(row=0, column=0, padx=10, pady=5)

        edit_button = ttk.Button(client_menu_frame, text="Edit Client", command=self.edit_client, style="TButton", width=15)
        edit_button.grid(row=0, column=1, padx=10, pady=5)

        delete_button = ttk.Button(client_menu_frame, text="Delete Client", command=self.delete_client, style="TButton", width=15)
        delete_button.grid(row=1, column=0, padx=10, pady=5)

        display_button = ttk.Button(client_menu_frame, text="Display Client", command=self.display_client, style="TButton", width=15)
        display_button.grid(row=1, column=1, padx=10, pady=5)

        close_button = ttk.Button(client_menu_frame, text="Close", command=self.back_to_main_menu, style="TButton", width=15)
        close_button.grid(row=2, columnspan=2, pady=10)

    def open_venue_menu(self):
        self.clear_frame()
        
        venue_menu_frame = tk.Frame(self.master, bg="#E6E6FA")
        venue_menu_frame.pack(pady=20)

        add_button = ttk.Button(venue_menu_frame, text="Add Venue", command=self.add_venue, style="TButton", width=15)
        add_button.grid(row=0, column=0, padx=10, pady=5)

        edit_button = ttk.Button(venue_menu_frame, text="Edit Venue", command=self.edit_venue, style="TButton", width=15)
        edit_button.grid(row=0, column=1, padx=10, pady=5)

        delete_button = ttk.Button(venue_menu_frame, text="Delete Venue", command=self.delete_venue, style="TButton", width=15)
        delete_button.grid(row=1, column=0, padx=10, pady=5)

        display_button = ttk.Button(venue_menu_frame, text="Display Venue", command=self.display_venue, style="TButton", width=15)
        display_button.grid(row=1, column=1, padx=10, pady=5)

        close_button = ttk.Button(venue_menu_frame, text="Close", command=self.back_to_main_menu, style="TButton", width=15)
        close_button.grid(row=2, columnspan=2, pady=10)

    def back_to_main_menu(self):
        self.clear_frame()
        self.create_main_menu()

    def clear_frame(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def add_employee(self):
        
        self.clear_frame()
        
        add_employee_frame = tk.Frame(self.master, bg="#E6E6FA")
        add_employee_frame.pack(pady=20)

        # Label and entry for employee details
        tk.Label(add_employee_frame, text="Name:", bg="#E6E6FA").grid(row=0, column=0, padx=5, pady=5)
        name_entry = ttk.Entry(add_employee_frame)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(add_employee_frame, text="Employee ID:", bg="#E6E6FA").grid(row=1, column=0, padx=5, pady=5)
        emp_id_entry = ttk.Entry(add_employee_frame)
        emp_id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(add_employee_frame, text="Department:", bg="#E6E6FA").grid(row=2, column=0, padx=5, pady=5)
        department_entry = ttk.Entry(add_employee_frame)
        department_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(add_employee_frame, text="Job Title:", bg="#E6E6FA").grid(row=3, column=0, padx=5, pady=5)
        job_title_entry = ttk.Entry(add_employee_frame)
        job_title_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(add_employee_frame, text="Basic Salary:", bg="#E6E6FA").grid(row=4, column=0, padx=5, pady=5)
        basic_salary_entry = ttk.Entry(add_employee_frame)
        basic_salary_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(add_employee_frame, text="Age:", bg="#E6E6FA").grid(row=5, column=0, padx=5, pady=5)
        age_entry = ttk.Entry(add_employee_frame)
        age_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(add_employee_frame, text="Date of Birth (DOB):", bg="#E6E6FA").grid(row=6, column=0, padx=5, pady=5)
        dob_entry = ttk.Entry(add_employee_frame)
        dob_entry.grid(row=6, column=1, padx=5, pady=5)

        tk.Label(add_employee_frame, text="Passport Details:", bg="#E6E6FA").grid(row=7, column=0, padx=5, pady=5)
        passport_details_entry = ttk.Entry(add_employee_frame)
        passport_details_entry.grid(row=7, column=1, padx=5, pady=5)

        # Button to add employee
        add_button = ttk.Button(add_employee_frame, text="Add Employee", command=lambda: self.add_employee_to_system(
            name_entry.get(), emp_id_entry.get(), department_entry.get(), job_title_entry.get(),
            basic_salary_entry.get(), age_entry.get(), dob_entry.get(), passport_details_entry.get()), style="TButton")
        add_button.grid(row=8, columnspan=2, pady=10)

    def add_employee_to_system(self, name, emp_id, department, job_title, basic_salary, age, dob, passport_details):
        if not all([name, emp_id, department, job_title, basic_salary, age, dob, passport_details]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Validation for name
        if not name.isalpha():
            messagebox.showerror("Error", "Name should contain alphabets only.")
            return

        # Validation for employee ID
        if not emp_id.isdigit():
            messagebox.showerror("Error", "Employee ID should contain digits only.")
            return

        # Additional validation if needed

        # If all validation passed, proceed with adding employee
        employee_data = {
            'Name': name,
            'Employee ID': emp_id,
            'Department': department,
            'Job Title': job_title,
            'Basic Salary': basic_salary,
            'Age': age,
            'Date of Birth (DOB)': dob,
            'Passport Details': passport_details
        }
        self.employee.add_employee(employee_data)
        messagebox.showinfo("Success", "Employee added successfully!")
        self.back_to_main_menu()

    def edit_employee(self):
        # Clear any existing widgets on the screen
        self.clear_frame()
        
        # Create a frame for editing employee details
        edit_employee_frame = tk.Frame(self.master, bg="#E6E6FA")
        edit_employee_frame.pack(pady=20)

        # Label and entry for employee ID
        tk.Label(edit_employee_frame, text="Enter Employee ID:", bg="#E6E6FA").grid(row=0, column=0, padx=5, pady=5)
        emp_id_entry = ttk.Entry(edit_employee_frame)
        emp_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Function to populate employee details for editing
        def populate_employee_details():
            emp_id = emp_id_entry.get()

            if emp_id:
                employees_obj = Employee('', '', '', '', '', '', '', '')
                employees = employees_obj.read_employees_from_file()
                if employees:
                    for employee in employees:
                        if employee.get('Employee ID') == emp_id:
                            # Create a new screen similar to add employee with fields filled
                            self.populate_edit_employee_screen(employee)
                            break
                    else:
                        messagebox.showerror("Error", "Employee not found!")
                else:
                    messagebox.showerror("Error", "No employees data found!")
            else:
                messagebox.showerror("Error", "Please enter Employee ID!")

        # Button to populate employee details for editing
        populate_button = ttk.Button(edit_employee_frame, text="Populate", command=populate_employee_details, style="TButton")
        populate_button.grid(row=0, column=2, padx=5, pady=5)

    def populate_edit_employee_screen(self, employee_details):
        # Clear any existing widgets on the screen
        self.clear_frame()
        
        # Create a frame for editing employee details
        edit_employee_frame = tk.Frame(self.master, bg="#E6E6FA")
        edit_employee_frame.pack(pady=20)

        # Labels and entries for employee details
        tk.Label(edit_employee_frame, text="Name:", bg="#E6E6FA").grid(row=0, column=0, padx=5, pady=5)
        name_entry = ttk.Entry(edit_employee_frame)
        name_entry.insert(0, employee_details.get('Name'))  # Populate with employee name
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(edit_employee_frame, text="Employee ID:", bg="#E6E6FA").grid(row=1, column=0, padx=5, pady=5)
        emp_id_entry = ttk.Entry(edit_employee_frame)
        emp_id_entry.insert(0, employee_details.get('Employee ID'))  # Populate with employee ID
        emp_id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(edit_employee_frame, text="Department:", bg="#E6E6FA").grid(row=2, column=0, padx=5, pady=5)
        department_entry = ttk.Entry(edit_employee_frame)
        department_entry.insert(0, employee_details.get('Department'))  # Populate with department
        department_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(edit_employee_frame, text="Job Title:", bg="#E6E6FA").grid(row=3, column=0, padx=5, pady=5)
        job_title_entry = ttk.Entry(edit_employee_frame)
        job_title_entry.insert(0, employee_details.get('Job Title'))  # Populate with job title
        job_title_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(edit_employee_frame, text="Basic Salary:", bg="#E6E6FA").grid(row=4, column=0, padx=5, pady=5)
        basic_salary_entry = ttk.Entry(edit_employee_frame)
        basic_salary_entry.insert(0, employee_details.get('Basic Salary'))  # Populate with basic salary
        basic_salary_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(edit_employee_frame, text="Age:", bg="#E6E6FA").grid(row=5, column=0, padx=5, pady=5)
        age_entry = ttk.Entry(edit_employee_frame)
        age_entry.insert(0, employee_details.get('Age'))  # Populate with age
        age_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(edit_employee_frame, text="Date of Birth (DOB):", bg="#E6E6FA").grid(row=6, column=0, padx=5, pady=5)
        dob_entry = ttk.Entry(edit_employee_frame)
        dob_entry.insert(0, employee_details.get('Date of Birth (DOB)'))  # Populate with DOB
        dob_entry.grid(row=6, column=1, padx=5, pady=5)

        tk.Label(edit_employee_frame, text="Passport Details:", bg="#E6E6FA").grid(row=7, column=0, padx=5, pady=5)
        passport_details_entry = ttk.Entry(edit_employee_frame)
        passport_details_entry.insert(0, employee_details.get('Passport Details'))  # Populate with passport details
        passport_details_entry.grid(row=7, column=1, padx=5, pady=5)

        # Button to update employee
        update_button = ttk.Button(edit_employee_frame, text="Update Employee", command=lambda: self.update_employee_in_system(
            emp_id_entry.get(), name_entry.get(), department_entry.get(), job_title_entry.get(),
            basic_salary_entry.get(), age_entry.get(), dob_entry.get(), passport_details_entry.get()), style="TButton")
        update_button.grid(row=8, columnspan=2, pady=10)

    def update_employee_in_system(self, emp_id, name, department, job_title, basic_salary, age, dob, passport_details):
        # Read all employees from the file
        employees_obj = Employee('', '', '', '', '', '', '', '')
        employees = employees_obj.read_employees_from_file()

        if employees:
            # Find the employee with the provided ID
            for employee in employees:
                if employee.get('Employee ID') == emp_id:
                    # Update employee details
                    employee['Name'] = name
                    employee['Department'] = department
                    employee['Job Title'] = job_title
                    employee['Basic Salary'] = basic_salary
                    employee['Age'] = age
                    employee['Date of Birth (DOB)'] = dob
                    employee['Passport Details'] = passport_details
                    break
            else:
                messagebox.showerror("Error", "Employee not found!")
                return

            # Write the updated employee data back to the file
            FileHandler.write_to_binary_file(employees, 'employees.pkl')
            messagebox.showinfo("Success", "Employee details updated successfully!")
            self.back_to_main_menu()
        else:
            messagebox.showerror("Error", "No employees data found!")

    def delete_employee(self):
        # Clear any existing widgets on the screen
        self.clear_frame()
        
        # Create a frame for delete employee functionality
        delete_frame = tk.Frame(self.master, bg="#E6E6FA")
        delete_frame.pack(pady=20)

        # Create label and entry for entering employee ID
        emp_id_label = tk.Label(delete_frame, text="Enter Employee ID:", font=("Arial", 12), bg="#E6E6FA")
        emp_id_label.grid(row=0, column=0, padx=5, pady=5)

        emp_id_entry = ttk.Entry(delete_frame, font=("Arial", 12))
        emp_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Function to delete employee when the "Delete" button is clicked
        def delete_employee_func():
            emp_id = emp_id_entry.get()

            if emp_id:
                employee_obj = Employee('', '', '', '', '', '', '', '')
                if employee_obj.delete_employee_by_id(emp_id):
                    messagebox.showinfo("Success", "Employee deleted successfully!")
                    self.back_to_main_menu()
                else:
                    messagebox.showerror("Error", "Employee not found!")
            else:
                messagebox.showerror("Error", "Please enter Employee ID!")

        # Button to delete employee
        delete_button = ttk.Button(delete_frame, text="Delete", command=delete_employee_func, style="TButton")
        delete_button.grid(row=0, column=2, padx=5, pady=5)

    def display_employee(self):
        # Clear any existing widgets on the screen
        self.clear_frame()
        
        # Create a frame to display employee details
        display_frame = tk.Frame(self.master, bg="#E6E6FA")
        display_frame.pack(pady=20)

        # Create label and entry for entering employee ID
        emp_id_label = tk.Label(display_frame, text="Enter Employee ID:", font=("Arial", 12), bg="#E6E6FA")
        emp_id_label.grid(row=0, column=0, padx=5, pady=5)

        emp_id_entry = ttk.Entry(display_frame, font=("Arial", 12))
        emp_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Function to display employee details when the "Display" button is clicked
        def display_details():
            emp_id = emp_id_entry.get()

            if emp_id:
                employee_obj = Employee('', '', '', '', '', '', '', '')
                employees = employee_obj.read_employees_from_file()

                if employees:
                    for employee in employees:
                        if employee.get('Employee ID') == emp_id:  # Accessing the ID from the dictionary
                            # Create a frame to display employee details
                            details_frame = tk.Frame(display_frame, bg="white")
                            details_frame.grid(row=2, column=0, columnspan=3, pady=10, padx=10, sticky="nsew")

                            # Create a label to display employee details inside the frame
                            details_label = tk.Label(details_frame, text=f"Name: {employee.get('Name')}\n"
                                                                        f"Employee ID: {employee.get('Employee ID')}\n"
                                                                        f"Department: {employee.get('Department')}\n"
                                                                        f"Job Title: {employee.get('Job Title')}\n"
                                                                        f"Basic Salary: {employee.get('Basic Salary')}\n"
                                                                        f"Age: {employee.get('Age')}\n"
                                                                        f"Date of Birth: {employee.get('Date of Birth (DOB)')}\n"
                                                                        f"Passport Details: {employee.get('Passport Details')}",
                                                    font=("Arial", 12), bg="white")
                            details_label.pack(padx=10, pady=10)
                            break
                    else:
                        messagebox.showerror("Error", "Employee not found!")
                else:
                    messagebox.showerror("Error", "No employees data found!")
                    self.back_to_main_menu()
            else:
                messagebox.showerror("Error", "Please enter Employee ID!")

        # Button to display employee details
        display_button = ttk.Button(display_frame, text="Display", command=display_details, style="TButton")
        display_button.grid(row=0, column=2, padx=5, pady=5)

        close_button = ttk.Button(display_frame, text="Close", command=self.back_to_main_menu, style="TButton", width=15)
        close_button.grid(row=1, columnspan=2, pady=10)

    def add_guest(self):
        self.clear_frame()

        add_guest_frame = tk.Frame(self.master, bg="#E6E6FA")
        add_guest_frame.pack(pady=20)

        tk.Label(add_guest_frame, text="Name:", bg="#E6E6FA").grid(row=0, column=0, padx=5, pady=5)
        name_entry = ttk.Entry(add_guest_frame)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(add_guest_frame, text="Guest ID:", bg="#E6E6FA").grid(row=1, column=0, padx=5, pady=5)
        guest_id_entry = ttk.Entry(add_guest_frame)
        guest_id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(add_guest_frame, text="Address:", bg="#E6E6FA").grid(row=2, column=0, padx=5, pady=5)
        address_entry = ttk.Entry(add_guest_frame)
        address_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(add_guest_frame, text="Contact Details:", bg="#E6E6FA").grid(row=3, column=0, padx=5, pady=5)
        contact_details_entry = ttk.Entry(add_guest_frame)
        contact_details_entry.grid(row=3, column=1, padx=5, pady=5)

        add_button = ttk.Button(add_guest_frame, text="Add Guest", command=lambda: self.add_guest_to_system(
            name_entry.get(), guest_id_entry.get(), address_entry.get(), contact_details_entry.get()), style="TButton")
        add_button.grid(row=4, columnspan=2, pady=10)

    def add_guest_to_system(self, name, guest_id, address, contact_details):
        if not all([name, guest_id, address, contact_details]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Validation for name
        if not name.isalpha():
            messagebox.showerror("Error", "Name should contain alphabets only.")
            return

        # Validation for guest ID
        if not guest_id.isdigit():
            messagebox.showerror("Error", "Guest ID should contain digits only.")
            return

        # Additional validation if needed

        # If all validation passed, proceed with adding guest
        guest_data = {
            'Name': name,
            'Guest ID': guest_id,
            'Address': address,
            'Contact Details': contact_details
        }
        self.guest.add_guest(guest_data)  # Assuming guest is the instance of the Guest class
        messagebox.showinfo("Success", "Guest added successfully!")
        self.back_to_main_menu()

    def edit_guest(self):
        # Clear any existing widgets on the screen
        self.clear_frame()
        
        # Create a frame for editing guest details
        edit_guest_frame = tk.Frame(self.master, bg="#E6E6FA")
        edit_guest_frame.pack(pady=20)

        # Label and entry for guest ID
        tk.Label(edit_guest_frame, text="Enter Guest ID:", bg="#E6E6FA").grid(row=0, column=0, padx=5, pady=5)
        guest_id_entry = ttk.Entry(edit_guest_frame)
        guest_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Function to populate guest details for editing
        def populate_guest_details():
            guest_id = guest_id_entry.get()

            if guest_id:
                guest_obj = Guest('', '', '', '')
                guests = guest_obj.read_guests_from_file()
                if guests:
                    for guest in guests:
                        if guest.get('Guest ID') == guest_id:
                            # Create a new screen similar to add guest with fields filled
                            self.populate_edit_guest_screen(guest)
                            break
                    else:
                        messagebox.showerror("Error", "Guest not found!")
                else:
                    messagebox.showerror("Error", "No guest data found!")
            else:
                messagebox.showerror("Error", "Please enter Guest ID!")

        # Button to populate guest details for editing
        populate_button = ttk.Button(edit_guest_frame, text="Populate", command=populate_guest_details, style="TButton")
        populate_button.grid(row=0, column=2, padx=5, pady=5)

    def populate_edit_guest_screen(self, guest_details):
        # Clear any existing widgets on the screen
        self.clear_frame()
        
        # Create a frame for editing guest details
        edit_guest_frame = tk.Frame(self.master, bg="#E6E6FA")
        edit_guest_frame.pack(pady=20)

        # Labels and entries for guest details
        tk.Label(edit_guest_frame, text="Name:", bg="#E6E6FA").grid(row=0, column=0, padx=5, pady=5)
        name_entry = ttk.Entry(edit_guest_frame)
        name_entry.insert(0, guest_details.get('Name'))  # Populate with guest name
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(edit_guest_frame, text="Guest ID:", bg="#E6E6FA").grid(row=1, column=0, padx=5, pady=5)
        guest_id_entry = ttk.Entry(edit_guest_frame)
        guest_id_entry.insert(0, guest_details.get('Guest ID'))  # Populate with guest ID
        guest_id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(edit_guest_frame, text="Address:", bg="#E6E6FA").grid(row=2, column=0, padx=5, pady=5)
        address_entry = ttk.Entry(edit_guest_frame)
        address_entry.insert(0, guest_details.get('Address'))  # Populate with address
        address_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(edit_guest_frame, text="Contact Details:", bg="#E6E6FA").grid(row=3, column=0, padx=5, pady=5)
        contact_details_entry = ttk.Entry(edit_guest_frame)
        contact_details_entry.insert(0, guest_details.get('Contact Details'))  # Populate with contact details
        contact_details_entry.grid(row=3, column=1, padx=5, pady=5)

        # Button to update guest
        update_button = ttk.Button(edit_guest_frame, text="Update Guest", command=lambda: self.update_guest_in_system(
            guest_id_entry.get(), name_entry.get(), address_entry.get(), contact_details_entry.get()), style="TButton")
        update_button.grid(row=4, columnspan=2, pady=10)

    def update_guest_in_system(self, guest_id, name, address, contact_details):
        # Read all guests from the file
        guest_obj = Guest('', '', '', '')
        guests = guest_obj.read_guests_from_file()

        if guests:
            # Find the guest with the provided ID
            for guest in guests:
                if guest.get('Guest ID') == guest_id:
                    # Update guest details
                    guest['Name'] = name
                    guest['Address'] = address
                    guest['Contact Details'] = contact_details
                    break
            else:
                messagebox.showerror("Error", "Guest not found!")
                return

            # Write the updated guest data back to the file
            FileHandler.write_to_binary_file(guests, 'guests.pkl')
            messagebox.showinfo("Success", "Guest details updated successfully!")
            self.back_to_main_menu()
        else:
            messagebox.showerror("Error", "No guests data found!")

    def delete_guest(self):
        # Clear any existing widgets on the screen
        self.clear_frame()
        
        # Create a frame for delete guest functionality
        delete_frame = tk.Frame(self.master, bg="#E6E6FA")
        delete_frame.pack(pady=20)

        # Create label and entry for entering guest ID
        guest_id_label = tk.Label(delete_frame, text="Enter Guest ID:", font=("Arial", 12), bg="#E6E6FA")
        guest_id_label.grid(row=0, column=0, padx=5, pady=5)

        guest_id_entry = ttk.Entry(delete_frame, font=("Arial", 12))
        guest_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Function to delete guest when the "Delete" button is clicked
        def delete_guest_func():
            guest_id = guest_id_entry.get()

            if guest_id:
                guest_obj = Guest('', '', '', '')
                if guest_obj.delete_guest_by_id(guest_id):
                    messagebox.showinfo("Success", "Guest deleted successfully!")
                    self.back_to_main_menu()
                else:
                    messagebox.showerror("Error", "Guest not found!")
            else:
                messagebox.showerror("Error", "Please enter Guest ID!")

        # Button to delete guest
        delete_button = ttk.Button(delete_frame, text="Delete", command=delete_guest_func, style="TButton")
        delete_button.grid(row=0, column=2, padx=5, pady=5)

    def display_guest(self):
        # Clear any existing widgets on the screen
        self.clear_frame()
        
        # Create a frame to display guest details
        display_frame = tk.Frame(self.master, bg="#E6E6FA")
        display_frame.pack(pady=20)

        # Create label and entry for entering guest ID
        guest_id_label = tk.Label(display_frame, text="Enter Guest ID:", font=("Arial", 12), bg="#E6E6FA")
        guest_id_label.grid(row=0, column=0, padx=5, pady=5)

        guest_id_entry = ttk.Entry(display_frame, font=("Arial", 12))
        guest_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Function to display guest details when the "Display" button is clicked
        def display_details():
            guest_id = guest_id_entry.get()

            if guest_id:
                guest_obj = Guest('', '', '', '')
                guests = guest_obj.read_guests_from_file()

                if guests:
                    for guest in guests:
                        if guest.get('Guest ID') == guest_id:  # Accessing the ID from the dictionary
                            # Create a frame to display guest details
                            details_frame = tk.Frame(display_frame, bg="white")
                            details_frame.grid(row=2, column=0, columnspan=3, pady=10, padx=10, sticky="nsew")

                            # Create a label to display guest details inside the frame
                            details_label = tk.Label(details_frame, text=f"Name: {guest.get('Name')}\n"
                                                                        f"Guest ID: {guest.get('Guest ID')}\n"
                                                                        f"Address: {guest.get('Address')}\n"
                                                                        f"Contact Details: {guest.get('Contact Details')}",
                                                    font=("Arial", 12), bg="white")
                            details_label.pack(padx=10, pady=10)
                            break
                    else:
                        messagebox.showerror("Error", "Guest not found!")
                else:
                    messagebox.showerror("Error", "No guests data found!")
                    self.back_to_main_menu()
            else:
                messagebox.showerror("Error", "Please enter Guest ID!")

        # Button to display guest details
        display_button = ttk.Button(display_frame, text="Display", command=display_details, style="TButton")
        display_button.grid(row=0, column=2, padx=5, pady=5)

        close_button = ttk.Button(display_frame, text="Close", command=self.back_to_main_menu, style="TButton", width=15)
        close_button.grid(row=1, columnspan=2, pady=10)


    def add_supplier(self):
        self.clear_frame()
        
        add_supplier_frame = tk.Frame(self.master, bg="#E6E6FA")
        add_supplier_frame.pack(pady=20)

        # Label and entry for supplier details
        tk.Label(add_supplier_frame, text="Name:", bg="#E6E6FA").grid(row=0, column=0, padx=5, pady=5)
        name_entry = ttk.Entry(add_supplier_frame)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(add_supplier_frame, text="Supplier ID:", bg="#E6E6FA").grid(row=1, column=0, padx=5, pady=5)
        supplier_id_entry = ttk.Entry(add_supplier_frame)
        supplier_id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(add_supplier_frame, text="Address:", bg="#E6E6FA").grid(row=2, column=0, padx=5, pady=5)
        address_entry = ttk.Entry(add_supplier_frame)
        address_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(add_supplier_frame, text="Contact Details:", bg="#E6E6FA").grid(row=3, column=0, padx=5, pady=5)
        contact_details_entry = ttk.Entry(add_supplier_frame)
        contact_details_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(add_supplier_frame, text="Menu:", bg="#E6E6FA").grid(row=4, column=0, padx=5, pady=5)
        menu_entry = ttk.Entry(add_supplier_frame)
        menu_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(add_supplier_frame, text="Min Guests:", bg="#E6E6FA").grid(row=5, column=0, padx=5, pady=5)
        min_guests_entry = ttk.Entry(add_supplier_frame)
        min_guests_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(add_supplier_frame, text="Max Guests:", bg="#E6E6FA").grid(row=6, column=0, padx=5, pady=5)
        max_guests_entry = ttk.Entry(add_supplier_frame)
        max_guests_entry.grid(row=6, column=1, padx=5, pady=5)

        # Button to add supplier
        add_button = ttk.Button(add_supplier_frame, text="Add Supplier", command=lambda: self.add_supplier_to_system(
            name_entry.get(), supplier_id_entry.get(), address_entry.get(), contact_details_entry.get(),
            menu_entry.get(), min_guests_entry.get(), max_guests_entry.get()), style="TButton")
        add_button.grid(row=7, columnspan=2, pady=10)

    def add_supplier_to_system(self, name, supplier_id, address, contact_details, menu, min_guests, max_guests):
        if not all([name, supplier_id, address, contact_details, menu, min_guests, max_guests]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Additional validation if needed

        # If all validation passed, proceed with adding supplier
        supplier_data = {
            'Name': name,
            'Supplier ID': supplier_id,
            'Address': address,
            'Contact Details': contact_details,
            'Menu': menu,
            'Min Guests': min_guests,
            'Max Guests': max_guests
        }
        self.supplier.add_supplier(supplier_data)
        messagebox.showinfo("Success", "Supplier added successfully!")
        self.back_to_main_menu()

    def edit_supplier(self):
        # Clear any existing widgets on the screen
        self.clear_frame()
        
        # Create a frame for editing supplier details
        edit_supplier_frame = tk.Frame(self.master, bg="#E6E6FA")
        edit_supplier_frame.pack(pady=20)

        # Label and entry for supplier ID
        tk.Label(edit_supplier_frame, text="Enter Supplier ID:", bg="#E6E6FA").grid(row=0, column=0, padx=5, pady=5)
        supplier_id_entry = ttk.Entry(edit_supplier_frame)
        supplier_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Function to populate supplier details for editing
        def populate_supplier_details():
            supplier_id = supplier_id_entry.get()

            if supplier_id:
                suppliers_obj = Supplier('', '', '', '', '', '', '')
                suppliers = suppliers_obj.read_suppliers_from_file()
                if suppliers:
                    for supplier in suppliers:
                        if supplier.get('Supplier ID') == supplier_id:
                            # Create a new screen similar to add supplier with fields filled
                            self.populate_edit_supplier_screen(supplier)
                            break
                    else:
                        messagebox.showerror("Error", "Supplier not found!")
                else:
                    messagebox.showerror("Error", "No suppliers data found!")
            else:
                messagebox.showerror("Error", "Please enter Supplier ID!")

        # Button to populate supplier details for editing
        populate_button = ttk.Button(edit_supplier_frame, text="Populate", command=populate_supplier_details, style="TButton")
        populate_button.grid(row=0, column=2, padx=5, pady=5)

    def populate_edit_supplier_screen(self, supplier_details):
        # Clear any existing widgets on the screen
        self.clear_frame()
        
        # Create a frame for editing supplier details
        edit_supplier_frame = tk.Frame(self.master, bg="#E6E6FA")
        edit_supplier_frame.pack(pady=20)

        # Labels and entries for supplier details
        tk.Label(edit_supplier_frame, text="Name:", bg="#E6E6FA").grid(row=0, column=0, padx=5, pady=5)
        name_entry = ttk.Entry(edit_supplier_frame)
        name_entry.insert(0, supplier_details.get('Name'))  # Populate with supplier name
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(edit_supplier_frame, text="Supplier ID:", bg="#E6E6FA").grid(row=1, column=0, padx=5, pady=5)
        supplier_id_entry = ttk.Entry(edit_supplier_frame)
        supplier_id_entry.insert(0, supplier_details.get('Supplier ID'))  # Populate with supplier ID
        supplier_id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(edit_supplier_frame, text="Address:", bg="#E6E6FA").grid(row=2, column=0, padx=5, pady=5)
        address_entry = ttk.Entry(edit_supplier_frame)
        address_entry.insert(0, supplier_details.get('Address'))  # Populate with address
        address_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(edit_supplier_frame, text="Contact Details:", bg="#E6E6FA").grid(row=3, column=0, padx=5, pady=5)
        contact_details_entry = ttk.Entry(edit_supplier_frame)
        contact_details_entry.insert(0, supplier_details.get('Contact Details'))  # Populate with contact details
        contact_details_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(edit_supplier_frame, text="Menu:", bg="#E6E6FA").grid(row=4, column=0, padx=5, pady=5)
        menu_entry = ttk.Entry(edit_supplier_frame)
        menu_entry.insert(0, supplier_details.get('Menu'))  # Populate with menu
        menu_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(edit_supplier_frame, text="Min Guests:", bg="#E6E6FA").grid(row=5, column=0, padx=5, pady=5)
        min_guests_entry = ttk.Entry(edit_supplier_frame)
        min_guests_entry.insert(0, supplier_details.get('Min Guests'))  # Populate with min guests
        min_guests_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(edit_supplier_frame, text="Max Guests:", bg="#E6E6FA").grid(row=6, column=0, padx=5, pady=5)
        max_guests_entry = ttk.Entry(edit_supplier_frame)
        max_guests_entry.insert(0, supplier_details.get('Max Guests'))  # Populate with max guests
        max_guests_entry.grid(row=6, column=1, padx=5, pady=5)

        # Button to update supplier
        update_button = ttk.Button(edit_supplier_frame, text="Update Supplier", command=lambda: self.update_supplier_in_system(
            supplier_id_entry.get(), name_entry.get(), address_entry.get(), contact_details_entry.get(),
            menu_entry.get(), min_guests_entry.get(), max_guests_entry.get()), style="TButton")
        update_button.grid(row=7, columnspan=2, pady=10)

    def update_supplier_in_system(self, supplier_id, name, address, contact_details, menu, min_guests, max_guests):
        # Read all suppliers from the file
        suppliers_obj = Supplier('', '', '', '', '', '', '')
        suppliers = suppliers_obj.read_suppliers_from_file()

        if suppliers:
            # Find the supplier with the provided ID
            for supplier in suppliers:
                if supplier.get('Supplier ID') == supplier_id:
                    # Update supplier details
                    supplier['Name'] = name
                    supplier['Address'] = address
                    supplier['Contact Details'] = contact_details
                    supplier['Menu'] = menu
                    supplier['Min Guests'] = min_guests
                    supplier['Max Guests'] = max_guests
                    break
            else:
                messagebox.showerror("Error", "Supplier not found!")
                return

            # Write the updated supplier data back to the file
            FileHandler.write_to_binary_file(suppliers, 'suppliers.pkl')
            messagebox.showinfo("Success", "Supplier details updated successfully!")
            self.back_to_main_menu()
        else:
            messagebox.showerror("Error", "No suppliers data found!")

    def delete_supplier(self):
        # Clear any existing widgets on the screen
        self.clear_frame()
        
        # Create a frame for delete supplier functionality
        delete_frame = tk.Frame(self.master, bg="#E6E6FA")
        delete_frame.pack(pady=20)

        # Create label and entry for entering supplier ID
        supplier_id_label = tk.Label(delete_frame, text="Enter Supplier ID:", font=("Arial", 12), bg="#E6E6FA")
        supplier_id_label.grid(row=0, column=0, padx=5, pady=5)

        supplier_id_entry = ttk.Entry(delete_frame, font=("Arial", 12))
        supplier_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Function to delete supplier when the "Delete" button is clicked
        def delete_supplier_func():
            supplier_id = supplier_id_entry.get()

            if supplier_id:
                supplier_obj = Supplier('', '', '', '', '', '', '')
                if supplier_obj.delete_supplier_by_id(supplier_id):
                    messagebox.showinfo("Success", "Supplier deleted successfully!")
                    self.back_to_main_menu()
                else:
                    messagebox.showerror("Error", "Supplier not found!")
            else:
                messagebox.showerror("Error", "Please enter Supplier ID!")

        # Button to delete supplier
        delete_button = ttk.Button(delete_frame, text="Delete", command=delete_supplier_func, style="TButton")
        delete_button.grid(row=0, column=2, padx=5, pady=5)

    def display_supplier(self):
        # Clear any existing widgets on the screen
        self.clear_frame()
        
        # Create a frame to display supplier details
        display_frame = tk.Frame(self.master, bg="#E6E6FA")
        display_frame.pack(pady=20)

        # Create label and entry for entering supplier ID
        supplier_id_label = tk.Label(display_frame, text="Enter Supplier ID:", font=("Arial", 12), bg="#E6E6FA")
        supplier_id_label.grid(row=0, column=0, padx=5, pady=5)

        supplier_id_entry = ttk.Entry(display_frame, font=("Arial", 12))
        supplier_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Function to display supplier details when the "Display" button is clicked
        def display_details():
            supplier_id = supplier_id_entry.get()

            if supplier_id:
                supplier_obj = Supplier('', '', '', '', '', '', '')
                suppliers = supplier_obj.read_suppliers_from_file()

                if suppliers:
                    for supplier in suppliers:
                        if supplier.get('Supplier ID') == supplier_id:  # Accessing the ID from the dictionary
                            # Create a frame to display supplier details
                            details_frame = tk.Frame(display_frame, bg="white")
                            details_frame.grid(row=2, column=0, columnspan=3, pady=10, padx=10, sticky="nsew")

                            # Create a label to display supplier details inside the frame
                            details_label = tk.Label(details_frame, text=f"Name: {supplier.get('Name')}\n"
                                                                        f"Supplier ID: {supplier.get('Supplier ID')}\n"
                                                                        f"Address: {supplier.get('Address')}\n"
                                                                        f"Contact Details: {supplier.get('Contact Details')}\n"
                                                                        f"Menu: {supplier.get('Menu')}\n"
                                                                        f"Min Guests: {supplier.get('Min Guests')}\n"
                                                                        f"Max Guests: {supplier.get('Max Guests')}",
                                                    font=("Arial", 12), bg="white")
                            details_label.pack(padx=10, pady=10)
                            break
                    else:
                        messagebox.showerror("Error", "Supplier not found!")
                else:
                    messagebox.showerror("Error", "No suppliers data found!")
                    self.back_to_main_menu()
            else:
                messagebox.showerror("Error", "Please enter Supplier ID!")

        # Button to display supplier details
        display_button = ttk.Button(display_frame, text="Display", command=display_details, style="TButton")
        display_button.grid(row=0, column=2, padx=5, pady=5)

        close_button = ttk.Button(display_frame, text="Close", command=self.back_to_main_menu, style="TButton", width=15)
        close_button.grid(row=1, columnspan=2, pady=10)


    def add_client(self):
        self.clear_frame()

        add_client_frame = tk.Frame(self.master, bg="#E6E6FA")
        add_client_frame.pack(pady=20)

        tk.Label(add_client_frame, text="Name:", bg="#E6E6FA").grid(row=0, column=0, padx=5, pady=5)
        name_entry = ttk.Entry(add_client_frame)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(add_client_frame, text="Client ID:", bg="#E6E6FA").grid(row=1, column=0, padx=5, pady=5)
        client_id_entry = ttk.Entry(add_client_frame)
        client_id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(add_client_frame, text="Address:", bg="#E6E6FA").grid(row=2, column=0, padx=5, pady=5)
        address_entry = ttk.Entry(add_client_frame)
        address_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(add_client_frame, text="Contact Details:", bg="#E6E6FA").grid(row=3, column=0, padx=5, pady=5)
        contact_details_entry = ttk.Entry(add_client_frame)
        contact_details_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(add_client_frame, text="Budget:", bg="#E6E6FA").grid(row=4, column=0, padx=5, pady=5)
        budget_entry = ttk.Entry(add_client_frame)
        budget_entry.grid(row=4, column=1, padx=5, pady=5)

        add_button = ttk.Button(add_client_frame, text="Add Client", command=lambda: self.add_client_to_system(
            name_entry.get(), client_id_entry.get(), address_entry.get(), contact_details_entry.get(),
            budget_entry.get()), style="TButton")
        add_button.grid(row=5, columnspan=2, pady=10)

    def add_client_to_system(self, name, client_id, address, contact_details, budget):
        if not all([name, client_id, address, contact_details, budget]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Validation for name
        if not name.replace(' ', '').isalpha():
            messagebox.showerror("Error", "Name should contain alphabets only.")
            return

        # Validation for client ID
        if not client_id.isdigit():
            messagebox.showerror("Error", "Client ID should contain digits only.")
            return

        client_data = {
            'Name': name,
            'Client ID': client_id,
            'Address': address,
            'Contact Details': contact_details,
            'Budget': budget
        }
        # Assuming you have a method to add client data to your data store
        self.client.add_client(client_data)
        messagebox.showinfo("Success", "Client added successfully!")
        self.back_to_main_menu()

    def edit_client(self):
        # Clear any existing widgets on the screen
        self.clear_frame()

        # Create a frame for editing client details
        edit_client_frame = tk.Frame(self.master, bg="#E6E6FA")
        edit_client_frame.pack(pady=20)

        # Label and entry for entering client ID
        tk.Label(edit_client_frame, text="Enter Client ID:", bg="#E6E6FA").grid(row=0, column=0, padx=5, pady=5)
        client_id_entry = ttk.Entry(edit_client_frame)
        client_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Function to populate client details for editing
        def populate_client_details():
            client_id = client_id_entry.get()

            if client_id:
                clients_obj = Client('', '', '', '', '')
                clients = clients_obj.read_clients_from_file()
                if clients:
                    for client in clients:
                        if client.get('Client ID') == client_id:
                            # Create a new screen similar to add client with fields filled
                            self.populate_edit_client_screen(client)
                            break
                    else:
                        messagebox.showerror("Error", "Client not found!")
                else:
                    messagebox.showerror("Error", "No clients data found!")
            else:
                messagebox.showerror("Error", "Please enter Client ID!")

        # Button to populate client details for editing
        populate_button = ttk.Button(edit_client_frame, text="Populate", command=populate_client_details, style="TButton")
        populate_button.grid(row=0, column=2, padx=5, pady=5)

    def populate_edit_client_screen(self, client_details):
        # Clear any existing widgets on the screen
        self.clear_frame()

        # Create a frame for editing client details
        edit_client_frame = tk.Frame(self.master, bg="#E6E6FA")
        edit_client_frame.pack(pady=20)

        # Labels and entries for client details
        tk.Label(edit_client_frame, text="Name:", bg="#E6E6FA").grid(row=0, column=0, padx=5, pady=5)
        name_entry = ttk.Entry(edit_client_frame)
        name_entry.insert(0, client_details.get('Name'))  # Populate with client name
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(edit_client_frame, text="Client ID:", bg="#E6E6FA").grid(row=1, column=0, padx=5, pady=5)
        client_id_entry = ttk.Entry(edit_client_frame)
        client_id_entry.insert(0, client_details.get('Client ID'))  # Populate with client ID
        client_id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(edit_client_frame, text="Address:", bg="#E6E6FA").grid(row=2, column=0, padx=5, pady=5)
        address_entry = ttk.Entry(edit_client_frame)
        address_entry.insert(0, client_details.get('Address'))  # Populate with address
        address_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(edit_client_frame, text="Contact Details:", bg="#E6E6FA").grid(row=3, column=0, padx=5, pady=5)
        contact_details_entry = ttk.Entry(edit_client_frame)
        contact_details_entry.insert(0, client_details.get('Contact Details'))  # Populate with contact details
        contact_details_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(edit_client_frame, text="Budget:", bg="#E6E6FA").grid(row=4, column=0, padx=5, pady=5)
        budget_entry = ttk.Entry(edit_client_frame)
        budget_entry.insert(0, client_details.get('Budget'))  # Populate with budget
        budget_entry.grid(row=4, column=1, padx=5, pady=5)

        # Button to update client
        update_button = ttk.Button(edit_client_frame, text="Update Client", command=lambda: self.update_client_in_system(
            client_id_entry.get(), name_entry.get(), address_entry.get(), contact_details_entry.get(),
            budget_entry.get()), style="TButton")
        update_button.grid(row=5, columnspan=2, pady=10)

    def update_client_in_system(self, client_id, name, address, contact_details, budget):
        # Read all clients from the file
        clients_obj = Client('', '', '', '', '')
        clients = clients_obj.read_clients_from_file()

        if clients:
            # Update the client details
            for client in clients:
                if client.get('Client ID') == client_id:
                    client['Name'] = name
                    client['Address'] = address
                    client['Contact Details'] = contact_details
                    client['Budget'] = budget
                    break
            else:
                messagebox.showerror("Error", "Client not found!")
                return
            # Write the updated client data back to the file
            FileHandler.write_to_binary_file(clients, 'clients.pkl')
            messagebox.showinfo("Success", "Client details updated successfully!")
            self.back_to_main_menu()
        else:
            messagebox.showerror("Error", "No clients data found!")

    def delete_client(self):
        # Clear any existing widgets on the screen
        self.clear_frame()

        # Create a frame for delete client functionality
        delete_frame = tk.Frame(self.master, bg="#E6E6FA")
        delete_frame.pack(pady=20)

        # Create label and entry for entering client ID
        client_id_label = tk.Label(delete_frame, text="Enter Client ID:", font=("Arial", 12), bg="#E6E6FA")
        client_id_label.grid(row=0, column=0, padx=5, pady=5)

        client_id_entry = ttk.Entry(delete_frame, font=("Arial", 12))
        client_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Function to delete client when the "Delete" button is clicked
        def delete_client_func():
            client_id = client_id_entry.get()

            if client_id:
                client_obj = Client('', '', '', '', '')  # Adjust with your Client class initialization
                if client_obj.delete_client_by_id(client_id):  # Adjust with your delete method
                    messagebox.showinfo("Success", "Client deleted successfully!")
                    self.back_to_main_menu()
                else:
                    messagebox.showerror("Error", "Client not found!")
            else:
                messagebox.showerror("Error", "Please enter Client ID!")

        # Button to delete client
        delete_button = ttk.Button(delete_frame, text="Delete", command=delete_client_func, style="TButton")
        delete_button.grid(row=0, column=2, padx=5, pady=5)

    def display_client(self):
        # Clear any existing widgets on the screen
        self.clear_frame()

        # Create a frame to display client details
        display_frame = tk.Frame(self.master, bg="#E6E6FA")
        display_frame.pack(pady=20)

        # Create label and entry for entering client ID
        client_id_label = tk.Label(display_frame, text="Enter Client ID:", font=("Arial", 12), bg="#E6E6FA")
        client_id_label.grid(row=0, column=0, padx=5, pady=5)

        client_id_entry = ttk.Entry(display_frame, font=("Arial", 12))
        client_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Function to display client details when the "Display" button is clicked
        def display_details():
            client_id = client_id_entry.get()

            if client_id:
                client_obj = Client('', '', '', '', '')  # Adjust with your Client class initialization
                clients = client_obj.read_clients_from_file()  # Adjust with your method to read client data

                if clients:
                    for client in clients:
                        if client.get('Client ID') == client_id:  # Accessing the ID from the dictionary
                            # Create a frame to display client details
                            details_frame = tk.Frame(display_frame, bg="white")
                            details_frame.grid(row=2, column=0, columnspan=3, pady=10, padx=10, sticky="nsew")

                            # Create a label to display client details inside the frame
                            details_label = tk.Label(details_frame, text=f"Name: {client.get('Name')}\n"
                                                                        f"Client ID: {client.get('Client ID')}\n"
                                                                        f"Address: {client.get('Address')}\n"
                                                                        f"Email: {client.get('Email')}\n"
                                                                        f"Phone: {client.get('Phone')}",
                                                    font=("Arial", 12), bg="white")
                            details_label.pack(padx=10, pady=10)
                            break
                    else:
                        messagebox.showerror("Error", "Client not found!")
                else:
                    messagebox.showerror("Error", "No clients data found!")
                    self.back_to_main_menu()
            else:
                messagebox.showerror("Error", "Please enter Client ID!")

        # Button to display client details
        display_button = ttk.Button(display_frame, text="Display", command=display_details, style="TButton")
        display_button.grid(row=0, column=2, padx=5, pady=5)

        close_button = ttk.Button(display_frame, text="Close", command=self.back_to_main_menu, style="TButton", width=15)
        close_button.grid(row=1, columnspan=2, pady=10)


    def add_venue(self):
        self.clear_frame()
        
        add_venue_frame = tk.Frame(self.master, bg="#E6E6FA")
        add_venue_frame.pack(pady=20)

        # Label and entry for venue details
        tk.Label(add_venue_frame, text="Name:", bg="#E6E6FA").grid(row=0, column=0, padx=5, pady=5)
        name_entry = ttk.Entry(add_venue_frame)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(add_venue_frame, text="Venue ID:", bg="#E6E6FA").grid(row=1, column=0, padx=5, pady=5)
        venue_id_entry = ttk.Entry(add_venue_frame)
        venue_id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(add_venue_frame, text="Address:", bg="#E6E6FA").grid(row=2, column=0, padx=5, pady=5)
        address_entry = ttk.Entry(add_venue_frame)
        address_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(add_venue_frame, text="Contact:", bg="#E6E6FA").grid(row=3, column=0, padx=5, pady=5)
        contact_entry = ttk.Entry(add_venue_frame)
        contact_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(add_venue_frame, text="Min Guests:", bg="#E6E6FA").grid(row=4, column=0, padx=5, pady=5)
        min_guests_entry = ttk.Entry(add_venue_frame)
        min_guests_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(add_venue_frame, text="Max Guests:", bg="#E6E6FA").grid(row=5, column=0, padx=5, pady=5)
        max_guests_entry = ttk.Entry(add_venue_frame)
        max_guests_entry.grid(row=5, column=1, padx=5, pady=5)

        # Button to add venue
        add_button = ttk.Button(add_venue_frame, text="Add Venue", command=lambda: self.add_venue_to_system(
            venue_id_entry.get(), name_entry.get(), address_entry.get(), contact_entry.get(),
            min_guests_entry.get(), max_guests_entry.get()), style="TButton")
        add_button.grid(row=6, columnspan=2, pady=10)

    def add_venue_to_system(self, venue_id, name, address, contact, min_guests, max_guests):
        if not all([name, venue_id, address, contact, min_guests, max_guests]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Validation for venue name
        if not name.replace(" ", "").isalpha():
            messagebox.showerror("Error", "Venue name should contain alphabets only.")
            return

        # Validation for venue ID
        if not venue_id.isdigit():
            messagebox.showerror("Error", "Venue ID should contain digits only.")
            return

        # If all validation passed, proceed with adding venue
        venue_data = {
            'Venue ID': venue_id,
            'Name': name,
            'Address': address,
            'Contact': contact,
            'Min Guests': min_guests,
            'Max Guests': max_guests
        }
        self.venue.add_venue(venue_data)
        messagebox.showinfo("Success", "Venue added successfully!")
        self.back_to_main_menu()

    def edit_venue(self):
        # Clear any existing widgets on the screen
        self.clear_frame()
        
        # Create a frame for editing venue details
        edit_venue_frame = tk.Frame(self.master, bg="#E6E6FA")
        edit_venue_frame.pack(pady=20)

        # Label and entry for venue ID
        tk.Label(edit_venue_frame, text="Enter Venue ID:", bg="#E6E6FA").grid(row=0, column=0, padx=5, pady=5)
        venue_id_entry = ttk.Entry(edit_venue_frame)
        venue_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Function to populate venue details for editing
        def populate_venue_details():
            venue_id = venue_id_entry.get()

            if venue_id:
                # Assuming you have a Venue class with appropriate methods
                venue_obj = Venue('', '', '', '', '', '')
                venues = venue_obj.read_venues_from_file()
                if venues:
                    for venue in venues:
                        if venue.get('Venue ID') == venue_id:
                            # Create a new screen similar to add venue with fields filled
                            self.populate_edit_venue_screen(venue)
                            break
                    else:
                        messagebox.showerror("Error", "Venue not found!")
                else:
                    messagebox.showerror("Error", "No venues data found!")
            else:
                messagebox.showerror("Error", "Please enter Venue ID!")

        # Button to populate venue details for editing
        populate_button = ttk.Button(edit_venue_frame, text="Populate", command=populate_venue_details, style="TButton")
        populate_button.grid(row=0, column=2, padx=5, pady=5)

    def populate_edit_venue_screen(self, venue_details):
        # Clear any existing widgets on the screen
        self.clear_frame()
        
        # Create a frame for editing venue details
        edit_venue_frame = tk.Frame(self.master, bg="#E6E6FA")
        edit_venue_frame.pack(pady=20)

        # Labels and entries for venue details
        tk.Label(edit_venue_frame, text="Name:", bg="#E6E6FA").grid(row=0, column=0, padx=5, pady=5)
        name_entry = ttk.Entry(edit_venue_frame)
        name_entry.insert(0, venue_details.get('Name'))  # Populate with venue name
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(edit_venue_frame, text="Venue ID:", bg="#E6E6FA").grid(row=1, column=0, padx=5, pady=5)
        venue_id_entry = ttk.Entry(edit_venue_frame)
        venue_id_entry.insert(0, venue_details.get('Venue ID'))  # Populate with venue ID
        venue_id_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(edit_venue_frame, text="Address:", bg="#E6E6FA").grid(row=2, column=0, padx=5, pady=5)
        address_entry = ttk.Entry(edit_venue_frame)
        address_entry.insert(0, venue_details.get('Address'))  # Populate with address
        address_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(edit_venue_frame, text="Contact:", bg="#E6E6FA").grid(row=3, column=0, padx=5, pady=5)
        contact_entry = ttk.Entry(edit_venue_frame)
        contact_entry.insert(0, venue_details.get('Contact'))  # Populate with contact
        contact_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(edit_venue_frame, text="Min Guests:", bg="#E6E6FA").grid(row=4, column=0, padx=5, pady=5)
        min_guests_entry = ttk.Entry(edit_venue_frame)
        min_guests_entry.insert(0, venue_details.get('Min Guests'))  # Populate with min guests
        min_guests_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(edit_venue_frame, text="Max Guests:", bg="#E6E6FA").grid(row=5, column=0, padx=5, pady=5)
        max_guests_entry = ttk.Entry(edit_venue_frame)
        max_guests_entry.insert(0, venue_details.get('Max Guests'))  # Populate with max guests
        max_guests_entry.grid(row=5, column=1, padx=5, pady=5)

        # Button to update venue
        update_button = ttk.Button(edit_venue_frame, text="Update Venue", command=lambda: self.update_venue_in_system(
            venue_id_entry.get(), name_entry.get(), address_entry.get(), contact_entry.get(),
            min_guests_entry.get(), max_guests_entry.get()), style="TButton")
        update_button.grid(row=6, columnspan=2, pady=10)

    def update_venue_in_system(self, venue_id, name, address, contact, min_guests, max_guests):
        # Read all venues from the file
        venue_obj = Venue('', '', '', '', '', '')
        venues = venue_obj.read_venues_from_file()

        if venues:
            # Find the venue with the provided ID
            for venue in venues:
                if venue.get('Venue ID') == venue_id:
                    # Update venue details
                    venue['Name'] = name
                    venue['Address'] = address
                    venue['Contact'] = contact
                    venue['Min Guests'] = min_guests
                    venue['Max Guests'] = max_guests
                    break
            else:
                messagebox.showerror("Error", "Venue not found!")
                return

            # Write the updated venue data back to the file
            # Assuming you have a method write_to_binary_file in your FileHandler class
            FileHandler.write_to_binary_file(venues, 'venues.pkl')
            messagebox.showinfo("Success", "Venue details updated successfully!")
            self.back_to_main_menu()
        else:
            messagebox.showerror("Error", "No venues data found!")

    def delete_venue(self):
        # Clear any existing widgets on the screen
        self.clear_frame()
        
        # Create a frame for delete venue functionality
        delete_frame = tk.Frame(self.master, bg="#E6E6FA")
        delete_frame.pack(pady=20)

        # Create label and entry for entering venue ID
        venue_id_label = tk.Label(delete_frame, text="Enter Venue ID:", font=("Arial", 12), bg="#E6E6FA")
        venue_id_label.grid(row=0, column=0, padx=5, pady=5)

        venue_id_entry = ttk.Entry(delete_frame, font=("Arial", 12))
        venue_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Function to delete venue when the "Delete" button is clicked
        def delete_venue_func():
            venue_id = venue_id_entry.get()

            if venue_id:
                venue_obj = Venue('', '', '', '', '', '')
                if venue_obj.delete_venue_by_id(venue_id):
                    messagebox.showinfo("Success", "Venue deleted successfully!")
                    self.back_to_main_menu()
                else:
                    messagebox.showerror("Error", "Venue not found!")
            else:
                messagebox.showerror("Error", "Please enter Venue ID!")

        # Button to delete venue
        delete_button = ttk.Button(delete_frame, text="Delete", command=delete_venue_func, style="TButton")
        delete_button.grid(row=0, column=2, padx=5, pady=5)

    def display_venue(self):
        # Clear any existing widgets on the screen
        self.clear_frame()
        
        # Create a frame to display venue details
        display_frame = tk.Frame(self.master, bg="#E6E6FA")
        display_frame.pack(pady=20)

        # Create label and entry for entering venue ID
        venue_id_label = tk.Label(display_frame, text="Enter Venue ID:", font=("Arial", 12), bg="#E6E6FA")
        venue_id_label.grid(row=0, column=0, padx=5, pady=5)

        venue_id_entry = ttk.Entry(display_frame, font=("Arial", 12))
        venue_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Function to display venue details when the "Display" button is clicked
        def display_details():
            venue_id = venue_id_entry.get()

            if venue_id:
                venue_obj = Venue('', '', '', '', '', '')
                venues = venue_obj.read_venues_from_file()

                if venues:
                    for venue in venues:
                        if venue.get('Venue ID') == venue_id:  # Accessing the ID from the dictionary
                            # Create a frame to display venue details
                            details_frame = tk.Frame(display_frame, bg="white")
                            details_frame.grid(row=2, column=0, columnspan=3, pady=10, padx=10, sticky="nsew")

                            # Create a label to display venue details inside the frame
                            details_label = tk.Label(details_frame, text=f"Name: {venue.get('Name')}\n"
                                                                        f"Venue ID: {venue.get('Venue ID')}\n"
                                                                        f"Address: {venue.get('Address')}\n"
                                                                        f"Contact: {venue.get('Contact')}\n"
                                                                        f"Min Guests: {venue.get('Min Guests')}\n"
                                                                        f"Max Guests: {venue.get('Max Guests')}",
                                                    font=("Arial", 12), bg="white")
                            details_label.pack(padx=10, pady=10)
                            break
                    else:
                        messagebox.showerror("Error", "Venue not found!")
                else:
                    messagebox.showerror("Error", "No venues data found!")
                    self.back_to_main_menu()
            else:
                messagebox.showerror("Error", "Please enter Venue ID!")

        # Button to display venue details
        display_button = ttk.Button(display_frame, text="Display", command=display_details, style="TButton")
        display_button.grid(row=0, column=2, padx=5, pady=5)

        close_button = ttk.Button(display_frame, text="Close", command=self.back_to_main_menu, style="TButton", width=15)
        close_button.grid(row=1, columnspan=2, pady=10)


    def add_event(self):
        self.clear_frame()

        add_event_frame = tk.Frame(self.master, bg="#E6E6FA")
        add_event_frame.pack(pady=20)

        # Label and entry for event details
        tk.Label(add_event_frame, text="Event ID:", bg="#E6E6FA").grid(row=0, column=0, padx=5, pady=5)
        event_id_entry = ttk.Entry(add_event_frame)
        event_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(add_event_frame, text="Event Type:", bg="#E6E6FA").grid(row=1, column=0, padx=5, pady=5)
        event_type_entry = ttk.Entry(add_event_frame)
        event_type_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(add_event_frame, text="Theme:", bg="#E6E6FA").grid(row=2, column=0, padx=5, pady=5)
        theme_entry = ttk.Entry(add_event_frame)
        theme_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(add_event_frame, text="Date:", bg="#E6E6FA").grid(row=3, column=0, padx=5, pady=5)
        date_entry = ttk.Entry(add_event_frame)
        date_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(add_event_frame, text="Time:", bg="#E6E6FA").grid(row=4, column=0, padx=5, pady=5)
        time_entry = ttk.Entry(add_event_frame)
        time_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(add_event_frame, text="Duration:", bg="#E6E6FA").grid(row=5, column=0, padx=5, pady=5)
        duration_entry = ttk.Entry(add_event_frame)
        duration_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(add_event_frame, text="Venue Address:", bg="#E6E6FA").grid(row=6, column=0, padx=5, pady=5)
        venue_address_entry = ttk.Entry(add_event_frame)
        venue_address_entry.grid(row=6, column=1, padx=5, pady=5)

        tk.Label(add_event_frame, text="Client ID:", bg="#E6E6FA").grid(row=7, column=0, padx=5, pady=5)
        client_id_entry = ttk.Entry(add_event_frame)
        client_id_entry.grid(row=7, column=1, padx=5, pady=5)

        tk.Label(add_event_frame, text="Guest List:", bg="#E6E6FA").grid(row=8, column=0, padx=5, pady=5)
        guest_list_entry = ttk.Entry(add_event_frame)
        guest_list_entry.grid(row=8, column=1, padx=5, pady=5)

        tk.Label(add_event_frame, text="Company:", bg="#E6E6FA").grid(row=9, column=0, padx=5, pady=5)
        company_entry = ttk.Entry(add_event_frame)
        company_entry.grid(row=9, column=1, padx=5, pady=5)

        tk.Label(add_event_frame, text="Invoice:", bg="#E6E6FA").grid(row=10, column=0, padx=5, pady=5)
        invoice_entry = ttk.Entry(add_event_frame)
        invoice_entry.grid(row=10, column=1, padx=5, pady=5)

        # Button to add event
        add_button = ttk.Button(add_event_frame, text="Add Event", command=lambda: self.add_event_to_system(
            event_id_entry.get(), event_type_entry.get(), theme_entry.get(), date_entry.get(), time_entry.get(),
            duration_entry.get(), venue_address_entry.get(), client_id_entry.get(),
            guest_list_entry.get(), company_entry.get(), invoice_entry.get()), style="TButton")
        add_button.grid(row=11, columnspan=2, pady=10)

    def add_event_to_system(self, event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, company, invoice):
        if not all([event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, company, invoice]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Validation for event ID
        if not event_id.isdigit():
            messagebox.showerror("Error", "Event ID should contain digits only.")
            return


        # If all validation passed, proceed with adding event
        event_data = {
            'Event ID': event_id,
            'Event Type': event_type,
            'Theme': theme,
            'Date': date,
            'Time': time,
            'Duration': duration,
            'Venue Address': venue_address,
            'Client ID': client_id,
            'Guest List': guest_list,
            'Company': company,
            'Invoice': invoice
        }
        self.event.add_event(event_data)  # Assuming self.events is a list to store events
        messagebox.showinfo("Success", "Event added successfully!")
        self.back_to_main_menu()

    def edit_event(self):
        # Clear any existing widgets on the screen
        self.clear_frame()
        
        # Create a frame for editing event details
        edit_event_frame = tk.Frame(self.master, bg="#E6E6FA")
        edit_event_frame.pack(pady=20)

        # Label and entry for event ID
        tk.Label(edit_event_frame, text="Enter Event ID:", bg="#E6E6FA").grid(row=0, column=0, padx=5, pady=5)
        event_id_entry = ttk.Entry(edit_event_frame)
        event_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Function to populate event details for editing
        def populate_event_details():
            event_id = event_id_entry.get()

            if event_id:
                events_obj = Event('', '', '', '', '', '', '', '', '', '', '')  # Adjust parameters accordingly
                events = events_obj.read_events_from_file()
                if events:
                    for event in events:
                        if event.get('Event ID') == event_id:
                            # Create a new screen similar to add event with fields filled
                            self.populate_edit_event_screen(event)
                            break
                    else:
                        messagebox.showerror("Error", "Event not found!")
                else:
                    messagebox.showerror("Error", "No events data found!")
            else:
                messagebox.showerror("Error", "Please enter Event ID!")

        # Button to populate event details for editing
        populate_button = ttk.Button(edit_event_frame, text="Populate", command=populate_event_details, style="TButton")
        populate_button.grid(row=0, column=2, padx=5, pady=5)

    def populate_edit_event_screen(self, event_details):
        # Clear any existing widgets on the screen
        self.clear_frame()
        
        # Create a frame for editing event details
        edit_event_frame = tk.Frame(self.master, bg="#E6E6FA")
        edit_event_frame.pack(pady=20)

        # Labels and entries for event details
        tk.Label(edit_event_frame, text="Event ID:", bg="#E6E6FA").grid(row=0, column=0, padx=5, pady=5)
        event_id_entry = ttk.Entry(edit_event_frame)
        event_id_entry.insert(0, event_details.get('Event ID'))  # Populate with event type
        event_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(edit_event_frame, text="Event Type:", bg="#E6E6FA").grid(row=1, column=0, padx=5, pady=5)
        event_type_entry = ttk.Entry(edit_event_frame)
        event_type_entry.insert(0, event_details.get('Event Type'))  # Populate with event type
        event_type_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(edit_event_frame, text="Theme:", bg="#E6E6FA").grid(row=2, column=0, padx=5, pady=5)
        theme_entry = ttk.Entry(edit_event_frame)
        theme_entry.insert(0, event_details.get('Theme'))  # Populate with theme
        theme_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(edit_event_frame, text="Date:", bg="#E6E6FA").grid(row=3, column=0, padx=5, pady=5)
        date_entry = ttk.Entry(edit_event_frame)
        date_entry.insert(0, event_details.get('Date'))  # Populate with date
        date_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(edit_event_frame, text="Time:", bg="#E6E6FA").grid(row=4, column=0, padx=5, pady=5)
        time_entry = ttk.Entry(edit_event_frame)
        time_entry.insert(0, event_details.get('Time'))  # Populate with time
        time_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(edit_event_frame, text="Duration:", bg="#E6E6FA").grid(row=5, column=0, padx=5, pady=5)
        duration_entry = ttk.Entry(edit_event_frame)
        duration_entry.insert(0, event_details.get('Duration'))  # Populate with time
        duration_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(edit_event_frame, text="Venue Address:", bg="#E6E6FA").grid(row=6, column=0, padx=5, pady=5)
        venue_address_entry = ttk.Entry(edit_event_frame)
        venue_address_entry.insert(0, event_details.get('Venue Address'))  # Populate with time
        venue_address_entry.grid(row=6, column=1, padx=5, pady=5)

        tk.Label(edit_event_frame, text="Client ID:", bg="#E6E6FA").grid(row=7, column=0, padx=5, pady=5)
        client_id_entry = ttk.Entry(edit_event_frame)
        client_id_entry.insert(0, event_details.get('Client ID'))  # Populate with time
        client_id_entry.grid(row=7, column=1, padx=5, pady=5)

        tk.Label(edit_event_frame, text="Guest List:", bg="#E6E6FA").grid(row=8, column=0, padx=5, pady=5)
        guest_list_entry = ttk.Entry(edit_event_frame)
        guest_list_entry.insert(0, event_details.get('Guest List'))  # Populate with time
        guest_list_entry.grid(row=8, column=1, padx=5, pady=5)

        tk.Label(edit_event_frame, text="Company:", bg="#E6E6FA").grid(row=9, column=0, padx=5, pady=5)
        company_entry = ttk.Entry(edit_event_frame)
        company_entry.insert(0, event_details.get('Company'))  # Populate with time
        company_entry.grid(row=9, column=1, padx=5, pady=5)

        tk.Label(edit_event_frame, text="Invoice:", bg="#E6E6FA").grid(row=10, column=0, padx=5, pady=5)
        invoice_entry = ttk.Entry(edit_event_frame)
        invoice_entry.insert(0, event_details.get('Invoice'))  # Populate with time
        invoice_entry.grid(row=10, column=1, padx=5, pady=5)

        # Button to update event
        update_button = ttk.Button(edit_event_frame, text="Update Event", command=lambda: self.update_event_in_system(
            event_id_entry.get(), event_type_entry.get(), theme_entry.get(), date_entry.get(), time_entry.get(), duration_entry.get(),
            venue_address_entry.get(), client_id_entry.get(),guest_list_entry.get(),company_entry.get(),invoice_entry.get()), style="TButton")
        update_button.grid(row=11, columnspan=2, pady=10)

    def update_event_in_system(self, event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, company, invoice):
        # Read all events from the file
        events_obj = Event('', '', '', '', '', '', '', '', '', '', '')  # Adjust parameters accordingly
        events = events_obj.read_events_from_file()

        if events:
            # Find the event with the provided ID
            for event in events:
                if event.get('Event ID') == event_id:
                    # Update event details
                    event['Event Type'] = event_type
                    event['Theme'] = theme
                    event['Date'] = date
                    event['Time'] = time
                    event['Duration'] = duration
                    event['Venue Address'] = venue_address
                    event['Client ID'] = client_id
                    event['Guest List'] = guest_list
                    event['Company'] = company
                    event['Invoice'] = invoice
                    # Update other fields similarly
                    break
            else:
                messagebox.showerror("Error", "Event not found!")
                return

            # Write the updated event data back to the file
            FileHandler.write_to_binary_file(events, 'events.pkl')
            messagebox.showinfo("Success", "Event details updated successfully!")
            self.back_to_main_menu()
        else:
            messagebox.showerror("Error", "No events data found!")

    def delete_event(self):
        # Clear any existing widgets on the screen
        self.clear_frame()
        
        # Create a frame for delete event functionality
        delete_frame = tk.Frame(self.master, bg="#E6E6FA")
        delete_frame.pack(pady=20)

        # Create label and entry for entering event ID
        event_id_label = tk.Label(delete_frame, text="Enter Event ID:", font=("Arial", 12), bg="#E6E6FA")
        event_id_label.grid(row=0, column=0, padx=5, pady=5)

        event_id_entry = ttk.Entry(delete_frame, font=("Arial", 12))
        event_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Function to delete event when the "Delete" button is clicked
        def delete_event_func():
            event_id = event_id_entry.get()

            if event_id:
                event_obj = Event('', '', '', '', '', '', '', '', '', '', '')  # Adjust parameters accordingly
                if event_obj.delete_event_by_id(event_id):
                    messagebox.showinfo("Success", "Event deleted successfully!")
                    self.back_to_main_menu()
                else:
                    messagebox.showerror("Error", "Event not found!")
            else:
                messagebox.showerror("Error", "Please enter Event ID!")

        # Button to delete event
        delete_button = ttk.Button(delete_frame, text="Delete", command=delete_event_func, style="TButton")
        delete_button.grid(row=0, column=2, padx=5, pady=5)

    def display_event(self):
        # Clear any existing widgets on the screen
        self.clear_frame()
        
        # Create a frame to display event details
        display_frame = tk.Frame(self.master, bg="#E6E6FA")
        display_frame.pack(pady=20)

        # Create label and entry for entering event ID
        event_id_label = tk.Label(display_frame, text="Enter Event ID:", font=("Arial", 12), bg="#E6E6FA")
        event_id_label.grid(row=0, column=0, padx=5, pady=5)

        event_id_entry = ttk.Entry(display_frame, font=("Arial", 12))
        event_id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Function to display event details when the "Display" button is clicked
        def display_details():
            event_id = event_id_entry.get()

            if event_id:
                event_obj = Event('', '', '', '', '', '', '', '', '', '', '')  # Adjust parameters accordingly
                events = event_obj.read_events_from_file()

                if events:
                    for event in events:
                        if event.get('Event ID') == event_id:  # Accessing the ID from the dictionary
                            # Create a frame to display event details
                            details_frame = tk.Frame(display_frame, bg="white")
                            details_frame.grid(row=2, column=0, columnspan=3, pady=10, padx=10, sticky="nsew")

                            # Create a label to display event details inside the frame
                            details_label = tk.Label(details_frame, text=f"Event Type: {event.get('Event Type')}\n"
                                                                        f"Theme: {event.get('Theme')}\n"
                                                                        f"Date: {event.get('Date')}\n"
                                                                        f"Time: {event.get('Time')}\n"
                                                                        f"Duration: {event.get('Duration')}\n"
                                                                        f"Venue Address: {event.get('Venue Address')}\n"
                                                                        f"Client ID: {event.get('Client ID')}\n"
                                                                        f"Guest List: {event.get('Guest List')}\n"
                                                                        f"Company: {event.get('Company')}\n"
                                                                        f"Invoice: {event.get('Invoice')}",
                                                    font=("Arial", 12), bg="white")
                            details_label.pack(padx=10, pady=10)
                            break
                    else:
                        messagebox.showerror("Error", "Event not found!")
                else:
                    messagebox.showerror("Error", "No events data found!")
                    self.back_to_main_menu()
            else:
                messagebox.showerror("Error", "Please enter Event ID!")

        # Button to display event details
        display_button = ttk.Button(display_frame, text="Display", command=display_details, style="TButton")
        display_button.grid(row=0, column=2, padx=5, pady=5)

        close_button = ttk.Button(display_frame, text="Close", command=self.back_to_main_menu, style="TButton", width=15)
        close_button.grid(row=1, columnspan=2, pady=10)

    def display_upcoming_events(self):
        # Clear any existing widgets on the screen
        self.clear_frame()

        display_frame = tk.Frame(self.master, bg="#E6E6FA")
        display_frame.pack(pady=20)

        # Get current date
        current_date = datetime.datetime.now().date()

        # Read events from file
        events_obj = Event('', '', '', '', '', '', '', '', '', '', '')  # Adjust parameters accordingly
        events = events_obj.read_events_from_file()

        # Filter upcoming events
        upcoming_events = [event for event in events if datetime.datetime.strptime(event['Date'], '%Y-%m-%d').date() >= current_date]

        # Create a frame to display upcoming events
        upcoming_events_frame = tk.Frame(self.master, bg="#E6E6FA")
        upcoming_events_frame.pack(pady=20)

        if upcoming_events:
            # Display upcoming events
            for i, event in enumerate(upcoming_events):
                event_details_label = tk.Label(upcoming_events_frame, text=f"Event {i+1}:\n"
                                                                            f"Event Type: {event.get('Event Type')}\n"
                                                                            f"Theme: {event.get('Theme')}\n"
                                                                            f"Date: {event.get('Date')}\n"
                                                                            f"Time: {event.get('Time')}\n"
                                                                            f"Duration: {event.get('Duration')}\n"
                                                                            f"Venue Address: {event.get('Venue Address')}\n"
                                                                            f"Client ID: {event.get('Client ID')}\n"
                                                                            f"Guest List: {event.get('Guest List')}\n"
                                                                            f"Company: {event.get('Company')}\n"
                                                                            f"Invoice: {event.get('Invoice')}",
                                                                            font=("Arial", 12), bg="#E6E6FA")
                event_details_label.grid(row=i, column=0, padx=10, pady=10, sticky="w")
        else:
            # No upcoming events
            no_events_label = tk.Label(upcoming_events_frame, text="No upcoming events", font=("Arial", 12), bg="#E6E6FA")
            no_events_label.pack(padx=10, pady=10)

        # Place close button below event details
        close_button = ttk.Button(display_frame, text="Close", command=self.back_to_main_menu, style="TButton", width=15)
        close_button.pack(pady=10)


    def clear_frame(self):
        for widget in self.master.winfo_children():
            widget.destroy()

def main():
    root = tk.Tk()
    app = ManagementGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

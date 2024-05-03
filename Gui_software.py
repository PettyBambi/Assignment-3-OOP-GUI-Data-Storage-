import tkinter as tk
from tkinter import messagebox
import pickle
from Employee import Employee
from Client import Client
from Guest import Guest
from Supplier import Supplier
from Event import Event, EventType

class MyGUI: # Created class
    """Main window of Event Manager"""
    def __init__(self): # Initialization
        self.employee_window = None
        self.main_window = tk.Tk()
        self.main_window.title("Event Management System")
        # creating buttons
        self.employee_button = tk.Button(self.main_window, text="Employee", command=self.employee_actions)
        self.employee_button.pack()
        self.Client_button = tk.Button(self.main_window, text="Client", command=self.client_actions)
        self.Client_button.pack()
        self.guest_button = tk.Button(self.main_window, text="Guest", command=self.guest_actions)
        self.guest_button.pack()
        self.supplier_button = tk.Button(self.main_window, text="Supplier", command=self.supplier_actions)
        self.supplier_button.pack()
        self.venue_button = tk.Button(self.main_window, text="Venue", command=self.venue_actions)
        self.venue_button.pack()
        self.event_button = tk.Button(self.main_window, text="Event", command=self.event_actions)
        self.event_button.pack()

    def employee_actions(self): #function of buttons to determine each action
        self.employee_window = tk.Toplevel(self.main_window)
        self.employee_window.title("Employee Actions")

        add_button = tk.Button(self.employee_window, text="Add", command=self.add_employee)
        add_button.pack()
        delete_button = tk.Button(self.employee_window, text="Delete Employee", command=self.delete_employee)
        delete_button.pack()
        modify_button = tk.Button(self.employee_window, text="Modify", command=self.modify_employee)
        modify_button.pack()
        display_button = tk.Button(self.employee_window, text="Display Employee Details",command=self.display_employee_details)
        display_button.pack()

    def add_employee(self):
        # Create a new window for adding an employee
        self.add_employee_window = tk.Toplevel(self.main_window)
        self.add_employee_window.title("Add Employee")

        # Labels and Entries for attributes
        tk.Label(self.add_employee_window, text="Personal ID").grid(row=0, column=0)
        self.personal_id_entry = tk.Entry(self.add_employee_window)
        self.personal_id_entry.grid(row=0, column=1)

        tk.Label(self.add_employee_window, text="First Name:").grid(row=1, column=0)
        self.first_name_entry = tk.Entry(self.add_employee_window)
        self.first_name_entry.grid(row=1, column=1)

        tk.Label(self.add_employee_window, text="Last Name:").grid(row=2, column=0)
        self.last_name_entry = tk.Entry(self.add_employee_window)
        self.last_name_entry.grid(row=2, column=1)

        tk.Label(self.add_employee_window, text="Email:").grid(row=3, column=0)
        self.email_entry = tk.Entry(self.add_employee_window)
        self.email_entry.grid(row=3, column=1)

        tk.Label(self.add_employee_window, text="Phone:").grid(row=4, column=0)
        self.phone_entry = tk.Entry(self.add_employee_window)
        self.phone_entry.grid(row=4, column=1)

        tk.Label(self.add_employee_window, text="Birth Date:").grid(row=5, column=0)
        self.birth_of_date_entry = tk.Entry(self.add_employee_window)
        self.birth_of_date_entry.grid(row=5, column=1)

        tk.Label(self.add_employee_window, text="Age:").grid(row=6, column=0)
        self.age_entry = tk.Entry(self.add_employee_window)
        self.age_entry.grid(row=6, column=1)

        tk.Label(self.add_employee_window, text="Gender:").grid(row=7, column=0)
        self.gender_entry = tk.Entry(self.add_employee_window)
        self.gender_entry.grid(row=7, column=1)

        tk.Label(self.add_employee_window, text="Nationality:").grid(row=8, column=0)
        self.nationality_entry = tk.Entry(self.add_employee_window)
        self.nationality_entry.grid(row=8, column=1)

        tk.Label(self.add_employee_window, text="Department:").grid(row=9, column=0)
        self.department_entry = tk.Entry(self.add_employee_window)
        self.department_entry.grid(row=9, column=1)

        tk.Label(self.add_employee_window, text="Job Title:").grid(row=10, column=0)
        self.job_title_entry = tk.Entry(self.add_employee_window)
        self.job_title_entry.grid(row=10, column=1)

        tk.Label(self.add_employee_window, text="Salary:").grid(row=11, column=0)
        self.salary_entry = tk.Entry(self.add_employee_window)
        self.salary_entry.grid(row=11, column=1)

        tk.Label(self.add_employee_window, text="Manager ID:").grid(row=12, column=0)
        self.manager_id_entry = tk.Entry(self.add_employee_window)
        self.manager_id_entry.grid(row=12, column=1)

        tk.Label(self.add_employee_window, text="Employee ID:").grid(row=13, column=0)
        self.employee_id_entry = tk.Entry(self.add_employee_window)
        self.employee_id_entry.grid(row=13, column=1)

        # Button to confirm adding the employee
        confirm_button = tk.Button(self.add_employee_window, text="Add", command=self.confirm_add_employee)
        confirm_button.grid(row=14, column=0, columnspan=2)
    def confirm_add_employee(self):
        # Retrieve values from the Entries
        personal_id = self.personal_id_entry.get()
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        birth_of_date = self.birth_of_date_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()
        nationality = self.nationality_entry.get()
        department = self.department_entry.get()
        job_title = self.job_title_entry.get()
        salary = self.salary_entry.get()
        manager_id = self.manager_id_entry.get()
        employee_id = self.employee_id_entry.get()
        # Checks for fields boxes
        if not (personal_id and first_name and last_name and email and phone and birth_of_date and age and gender
                and nationality and department and job_title and salary and manager_id and employee_id):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            # Check if age can be converted to integer
            age = int(age)
            # Add more checks for other fields if needed
        except ValueError:
            messagebox.showerror("Error", "Age must be a number.")
            return

        try:
            # Check if salary can be converted to float
            salary = float(salary)
            # Add more checks for other fields if needed
        except ValueError:
            messagebox.showerror("Error", "Salary must be a number.")
            return
        # Create an instance of the Employee class
        new_employee = Employee(personal_id, first_name, last_name, email, phone, birth_of_date, age, gender,nationality, department, job_title, salary, manager_id, employee_id)
        # Checks if the Employee ID already exists in the pickle file
        try:
            with open('employees_data.pickle', 'rb') as file:
                employees = pickle.load(file)
        except FileNotFoundError:
            employees = {}

        if employee_id in employees:
            messagebox.showerror("Error", f"Employee ID {employee_id} already exists!")
            return

        # Adds the new employee to the dictionary
        employees[employee_id] = new_employee.get_employee_info()

        # Save the updated employee data
        with open('employees_data.pickle', 'wb') as file:
            pickle.dump(employees, file)

        messagebox.showinfo("Success", "Employee added successfully!")
        self.add_employee_window.destroy()
    def display_employee_details(self):
        # Create a new window for displaying employee details
        self.display_employee_window = tk.Toplevel(self.main_window)
        self.display_employee_window.title("Employee Details")

        # Label and Entry widget for entering the employee ID
        tk.Label(self.display_employee_window, text="Employee ID:").grid(row=0, column=0)
        self.employee_id_entry_display = tk.Entry(self.display_employee_window)
        self.employee_id_entry_display.grid(row=0, column=1)

        # Button to confirm displaying the employee details
        confirm_button = tk.Button(self.display_employee_window, text="Display Details",command=self.confirm_display_employee_details)
        confirm_button.grid(row=1, column=0, columnspan=2)
    def confirm_display_employee_details(self):
        # Get the employee ID entered by the user
        employee_id = self.employee_id_entry_display.get()

        try:
            # Load existing employees from the pickle file
            with open('employees_data.pickle', 'rb') as file:
                employees = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "No employees found!")
            return

        # Check if the entered employee ID exists in the dictionary
        if employee_id in employees:
            # Get the details of the employee with the specified ID
            employee_details = employees[employee_id]

            # Create a new window to display the employee details
            display_details_window = tk.Toplevel(self.display_employee_window)
            display_details_window.title("Employee Details")

            # Display employee details using labels
            row_index = 0
            for key, value in employee_details.items():
                detail_label = tk.Label(display_details_window, text=f"{key}: {value}")
                detail_label.grid(row=row_index, column=0, sticky="w")
                row_index += 1
        else:
            messagebox.showerror("Error", f"No employee found with ID {employee_id}")
    def delete_employee(self):
        # Create a new window for deleting an employee
        self.delete_employee_window = tk.Toplevel(self.main_window)
        self.delete_employee_window.title("Delete Employee")

        # Label and Entry widget for employee ID
        tk.Label(self.delete_employee_window, text="Employee ID:").grid(row=0, column=0)
        self.delete_employee_id_entry = tk.Entry(self.delete_employee_window)
        self.delete_employee_id_entry.grid(row=0, column=1)

        # Button to confirm deleting the employee
        confirm_button = tk.Button(self.delete_employee_window, text="Delete", command=self.confirm_delete_employee)
        confirm_button.grid(row=1, column=0, columnspan=2)
    def confirm_delete_employee(self):
        # Retrieve employee ID from the Entry widget
        employee_id = self.delete_employee_id_entry.get()

        try:
            # Load the dictionary of employees from the pickle file
            with open('employees_data.pickle', 'rb') as file:
                employees = pickle.load(file)
        except FileNotFoundError:
            # If the file is not found, create an empty dictionary
            employees = {}

        # Check if the employee ID exists in the dictionary
        if employee_id in employees:
            # Remove the employee with the given ID from the dictionary
            employees.pop(employee_id)
            # Save the updated dictionary back to the pickle file
            with open('employees_data.pickle', 'wb') as file:
                pickle.dump(employees, file)
            # Show success message
            messagebox.showinfo("Success", f"Employee with ID {employee_id} deleted successfully!")
        else:
            # If the employee ID is not found, show error message
            messagebox.showerror("Error", f"No employee found with ID {employee_id}")

        # Destroy the delete employee window
        self.delete_employee_window.destroy()
    def modify_employee(self):
        # Create a new window for modifying an employee
        self.modify_employee_window = tk.Toplevel(self.main_window)
        self.modify_employee_window.title("Modify Employee")

        # Label and Entry widget for employee ID
        tk.Label(self.modify_employee_window, text="Employee ID:").grid(row=0, column=0)
        self.modify_employee_id_entry = tk.Entry(self.modify_employee_window)
        self.modify_employee_id_entry.grid(row=0, column=1)

        tk.Label(self.modify_employee_window, text="Modify details").grid(row=0, column=0)

        tk.Label(self.modify_employee_window, text="First Name:").grid(row=4, column=0)
        self.new_first_name_entry = tk.Entry(self.modify_employee_window)
        self.new_first_name_entry.grid(row=4, column=1)

        # Label and Entry widget for modifying Last Name
        tk.Label(self.modify_employee_window, text="Last Name:").grid(row=5, column=0)
        self.new_last_name_entry = tk.Entry(self.modify_employee_window)
        self.new_last_name_entry.grid(row=5, column=1)

        # Label and Entry widget for modifying Email
        tk.Label(self.modify_employee_window, text="Email:").grid(row=6, column=0)
        self.new_email_entry = tk.Entry(self.modify_employee_window)
        self.new_email_entry.grid(row=6, column=1)


        # Label and Entry widget for modifying Phone
        tk.Label(self.modify_employee_window, text="Phone:").grid(row=7, column=0)
        self.new_phone_entry = tk.Entry(self.modify_employee_window)
        self.new_phone_entry.grid(row=7, column=1)

        # Label and Entry widget for modifying Birth of Date
        tk.Label(self.modify_employee_window, text="Birth of Date:").grid(row=8, column=0)
        self.new_birth_of_date_entry = tk.Entry(self.modify_employee_window)
        self.new_birth_of_date_entry.grid(row=8, column=1)

        # Label and Entry widget for modifying Age
        tk.Label(self.modify_employee_window, text="Age:").grid(row=9, column=0)
        self.new_age_entry = tk.Entry(self.modify_employee_window)
        self.new_age_entry.grid(row=9, column=1)

        # Label and Entry widget for modifying Gender
        tk.Label(self.modify_employee_window, text="Gender:").grid(row=10, column=0)
        self.new_gender_entry = tk.Entry(self.modify_employee_window)
        self.new_gender_entry.grid(row=10, column=1)

        # Label and Entry widget for modifying Nationality
        tk.Label(self.modify_employee_window, text="Nationality:").grid(row=11, column=0)
        self.new_nationality_entry = tk.Entry(self.modify_employee_window)
        self.new_nationality_entry.grid(row=11, column=1)

        # Label and Entry widget for modifying Department
        tk.Label(self.modify_employee_window, text="Department:").grid(row=12, column=0)
        self.new_department_entry = tk.Entry(self.modify_employee_window)
        self.new_department_entry.grid(row=12, column=1)

        # Label and Entry widget for modifying Job Title
        tk.Label(self.modify_employee_window, text="Job Title:").grid(row=13, column=0)
        self.new_job_title_entry = tk.Entry(self.modify_employee_window)
        self.new_job_title_entry.grid(row=13, column=1)

        # Label and Entry widget for modifying Salary
        tk.Label(self.modify_employee_window, text="Salary:").grid(row=14, column=0)
        self.new_salary_entry = tk.Entry(self.modify_employee_window)
        self.new_salary_entry.grid(row=14, column=1)

        # Label and Entry widget for modifying Manager ID
        tk.Label(self.modify_employee_window, text="Manager ID:").grid(row=15, column=0)
        self.new_manager_id_entry = tk.Entry(self.modify_employee_window)
        self.new_manager_id_entry.grid(row=15, column=1)

        # Label and Entry widget for modifying Employee ID
        tk.Label(self.modify_employee_window, text="Employee ID:").grid(row=16, column=0)
        self.new_employee_id_entry = tk.Entry(self.modify_employee_window)
        self.new_employee_id_entry.grid(row=16, column=1)

        # Button to confirm modifying the employee
        confirm_button = tk.Button(self.modify_employee_window, text="Modify", command=self.confirm_modify_employee)
        confirm_button.grid(row=1, column=0, columnspan=2)
    def confirm_modify_employee(self):
        # Retrieve the employee ID from the entry widget
        employee_id = self.modify_employee_id_entry.get()

        try:
            # Load existing employees from the pickle file
            with open('employees_data.pickle', 'rb') as file:
                employees = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "No employees found!")
            return

        # Check if the employee ID exists
        if employee_id not in employees:
            messagebox.showerror("Error", f"No employee found with ID {employee_id}")
            return

        # Retrieve the modified details from the user input
        new_first_name = self.new_first_name_entry.get()
        new_last_name = self.new_last_name_entry.get()
        new_email = self.new_email_entry.get()
        new_phone = self.new_phone_entry.get()
        new_birth_of_date = self.new_birth_of_date_entry.get()
        new_age = self.new_age_entry.get()
        new_gender = self.new_gender_entry.get()
        new_nationality = self.new_nationality_entry.get()
        new_department = self.new_department_entry.get()
        new_job_title = self.new_job_title_entry.get()
        new_salary = self.new_salary_entry.get()
        new_manager_id = self.new_manager_id_entry.get()
        new_employee_id = self.new_employee_id_entry.get()
        try:
            # Check if age can be converted to integer
            new_age = int(new_age)
            # Add more checks for other fields if needed
        except ValueError:
            messagebox.showerror("Error", "Age must be a number.")
            return

        try:
            # Check if salary can be converted to float
            new_salary = float(new_salary)
            # Add more checks for other fields if needed
        except ValueError:
            messagebox.showerror("Error", "Salary must be a number.")
            return
        # Modify the employee object with the new details
        if new_first_name:
            employees[employee_id]['First name'] = new_first_name
        if new_last_name:
            employees[employee_id]['Last name'] = new_last_name
        if new_email:
            employees[employee_id]['Email'] = new_email
        if new_phone:
            employees[employee_id]['Phone'] = new_phone
        if new_birth_of_date:
            employees[employee_id]['Birth Date'] = new_birth_of_date
        if new_age:
            employees[employee_id]['Age'] = new_age
        if new_gender:
            employees[employee_id]['Gender'] = new_gender
        if new_nationality:
            employees[employee_id]['Nationality'] = new_nationality
        if new_department:
            employees[employee_id]['Department'] = new_department
        if new_job_title:
            employees[employee_id]['Job Title'] = new_job_title
        if new_salary:
            employees[employee_id]['Salary'] = new_salary
        if new_manager_id:
            employees[employee_id]['Manager ID'] = new_manager_id
        if new_employee_id:
            employees[employee_id]['Employee ID'] = new_employee_id

        # Save the updated employee data
        with open('employees_data.pickle', 'wb') as file:
            pickle.dump(employees, file)

        messagebox.showinfo("Success", "Employee details modified successfully!")
        self.modify_employee_window.destroy()



    def client_actions(self):
        self.Guest_window = tk.Toplevel(self.main_window)
        self.Guest_window.title("Client Actions")

        add_button = tk.Button(self.Guest_window, text="Add Client", command=self.add_client)
        add_button.pack()
        delete_button = tk.Button(self.Guest_window, text="Delete Client", command=self.delete_client)
        delete_button.pack()
        modify_button = tk.Button(self.Guest_window, text="Modify Client", command=self.modify_client)
        modify_button.pack()
        display_button = tk.Button(self.Guest_window, text="Display Client", command=self.display_client_details)
        display_button.pack()

    def add_client(self):
        # Create a new window for adding a client
        self.add_client_window = tk.Toplevel(self.Guest_window)
        self.add_client_window.title("Add Client")

        # Labels and Entry widgets for client details
        tk.Label(self.add_client_window, text="Client ID").grid(row=0, column=0)
        self.client_id_entry = tk.Entry(self.add_client_window)
        self.client_id_entry.grid(row=0, column=1)

        tk.Label(self.add_client_window, text="Personal ID").grid(row=1, column=0)
        self.personal_id_entry = tk.Entry(self.add_client_window)
        self.personal_id_entry.grid(row=1, column=1)

        tk.Label(self.add_client_window, text="First Name:").grid(row=2, column=0)
        self.first_name_entry = tk.Entry(self.add_client_window)
        self.first_name_entry.grid(row=2, column=1)

        tk.Label(self.add_client_window, text="Last Name:").grid(row=3, column=0)
        self.last_name_entry = tk.Entry(self.add_client_window)
        self.last_name_entry.grid(row=3, column=1)

        tk.Label(self.add_client_window, text="Email:").grid(row=4, column=0)
        self.email_entry = tk.Entry(self.add_client_window)
        self.email_entry.grid(row=4, column=1)

        tk.Label(self.add_client_window, text="Phone:").grid(row=5, column=0)
        self.phone_entry = tk.Entry(self.add_client_window)
        self.phone_entry.grid(row=5, column=1)

        tk.Label(self.add_client_window, text="Birth of Date:").grid(row=6, column=0)
        self.birth_of_date_entry = tk.Entry(self.add_client_window)
        self.birth_of_date_entry.grid(row=6, column=1)

        tk.Label(self.add_client_window, text="Age:").grid(row=7, column=0)
        self.age_entry = tk.Entry(self.add_client_window)
        self.age_entry.grid(row=7, column=1)

        tk.Label(self.add_client_window, text="Gender:").grid(row=8, column=0)
        self.gender_entry = tk.Entry(self.add_client_window)
        self.gender_entry.grid(row=8, column=1)

        tk.Label(self.add_client_window, text="Nationality:").grid(row=9, column=0)
        self.nationality_entry = tk.Entry(self.add_client_window)
        self.nationality_entry.grid(row=9, column=1)

        tk.Label(self.add_client_window, text="Budget:").grid(row=10, column=0)
        self.budget_entry = tk.Entry(self.add_client_window)
        self.budget_entry.grid(row=10, column=1)

        # Button to confirm adding the client
        confirm_button = tk.Button(self.add_client_window, text="Add", command=self.confirm_add_client)
        confirm_button.grid(row=11, column=0, columnspan=2)
    def confirm_add_client(self):
        # Retrieve values from the Entry widgets
        client_id = self.client_id_entry.get()
        personal_id = self.personal_id_entry.get()
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        birth_of_date = self.birth_of_date_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()
        nationality = self.nationality_entry.get()
        budget = self.budget_entry.get()
        if not (client_id and personal_id and first_name and last_name and email and phone
                and birth_of_date and age and gender and nationality and budget):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Check data types
        try:
            # Check if age can be converted to integer
            age = int(age)
            # Add more checks for other fields if needed
        except ValueError:
            messagebox.showerror("Error", "Age must be a number.")
            return

        try:
            # Check if budget can be converted to float
            budget = float(budget)
            # Add more checks for other fields if needed
        except ValueError:
            messagebox.showerror("Error", "Budget must be a number.")
            return
        # Create an instance of the Client class
        new_client = Client(client_id, personal_id, first_name, last_name, email, phone, birth_of_date, age, gender,
                            nationality, budget)

        # Check if the Client ID already exists in the pickle file
        try:
            with open('clients_data.pickle', 'rb') as file:
                clients = pickle.load(file)
        except FileNotFoundError:
            clients = {}

        if client_id in clients:
            messagebox.showerror("Error", f"Client ID {client_id} already exists!")
            return

        # Add the new client to the dictionary
        clients[client_id] = new_client.get_client_info()

        # Save the updated client data
        with open('clients_data.pickle', 'wb') as file:
            pickle.dump(clients, file)

        messagebox.showinfo("Success", "Client added successfully!")
        self.add_client_window.destroy()
    def delete_client(self):
        # Create a new window for deleting a client
        self.delete_client_window = tk.Toplevel(self.Guest_window)
        self.delete_client_window.title("Delete Client")

        # Label and Entry widget for client ID
        tk.Label(self.delete_client_window, text="Client ID:").grid(row=0, column=0)
        self.delete_client_id_entry = tk.Entry(self.delete_client_window)
        self.delete_client_id_entry.grid(row=0, column=1)

        # Button to confirm deleting the client
        confirm_button = tk.Button(self.delete_client_window, text="Delete", command=self.confirm_delete_client)
        confirm_button.grid(row=1, column=0, columnspan=2)
    def confirm_delete_client(self):
        # Retrieve client ID from the Entry widget
        client_id = self.delete_client_id_entry.get()

        try:
            # Load the dictionary of clients from the pickle file
            with open('clients_data.pickle', 'rb') as file:
                clients = pickle.load(file)
        except FileNotFoundError:
            # If the file is not found, create an empty dictionary
            clients = {}

        # Check if the client ID exists in the dictionary
        if client_id in clients:
            # Remove the client with the given ID from the dictionary
            clients.pop(client_id)
            # Save the updated dictionary back to the pickle file
            with open('clients_data.pickle', 'wb') as file:
                pickle.dump(clients, file)
            # Show success message
            messagebox.showinfo("Success", f"Client with ID {client_id} deleted successfully!")
        else:
            # If the client ID is not found, show error message
            messagebox.showerror("Error", f"No client found with ID {client_id}")

        # Destroy the delete client window
        self.delete_client_window.destroy()
    def modify_client(self):
        # Create a new window for modifying a client
        self.modify_client_window = tk.Toplevel(self.main_window)
        self.modify_client_window.title("Modify Client")

        # Label and Entry widget for client ID
        tk.Label(self.modify_client_window, text="Client ID:").grid(row=0, column=0)
        self.modify_client_id_entry = tk.Entry(self.modify_client_window)
        self.modify_client_id_entry.grid(row=0, column=1)

        tk.Label(self.modify_client_window, text="Modify details").grid(row=1, column=0)

        # Labels and Entries widget for modifying
        tk.Label(self.modify_client_window, text="Client ID").grid(row=2, column=0)
        self.new_client_id_entry = tk.Entry(self.modify_client_window)
        self.new_client_id_entry.grid(row=2, column=1)

        tk.Label(self.modify_client_window, text="First Name:").grid(row=3, column=0)
        self.new_first_name_entry = tk.Entry(self.modify_client_window)
        self.new_first_name_entry.grid(row=3, column=1)

        tk.Label(self.modify_client_window, text="Last Name:").grid(row=4, column=0)
        self.new_last_name_entry = tk.Entry(self.modify_client_window)
        self.new_last_name_entry.grid(row=4, column=1)

        tk.Label(self.modify_client_window, text="Email:").grid(row=5, column=0)
        self.new_email_entry = tk.Entry(self.modify_client_window)
        self.new_email_entry.grid(row=5, column=1)

        tk.Label(self.modify_client_window, text="Phone:").grid(row=6, column=0)
        self.new_phone_entry = tk.Entry(self.modify_client_window)
        self.new_phone_entry.grid(row=6, column=1)

        tk.Label(self.modify_client_window, text="Birth of Date:").grid(row=7, column=0)
        self.new_birth_of_date_entry = tk.Entry(self.modify_client_window)
        self.new_birth_of_date_entry.grid(row=7, column=1)

        tk.Label(self.modify_client_window, text="Age:").grid(row=8, column=0)
        self.new_age_entry = tk.Entry(self.modify_client_window)
        self.new_age_entry.grid(row=8, column=1)

        tk.Label(self.modify_client_window, text="Gender:").grid(row=9, column=0)
        self.new_gender_entry = tk.Entry(self.modify_client_window)
        self.new_gender_entry.grid(row=9, column=1)

        tk.Label(self.modify_client_window, text="Nationality:").grid(row=10, column=0)
        self.new_nationality_entry = tk.Entry(self.modify_client_window)
        self.new_nationality_entry.grid(row=10, column=1)

        tk.Label(self.modify_client_window, text="Budget:").grid(row=11, column=0)
        self.new_budget_entry = tk.Entry(self.modify_client_window)
        self.new_budget_entry.grid(row=11, column=1)

        # Button to confirm modifying the client
        confirm_button = tk.Button(self.modify_client_window, text="Modify", command=self.confirm_modify_client)
        confirm_button.grid(row=11, column=0, columnspan=2)
    def confirm_modify_client(self):
        # Retrieve the client ID from the entry widget
        client_id = self.modify_client_id_entry.get()

        try:
            # Load existing clients from the pickle file
            with open('clients_data.pickle', 'rb') as file:
                clients = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "No clients found!")
            return

        # Check if the client ID exists
        if client_id not in clients:
            messagebox.showerror("Error", f"No client found with ID {client_id}")
            return

        # Retrieve the modified details from the user input
        new_client_id = self.new_client_id_entry.get()
        new_first_name = self.new_first_name_entry.get()
        new_last_name = self.new_last_name_entry.get()
        new_email = self.new_email_entry.get()
        new_phone = self.new_phone_entry.get()
        new_birth_of_date = self.new_birth_of_date_entry.get()
        new_age = self.new_age_entry.get()
        new_gender = self.new_gender_entry.get()
        new_nationality = self.new_nationality_entry.get()
        new_budget = self.new_budget_entry.get()
        if not (
                new_client_id and new_first_name and new_last_name and new_email and new_phone
                and new_birth_of_date and new_age and new_gender and new_nationality and new_budget
        ):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Check data types
        try:
            # Check if age can be converted to integer
            new_age = int(new_age)
            # Add more checks for other fields if needed
        except ValueError:
            messagebox.showerror("Error", "Age must be a number.")
            return

        try:
            # Check if budget can be converted to float
            new_budget = float(new_budget)
            # Add more checks for other fields if needed
        except ValueError:
            messagebox.showerror("Error", "Budget must be a number.")
            return
        # Modify the client object with the new details
        if new_client_id:
            clients[client_id]['Client ID'] = new_client_id
        if new_first_name:
            clients[client_id]['First name'] = new_first_name
        if new_last_name:
            clients[client_id]['Last name'] = new_last_name
        if new_email:
            clients[client_id]['Email'] = new_email
        if new_phone:
            clients[client_id]['Phone'] = new_phone
        if new_birth_of_date:
            clients[client_id]['Birth Date'] = new_birth_of_date
        if new_age:
            clients[client_id]['Age'] = new_age
        if new_gender:
            clients[client_id]['Gender'] = new_gender
        if new_nationality:
            clients[client_id]['Nationality'] = new_nationality
        if new_budget:
            clients[client_id]['Budget'] = new_budget

        # Save the updated client data
        with open('clients_data.pickle', 'wb') as file:
            pickle.dump(clients, file)

        messagebox.showinfo("Success", "Client details modified successfully!")
        self.modify_client_window.destroy()
    def display_client_details(self):
        # Create a new window for displaying client details
        self.display_client_window = tk.Toplevel(self.Guest_window)
        self.display_client_window.title("Client Details")

        # Label and Entry widget for entering the client ID
        tk.Label(self.display_client_window, text="Client ID:").grid(row=0, column=0)
        self.client_id_entry_display = tk.Entry(self.display_client_window)
        self.client_id_entry_display.grid(row=0, column=1)

        # Button to confirm displaying the client details
        confirm_button = tk.Button(self.display_client_window, text="Display Details",
                                   command=self.confirm_display_client_details)
        confirm_button.grid(row=1, column=0, columnspan=2)
    def confirm_display_client_details(self):
        # Get the client ID entered by the user
        client_id = self.client_id_entry_display.get()

        try:
            # Load existing clients from the pickle file
            with open('clients_data.pickle', 'rb') as file:
                clients = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "No clients found!")
            return

        # Check if the entered client ID exists in the dictionary
        if client_id in clients:
            # Get the details of the client with the specified ID
            client_details = clients[client_id]
            # Create a new window to display the client details
            display_details_window = tk.Toplevel(self.display_client_window)
            display_details_window.title("Client Details")
            row_index = 0
            for key, value in client_details.items():
                detail_label = tk.Label(display_details_window, text=f"{key}: {value}")
                detail_label.grid(row=row_index, column=0, sticky="w")
                row_index += 1

        else:
            messagebox.showerror("Error", f"No client found with ID {client_id}")


    def guest_actions(self):
        self.Guest_window = tk.Toplevel(self.main_window)
        self.Guest_window.title("Client Actions")

        add_button = tk.Button(self.Guest_window, text="Add Guest", command=self.add_guest)
        add_button.pack()
        delete_button = tk.Button(self.Guest_window, text="Delete Guest", command=self.delete_guest)
        delete_button.pack()
        modify_button = tk.Button(self.Guest_window, text="Modify Guest", command=self.modify_guest)
        modify_button.pack()
        display_button = tk.Button(self.Guest_window, text="Display Guest", command=self.display_guest)
        display_button.pack()

    def add_guest(self):
        # Create a new window for adding a guest
        self.add_guest_window = tk.Toplevel(self.main_window)
        self.add_guest_window.title("Add Guest")

        # Labels and Entries widget for adding
        tk.Label(self.add_guest_window, text="Guest ID:").grid(row=0, column=0)
        self.guest_id_entry = tk.Entry(self.add_guest_window)
        self.guest_id_entry.grid(row=0, column=1)

        tk.Label(self.add_guest_window, text="First Name:").grid(row=1, column=0)
        self.first_name_entry = tk.Entry(self.add_guest_window)
        self.first_name_entry.grid(row=1, column=1)

        tk.Label(self.add_guest_window, text="Last Name:").grid(row=2, column=0)
        self.last_name_entry = tk.Entry(self.add_guest_window)
        self.last_name_entry.grid(row=2, column=1)

        tk.Label(self.add_guest_window, text="Email:").grid(row=3, column=0)
        self.email_entry = tk.Entry(self.add_guest_window)
        self.email_entry.grid(row=3, column=1)

        tk.Label(self.add_guest_window, text="Phone:").grid(row=4, column=0)
        self.phone_entry = tk.Entry(self.add_guest_window)
        self.phone_entry.grid(row=4, column=1)

        tk.Label(self.add_guest_window, text="Birth of Date:").grid(row=5, column=0)
        self.birth_of_date_entry = tk.Entry(self.add_guest_window)
        self.birth_of_date_entry.grid(row=5, column=1)

        tk.Label(self.add_guest_window, text="Age:").grid(row=6, column=0)
        self.age_entry = tk.Entry(self.add_guest_window)
        self.age_entry.grid(row=6, column=1)

        tk.Label(self.add_guest_window, text="Gender:").grid(row=7, column=0)
        self.gender_entry = tk.Entry(self.add_guest_window)
        self.gender_entry.grid(row=7, column=1)

        tk.Label(self.add_guest_window, text="Nationality:").grid(row=8, column=0)
        self.nationality_entry = tk.Entry(self.add_guest_window)
        self.nationality_entry.grid(row=8, column=1)

        tk.Label(self.add_guest_window, text="Personal ID:").grid(row=9, column=0)
        self.personal_id_entry = tk.Entry(self.add_guest_window)
        self.personal_id_entry.grid(row=9, column=1)

        tk.Label(self.add_guest_window, text="Birth of Date:").grid(row=10, column=0)
        self.birth_of_date_entry = tk.Entry(self.add_guest_window)
        self.birth_of_date_entry.grid(row=10, column=1)

        tk.Label(self.add_guest_window, text="Nationality:").grid(row=11, column=0)
        self.nationality_entry = tk.Entry(self.add_guest_window)
        self.nationality_entry.grid(row=11, column=1)

        # Button to confirm adding the guest
        confirm_button = tk.Button(self.add_guest_window, text="Add Guest", command=self.confirm_add_guest)
        confirm_button.grid(row=12, column=0, columnspan=2)
    def confirm_add_guest(self):
        # Retrieve guest details from entry widgets
        guest_id = self.guest_id_entry.get()
        personal_id = self.personal_id_entry.get()
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        birth_of_date = self.birth_of_date_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()
        nationality = self.nationality_entry.get()
        if not (
                guest_id and personal_id and first_name and last_name and email
                and phone and birth_of_date and age and gender and nationality
        ):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Check data types
        try:
            # Check if age can be converted to integer
            age = int(age)
            # Add more checks for other fields if needed
        except ValueError:
            messagebox.showerror("Error", "Age must be a number.")
            return
        # Create an instance of the Guest class
        new_guest = Guest(guest_id, personal_id, first_name, last_name, email, phone, birth_of_date, age, gender,
                          nationality)

        # Check if the Guest ID already exists in the pickle file
        try:
            with open('guests_data.pickle', 'rb') as file:
                guests = pickle.load(file)
        except FileNotFoundError:
            guests = {}

        if guest_id in guests:
            messagebox.showerror("Error", f"Guest ID {guest_id} already exists!")
            return

        # Add the new guest to the dictionary
        guests[guest_id] = new_guest.get_guest_info()

        # Save the updated guest data
        with open('guests_data.pickle', 'wb') as file:
            pickle.dump(guests, file)

        messagebox.showinfo("Success", "Guest added successfully!")
        self.add_guest_window.destroy()
    def delete_guest(self):
        # Create a new window for deleting a guest
        self.delete_guest_window = tk.Toplevel(self.Guest_window)
        self.delete_guest_window.title("Delete Guest")

        # Label and Entry widget for guest ID
        tk.Label(self.delete_guest_window, text="Guest ID:").grid(row=0, column=0)
        self.delete_guest_id_entry = tk.Entry(self.delete_guest_window)
        self.delete_guest_id_entry.grid(row=0, column=1)

        # Button to confirm deleting the guest
        confirm_button = tk.Button(self.delete_guest_window, text="Delete", command=self.confirm_delete_guest)
        confirm_button.grid(row=1, column=0, columnspan=2)
    def confirm_delete_guest(self):
        # Retrieve guest ID from the Entry widget
        guest_id = self.delete_guest_id_entry.get()

        try:
            # Load the dictionary of guests from the pickle file
            with open('guests_data.pickle', 'rb') as file:
                guests = pickle.load(file)
        except FileNotFoundError:
            # If the file is not found, create an empty dictionary
            guests = {}

        # Check if the guest ID exists in the dictionary
        if guest_id in guests:
            # Remove the guest with the given ID from the dictionary
            guests.pop(guest_id)
            # Save the updated dictionary back to the pickle file
            with open('guests_data.pickle', 'wb') as file:
                pickle.dump(guests, file)
            # Show success message
            messagebox.showinfo("Success", f"Guest with ID {guest_id} deleted successfully!")
        else:
            # If the guest ID is not found, show error message
            messagebox.showerror("Error", f"No guest found with ID {guest_id}")

        # Destroy the delete guest window
        self.delete_guest_window.destroy()
    def modify_guest(self):
        # Create a new window for modifying a guest
        self.modify_guest_window = tk.Toplevel(self.Guest_window)
        self.modify_guest_window.title("Modify Guest")

        # Labels and Entries widget for modifying
        tk.Label(self.modify_guest_window, text="Guest ID:").grid(row=0, column=0)
        self.modify_guest_id_entry = tk.Entry(self.modify_guest_window)
        self.modify_guest_id_entry.grid(row=0, column=1)

        tk.Label(self.modify_guest_window, text="Modify details").grid(row=1, column=0)

        tk.Label(self.modify_guest_window, text="Guest ID").grid(row=2, column=0)
        self.new_guest_id_entry = tk.Entry(self.modify_guest_window)
        self.new_guest_id_entry.grid(row=2, column=1)

        tk.Label(self.modify_guest_window, text="First Name:").grid(row=3, column=0)
        self.new_first_name_entry = tk.Entry(self.modify_guest_window)
        self.new_first_name_entry.grid(row=3, column=1)

        tk.Label(self.modify_guest_window, text="Last Name:").grid(row=4, column=0)
        self.new_last_name_entry = tk.Entry(self.modify_guest_window)
        self.new_last_name_entry.grid(row=4, column=1)

        tk.Label(self.modify_guest_window, text="Email:").grid(row=5, column=0)
        self.new_email_entry = tk.Entry(self.modify_guest_window)
        self.new_email_entry.grid(row=5, column=1)

        tk.Label(self.modify_guest_window, text="Phone:").grid(row=6, column=0)
        self.new_phone_entry = tk.Entry(self.modify_guest_window)
        self.new_phone_entry.grid(row=6, column=1)

        tk.Label(self.modify_guest_window, text="Birth of Date:").grid(row=7, column=0)
        self.new_birth_of_date_entry = tk.Entry(self.modify_guest_window)
        self.new_birth_of_date_entry.grid(row=7, column=1)

        tk.Label(self.modify_guest_window, text="Age:").grid(row=8, column=0)
        self.new_age_entry = tk.Entry(self.modify_guest_window)
        self.new_age_entry.grid(row=8, column=1)

        tk.Label(self.modify_guest_window, text="Gender:").grid(row=9, column=0)
        self.new_gender_entry = tk.Entry(self.modify_guest_window)
        self.new_gender_entry.grid(row=9, column=1)

        tk.Label(self.modify_guest_window, text="Nationality:").grid(row=10, column=0)
        self.new_nationality_entry = tk.Entry(self.modify_guest_window)
        self.new_nationality_entry.grid(row=10, column=1)

        # Button to confirm modifying the guest
        confirm_button = tk.Button(self.modify_guest_window, text="Modify", command=self.confirm_modify_guest)
        confirm_button.grid(row=11, column=0, columnspan=2)
    def confirm_modify_guest(self):
        # Retrieve the guest ID from the entry widget
        guest_id = self.modify_guest_id_entry.get()

        try:
            # Load existing guests from the pickle file
            with open('guests_data.pickle', 'rb') as file:
                guests = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "No guests found!")
            return

        # Check if the guest ID exists
        if guest_id not in guests:
            messagebox.showerror("Error", f"No guest found with ID {guest_id}")
            return

        # Retrieve the modified details from the user input
        new_guest_id = self.new_guest_id_entry.get()  # New guest ID
        new_first_name = self.new_first_name_entry.get()
        new_last_name = self.new_last_name_entry.get()
        new_email = self.new_email_entry.get()
        new_phone = self.new_phone_entry.get()
        new_birth_of_date = self.new_birth_of_date_entry.get()
        new_age = self.new_age_entry.get()
        new_gender = self.new_gender_entry.get()
        new_nationality = self.new_nationality_entry.get()
        if not (
                new_first_name and new_last_name and new_email
                and new_phone and new_birth_of_date and new_age
                and new_gender and new_nationality
        ):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

            # Check data types
        try:
            # Check if age can be converted to integer
            new_age = int(new_age)
            # Add more checks for other fields if needed
        except ValueError:
            messagebox.showerror("Error", "Age must be a number.")
            return
        # Modify the guest object with the new details
        if new_guest_id:
            guests[guest_id]['Guest ID'] = new_guest_id
        if new_first_name:
            guests[guest_id]['First name'] = new_first_name
        if new_last_name:
            guests[guest_id]['Last name'] = new_last_name
        if new_email:
            guests[guest_id]['Email'] = new_email
        if new_phone:
            guests[guest_id]['Phone'] = new_phone
        if new_birth_of_date:
            guests[guest_id]['Birth Date'] = new_birth_of_date
        if new_age:
            guests[guest_id]['Age'] = new_age
        if new_gender:
            guests[guest_id]['Gender'] = new_gender
        if new_nationality:
            guests[guest_id]['Nationality'] = new_nationality

        # Save the updated guest data
        with open('guests_data.pickle', 'wb') as file:
            pickle.dump(guests, file)

        messagebox.showinfo("Success", "Guest details modified successfully!")
        self.modify_guest_window.destroy()
    def display_guest(self):
        # Create a new window for displaying guest details
        self.display_guest_window = tk.Toplevel(self.Guest_window)
        self.display_guest_window.title("Guest Details")

        # Label and Entry widget for entering the guest ID
        tk.Label(self.display_guest_window, text="Guest ID:").grid(row=0, column=0)
        self.guest_id_entry_display = tk.Entry(self.display_guest_window)
        self.guest_id_entry_display.grid(row=0, column=1)

        # Button to confirm displaying the guest details
        confirm_button = tk.Button(self.display_guest_window, text="Display Details",
                                   command=self.confirm_display_guest_details)
        confirm_button.grid(row=1, column=0, columnspan=2)
    def confirm_display_guest_details(self):
        # Get the guest ID entered by the user
        guest_id = self.guest_id_entry_display.get()

        try:
            # Load existing guests from the pickle file
            with open('guests_data.pickle', 'rb') as file:
                guests_data = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "No guests found!")
            return

        # Check if the entered guest ID exists in the dictionary
        if guest_id in guests_data:
            # Get the guest data with the specified ID
            guest_info = guests_data[guest_id]
            # Create a new window to display the guest details
            display_details_window = tk.Toplevel(self.display_guest_window)
            display_details_window.title("Guest Details")
            row_index = 0
            for key, value in guest_info.items():
                detail_label = tk.Label(display_details_window, text=f"{key}: {value}")
                detail_label.grid(row=row_index, column=0, sticky="w")
                row_index += 1

        else:
            messagebox.showerror("Error", f"No guest found with ID {guest_id}")


    def supplier_actions(self):
        self.supplier_window = tk.Toplevel(self.main_window)
        self.supplier_window.title("Supplier Actions")

        add_button = tk.Button(self.supplier_window, text="Add Supplier", command=self.add_supplier)
        add_button.pack()
        delete_button = tk.Button(self.supplier_window, text="Delete Supplier", command=self.delete_supplier)
        delete_button.pack()
        modify_button = tk.Button(self.supplier_window, text="Modify Supplier", command=self.modify_supplier)
        modify_button.pack()
        display_button = tk.Button(self.supplier_window, text="Display Supplier", command=self.display_supplier)
        display_button.pack()

    def add_supplier(self):
        # Create a new window for adding a supplier
        self.add_supplier_window = tk.Toplevel(self.main_window)
        self.add_supplier_window.title("Add Supplier")

        # Labels and Entries widget for adding
        tk.Label(self.add_supplier_window, text="Supplier ID:").grid(row=0, column=0)
        self.supplier_id_entry = tk.Entry(self.add_supplier_window)
        self.supplier_id_entry.grid(row=0, column=1)

        tk.Label(self.add_supplier_window, text="Company Name:").grid(row=1, column=0)
        self.company_name_entry = tk.Entry(self.add_supplier_window)
        self.company_name_entry.grid(row=1, column=1)

        # Label and Entry widget for phone
        self.phone_entry = tk.Entry(self.add_supplier_window)
        self.phone_entry.grid(row=2, column=1)

        tk.Label(self.add_supplier_window, text="Email:").grid(row=3, column=0)
        self.email_entry = tk.Entry(self.add_supplier_window)
        self.email_entry.grid(row=3, column=1)

        tk.Label(self.add_supplier_window, text="Services Provided:").grid(row=4, column=0)
        self.services_provided_entry = tk.Entry(self.add_supplier_window)
        self.services_provided_entry.grid(row=4, column=1)

        tk.Label(self.add_supplier_window, text="Minimum Guests:").grid(row=5, column=0)
        self.min_guests_entry = tk.Entry(self.add_supplier_window)
        self.min_guests_entry.grid(row=5, column=1)

        tk.Label(self.add_supplier_window, text="Maximum Guests:").grid(row=6, column=0)
        self.max_guests_entry = tk.Entry(self.add_supplier_window)
        self.max_guests_entry.grid(row=6, column=1)

        tk.Label(self.add_supplier_window, text="Menu:").grid(row=7, column=0)
        self.menu_entry = tk.Entry(self.add_supplier_window)
        self.menu_entry.grid(row=7, column=1)

        # Button to confirm adding the supplier
        confirm_button = tk.Button(self.add_supplier_window, text="Add Supplier", command=self.confirm_add_supplier)
        confirm_button.grid(row=8, column=0, columnspan=2)
    def confirm_add_supplier(self):
        # Retrieve supplier details from entry widgets
        supplier_id = self.supplier_id_entry.get()
        company_name = self.company_name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        services_provided = self.services_provided_entry.get()
        min_guests = self.min_guests_entry.get()
        max_guests = self.max_guests_entry.get()
        menu = self.menu_entry.get()
        if not (
                supplier_id and company_name and phone and email and services_provided and min_guests and max_guests and menu):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

            # Check if min_guests and max_guests can be converted to integers
        try:
            min_guests = int(min_guests)
            max_guests = int(max_guests)
        except ValueError:
            messagebox.showerror("Error", "Minimum and maximum guests must be numbers.")
            return
        # Create an instance of the Supplier class
        new_supplier = Supplier(supplier_id, company_name, phone, email, services_provided, min_guests, max_guests,
                                menu)

        # Check if the Supplier ID already exists in the pickle file
        try:
            with open('suppliers_data.pickle', 'rb') as file:
                suppliers = pickle.load(file)
        except FileNotFoundError:
            suppliers = {}

        if supplier_id in suppliers:
            messagebox.showerror("Error", f"Supplier ID {supplier_id} already exists!")
            return

        # Add the new supplier to the dictionary
        suppliers[supplier_id] = new_supplier.get_supplier_info()

        # Save the updated supplier data
        with open('suppliers_data.pickle', 'wb') as file:
            pickle.dump(suppliers, file)

        messagebox.showinfo("Success", "Supplier added successfully!")
        self.add_supplier_window.destroy()
    def delete_supplier(self):
        # Create a new window for deleting a supplier
        self.delete_supplier_window = tk.Toplevel(self.main_window)
        self.delete_supplier_window.title("Delete Supplier")

        # Label and Entry widget for supplier ID
        tk.Label(self.delete_supplier_window, text="Supplier ID:").grid(row=0, column=0)
        self.delete_supplier_id_entry = tk.Entry(self.delete_supplier_window)
        self.delete_supplier_id_entry.grid(row=0, column=1)

        # Button to confirm deleting the supplier
        confirm_button = tk.Button(self.delete_supplier_window, text="Delete", command=self.confirm_delete_supplier)
        confirm_button.grid(row=1, column=0, columnspan=2)
    def confirm_delete_supplier(self):
        # Retrieve supplier ID from the Entry widget
        supplier_id = self.delete_supplier_id_entry.get()

        try:
            # Load the dictionary of suppliers from the pickle file
            with open('suppliers_data.pickle', 'rb') as file:
                suppliers = pickle.load(file)
        except FileNotFoundError:
            # If the file is not found, create an empty dictionary
            suppliers = {}

        # Check if the supplier ID exists in the dictionary
        if supplier_id in suppliers:
            # Remove the supplier with the given ID from the dictionary
            suppliers.pop(supplier_id)
            # Save the updated dictionary back to the pickle file
            with open('suppliers_data.pickle', 'wb') as file:
                pickle.dump(suppliers, file)
            # Show success message
            messagebox.showinfo("Success", f"Supplier with ID {supplier_id} deleted successfully!")
        else:
            # If the supplier ID is not found, show error message
            messagebox.showerror("Error", f"No supplier found with ID {supplier_id}")

        # Destroy the delete supplier window
        self.delete_supplier_window.destroy()
    def modify_supplier(self):
        # Create a new window for modifying a supplier
        self.modify_supplier_window = tk.Toplevel(self.main_window)
        self.modify_supplier_window.title("Modify Supplier")

        # Labels and Entries widget for modifying
        tk.Label(self.modify_supplier_window, text="Supplier ID:").grid(row=0, column=0)
        self.modify_supplier_id_entry = tk.Entry(self.modify_supplier_window)
        self.modify_supplier_id_entry.grid(row=0, column=1)

        tk.Label(self.modify_supplier_window, text="Modify details").grid(row=1, column=0)

        tk.Label(self.modify_supplier_window, text="Supplier ID").grid(row=2, column=0)
        self.new_supplier_id_entry = tk.Entry(self.modify_supplier_window)
        self.new_supplier_id_entry.grid(row=2, column=1)

        tk.Label(self.modify_supplier_window, text="Company Name:").grid(row=3, column=0)
        self.new_company_name_entry = tk.Entry(self.modify_supplier_window)
        self.new_company_name_entry.grid(row=3, column=1)

        tk.Label(self.modify_supplier_window, text="Phone:").grid(row=4, column=0)
        self.new_phone_entry = tk.Entry(self.modify_supplier_window)
        self.new_phone_entry.grid(row=4, column=1)

        tk.Label(self.modify_supplier_window, text="Email:").grid(row=5, column=0)
        self.new_email_entry = tk.Entry(self.modify_supplier_window)
        self.new_email_entry.grid(row=5, column=1)

        tk.Label(self.modify_supplier_window, text="Services Provided:").grid(row=6, column=0)
        self.new_services_provided_entry = tk.Entry(self.modify_supplier_window)
        self.new_services_provided_entry.grid(row=6, column=1)

        tk.Label(self.modify_supplier_window, text="Minimum Guests:").grid(row=7, column=0)
        self.new_min_guests_entry = tk.Entry(self.modify_supplier_window)
        self.new_min_guests_entry.grid(row=7, column=1)

        tk.Label(self.modify_supplier_window, text="Maximum Guests:").grid(row=8, column=0)
        self.new_max_guests_entry = tk.Entry(self.modify_supplier_window)
        self.new_max_guests_entry.grid(row=8, column=1)

        tk.Label(self.modify_supplier_window, text="Menu:").grid(row=9, column=0)
        self.new_menu_entry = tk.Entry(self.modify_supplier_window)
        self.new_menu_entry.grid(row=9, column=1)

        # Button to confirm modifying the supplier
        confirm_button = tk.Button(self.modify_supplier_window, text="Modify", command=self.confirm_modify_supplier)
        confirm_button.grid(row=10, column=0, columnspan=2)
    def confirm_modify_supplier(self):
        # Retrieve the supplier ID from the entry widget
        supplier_id = self.modify_supplier_id_entry.get()

        try:
            # Load existing suppliers from the pickle file
            with open('suppliers_data.pickle', 'rb') as file:
                suppliers_data = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "No suppliers found!")
            return

        # Check if the supplier ID exists
        if supplier_id not in suppliers_data:
            messagebox.showerror("Error", f"No supplier found with ID {supplier_id}")
            return

        # Retrieve the modified details from the user input
        new_supplier_id = self.new_supplier_id_entry.get()  # New supplier ID
        new_company_name = self.new_company_name_entry.get()
        new_phone = self.new_phone_entry.get()
        new_email = self.new_email_entry.get()
        new_services_provided = self.new_services_provided_entry.get()
        new_min_guests = self.new_min_guests_entry.get()
        new_max_guests = self.new_max_guests_entry.get()
        new_menu = self.new_menu_entry.get()
        try:
            if new_min_guests:
                new_min_guests = int(new_min_guests)
            if new_max_guests:
                new_max_guests = int(new_max_guests)
        except ValueError:
            messagebox.showerror("Error", "Minimum and maximum guests must be numbers.")
            return
        # Modify the supplier object with the new details
        if new_supplier_id:
            suppliers_data[supplier_id]['Supplier ID'] = new_supplier_id
        if new_company_name:
            suppliers_data[supplier_id]['Company Name'] = new_company_name
        if new_phone:
            suppliers_data[supplier_id]['Phone'] = new_phone
        if new_email:
            suppliers_data[supplier_id]['Email'] = new_email
        if new_services_provided:
            suppliers_data[supplier_id]['Services Provided'] = new_services_provided
        if new_min_guests:
            suppliers_data[supplier_id]['Min Guests'] = new_min_guests
        if new_max_guests:
            suppliers_data[supplier_id]['Max Guests'] = new_max_guests
        if new_menu:
            suppliers_data[supplier_id]['Menu'] = new_menu

        # Save the updated supplier data
        with open('suppliers_data.pickle', 'wb') as file:
            pickle.dump(suppliers_data, file)

        messagebox.showinfo("Success", "Supplier details modified successfully!")
        self.modify_supplier_window.destroy()
    def display_supplier(self):
        # Create a new window for displaying supplier details
        self.display_supplier_window = tk.Toplevel(self.supplier_window)
        self.display_supplier_window.title("Supplier Details")

        # Label and Entry widget for entering the supplier ID
        tk.Label(self.display_supplier_window, text="Supplier ID:").grid(row=0, column=0)
        self.supplier_id_entry_display = tk.Entry(self.display_supplier_window)
        self.supplier_id_entry_display.grid(row=0, column=1)

        # Button to confirm displaying the supplier details
        confirm_button = tk.Button(self.display_supplier_window, text="Display Details",
                                   command=self.confirm_display_supplier_details)
        confirm_button.grid(row=1, column=0, columnspan=2)
    def confirm_display_supplier_details(self):
        # Get the supplier ID entered by the user
        supplier_id = self.supplier_id_entry_display.get()

        try:
            # Load existing suppliers from the pickle file
            with open('suppliers_data.pickle', 'rb') as file:
                suppliers_data = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "No suppliers found!")
            return

        # Check if the entered supplier ID exists in the dictionary
        if supplier_id in suppliers_data:
            # Get the supplier data with the specified ID
            supplier_info = suppliers_data[supplier_id]
            # Create a new window to display the supplier details
            display_details_window = tk.Toplevel(self.display_supplier_window)
            display_details_window.title("Supplier Details")
            row_index = 0
            for key, value in supplier_info.items():
                detail_label = tk.Label(display_details_window, text=f"{key}: {value}")
                detail_label.grid(row=row_index, column=0, sticky="w")
                row_index += 1

        else:
            messagebox.showerror("Error", f"No supplier found with ID {supplier_id}")


    def venue_actions(self):
        self.venue_window = tk.Toplevel(self.main_window)
        self.venue_window.title("Venue Actions")

        add_button = tk.Button(self.venue_window, text="Add Venue", command=self.add_venue)
        add_button.pack()
        delete_button = tk.Button(self.venue_window, text="Delete Venue", command=self.delete_venue)
        delete_button.pack()
        modify_button = tk.Button(self.venue_window, text="Modify Venue", command=self.modify_venue)
        modify_button.pack()
        display_button = tk.Button(self.venue_window, text="Display Venue", command=self.display_venue)
        display_button.pack()

    def add_venue(self):
        # Create a new window for adding a venue
        self.add_venue_window = tk.Toplevel(self.main_window)
        self.add_venue_window.title("Add Venue")

        # Labels and Entries widget for adding
        tk.Label(self.add_venue_window, text="Venue ID:").grid(row=0, column=0)
        self.venue_id_entry = tk.Entry(self.add_venue_window)
        self.venue_id_entry.grid(row=0, column=1)

        tk.Label(self.add_venue_window, text="Venue Name:").grid(row=1, column=0)
        self.venue_name_entry = tk.Entry(self.add_venue_window)
        self.venue_name_entry.grid(row=1, column=1)

        tk.Label(self.add_venue_window, text="Location:").grid(row=2, column=0)
        self.venue_location_entry = tk.Entry(self.add_venue_window)
        self.venue_location_entry.grid(row=2, column=1)

        tk.Label(self.add_venue_window, text="Email:").grid(row=3, column=0)
        self.venue_email_entry = tk.Entry(self.add_venue_window)
        self.venue_email_entry.grid(row=3, column=1)

        tk.Label(self.add_venue_window, text="Phone:").grid(row=4, column=0)
        self.venue_phone_entry = tk.Entry(self.add_venue_window)
        self.venue_phone_entry.grid(row=4, column=1)

        tk.Label(self.add_venue_window, text="Minimum Number of Guests:").grid(row=5, column=0)
        self.venue_min_guests_entry = tk.Entry(self.add_venue_window)
        self.venue_min_guests_entry.grid(row=5, column=1)

        tk.Label(self.add_venue_window, text="Maximum Number of Guests:").grid(row=6, column=0)
        self.venue_max_guests_entry = tk.Entry(self.add_venue_window)
        self.venue_max_guests_entry.grid(row=6, column=1)

        # Button to confirm adding the venue
        confirm_button = tk.Button(self.add_venue_window, text="Add Venue", command=self.confirm_add_venue)
        confirm_button.grid(row=7, column=0, columnspan=2)
    def confirm_add_venue(self):
        # Retrieve the venue details from the entry widgets
        venue_id = self.venue_id_entry.get()
        venue_name = self.venue_name_entry.get()
        venue_location = self.venue_location_entry.get()
        venue_email = self.venue_email_entry.get()
        venue_phone = self.venue_phone_entry.get()
        min_guests = self.venue_min_guests_entry.get()
        max_guests = self.venue_max_guests_entry.get()

        # Check if any of the fields are empty
        if not (
                venue_id and venue_name and venue_location and venue_email and venue_phone and min_guests and max_guests):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Convert min_guests and max_guests to integers
        try:
            min_guests = int(min_guests)
            max_guests = int(max_guests)
        except ValueError:
            messagebox.showerror("Error", "Minimum and Maximum Guests must be integers.")
            return

        # Check if max_guests is greater than or equal to min_guests
        if max_guests < min_guests:
            messagebox.showerror("Error", "Maximum Guests must be greater than or equal to Minimum Guests.")
            return

        # Create a dictionary with the venue details
        new_venue = {
            'Venue ID': venue_id,
            'Venue Name': venue_name,
            'Location': venue_location,
            'Email': venue_email,
            'Phone': venue_phone,
            'Minimum Number of Guests': min_guests,
            'Maximum Number of Guests': max_guests
        }

        # Save the new venue data
        try:
            # Load existing venues from the pickle file
            with open('venues_data.pickle', 'rb') as file:
                venues = pickle.load(file)
        except FileNotFoundError:
            venues = {}

        # Check if the venue ID already exists
        if venue_id in venues:
            messagebox.showerror("Error", f"Venue with ID {venue_id} already exists.")
            return

        # Add the new venue to the dictionary
        venues[venue_id] = new_venue

        # Save the updated venue data
        with open('venues_data.pickle', 'wb') as file:
            pickle.dump(venues, file)

        # Show success message
        messagebox.showinfo("Success", "Venue added successfully!")

        # Close the add venue window
        self.add_venue_window.destroy()
    def delete_venue(self):
        # Create a new window for deleting a venue
        self.delete_venue_window = tk.Toplevel(self.main_window)
        self.delete_venue_window.title("Delete Venue")

        # Label and Entry widget for venue ID
        tk.Label(self.delete_venue_window, text="Venue ID:").grid(row=0, column=0)
        self.delete_venue_id_entry = tk.Entry(self.delete_venue_window)
        self.delete_venue_id_entry.grid(row=0, column=1)

        # Button to confirm deleting the venue
        confirm_button = tk.Button(self.delete_venue_window, text="Delete", command=self.confirm_delete_venue)
        confirm_button.grid(row=1, column=0, columnspan=2)
    def confirm_delete_venue(self):
        # Retrieve venue ID from the Entry widget
        venue_id = self.delete_venue_id_entry.get()

        try:
            # Load the dictionary of venues from the pickle file
            with open('venues_data.pickle', 'rb') as file:
                venues = pickle.load(file)
        except FileNotFoundError:
            # If the file is not found, create an empty dictionary
            venues = {}

        # Check if the venue ID exists in the dictionary
        if venue_id in venues:
            # Remove the venue with the given ID from the dictionary
            venues.pop(venue_id)
            # Save the updated dictionary back to the pickle file
            with open('venues_data.pickle', 'wb') as file:
                pickle.dump(venues, file)
            # Show success message
            messagebox.showinfo("Success", f"Venue with ID {venue_id} deleted successfully!")
        else:
            # If the venue ID is not found, show error message
            messagebox.showerror("Error", f"No venue found with ID {venue_id}")

        # Destroy the delete venue window
        self.delete_venue_window.destroy()
    def modify_venue(self):
        # Create a new window for modifying a venue
        self.modify_venue_window = tk.Toplevel(self.main_window)
        self.modify_venue_window.title("Modify Venue")

        # Labels and Entries widget for modifying
        tk.Label(self.modify_venue_window, text="Venue ID:").grid(row=0, column=0)
        self.modify_venue_id_entry = tk.Entry(self.modify_venue_window)
        self.modify_venue_id_entry.grid(row=0, column=1)

        tk.Label(self.modify_venue_window, text="New Venue Name:").grid(row=1, column=0)
        self.new_venue_name_entry = tk.Entry(self.modify_venue_window)
        self.new_venue_name_entry.grid(row=1, column=1)

        tk.Label(self.modify_venue_window, text="New Location:").grid(row=2, column=0)
        self.new_location_entry = tk.Entry(self.modify_venue_window)
        self.new_location_entry.grid(row=2, column=1)

        tk.Label(self.modify_venue_window, text="New Email:").grid(row=3, column=0)
        self.new_email_entry = tk.Entry(self.modify_venue_window)
        self.new_email_entry.grid(row=3, column=1)

        tk.Label(self.modify_venue_window, text="New Phone:").grid(row=4, column=0)
        self.new_phone_entry = tk.Entry(self.modify_venue_window)
        self.new_phone_entry.grid(row=4, column=1)

        tk.Label(self.modify_venue_window, text="New Minimum Number of Guests:").grid(row=5, column=0)
        self.new_min_guests_entry = tk.Entry(self.modify_venue_window)
        self.new_min_guests_entry.grid(row=5, column=1)

        tk.Label(self.modify_venue_window, text="New Maximum Number of Guests:").grid(row=6, column=0)
        self.new_max_guests_entry = tk.Entry(self.modify_venue_window)
        self.new_max_guests_entry.grid(row=6, column=1)

        # Button to confirm modifying the venue
        confirm_button = tk.Button(self.modify_venue_window, text="Modify", command=self.confirm_modify_venue)
        confirm_button.grid(row=7, column=0, columnspan=2)
    def confirm_modify_venue(self):
        # Retrieve the venue ID from the entry widget
        venue_id = self.modify_venue_id_entry.get()

        try:
            # Load existing venues from the pickle file
            with open('venues_data.pickle', 'rb') as file:
                venues = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "No venues found!")
            return

        # Check if the venue ID exists
        if venue_id not in venues:
            messagebox.showerror("Error", f"No venue found with ID {venue_id}")
            return

        # Retrieve the modified details from the user input
        new_venue_name = self.new_venue_name_entry.get()
        new_location = self.new_location_entry.get()
        new_email = self.new_email_entry.get()
        new_phone = self.new_phone_entry.get()
        new_min_guests = self.new_min_guests_entry.get()
        new_max_guests = self.new_max_guests_entry.get()

        # Modify the venue object with the new details
        venue = venues[venue_id]
        if new_venue_name:
            venue['Venue Name'] = new_venue_name
        if new_location:
            venue['Location'] = new_location
        if new_email:
            venue['Email'] = new_email
        if new_phone:
            venue['Phone'] = new_phone
        if new_min_guests:
            venue['Minimum Number of Guests'] = new_min_guests
        if new_max_guests:
            venue['Maximum Number of Guests'] = new_max_guests

        # Save the updated venue data
        with open('venues_data.pickle', 'wb') as file:
            pickle.dump(venues, file)

        messagebox.showinfo("Success", "Venue details modified successfully!")
        self.modify_venue_window.destroy()
    def display_venue(self):
        # Create a new window for displaying venue details
        self.display_venue_window = tk.Toplevel(self.venue_window)
        self.display_venue_window.title("Display Venue")

        # Label and Entry widget for entering the venue ID
        tk.Label(self.display_venue_window, text="Venue ID:").grid(row=0, column=0)
        self.venue_id_entry_display = tk.Entry(self.display_venue_window)
        self.venue_id_entry_display.grid(row=0, column=1)

        # Button to confirm displaying the venue details
        confirm_button = tk.Button(self.display_venue_window, text="Display Details",
                                   command=self.confirm_display_venue_details)
        confirm_button.grid(row=1, column=0, columnspan=2)
    def confirm_display_venue_details(self):
        # Get the venue ID entered by the user
        venue_id = self.venue_id_entry_display.get()

        try:
            # Load existing venues from the pickle file
            with open('venues_data.pickle', 'rb') as file:
                venues_data = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "No venues found!")
            return

        # Check if the entered venue ID exists in the dictionary
        if venue_id in venues_data:
            # Get the venue data with the specified ID
            venue_info = venues_data[venue_id]
            # Create a new window to display the venue details
            display_details_window = tk.Toplevel(self.display_venue_window)
            display_details_window.title("Venue Details")
            row_index = 0
            for key, value in venue_info.items():
                detail_label = tk.Label(display_details_window, text=f"{key}: {value}")
                detail_label.grid(row=row_index, column=0, sticky="w")
                row_index += 1

        else:
            messagebox.showerror("Error", f"No venue found with ID {venue_id}")


    def event_actions(self):
        self.event_window = tk.Toplevel(self.main_window)
        self.event_window.title("Event Actions")

        add_button = tk.Button(self.event_window, text="Add Event", command=self.add_event)
        add_button.pack()
        delete_button = tk.Button(self.event_window, text="Delete Event", command=self.delete_event)
        delete_button.pack()
        modify_button = tk.Button(self.event_window, text="Modify Event", command=self.modify_event)
        modify_button.pack()
        display_button = tk.Button(self.event_window, text="Display Event", command=self.display_event)
        display_button.pack()

    def add_event(self):
        # Create a new window for adding an event
        self.add_event_window = tk.Toplevel(self.main_window)
        self.add_event_window.title("Add Event")

        # Labels and Entries widget for adding
        tk.Label(self.add_event_window, text="Event ID:").grid(row=0, column=0)
        self.event_id_entry = tk.Entry(self.add_event_window)
        self.event_id_entry.grid(row=0, column=1)

        tk.Label(self.add_event_window, text="Event Type:").grid(row=1, column=0)
        self.event_type_entry = tk.Entry(self.add_event_window)
        self.event_type_entry.grid(row=1, column=1)

        tk.Label(self.add_event_window, text="Theme:").grid(row=2, column=0)
        self.theme_entry = tk.Entry(self.add_event_window)
        self.theme_entry.grid(row=2, column=1)

        tk.Label(self.add_event_window, text="Date:").grid(row=3, column=0)
        self.date_entry = tk.Entry(self.add_event_window)
        self.date_entry.grid(row=3, column=1)

        tk.Label(self.add_event_window, text="Time:").grid(row=4, column=0)
        self.time_entry = tk.Entry(self.add_event_window)
        self.time_entry.grid(row=4, column=1)

        tk.Label(self.add_event_window, text="Duration:").grid(row=5, column=0)
        self.duration_entry = tk.Entry(self.add_event_window)
        self.duration_entry.grid(row=5, column=1)

        tk.Label(self.add_event_window, text="Venue ID:").grid(row=6, column=0)
        self.venue_id_entry = tk.Entry(self.add_event_window)
        self.venue_id_entry.grid(row=6, column=1)

        tk.Label(self.add_event_window, text="Client ID:").grid(row=7, column=0)
        self.client_id_entry = tk.Entry(self.add_event_window)
        self.client_id_entry.grid(row=7, column=1)

        tk.Label(self.add_event_window, text="Guest List:").grid(row=8, column=0)
        self.guest_list_entry = tk.Entry(self.add_event_window)
        self.guest_list_entry.grid(row=8, column=1)

        tk.Label(self.add_event_window, text="Suppliers:").grid(row=9, column=0)
        self.suppliers_entry = tk.Entry(self.add_event_window)
        self.suppliers_entry.grid(row=9, column=1)

        tk.Label(self.add_event_window, text="Invoice:").grid(row=10, column=0)
        self.invoice_entry = tk.Entry(self.add_event_window)
        self.invoice_entry.grid(row=10, column=1)

        # Button to confirm adding the event
        confirm_button = tk.Button(self.add_event_window, text="Add Event", command=self.confirm_add_event)
        confirm_button.grid(row=11, column=0, columnspan=2)
    def confirm_add_event(self):
        # Retrieve values from the Entry widgets
        event_id = self.event_id_entry.get()
        event_type_str = self.event_type_entry.get()
        theme = self.theme_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        duration = self.duration_entry.get()
        venue_id = self.venue_id_entry.get()
        client_id = self.client_id_entry.get()
        guest_list = self.guest_list_entry.get()
        suppliers = self.suppliers_entry.get()
        invoice = self.invoice_entry.get()

        # Convert event type string to an integer
        try:
            event_type = int(event_type_str)
        except ValueError:
            messagebox.showerror("Error", "Event Type must be an integer.")
            return

        # Create an instance of the Event class
        new_event = Event(event_id, event_type, theme, date, time, duration, venue_id, client_id)

        # Check if the event ID already exists in the pickle file
        try:
            with open('events_data.pickle', 'rb') as file:
                events = pickle.load(file)
        except FileNotFoundError:
            events = {}
        # Check if the event ID already exists
        if event_id in events:
            messagebox.showerror("Error", f"Event ID {event_id} already exists!")
            return

        # Add the new event to the dictionary
        events[event_id] = {
            'Event ID': new_event.get_event_info()['Event ID'],
            'Event Type': new_event.get_event_info()['Event Type'],
            'Theme': new_event.get_event_info()['Theme'],
            'Date': new_event.get_event_info()['Date'],
            'Time': new_event.get_event_info()['Time'],
            'Duration': new_event.get_event_info()['Duration'],
            'Venue ID': new_event.get_event_info()['Venue ID'],
            'Client ID': new_event.get_event_info()['Client ID'],
            'Guest List': guest_list,
            'Suppliers': suppliers,
            'Invoice': invoice
        }

        # Save the updated event data
        with open('events_data.pickle', 'wb') as file:
            pickle.dump(events, file)

        messagebox.showinfo("Success", "Event added successfully!")
        self.add_event_window.destroy()
    def delete_event(self):
        # Create a new window for deleting an event
        self.delete_event_window = tk.Toplevel(self.main_window)
        self.delete_event_window.title("Delete Event")

        # Label and Entry widget for event ID
        tk.Label(self.delete_event_window, text="Event ID:").grid(row=0, column=0)
        self.delete_event_id_entry = tk.Entry(self.delete_event_window)
        self.delete_event_id_entry.grid(row=0, column=1)

        # Button to confirm deleting the event
        confirm_button = tk.Button(self.delete_event_window, text="Delete", command=self.confirm_delete_event)
        confirm_button.grid(row=1, column=0, columnspan=2)
    def confirm_delete_event(self):
        # Retrieve event ID from the Entry widget
        event_id = self.delete_event_id_entry.get()

        try:
            # Load the list of events from the pickle file
            with open('events_data.pickle', 'rb') as file:
                events = pickle.load(file)
        except FileNotFoundError:
            # If the file is not found, create an empty list
            events = {}

        # Check if the event ID exists in the list
        if event_id in events:
            # Remove the event with the specified ID
            del events[event_id]
            # Save the updated list back to the pickle file
            with open('events_data.pickle', 'wb') as file:
                pickle.dump(events, file)
            # Show success message
            messagebox.showinfo("Success", f"Event with ID {event_id} deleted successfully!")
        else:
            # If the event ID is not found, show error message
            messagebox.showerror("Error", f"No event found with ID {event_id}")

        # Destroy the delete event window
        self.delete_event_window.destroy()
    def modify_event(self):
        # Create a new window for modifying an event
        self.modify_event_window = tk.Toplevel(self.main_window)
        self.modify_event_window.title("Modify Event")

        # Labels and Entries widget for modifying
        tk.Label(self.modify_event_window, text="Event ID:").grid(row=0, column=0)
        self.modify_event_id_entry = tk.Entry(self.modify_event_window)
        self.modify_event_id_entry.grid(row=0, column=1)

        tk.Label(self.modify_event_window, text="Modify details").grid(row=1, column=0)

        tk.Label(self.modify_event_window, text="Event Type:").grid(row=2, column=0)
        self.new_event_type_entry = tk.Entry(self.modify_event_window)
        self.new_event_type_entry.grid(row=2, column=1)

        tk.Label(self.modify_event_window, text="Theme:").grid(row=3, column=0)
        self.new_theme_entry = tk.Entry(self.modify_event_window)
        self.new_theme_entry.grid(row=3, column=1)

        tk.Label(self.modify_event_window, text="Date:").grid(row=4, column=0)
        self.new_date_entry = tk.Entry(self.modify_event_window)
        self.new_date_entry.grid(row=4, column=1)

        tk.Label(self.modify_event_window, text="Time:").grid(row=5, column=0)
        self.new_time_entry = tk.Entry(self.modify_event_window)
        self.new_time_entry.grid(row=5, column=1)

        tk.Label(self.modify_event_window, text="Duration:").grid(row=6, column=0)
        self.new_duration_entry = tk.Entry(self.modify_event_window)
        self.new_duration_entry.grid(row=6, column=1)

        tk.Label(self.modify_event_window, text="Venue ID:").grid(row=7, column=0)
        self.new_venue_id_entry = tk.Entry(self.modify_event_window)
        self.new_venue_id_entry.grid(row=7, column=1)

        tk.Label(self.modify_event_window, text="Client ID:").grid(row=8, column=0)
        self.new_client_id_entry = tk.Entry(self.modify_event_window)
        self.new_client_id_entry.grid(row=8, column=1)

        # Button to confirm modifying the event
        confirm_button = tk.Button(self.modify_event_window, text="Modify", command=self.confirm_modify_event)
        confirm_button.grid(row=9, column=0, columnspan=2)
    def confirm_modify_event(self):
        # Retrieve the event ID from the entry widget
        event_id = self.modify_event_id_entry.get()

        if not event_id:
            messagebox.showerror("Error", "Please enter an Event ID.")
            return

        try:
            # Load existing events from the pickle file
            with open('events_data.pickle', 'rb') as file:
                events = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "No events found!")
            return

        # Check if the event ID exists
        if event_id not in events:
            messagebox.showerror("Error", f"No event found with ID {event_id}")
            return

        # Retrieve the modified details from the user input
        new_event_type = Event.get_event_type_word(self.new_event_type_entry.get())
        new_theme = self.new_theme_entry.get()
        new_date = self.new_date_entry.get()
        new_time = self.new_time_entry.get()
        new_duration = self.new_duration_entry.get()
        new_venue_id = self.new_venue_id_entry.get()
        new_client_id = self.new_client_id_entry.get()

        # Modify the event object with the new details
        event = events[event_id]
        if new_event_type:
            event["Event Type"] = new_event_type
        if new_theme:
            event["Theme"] = new_theme
        if new_date:
            event["Date"] = new_date
        if new_time:
            event["Time"] = new_time
        if new_duration:
            event["Duration"] = new_duration
        if new_venue_id:
            event["Venue ID"] = new_venue_id
        if new_client_id:
            event["Client ID"] = new_client_id

        # Save the updated event data
        with open('events_data.pickle', 'wb') as file:
            pickle.dump(events, file)

        messagebox.showinfo("Success", "Event details modified successfully!")
        self.modify_event_window.destroy()
    def display_event(self):
        # Create a new window for displaying event details
        self.display_event_window = tk.Toplevel(self.main_window)
        self.display_event_window.title("Display Event")

        # Label and Entry widget for entering the event ID
        tk.Label(self.display_event_window, text="Event ID:").grid(row=0, column=0)
        self.event_id_entry_display = tk.Entry(self.display_event_window)
        self.event_id_entry_display.grid(row=0, column=1)

        # Button to confirm displaying the event details
        confirm_button = tk.Button(self.display_event_window, text="Display Details",
                                   command=self.confirm_display_event_details)
        confirm_button.grid(row=1, column=0, columnspan=2)
    def confirm_display_event_details(self):
        # Get the event ID entered by the user
        event_id = self.event_id_entry_display.get()

        try:
            # Load existing events from the pickle file
            with open('events_data.pickle', 'rb') as file:
                events_data = pickle.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "No events found!")
            return

        # Check if the entered event ID exists in the dictionary
        if event_id in events_data:
            # Get the event data with the specified ID
            event_info = events_data[event_id]
            # Create a new window to display the event details
            display_details_window = tk.Toplevel(self.display_event_window)
            display_details_window.title("Event Details")
            row_index = 0
            for key, value in event_info.items():
                detail_label = tk.Label(display_details_window, text=f"{key}: {value}")
                detail_label.grid(row=row_index, column=0, sticky="w")
                row_index += 1

        else:
            messagebox.showerror("Error", f"No event found with ID {event_id}")


def main():
    app = MyGUI()
    app.main_window.mainloop()

if __name__ == "__main__":
    main()



from Person import Person

class Employee(Person):
    """Class to represent an employee"""

    def __init__(self, person_id, first_name, last_name, email, phone, birth_of_date, age, gender, nationality,
                 department, job_title, salary, manager_id, employee_id):
        Person.__init__(self, person_id, first_name, last_name, email, phone, birth_of_date, age, gender, nationality)
        self._department = department
        self._job_title = job_title
        self._salary = salary
        self._manager_id = manager_id
        self._employee_id = employee_id

    # Setters and getters
    def set_department(self, department):
        self._department = department
    def get_department(self):
        return self._department

    def set_job_title(self, job_title):
        self._job_title = job_title
    def get_job_title(self):
        return self._job_title

    def set_salary(self, salary):
        self._salary = salary
    def get_salary(self):
        return self._salary

    def set_manager_id(self, manager_id):
        self._manager_id = manager_id
    def get_manager_id(self):
        return self._manager_id

    def set_employee_id(self, employee_id):
        self._employee_id = employee_id
    def get_employee_id(self):
        return self._employee_id

    def get_employee_info(self):
        employee_info = {
            'Person ID': self.get_id(),
            'Name': self.get_name(),
            'Email': self.get_email(),
            'Phone': self.get_phone(),
            'Birth Date': self.get_birth_of_date(),
            'Age': self.get_age(),
            'Gender': self.get_gender(),
            'Nationality': self.get_nationality(),
            'Department': self._department,
            'Job Title': self._job_title,
            'Salary': self._salary,
            'Manager ID': self._manager_id,
            'Employee ID': self._employee_id
        }
        return employee_info

    def __str__(self):
        return "Department: " + self._department + ", Job Title: " + self._job_title + ", Salary: " + str(
            self._salary) + ", Manager ID: " + str(self._manager_id) + ", Employee ID: " + str(
            self._employee_id) + ", Passport Details: " + str(self.get_passport_info())

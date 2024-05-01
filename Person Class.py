class Person:
    """Class to represent a person"""

    def __init__(self, person_id, first_name, last_name, email, phone, birth_of_date, age):
        self._person_id = person_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._phone = phone
        self._birth_of_date = birth_of_date
        self._age = age

    def set_id(self, person_id):
        self._person_id = person_id
    def get_id(self):
        return self._person_id

    def set_name(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
    def get_name(self):
        return self._first_name + " " + self._last_name

    def set_email(self, email):
        self._email = email
    def get_email(self):
        return self._email

    def set_phone(self, phone):
        self._phone = phone
    def get_phone(self):
        return self._phone

    def set_age(self, age):
        self._age = age
    def get_age(self):
        return self._age

    def set_birth_of_date(self, birth_of_date):
        self._birth_of_date = birth_of_date
    def get_birth_of_date(self):
        return self._birth_of_date

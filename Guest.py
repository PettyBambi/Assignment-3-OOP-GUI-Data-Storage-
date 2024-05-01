from Person import Person

class Guest(Person):
    """Class to represent a guest"""

    def __init__(self, guest_id,person_id, first_name, last_name, email, phone, birth_of_date, age, gender, nationality):
        Person.__init__(self, person_id, first_name, last_name, email, phone, birth_of_date, age, gender, nationality)
        self._guest_id = guest_id

    # Setter and getter
    def set_guest_id(self, guest_id):
        self._guest_id = guest_id
    def get_guest_id(self):
        return self._guest_id

    def get_guest_info(self):
        guest_info = {
            'Guest ID': self._guest_id,
            'Name': self.get_name(),
            'Email': self.get_email(),
            'Phone': self.get_phone()
        }
        return guest_info

    def __str__(self):
        return "Guest ID: " + str(self._guest_id) + ", Name: " + self.get_name() + ", Email: " + self.get_email() + ", Phone: " + self.get_phone()

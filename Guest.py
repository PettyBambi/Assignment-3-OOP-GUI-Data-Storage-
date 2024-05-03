from Person import Person

class Guest(Person):
    """Class to represent a guest"""

    # Initializes the variables
    def __init__(self, guest_id,personal_id, first_name, last_name, email, phone, birth_of_date, age, gender, nationality):
        Person.__init__(self, personal_id, first_name, last_name, email, phone, birth_of_date, age, gender, nationality)
        self._guest_id = guest_id

    # Setter and getters
    def set_guest_id(self, guest_id):
        self._guest_id = guest_id
    def get_guest_id(self):
        return self._guest_id

    def get_guest_info(self): # Returns information of gesuts
        guest_info = {
            'Guest ID': self._guest_id,
            'Name': self.get_name(),
            'Email': self.get_email(),
            'Phone': self.get_phone()
        }
        return guest_info

    def __str__(self): # String print
        return "Guest ID: " + str(self._guest_id) + ", Name: " + self.get_name() + ", Email: " + self.get_email() + ", Phone: " + self.get_phone()



guest1 = Guest(1, "123456789", "John", "Doe", "john@example.com", "1234567890", "1990-01-01", 31, "Male", "American")
guest2 = Guest(2, "987654321", "Alice", "Smith", "alice@example.com", "9876543210", "1985-05-15", 36, "Female", "British")
guest3 = Guest(3, "456789123", "Michael", "Johnson", "michael@example.com", "4567891230", "1982-11-20", 39, "Male", "Canadian")
guest4 = Guest(4, "789123456", "Emily", "Davis", "emily@example.com", "7891234560", "1978-08-10", 43, "Female", "Australian")

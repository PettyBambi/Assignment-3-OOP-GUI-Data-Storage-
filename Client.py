from Person import Person


class Client(Person):
    """Class to represent a client"""

    # Constructor
    def __init__(self, client_id, personal_id, first_name, last_name, email, phone, birth_of_date, age, gender, nationality, budget):
        Person.__init__(self, personal_id, first_name, last_name, email, phone, birth_of_date, age, gender, nationality)
        self._client_id = client_id
        self._budget = budget

    # setters and getters
    def set_client_id(self, client_id):
        self._client_id = client_id
    def get_client_id(self):
        return self._client_id

    def set_budget(self, budget):
        self._budget = budget
    def get_budget(self):
        return self._budget

    def get_client_info(self): # Client information as a dictionary
        client_info = {
            'Client ID': self.get_client_id(),
            'Name': self.get_name(),
            'Email': self.get_email(),
            'Phone': self.get_phone(),
            'Budget': str(self.get_budget())
        }
        return client_info

    def __str__(self): # Returns string
        return "Client ID: " + str(
            self.get_client_id()) + ", Name: " + self.get_name() + ", Email: " + self.get_email() + ", Phone: " + str(
            self.get_phone()) + ", Budget: " + str(self.get_budget())

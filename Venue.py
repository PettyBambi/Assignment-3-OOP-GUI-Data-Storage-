class Venue:
    """Class to represent a venue"""

    # Initializes attributes
    def __init__(self, venue_id, venue_name, email, phone, location, min_guests, max_guests):
        self._venue_id = venue_id
        self._venue_name = venue_name
        self._email = email
        self._phone = phone
        self._location = location
        self._min_guests = min_guests
        self._max_guests = max_guests

    # Setters and getters
    def set_venue_id(self, venue_id):
        self._venue_id = venue_id
    def get_venue_id(self):
        return self._venue_id

    def set_venue_name(self, venue_name):
        self._venue_name = venue_name
    def get_venue_name(self):
        return self._venue_name

    def set_email(self, email):
        self._email = email
    def get_email(self):
        return self._email

    def set_phone(self, phone):
        self._phone = phone
    def get_phone(self):
        return self._phone

    def set_location(self, location):
        self._location = location
    def get_location(self):
        return self._location

    def set_min_guests(self, min_guests):
        self._min_guests = min_guests
    def get_min_guests(self):
        return self._min_guests

    def set_max_guests(self, max_guests):
        self._max_guests = max_guests
    def get_max_guests(self):
        return self._max_guests

    def get_venue_info(self): # Retrieves information
        venue_info = {
            'Venue ID': self._venue_id,
            'Venue Name': self._venue_name,
            'Email': self._email,
            'Phone': self._phone,
            'Location': self._location,
            'Minimum Number of Guests': self._min_guests,
            'Maximum Number of Guests': self._max_guests
        }
        return venue_info

    def __str__(self): # Prints String
        return "Venue ID: " + str(self._venue_id) + ", Venue Name: " + self._venue_name + ", Email: " + self._email + ", Phone: " + self._phone + ", Location: " + self._location + ", Minimum Number of Guests: " + str(self._min_guests) + ", Maximum Number of Guests: " + str(self._max_guests)


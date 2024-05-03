class Supplier:
    """Class to represent a supplier"""

    # Constructor
    def __init__(self, supplier_id, company_name, phone, email, services_provided, min_guests=None, max_guests=None, menu=None):
        self._supplier_id = supplier_id
        self._company_name = company_name
        self._phone = phone
        self._email = email
        self._services_provided = services_provided
        self._min_guests = min_guests
        self._max_guests = max_guests
        self._menu = menu

    # Setters and getters
    def set_supplier_id(self, supplier_id):
        self._supplier_id = supplier_id
    def get_supplier_id(self):
        return self._supplier_id

    def set_company_name(self, company_name):
        self._company_name = company_name
    def get_company_name(self):
        return self._company_name

    def set_phone(self, phone):
        self._phone = phone
    def get_phone(self):
        return self._phone

    def set_email(self, email):
        self._email = email
    def get_email(self):
        return self._email

    def set_services_provided(self, services_provided):
        self._services_provided = services_provided
    def get_services_provided(self):
        return self._services_provided

    def set_min_guests(self, min_guests):
        self._min_guests = min_guests
    def get_min_guests(self):
        return self._min_guests

    def set_max_guests(self, max_guests):
        self._max_guests = max_guests
    def get_max_guests(self):
        return self._max_guests

    def set_menu(self, menu):
        self._menu = menu
    def get_menu(self):
        return self._menu

    def get_supplier_info(self): # Stores supplier information
        supplier_info = {
            'Supplier ID': self._supplier_id,
            'Company Name': self._company_name,
            'Phone': self._phone,
            'Email': self._email,
            'Services Provided': self._services_provided,
            'Minimum Number of Guests': self._min_guests,
            'Maximum Number of Guests': self._max_guests,
            'Menu': self._menu
        }
        return supplier_info

    def __str__(self): # Returns string
        return "Supplier ID: " + str(self._supplier_id) + ", Company Name: " + self._company_name + ", Phone: " + str(self._phone) + ", Email: " + self._email + ", Services Provided: " + self._services_provided + ", Minimum Number of Guests: " + str(self._min_guests) + ", Maximum Number of Guests: " + str(self._max_guests) + ", Menu: " + str(self._menu)


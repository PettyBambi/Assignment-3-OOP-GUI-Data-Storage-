from enum import Enum
class EventType(Enum): # Enum defining event types
    Wedding = 1
    Birthday = 2
    Themed_Party = 3
    Graduation = 4

class Event:
    """Class to represent an event"""

    # Constructor
    def __init__(self, event_id, event_type, theme, date, time, duration, venue_id, client_id, guests=None, suppliers=None, invoice=None):
        self._event_id = event_id
        self._event_type = event_type
        self._theme = theme
        self._date = date
        self._time = time
        self._duration = duration
        self._venue_id = venue_id
        self._client_id = client_id
        self._guests = guests
        self._suppliers = suppliers
        self._invoice = invoice

    # Setters and getters
    def set_event_id(self, event_id):
        self._event_id = event_id
    def get_event_id(self):
        return self._event_id

    def set_event_type(self, event_type):
        self._event_type = event_type

    def get_event_type_word(event_type):
        return EventType(int(event_type)).name.replace("_", " ")

    def set_theme(self, theme):
        self._theme = theme
    def get_theme(self):
        return self._theme

    def set_date(self, date):
        self._date = date
    def get_date(self):
        return self._date

    def set_time(self, time):
        self._time = time
    def get_time(self):
        return self._time

    def set_duration(self, duration):
        self._duration = duration
    def get_duration(self):
        return self._duration

    def set_venue_id(self, venue_id):
        self._venue_id = venue_id
    def get_venue_id(self):
        return self._venue_id

    def set_client_id(self, client_id):
        self._client_id = client_id
    def get_client_id(self):
        return self._client_id

    def set_guests(self, guests):
        if guests is None:
            guests = []
        self._guests=guests
    def get_guests(self):
        return self._guests
    def guest_list(self):
        guest_list = []
        if self._guests:
            for guest in self._guests:
                guest_list.append(guest.get_name())
        return guest_list

    def set_suppliers(self, suppliers):
        if suppliers is None:
            suppliers = []
        self._suppliers=suppliers
    def get_suppliers(self):
        return self._suppliers
    def supplier_list(self):
        supplier_list = []
        if self._suppliers:
            for supplier in self._suppliers:
                supplier_list.append(supplier.get_company_name())
        return supplier_list

    def set_invoice(self, invoice):
        self._invoice = invoice
    def get_invoice(self):
        return self._invoice

    def get_event_info(self): # Event information as a dictionary
        event_info = {
            'Event ID': self._event_id,
            'Event Type': Event.get_event_type_word(self._event_type),
            'Theme': self._theme,
            'Date': self._date,
            'Time': self._time,
            'Duration': self._duration,
            'Venue ID': self._venue_id,
            'Client ID': self._client_id,
            'Guest List': self._guests,
            'Suppliers': self._suppliers,
            'Invoice': self._invoice
        }
        return event_info

    def __str__(self): # Returns string
        return ("Event ID: " + str(self._event_id) +
                ", Event Type: " + Event.get_event_type_word(self._event_type) +
                ", Theme: " + str(self._theme) +
                ", Date: " + str(self._date) +
                ", Time: " + str(self._time) +
                ", Duration: " + str(self._duration) + " hours" +
                ", Venue ID: " + str(self._venue_id) +
                ", Client ID: " + str(self._client_id) +
                ", Guest List: " + str(self.guest_list()) +
                ", Suppliers: " + str(self.supplier_list()) +
                ", Invoice: " + str(self._invoice))
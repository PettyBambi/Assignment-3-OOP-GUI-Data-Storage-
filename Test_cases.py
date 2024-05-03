from Person import Person
from Guest import Guest
from Venue import Venue
from Employee import Employee
from Client import Client
from Supplier import Supplier
from Event import Event, EventType

# Creating guests
guest1 = Guest("G001", "123456789", "John", "Doe", "john@example.com", "1234567890", "1990-01-01", 31, "Male", "American")
guest2 = Guest("G002", "987654321", "Alice", "Smith", "alice@example.com", "9876543210", "1985-05-15", 36, "Female", "British")
guest3 = Guest("G003", "456789123", "Michael", "Johnson", "michael@example.com", "4567891230", "1982-11-20", 39, "Male", "Canadian")
# Printing details of guests
#print("Guest 1:", guest1)

# Creating multiple instances of the Venue class
venue1 = Venue(101, "Grand Hall", "info@grandhall.com", "1234567890", "123 Main Street", 100, 500)
venue2 = Venue(102, "City Center", "info@citycenter.com", "0987654321", "456 Park Avenue", 200, 1000)
# Printing details of venues
#print("Venue 1:", venue1)

# Creating multiple instances of the Employee class
employee1 = Employee("123456789", "John", "Doe", "john@example.com", "1234567890", "1990-01-01", 31, "Male", "American", "HR", "Manager", 60000, "987654321", "E001")
employee2 = Employee("987654321", "Alice", "Smith", "alice@example.com", "9876543210", "1985-05-15", 36, "Female", "British", "Finance", "Accountant", 50000, "123456789", "E002")
# Printing details of employees
#print("Employee 1:", employee1)

# Creating multiple instances of the Client class
client1 = Client(201, "123456789", "John", "Doe", "john@example.com", "1234567890", "1990-01-01", 31, "Male", "American", 5000)
client2 = Client(202, "987654321", "Alice", "Smith", "alice@example.com", "9876543210", "1985-05-15", 36, "Female", "British", 10000)
# Printing details of clients
#print("Client 1:", client1)

# Creating multiple instances of the Supplier class
supplier1 = Supplier(1, "Catering Inc.", "1234567890", "catering@example.com", "Catering Service", 50, 200, ["Starter", "Main Course", "Dessert"])
supplier2 = Supplier(2, "Decorations R Us", "9876543210", "decorations@example.com", "Decoration Service", 0, None, ["Balloons", "Flowers", "Banners"])
# Printing details of suppliers
#print("Supplier 1:", supplier1)

# Creating multiple instances of the Event class with guest lists
event1 = Event(1, 1, "Garden", "2024-05-01", "18:00", 3, 101, 201, [guest1, guest2],[supplier1,supplier2])
event2 = Event(2, 2, "Superhero", "2024-06-15", "14:00", 4, 102, 202, [guest2, guest3],[supplier1])
# Printing details of events
#print("Event 1:", event1)

# NOTE: Exceptions are in the GUI_software.py
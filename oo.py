"""Discussion Questions

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

- abstraction: hiding unecessary details
- polymorphism: allowing data structures to be replicated with varying differences 
- encapsulation: keeping all relevant data together


2. What is a class?

A class is a template with which one can create several instances. 
Each instance inherits attributes and methods from the class from which it was created, allowing similar 
    information to be stored in separate but related structures.


3. What is a method?

A method is a function that takes place within a class or instance, using attributes


4. What is an instance in object orientation?

An instance is a replica of a class that inherits attributes and methods from that class. 
Data specific to that class can be manually changed or added via instance attributes and methods

5. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

A class attribute is stored data that will be passed down to each instance of that class
An instance attribute is data that will pertain to only that instance, and no other instance of that class
"""

#------------------------------------------------------------------------------------------------------------
"""2. Road Class"""


class Road:
    num_lanes = 2
    speed_limit = 25

road_1 = Road()
road_2 = Road()

road_1.num_lanes = 4
road_1.speed_limit = 60

#------------------------------------------------------------------------------------------------------------
"""3. Update Password"""

class User:
    """A user object."""

    def __init__(self, username, password):
        """Create a user with the given username and password."""

        self.username = username
        self.password = password
    
    def update_password(self, current_password, new_password):
        if current_password == self.password:
            self.current_password = new_password
        else:
            print("Invalid password")

ilana = User("violatido", "catkitty01")
ilana.update_password("catkitty01", "madhat65")
print(ilana.current_password)

#------------------------------------------------------------------------------------------------------------
"""4. Build a Library"""


class Book(object):
    """A Book object."""

    def __init__(self, title, author):
        """Create a book with the given title and author."""

        self.title = title
        self.author = author

#------------------------------------------------------------------------------------------------------------
"""5. Rectangle"""

class Rectangle:
    """A rectangle."""

    def __init__(self, length, width):
        """Create a rectangle with the given length and width."""

        self.length = float(length)
        self.width = float(width)

    def calculate_area(self):
        """Return the area of the rectangle."""

        return self.length * self.width

# Create a class called Square that inherits from Rectangle
class Square(Rectangle):
    # Create an __init__ for the Square class:
    def __init__(self, side):
        # Be sure to use super in order to call Rectangle.__init__ in your implementation
        super().__init__(side, side) # => placing "side" as the argument for "width" and length"
    
    # Create a method called calculate_area for the Square class. 
    # Square.calculate_area should check to see if the square’s length and width have the same values

    def calculate_area(self):
        # If length and width are equivalent, use super to call Rectangle.calculate_area and return its result
        if self.width == self.length:
            super().calculate_area()
        # Otherwise, Square.calculate_area should print Invalid square and return None
        else:
            print("Invalid square")
            return None
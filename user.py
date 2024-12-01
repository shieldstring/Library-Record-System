class User:
    def __init__(self, username, firstname, surname, house_number, street_name, postcode, email, dob):
        """
        Initialize a User instance with attributes.
        """
        self.username = username
        self.firstname = firstname
        self.surname = surname
        self.house_number = house_number
        self.street_name = street_name
        self.postcode = postcode
        self.email = email
        self.dob = dob

    # Getters
    def get_username(self):
        return self.username

    def get_firstname(self):
        return self.firstname

    def get_surname(self):
        return self.surname

    def get_email(self):
        return self.email

    def get_dob(self):
        return self.dob

    # Setters
    def set_firstname(self, firstname):
        self.firstname = firstname

    def set_surname(self, surname):
        self.surname = surname

    def set_email(self, email):
        self.email = email

    def set_dob(self, dob):
        self.dob = dob

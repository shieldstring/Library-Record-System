from user import User

class UserList:
    def __init__(self):
        """
        Initialize the UserList with an empty dictionary.
        """
        self.users = {}

    def add_user(self, user):
        """
        Add a user object to the collection using their username as the key.
        """
        if user.username in self.users:
            raise ValueError("A user with this username already exists.")
        self.users[user.username] = user

    def remove_user(self, firstname):
        """
        Remove a user by their first name. Inform if multiple users have the same first name.
        """
        users_with_name = [u for u in self.users.values() if u.firstname == firstname]
        if len(users_with_name) == 0:
            raise ValueError("No users found with this first name.")
        elif len(users_with_name) > 1:
            raise ValueError("Multiple users found with this first name.")
        else:
            user_to_remove = users_with_name[0]
            del self.users[user_to_remove.username]

    def count_users(self):
        """
        Return the total number of users in the system.
        """
        return len(self.users)

    def get_user_details(self, username):
        """
        Return a user's details by username.
        """
        return self.users.get(username, None)

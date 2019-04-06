import pyperclip
class User:
    """
    Class that generates new instances of contacts.
    """

    user_detail = [] # Empty contact list

    def __init__(self,first_name,last_name,number,email):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email

    user_detail = [] # Empty contact list
 # Init method up here
    def save_user(self):

        '''
        save_user method saves uesr objects into user_detail
        '''

        User.user_detail.append(self)


    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_detail
        '''

        User.user_detail.remove(self)

    @classmethod
    def find_by_number(cls,number):
        for user in cls.user_detail:
            if user.phone_number == number:
                return user

    @classmethod
    def user_exist(cls,number):
        for user in cls.user_detail:
            if user.phone_number == number:
                    return True

    @classmethod
    def display_users(cls):
        return cls.user_detail

    @classmethod
    def copy_email(cls,number):
        user_found = User.find_by_number(number)
        pyperclip.copy(user_found.email)

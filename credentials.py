import pyperclip
class Credentials:
    """
    Class that generates new instances of credentials.
    """

    credentials_account = []

    def __init__(self,user_name,social_account,number,email):

      # docstring removed for simplicity

        self.user_name = user_name
        self.social_account = social_account
        self.password = number
        self.email = email

    credentials_account = [] # Empty credentials account
 # Init method up here
    def save_credentials(self):

        '''
        save_credentials method saves credentials objects into credentials account
        '''

        Credentials.credentials_account.append(self)

    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credentials from the credentials account
        '''

        Credentials.credentials_account.remove(self)

    @classmethod
    def credentials_exist(cls,number):
        for credentials in cls.credentials_account:
            if credentials.password == number:
                    return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials account
        '''
        return cls.credentials_account

    @classmethod
    def copy_email(cls,number):
        credentials_found = Credentials.find_by_number(number)
        pyperclip.copy(credentials_found.email)

    # def password_credentials(self):
    #     '''
    #     Generate a password randomly
    #     '''
    #     Credentials.credentials_account.reverse(self)


    @classmethod
    def find_by_number(cls,number):
    
        for credentials in cls.credentials_account:
            if credentials.password == number:
                return credentials

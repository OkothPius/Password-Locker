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
        save_credentials method saves credentials objects into credentials_account
        '''

        Credentials.credentials_account.append(self)

    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credentials from the credentials_account
        '''

        Credentials.credentials_account.remove(self)
        

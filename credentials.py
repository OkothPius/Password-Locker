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

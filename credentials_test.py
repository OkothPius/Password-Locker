import pyperclip
import unittest # Importing the unittest module
from credentials import Credentials # Importing the contact class

class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    #FirstTest
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("Clark","Twitter","1613","clark@ms.com") # create credentials object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.user_name,"Clark")
        self.assertEqual(self.new_credentials.social_account,"Twitter")
        self.assertEqual(self.new_credentials.password,"1613")
        self.assertEqual(self.new_credentials.email,"clark@ms.com")

    #SecondTest
    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into
         the credentials_account
        '''
        self.new_credentials.save_credentials() # saving the new credentials
        self.assertEqual(len(Credentials.credentials_account),1)

    #ThirdTest
    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credentials
            objects to our credentials_account
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Test","account","1613","test@user.com") # new credentials
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.credentials_account),2)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_account = []

    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credentials
            objects to our credentials_account
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Test","account","1613","test@user.com") # new credentials
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.credentials_account),2)

    #FourthTest
    def test_delete_credentials(self):
            '''
            test_delete_credentials to test if we can remove a credentials from our credentials account
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Test","account","1613","test@user.com") # new credentials
            test_credentials.save_credentials()

            self.new_credentials.delete_credentials()# Deleting a credentials object
            self.assertEqual(len(Credentials.credentials_account),1)

    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credentials from the credentials_account
        '''

        Credentials.credentials_account.remove(self)

    #Credentials Exist
    def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credentials.
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Test","account","1613","test@user.com") # new credentials
        test_credentials.save_credentials()

        credentials_exists = Credentials.credentials_exist("1613")

        self.assertTrue(credentials_exists)

    @classmethod
    def credentials_exist(cls,number):
        '''
        Method that checks if a credentials exists from the credentials_account.
        Args:
            number: Password to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for credentials in cls.credentials_account:
            if credentials.password == number:
                    return True

        return False

    #Display Credentials
    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_account)

    def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found credentials
        '''

        self.new_credentials.save_credentials()
        Credentials.copy_email("1613")

        self.assertEqual(self.new_credentials.email,pyperclip.paste())

    @classmethod
    def copy_email(cls,number):
        credentials_found = Credentials.find_by_number(number)
        pyperclip.copy(credentials_found.email)

    # #FifthTest
    # def test_password_credentials(self):
    #     '''
    #     Returns a string of random characters,useful in generating temporary
    #     passwords for automated password resets.
    #     '''
    #     self.new_credentials.save_credentials()
    #     test_credentials = Credentials("Test","account","1613","test@user.com") # new credentials
    #     test_credentials.save_credentials()
    #
    #     self.new_credentials.password_credentials()#creating a password in Credentials
    #     self.assertEqual(len(Credentials.credentials_account),1)
    #
    # def password_credentials(self):
    #     '''
    #     Generate a password randomly
    #     '''
    #     Credentials.credentials_account.reverse(self)

    # #FifthTest
    # def test_find_credentials_by_number(self):
    #     '''
    #     test to check if we can find a credentials by password and display information
    #     '''
    #
    #     self.new_credentials.save_credentials()
    #     test_credentials = Credentials("Test","user","1613","test@user.com") # new credentials
    #     test_credentials.save_credentials()
    #
    #     found_credentials = Credentials.find_by_number("1613")
    #
    #     self.assertEqual(found_credentials.email,test_credentials.email)
    #
    # @classmethod
    # def find_by_number(cls,number):
    #     '''
    #     Method that takes in a number and returns a credentials that matches that number.
    #
    #     Args:
    #         number: Password to search for
    #     Returns :
    #         Credentials of person that matches the number.
    #     '''
    #
    #     for credentials in cls.credentials_account:
    #         if credentials.password == number:
    #             return credentials







if __name__ == '__main__':
    unittest.main()

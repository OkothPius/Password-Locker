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






if __name__ == '__main__':
    unittest.main()

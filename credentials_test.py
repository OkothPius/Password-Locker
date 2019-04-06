# import unittest # Importing the unittest module
from credentials import Credentials # Importing the contact class

class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

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


if __name__ == '__main__':
    unittest.main()

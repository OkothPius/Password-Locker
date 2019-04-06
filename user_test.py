import pyperclip
import unittest # Importing the unittest module
from user import User # Importing the contact class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Clark","Oruko","0712345678","clark@ms.com") # create contact object

    #FirstTest
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Clark")
        self.assertEqual(self.new_user.last_name,"Oruko")
        self.assertEqual(self.new_user.phone_number,"0712345678")
        self.assertEqual(self.new_user.email,"clark@ms.com")

      #SecondTest
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user_detail
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_detail),1)

      #ThirdTest
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_detail
            '''
            self.new_user.save_user()
            test_user = User("Test","user","0712345678","test@user.com") # new contact
            test_user.save_user()
            self.assertEqual(len(User.user_detail),2)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_detail = []

# other test cases here
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_detail
            '''
            self.new_user.save_user()
            test_user = User("Test","user","0712345678","test@user.com") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_detail),2)



      #FourthTest
    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user_detail
            '''
            self.new_user.save_user()
            test_user = User("Test","user","0712345678","test@user.com") # new user
            test_user.save_user()

            self.new_user.delete_user()# Deleting a user object
            self.assertEqual(len(User.user_detail),1)


     #FifthTest
    def test_find_user_by_number(self):
        '''
        test to check if we can find a user by phone number and display information
        '''

        self.new_user.save_user()
        test_user = User("Test","user","0711223344","test@user.com") # new contact
        test_user.save_user()

        found_user = User.find_by_number("0711223344")

        self.assertEqual(found_user.email,test_user.email)

    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a user that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            User that matches the number.
        '''

        for user in cls.user_detail:
            if user.phone_number == number:
                return user

       #sixthTest
    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("Test","user","0711223344","test@user.com") # new user
        test_user.save_user()

        user_exists = User.user_exist("0711223344")

        self.assertTrue(user_exists)

    @classmethod
    def user_exist(cls,number):
        '''
        Method that checks if a user exists from the user_detail.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for user in cls.user_detail:
            if user.phone_number == number:
                    return True

        return False

    def test_display_all_users(self):
        '''
        method that returns a list of all  saved users
        '''

        self.assertEqual(User.display_users(),User.user_detail)

    @classmethod
    def display_users(cls):
        '''
        method that returns the user_detail
        '''
        return cls.user_detail

    def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found user
        '''

        self.new_user.save_user()
        User.copy_email("0712345678")

        self.assertEqual(self.new_user.email,pyperclip.paste())

    @classmethod
    def copy_email(cls,number):
        user_found = User.find_by_number(number)
        pyperclip.copy(user_found.email)





if __name__ == '__main__':
    unittest.main()

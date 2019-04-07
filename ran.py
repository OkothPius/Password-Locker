#!/usr/bin/python3.6
from credentials import Credentials
import string
import random

#creating Credentials
def create_credentials(uname,account,password,email):
    '''
    Function to create a new credentials
    '''
    new_credentials = Credentials(uname,account,password,email)
    return new_credentials

#save credentials
def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()

#Delete Credentials
def del_credentials(credentials):
    '''
    Function to delete a credentials
    '''
    credentials.delete_credentials()

#Finding a credentials
def find_credentials(number):
    '''
    Function that finds a credentials by number and returns the credentials
    '''
    return Contact.find_by_number(number)

#Checking if a credentials exists
def check_existing_credentials(number):
    '''
    Function that check if a credentials exists with that number and return a Boolean
    '''
    return Credentials.credentials_exist(number)

#Displaying credentials
def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()

#Generating a random password
def password_generator(size=8, chars=string.ascii_letters + string.digits):
    '''
    Returns a string of random characters, useful in generating temporary
    passwords for automated password resets.
    '''
    return ''.join(random.choice(chars) for i in range (size))

def main():
    print("Hello Welcome to your credentials_account. What is your username?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
            print("Use these short codes : cc - create a new credential account, dc - display credentials, fc -find a credential, xx -delete a credential account, ex -exit the credentials account ")

            short_code = input().lower()

            if short_code == 'cc':
                    print("New Credentials")
                    print("-"*10)

                    print ("User name ....")
                    u_name = input()

                    print("Social account ...")
                    s_account = input()

                    print("Password ...")
                    p_word = input()

                    print("Email address ...")
                    e_address = input()


                    save_credentials(create_credentials(u_name,s_account,p_word,e_address)) # create and save new credential.
                    print ('\n')
                    print(f"New Credentials {u_name} {p_word} created")
                    print ('\n')

                    del_credentials(pop_credentials(u_name,s_account,p_word,e_address)) # Deleting a credential account
                    print('\n')
                    print(f"The Credentials {u_name} {p_word} deleted")
                    print('\n')

            elif short_code == 'dc':

                    if display_credentials():
                            print("Here is a list of all your credentials")
                            print('\n')

                            for credentials in display_credentials():
                                    print(f"{credentials.user_name} {credentials.social_account} .....{credentials.password}")

                            print('\n')
                    else:
                            print('\n')
                            print("You dont seem to have any credentials saved yet")
                            print('\n')

            elif short_code == 'fc':

                    print("Enter the number you want to search for")

                    search_number = input()
                    if check_existing_credentials(search_number):
                            search_credentials = find_credentials(search_number)
                            print(f"{search_credentials.user_name} {search_credentials.password}")
                            print('-' * 20)

                            print(f"Password.......{search_credentials.password}")
                            print(f"Email address.......{search_credentials.email}")
                    else:
                            print("That credentials does not exist")

            elif short_code == "ex":
                    print("Bye .......")
                    break
            else:
                    print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':
    main()

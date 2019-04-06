#!/usr/bin/env python3.6
from user import User

#creating a contact
def create_user(fname,lname,phone,email):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,phone,email)
    return new_user

#save user
def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

#Deleting a user
def delete_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()


#Finding a user
def find_user(number):
    '''
    Function that finds a user by number and returns a user
    '''
    return User.find_by_number(number)

#Checking if a user exists
def check_existing_user(number):
    '''
    Function that checks if a user exist with that number
    '''
    return User.user_exist(number)

#Display user
def dispaly_user():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

#Main Function
def main():
    print("Hello Welcome to your user detail. What is your name?")
        user_name = input()

        print(f"Hello {user_name}. what would you like to do?")
        print('\n')

        while True:
                print("Use these short codes : cc - create a new user, dc - display users, fc -find a user, ex -exit the user details ")

                short_code = input().lower()

                if short_code == 'cc':
                        print("New User")
                        print("-"*10)

                        print ("First name ....")
                        f_name = input()

                        print("Last name ...")
                        l_name = input()

                        print("Phone number ...")
def main():
print("Hello Welcome to your user details. What is your name?")
        user_name = input()

        print(f"Hello {user_name}. what would you like to do?")
        print('\n')

        while True:
                print("Use these short codes : cc - create a new user, dc - display users, fc -find a user, ex -exit the user details ")

                short_code = input().lower()

                if short_code == 'cc':
                        print("New User")
                        print("-"*10)

                        print ("First name ....")
                        f_name = input()

                        print("Last name ...")
                        l_name = input()

                        print("Phone number ...")
                        p_number = input()

                        print("Email address ...")
                        e_address = input()


                        save_users(create_user(f_name,l_name,p_number,e_address)) # create and save new user
                        print ('\n')
                        print(f"New User {f_name} {l_name} created")
                        print ('\n')

                elif short_code == 'dc':

                        if display_users():
                                print("Here is a list of all  users")
                                print('\n')

                                for user in display_users():
                                        print(f"{user.first_name} {user.last_name} .....{user.phone_number}")

                                print('\n')
                        else:
                                print('\n')
                                print("You dont seem to have any users saved yet")
                                print('\n')

                elif short_code == 'fc':

                        print("Enter the number you want to search for")

                        search_number = input()
                        if check_existing_users(search_number):
                                search_user = find_contact(search_number)
                                print(f"{search_user.first_name} {search_user.last_name}")
                                print('-' * 20)

                                print(f"Phone number.......{search_user.phone_number}")
                                print(f"Email address.......{search_user.email}")
                        else:
                                print("That user does not exist")

                elif short_code == "ex":
                        print("Bye .......")
                        break
                else:
                        print("I really didn't get that. Please use the short codes")                        p_number = input()

                        print("Email address ...")
                        e_address = input()


                        save_users(create_user(f_name,l_name,p_number,e_address)) # create and save new user.
                        print ('\n')
                        print(f"New User {f_name} {l_name} created")
                        print ('\n')

                elif short_code == 'dc':

                        if display_users():
                                print("Here is a list of all users")
                                print('\n')

                                for user in display_users():
                                        print(f"{user.first_name} {user.last_name} .....{user.phone_number}")

                                print('\n')
                        else:
                                print('\n')
                                print("You dont seem to have any users saved yet")
                                print('\n')

                elif short_code == 'fc':

                        print("Enter the number you want to search for")

                        search_number = input()
                        if check_existing_users(search_number):
                                search_user = find_user(search_number)
                                print(f"{search_user.first_name} {search_user.last_name}")
                                print('-' * 20)

                                print(f"Phone number.......{search_user.phone_number}")
                                print(f"Email address.......{search_user.email}")
                        else:
                                print("That user does not exist")

                elif short_code == "ex":
                        print("Bye .......")
                        break
                else:
                        print("I really didn't get that. Please use the short codes")

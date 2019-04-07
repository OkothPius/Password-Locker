# _Password-Locker_

#### By _Okoth Pius Ogutu_

#### Date _05-04-2019_

## Description

_An application that will help us manage our passwords and even generate new passwords for us._

## Behavior Driven Development(BDD)

| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| User runs ./run.py | User enter their details | The application saves the details |
| Player 1 clicks ROLL button | Click ROLL button | Dice rolls and number is generated
| If Player 1 rolls any number other than 1, that roll is added to round total | Roll = 2 | Round total = 2 |
| If Player 1 rolls a 1, no score is added and round for Player 1 ends | Roll = 1 | Round total = 2 / Total score = 2 / Player 2 begins |
| Repeat for Player 2 | Roll = 1 | Round total = 0 / Total score = 0 / Player 1 begins |
| When a player's total score reaches 100 or more, game ends and winner page shows | Player 1 total score = 100 | Winner page |


## Setup/Installation Requirements

* _Open your GITHUB account_
* _Clone this repository_
* _Open the repository in your favourite editor_
* _The apllication mainly uses the terminal(Linux)/prompt(windows)_
* _Open run the file by python3.6 filename_
* _./run.py to run the module_


## Bugs

* _Since there is no database to support the app, once you exit or log out of a session you loose all the credentials and created user. You have to create a new user for every session. You can still use the default login but if you exit the app, you will still loose all the credentials you created._

## Technologies Used

* _Python_

## Contact Information

* _FACEBOOK:_orukopius
* _IG:__oruko_
* _TEL:_0719-121-890

### License

*This software is licensed under the MIT license.*

Copyright (c) 2019 **_Okoth Pius Ogutu_**

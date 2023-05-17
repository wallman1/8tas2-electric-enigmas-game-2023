import os


def login():
  print("Create Your Account")
  User = input("Create Username: ")
  Pass = input("Create Password: ")
  Pass2 = input("Type in your password again: ")

  while Pass != Pass2:
   print("Your Password Does Not Match. Please Try Again!")
  
   User = input("Create Username: ")
   Pass = input("Create Password: ")
   Pass2 = input("Type in your password again: ")

  print("Account Created!")

  print("Login!")

  Username = input("Username: ")
  Password = input("Password: ")

  while User != User or Pass != Password:
    print("Your Username or Password does not match. Please try again")
  
    Username = input("Username: ")
    Password = input("Password: ")

  print("Login Success!")


def MiniMap():
    print('''
             ▫️---▫️
             |
    ▫️-\          ▫️
    |  \        / \ 
    ▫️   \       ▫️ ▫️
    |    \      \ /
    ▫️-----\-▫️    ▫️
           \|    |
            ▫️----▫️
    ''')


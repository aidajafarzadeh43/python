# منطق لاگین کردن در یک سایت

# stired_password = "12345"
# entered_password = input ("enter your password: ")
# if  entered_password == stired_password :
#     print ("you loged successfuly")
# else :
#     print ("try again")    


# stired_password = "12345"
# entered_password = input ("enter your password: ")
# while entered_password != stired_password :
#   entered_password = input ("try again: ")
# else :
#   print ("you loged successfuly")


# users = { 
#     "aida" : 1234,
#     "reza" : 5678,
#     "sara" : 9012
#     } 
# entered_username = input("enter your username: ")
# entered_password = input("enter your password: ")
# if entered_username in users :
#     print("yes you are user")
# else :
#     print("no you not user")


    
    
        
# users = { 
#     "aida": "112",
#     "reza": "678",
#     "sara": "012"
# }

# entered_username = input("Enter your username: ")
# entered_password = input("Enter your password: ")

# if entered_username in users and users[entered_username] == entered_password:
#     print("You logged in successfully.")
# else:
#     print("Your username or password is incorrect.")

# users = {
#     "aida": "112",
#     "reza": "678",
#     "sara": "012"
# }

# while True:
#     entered_username = input("Enter your username: ")
#     entered_password = input("Enter your password: ")

#     if entered_username in users and users[entered_username] == entered_password:
#         print("You logged in successfully.")
#         break  # خروج از حلقه در صورت ورود موفق
#     else:
#         print("Your username or password is incorrect. Please try again.")



users = {
     "aida": "112",
     "reza": "678",
     "sara": "012"
}

entered_username = input("Enter your username: ")
entered_password = input("Enter your password: ")

while entered_username not in users or users[entered_username] != entered_password:
    print("our username or password is incorrect. Please try agai") 
    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")
print("login")
 

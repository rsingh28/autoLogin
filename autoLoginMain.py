import os
import time

# if os.path.isfile("test.txt"):

# 	print("File Exists")

# else:

# 	f = open("test.txt","w+")
# 	print("File Created")

# user_choice = raw_input('Please press 1 to delete file: ')

# if (user_choice == "1"):
# 	os.remove("test.txt")

# if(user_choice == "2"):
# 	f = open("test2.txt","w+")

# if os.path.isfile("test.txt"):
# 	print("test Exists")

# if os.path.isfile("test2.txt"):
# 	print("test2 Exists")

def set_email():

	email = raw_input("Please enter your E-mail ID: ")

	time.sleep(1)

	email_confirm = raw_input('Please confirm your E-mail ID: ')

	if (email == email_confirm):

		print("**** E-mail ID Confirmed ****")
		print(email) # Remove This
		time.sleep(2)
		return 1

	else:

		print("!!!! E-mail did not match. Please try again !!!!")
		return 0

def set_password():

	password = raw_input('Please enter your Password: ')

	time.sleep(1)

	password_confirm = raw_input('Please confirm your Password: ')

	if (password == password_confirm):

		print("**** Password Confirmed ****")
		print(password) # Remove This
		time.sleep(2)
		return 1

	else:

		print("!!!! Password did not match. Please try again !!!!")
		return 0


def main():

	if os.path.isfile("credentials.txt"):

		print("Will Come Back To it")

	else:

		#f = open("credentials.txt","w+")

		print("**** Welcome to Auto-Login! This is a one time set-up for your Gmail Credentials ****")

		time.sleep(2)

		return_code = set_email()

		while(return_code != 1):

			return_code = set_email()

		return_code1 = set_password()

		while(return_code1 != 1):

			return_code1 = set_password()

main()




from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

def login(email,password):

	driver = webdriver.Chrome();

	driver.get("http://gmail.com")

	driver.set_page_load_timeout(10)

	driver.maximize_window()

	email_input = driver.find_element_by_name("identifier")

	email_input.send_keys(email)

	next_btn = driver.find_element_by_xpath("//div[contains(@id,'identifierNext') and contains(@tabindex,'0')]") 

	next_btn.send_keys(Keys.RETURN)

	driver.set_page_load_timeout(5)

	time.sleep(2)

	password_input = driver.find_element_by_name("password");

	password_input.send_keys(password);

	next_btn1 = driver.find_element_by_xpath("//div[contains(@id,'passwordNext')]")

	next_btn1.send_keys(Keys.RETURN)

	user_choice = raw_input('Please click ENTER button to close script')
	if not user_choice:
		print("ABORTED")
		quit()


def main():

	if (len(sys.argv)!=3):

		print("Please provide Email and Password as arguments")

	else:

		print("Logging You In ")

		email = sys.argv[1]

		password = sys.argv[2]

		login(email,password)

main()


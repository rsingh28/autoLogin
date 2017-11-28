import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Array of arguments (Not starting from 0 since thats the name of the script)
arguments = sys.argv[1:]

def googleSearch():

	# Specify the browser driver desired - Chrome driver in this case
	driver = webdriver.Chrome()

	# Set the URL to be opened in the specified bowser 
	driver.get("http://google.com")

	# Give 10 seconds to load the webPage
	driver.set_page_load_timeout(10)

	 # Get the Search-Box using "ID" found by inspecting search box element on google
	# Alternate Way => searchBox = driver.find_element_by_name("q")
	searchBox = driver.find_element_by_id("lst-ib")

	#Type this string in the search box
	searchBox.send_keys("Automation is Cool")

	# Find the "Google Search" button
	btn = driver.find_element_by_name("btnK")

	# Press the button
	btn.click()

	user_choice = raw_input('Please click ENTER button to close script')
	if not user_choice:
		print("ABORTED")
		quit()

def googleSearchAuto():

	driver = webdriver.Chrome()

	driver.get("http://google.com")

	driver.set_page_load_timeout(10)

	input = driver.find_element_by_name("q")

	input.send_keys(arguments[0])

	print(arguments[0])

	btn = driver.find_element_by_name("btnK")

	# Alternate of btn.click() - Press Enter on the button instead
	btn.send_keys(Keys.ENTER)

	user_choice = raw_input('Please click ENTER button to close scipt')
	if not user_choice:
		print("ABORTED")
		quit()

def main():

	if not arguments:

		print("Doing default search since no argument is specified")

		googleSearch()

	else:

		print("Doing a google search for - " + arguments[0])

		googleSearchAuto()


main()
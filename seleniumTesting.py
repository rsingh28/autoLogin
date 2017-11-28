import time
import sys
from selenium import webdriver

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

	user_choice = raw_input('Please click ENTER button to close application')
	if not user_choice:
		print("ABORTED")
		quit()

googleSearch() 

	



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


username = "*******"
password = "*******"


def loginInstagram(username,password,driver):
	driver.get("https://www.instagram.com")

	username_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
	password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
	username_field.send_keys(username)
	password_field.send_keys(password)
	login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

	return driver

def goToMyProfile(driver):
	sleep(3)
	driver.get("https://www.instagram.com/" + username)
	sleep(1)
	return driver

def findFollowing(driver): #Get list of following accounts

	sleep(2)
	driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]").click()
	#open_list_of_folowers =  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "/html/body/div[1]/section/main/div/header/section/ul/li[3]']"))).click()
	sleep(2)

	#find scrollbox,scroll x-times
	scroll_box = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')

	last_ht = 0
	ht = 0.1
	while last_ht!=ht:
		last_ht =ht
		sleep(1)
		#ht = driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight; return arguments[0].scrollHeight',scroll_box)
		ht = driver.execute_script('arguments[0].scrollTo(0,arguments[0].scrollHeight); return arguments[0].scrollHeight',scroll_box)

	links = scroll_box.find_elements_by_xpath("//a[@class='FPmhX notranslate  _0imsa ']")
	followingNamesList = [link.text for link in links if link!='']

	close  = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button").click()
	return followingNamesList


def findFollowers(driver):#Get list of followers accounts
	sleep(2)
	open_list_of_folowers = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]").click()
	sleep(2)

	#find scrollbox,scroll x-times
	scroll_box = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')

	last_ht = 0
	ht = 0.1
	while last_ht!=ht:
		last_ht =ht
		sleep(1)
		#ht = driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight; return arguments[0].scrollHeight',scroll_box)
		ht = driver.execute_script('arguments[0].scrollTo(0,arguments[0].scrollHeight); return arguments[0].scrollHeight',scroll_box)

	links = scroll_box.find_elements_by_xpath("//a[@class='FPmhX notranslate  _0imsa ']")
	followersNamesList = [link.text for link in links if link!='']

	close  = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button").click()
	return followersNamesList

def unfollow(driver,num_of_unfollow,scroll_box):
	list_of_links = scroll_box.find_elements_by_xpath("//li[@class='wo9IH']")

	for x in range(0,num_of_unfollow):

		#print username
		username = list_of_links[x].find_elements_by_xpath("//a[@class='FPmhX notranslate  _0imsa ']")

		#unfollow
		unfollow_button = list_of_links[x].find_element_by_xpath("//button[@class='sqdOP  L3NKy    _8A5w5    ']")
		unfollow_button.click()
		sleep(2)
		#confirm unfollow
		print(str(x+1) + "." + username[x].text + "\tunfollowed")
		confirm_button = driver.find_element_by_xpath("//button[@class='aOOlW -Cab_   ']")
		confirm_button.click()
		scroll_box = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
		list_of_links = scroll_box.find_elements_by_xpath("//li[@class='wo9IH']")
		sleep(6)

def unfollowUsers(driver,username,password):

	num_of_unfollow = 0 #input("How many want to unfollow?\n")
	driver = loginInstagram(username,password,driver)
	driver = goToMyProfile(driver)

	followingList = findFollowing(driver)

	followersList = findFollowers(driver)

	notFolowMeBack = [user for user in followingList if user not in followersList]
	print(notFolowMeBack)

def gain_followers_from_account(driver,username,password):

	name_of_account = input("Enter a name of account that want to copy followers: ")
	driver = login_insta(username,password,driver)

	driver.get("https://www.instagram.com/"+ name_of_account)
	sleep(3)
	images_holder = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[3]/article/div[1]/div')
	images_holder.find_elements_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']")
	sleep(1)
	images_holder[0].find_element_by_tag_name("a").click()

driver = webdriver.Chrome(executable_path="C:/Users/chrome_driver/chromedriver.exe")

unfollowUsers(driver,username,password)

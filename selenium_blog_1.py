#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

TIMEOUT = 15
PHONE = '555-555-5555'
COMPANY = "Cowabunga Pizzas"
MESSAGE = "Hi,\n\nIt's Mikey from CowabungaPizzas! Just wanted ask quesitons about your payment software!"

def phone_input(driver):
	phone_box = WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="wpforms-32656-field_4"]' ) ))
	phone_box.send_keys(PHONE)

def company_input(driver):
	company_box = WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="wpforms-32656-field_3"]' ) ))
	company_box.send_keys(COMPANY)

def message_input(driver):
	message_box = WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="wpforms-32656-field_2"]' ) ))
	message_box.send_keys(MESSAGE)

def email_input(email, driver):
  email_box = WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="wpforms-32656-field_1"]' ) ))
  email_box.send_keys(email)

def name_input(first_name, last_name, driver):
	first_name_box = WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="wpforms-32656-field_0"]' ) ))
	first_name_box.send_keys(first_name)
	last_name_box = WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="wpforms-32656-field_5"]' ) ))
	last_name_box.send_keys(last_name)

def click_send(driver):
	button = WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located( ( By.XPATH, '//*[@id="contact-form"]/button' ) ))
	button.click()
	sleep(20)
	
def input_info(first_name, last_name, email, driver):
	name_input(first_name, last_name, driver)
	email_input(email, driver)
	message_input(driver)
	company_input(driver)
	phone_input(driver)
	click_send(driver)

def commandline():
  first_name_check = ''
  last_name_check = ''
  email_check = ''
  while first_name_check != 'y':
    first_name = input("Enter your first name: ")
    first_name_check = input(f"You entered {first_name}, is this correct? (y or n): ")
  while last_name_check != 'y':
    last_name = input("Enter your last name: ")
    last_name_check = input(f"You entered {last_name}, is this correct? (y or n): ")
  while email_check != 'y':
    email = input("Enter your email: ")
    email_check = input(f"You entered {email}, is this correct? (y or n): ")
  return first_name, last_name, email
  
def main():
  first_name, last_name, email = commandline()
  driver = webdriver.Chrome(ChromeDriverManager().install())
  driver.get("https://pineapplepayments.com/contact-us/#general-pineapple-contact-form")
  input_info(first_name, last_name, email, driver)

if __name__== "__main__":
  main()

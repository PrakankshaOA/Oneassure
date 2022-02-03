from lib2to3.pgen2 import driver
from selenium import webdriver
import random
import time


def input_Cred(driver):
    """input credentials"""
    driver.find_elements_by_class_name("MuiInput-input")[0].send_keys("9166833189")
    driver.find_elements_by_class_name("MuiInput-input")[1].send_keys("Prakanksha123")
    time.sleep(2)
    """submit"""
    driver.find_element_by_class_name("MuiButton-label").click()

def age_insert(driver):
    """self"""
    time.sleep(3)
    driver.find_elements_by_class_name("MuiSvgIcon-root")[1].click()
    time.sleep(2)
    print("input age")
    a = input()
    driver.find_elements_by_class_name("MuiInputBase-input")[0].send_keys(a)
    time.sleep(3)
    button = driver.find_elements_by_class_name("MuiSvgIcon-root")
    length = len(button)
    button[length - 1].click()
    time.sleep(2)

def coverage_number(driver):
    L1 = [1, 2, 3, 4]
    a = random.choice(L1)
    driver.find_elements_by_class_name("MuiSvgIcon-root")[a].click()
    time.sleep(3)

def insert_pincode(driver):
    print("enter Pincode")
    z = input()
    for i in range(6):
        driver.find_elements_by_class_name("pincode-input-text")[i].send_keys(z[i])
        time.sleep(1)

def policy_proposer(driver):
    print("enter name of policy proposer")
    y = input()
    driver.find_elements_by_class_name("MuiInputBase-input")[0].send_keys(y)
    time.sleep(3)
    button = driver.find_elements_by_class_name("MuiSvgIcon-root")
    length = len(button)
    button[length - 1].click()
    time.sleep(2)

def insert_phoneNumber(driver):
    print("enter phone no.")
    pho = input()
    driver.find_elements_by_class_name("MuiInputBase-input")[0].send_keys(pho)
    button = driver.find_elements_by_class_name("MuiSvgIcon-root")
    length = len(button)
    button[length - 1].click()

def insert_gender(driver):
    time.sleep(2)
    L2 = [0, 1, 2, ]
    T = random.choice(L2)
    driver.find_elements_by_class_name("space_betwwen")[T].click()
    button = driver.find_elements_by_class_name("MuiSvgIcon-root")
    length = len(button)
    button[length - 1].click()

def recommendation_form(driver):
    """get recommendation click"""
    time.sleep(2)
    driver.find_elements_by_class_name("MuiButton-label")[6].click()
    """continue click"""
    time.sleep(2)
    driver.find_elements_by_class_name("MuiButton-label")[0].click()
    """page wise function calling"""
    age_insert(driver)
    coverage_number(driver)
    insert_pincode(driver)
    policy_proposer(driver)
    insert_phoneNumber(driver)
    insert_gender(driver)



driver = webdriver.Chrome(r"C:\Users\Syn_A\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("https://app.oneassure.in")
driver.implicitly_wait(5)
input_Cred(driver)
recommendation_form(driver)

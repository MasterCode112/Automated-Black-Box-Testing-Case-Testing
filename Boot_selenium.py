import chromedriver_autoinstaller
import geckodriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
options = FirefoxOptions()
driver_path = geckodriver_autoinstaller.install()
driver = webdriver.Firefox(options=options, executable_path=driver_path)
driver.set_page_load_timeout(100)
driver.get("http://localhost/patientrecords/usercontrol/login")

username_input = driver.find_element(By.NAME, "user1")
password_input = driver.find_element(By.NAME, "pass1")
print("                                 LOGIN PAGE       ")
username = input("Enter Username: ")
password = input("Enter Password: ")
username_input.send_keys(username)
password_input.send_keys(password)
login_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Login')]")
login_button.click()
wait = WebDriverWait(driver, 4)
css_selector = "div.alert.alert-danger.alert-dismissible.text-center"
try:
    welcome_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))
    print(" Login failed!")
    print("Failed!")
    driver.quit()
except TimeoutException:
    print(" Login successful!")
    print("Pass!")
    print('''

        ''')
    print('''
                                                   EDIT PATIENT RECORD
        ''')

driver.get("http://localhost/patientrecords/admissioncontrol/edit_form/1")
lname_input = driver.find_element(By.NAME, "lname")
fname_input = driver.find_element(By.NAME, "fname")
middlen_input = driver.find_element(By.NAME, "middlen")
address_input = driver.find_element(By.NAME, "address")
age_input = driver.find_element(By.NAME, "age")
number_input = driver.find_element(By.NAME, "number")
occup_input = driver.find_element(By.NAME, "occup")
fname = input("Enter First Name: ")
middlen = input("Enter Middle Name: ")
lname = input("Enter Last Name: ")
address = input("Enter Address: ")
age = input("Enter Age: ")
# number = input("Enter Phone Number: ")
occup = input("Enter Occupation: ")
lname_input.clear()
lname_input.send_keys(lname)
fname_input.clear()
fname_input.send_keys(fname)
middlen_input.clear()
middlen_input.send_keys(middlen)
address_input.clear()
address_input.send_keys(address)
age_input.clear()
age_input.send_keys(age)
# number_input.clear()
# number_input.send_keys(number)
occup_input.clear()
occup_input.send_keys(occup)
Save_Record_button = driver.find_element(By.NAME, "submit")
Save_Record_button.click()
wait = WebDriverWait(driver, 4)
css_selector = "div.alert.alert-success.alert-dismissible.text-center"
try:
    Updated_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))
    print(" Patient Data Updated!")
    print("Pass!")
    print('''

        ''')
    print('''
                                                   ADD PATIENT RECORD
        ''')

    driver.get("http://localhost/patientrecords/multiplerecordcontrol/multiplerecordview")
    a_casenumber_input = driver.find_element(By.NAME, "a_casenumber")
    a_chief_complaint_input = driver.find_element(By.NAME, "a_chief_complaint")
    a_historyillness_input = driver.find_element(By.NAME, "a_historyillness")
    a_bp_input = driver.find_element(By.NAME, "a_bp")
    a_rr_input = driver.find_element(By.NAME, "a_rr")
    a_cr_input = driver.find_element(By.NAME, "a_cr")
    a_temp_input = driver.find_element(By.NAME, "a_temp")
    a_wt_input = driver.find_element(By.NAME, "a_wt")
    a_pr_input = driver.find_element(By.NAME, "a_pr")
    # a_date = driver.find_element(By.NAME, "a_date")
    a_physician_input = driver.find_element(By.NAME, "a_physician")
    a_physicalexam_input = driver.find_element(By.NAME, "a_physicalexam")
    a_medical_treatment_input = driver.find_element(By.NAME, "a_medical_treatment")
    a_diagnosis_input = driver.find_element(By.NAME, "a_diagnosis")
    a_casenumber = input("Enter Case Number: ")
    a_chief_complaint = input("Enter Chief Complaint: ")
    a_physicalexam = input("Enter Physical Examination: ")
    a_historyillness = input("History of Present Illness: ")
    a_bp = input("Enter Blood Pressure: ")
    a_rr = input("Enter Respiratory Rate ")
    a_cr = input("Enter Capillary Refill: ")
    a_temp = input("Enter Temperature: ")
    a_wt = input("Enter Weight: ")
    a_pr = input("Enter Pulse Rate: ")
    a_medical = input("Enter Medication/Treatment: ")
    a_diagnosis = input("Enter Diagnosis: ")
    a_casenumber_input.clear()
    a_casenumber_input.send_keys(a_casenumber)
    a_chief_complaint_input.clear()
    a_chief_complaint_input.send_keys(a_chief_complaint)
    a_historyillness_input.clear()
    a_historyillness_input.send_keys(a_historyillness)
    a_bp_input.clear()
    a_bp_input.send_keys(a_bp)
    a_physicalexam_input.clear()
    a_physicalexam_input.send_keys(a_physicalexam)
    a_medical_treatment_input.clear()
    a_medical_treatment_input.send_keys(a_medical)
    # a_date.send_keys("12/03/2023")
    a_rr_input.clear()
    a_rr_input.send_keys(a_rr)
    a_cr_input.clear()
    a_cr_input.send_keys(a_cr)
    a_temp_input.clear()
    a_temp_input.send_keys(a_temp)
    a_wt_input.clear()
    a_wt_input.send_keys(a_wt)
    a_pr_input.clear()
    a_pr_input.send_keys(a_pr)
    a_diagnosis_input.clear()
    a_diagnosis_input.send_keys(a_diagnosis)
    Add_Findings_button = driver.find_element(By.NAME, "submit")
    Add_Findings_button.click()
    wait = WebDriverWait(driver, 4)
    css_selector = "div.alert.alert-success.alert-dismissible.text-center"
    try:
        Adding_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))
        print(" OPD Findings Added!")
        print("Pass!")
        print('''

        ''')
        print('''
                                                       ADD USERS 
            ''')

        driver.get("http://localhost/patientrecords/addusercontrol/adduserview")
        a_user_input = driver.find_element(By.NAME, "a_user")
        a_pass_input = driver.find_element(By.NAME, "a_pass")
        a_fname_input = driver.find_element(By.NAME, "a_fname")
        a_fname = input("Enter First Name: ")
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        Confirm = input("Enter Confirm Password: ")
        a_user_input.send_keys(username)
        if(password==Confirm):
            a_pass_input.send_keys(password)
        else:
            print("            WARNING:-     PASSWORD DOES NOT MATCH GOOD BYE!!!!!")
            driver.quit()
        a_fname_input.send_keys(a_fname)
        Add_User_button = driver.find_element(By.NAME, "submit")
        Add_User_button.click()
        wait = WebDriverWait(driver, 4)
        css_selector = "div.alert.alert-danger.alert-dismissible.text-center"
        try:
            user_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))
            print(" User Registerd Successfull!")
            print("Pass!")
            driver.quit()
        except TimeoutException:
            print(" User Failed to be Registerd!")
            print("Failed!")
            driver.quit()
    except TimeoutException:
        print(" Failed To Adding OPD Findings!")
        print("Failed!")
        driver.quit()
except TimeoutException:
    print("Failed Patient Data to be Updated!")
    print("Failed!")
    driver.quit()


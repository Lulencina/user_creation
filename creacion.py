import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path="C:/Program Files/Google/Chrome/Application/chromedriver.exe", options=options)
driver.get("https://lavandanatural.com/")
driver.maximize_window()
time.sleep(3)

user1 = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[4]/div[1]/header/div/div[2]/div[2]/div[1]/a")
user1.click()
time.sleep(3)

create = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[4]/div[1]/header/div/div[2]/div[2]/div[1]/div/a[1]")
create.click()
time.sleep(3)

username = driver.find_element(By.ID, "name")
username.send_keys("Valeria Pérez")
username.send_keys(Keys.ENTER)
time.sleep(3)


requirement = ()     #Expected Result
labelObtained = ()      #Actual Result

def compareLabels():
    if requirement in labelObtained:
        print("Pass. El campo con el label EMAIL se visualiza correctamente")
    else:
        print("Fail. El campo con el label EMAIL NO se visualiza correctamente")



campoEmail = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div/div[3]/form/div[2]/label")   
#Aquí identificamos el elemento

labelCampoEmail =  driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div/div[3]/form/div[2]/label").text
#Aquí extraemos el texto dentro del elemento

labelObtained =labelCampoEmail

print(labelObtained)

requirement = 'EMAIL'

compareLabels()

email1 = driver.find_element(By.ID, "email")
email1.send_keys("valelu9@hotmail.com")
email1.send_keys(Keys.ENTER)
time.sleep(3)

passw = driver.find_element(By.ID, "password")
passw.send_keys("testing1")
passw.send_keys(Keys.ENTER)
time.sleep(3)

repeat_Pass = driver.find_element(By.ID, "password_confirmation")
repeat_Pass.send_keys("testing1")
repeat_Pass.send_keys(Keys.ENTER)
time.sleep(3)

captcha = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div/div[3]/form/div[6]/div/div/iframe")
captcha.click()
time.sleep(6)


button = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[5]/div/div[3]/form/input")
button.click()
time.sleep(3)


driver.close()
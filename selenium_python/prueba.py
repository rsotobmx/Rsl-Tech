from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, json

driver = webdriver.Firefox(executable_path="C:/firefox_webdriver/geckodriver.exe")

with open("mensajes.json") as json_file:
    data= json.load(json_file)

    for p in data["mensajes"]:

        print(p["nombre"]+ " is loading")
        driver.get("http://localhost:8080/")

        time.sleep(5)


        modalbtn = driver.find_element_by_id("btnmodal")
        modalbtn.click()
        
        username= driver.find_element_by_name("nombre")
        username.send_keys(p["nombre"])

        username= driver.find_element_by_name("email")
        username.send_keys(p["email"])

        username= driver.find_element_by_name("telefono")
        username.send_keys(p["telefono"])

        username= driver.find_element_by_name("mensaje")
        username.send_keys(p["mensaje"])
        
        time.sleep(3)

        btnenviar= driver.find_element_by_name("enviar")
        btnenviar.click()

        time.sleep(5)

driver.close()
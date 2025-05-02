from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


def exploratorio(driver,d_usuario="luisortegar99@gmail.com",d_contraseña="MkD7739g!Haj&99"):

    try:
        driver.get("https://www.occ.com.mx/candidatos/inicia-sesion/login/")
        time.sleep(2)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        html_pretty = soup.prettify()
        with open("occ_inicio.html", "w", encoding="utf-8") as f:
            f.write(html_pretty)

        #<input class="input-0-2-408" id="inputID_identifier" name="identifier" type="text" value="">
        usuario = driver.find_element(By.ID, "inputID_identifier")
        usuario.send_keys(d_usuario)

        #<input name="password" id="inputID_password" class="input-0-2-408 hasPass-0-2-414" type="password" value="">
        contraseña = driver.find_element(By.ID,"inputID_password")
        contraseña.send_keys(d_contraseña)
        contraseña.send_keys(Keys.RETURN)
        time.sleep(30)
        driver.quit()
        
    except:
        print("Se produjo un Error")
        driver.quit()
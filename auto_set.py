from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from time import sleep


def set_env():
    with open('./set_env_heroku/config.txt', 'r') as f:
        for i, line in enumerate(f):
            keys_value = line.strip().split('=')
            without_white_spaces = []
            without_white_spaces.append(keys_value[0].strip())
            without_white_spaces.append(keys_value[1].strip())
            print(without_white_spaces)
            Chrome_browser.implicitly_wait(20)
            if line.strip() == None:
                i -= 1
                continue

            if i == 0:
                Chrome_browser.find_element(
                    by=By.XPATH, value=f"/html/body/div[5]/main/div[2]/div[2]/ul/li[2]/div/div[2]/div/div/form/table/tbody/tr/td[1]/div/input").send_keys(without_white_spaces[0])
                Chrome_browser.find_element(
                    by=By.XPATH, value=f"/html/body/div[5]/main/div[2]/div[2]/ul/li[2]/div/div[2]/div/div/form/table/tbody/tr/td[2]/div/textarea").send_keys(without_white_spaces[1])

                Chrome_browser.find_element(
                    by=By.XPATH, value=f"/html/body/div[5]/main/div[2]/div[2]/ul/li[2]/div/div[2]/div/div/form/table/tbody/tr/td[3]/button").click()
                continue

            Chrome_browser.find_element(
                by=By.XPATH, value=f"/html/body/div[5]/main/div[2]/div[2]/ul/li[2]/div/div[2]/div/div/form/table/tbody/tr[{i+1}]/td[1]/div/input").send_keys(without_white_spaces[0])
            Chrome_browser.find_element(
                by=By.XPATH, value=f"/html/body/div[5]/main/div[2]/div[2]/ul/li[2]/div/div[2]/div/div/form/table/tbody/tr[{i+1}]/td[2]/div/textarea").send_keys(without_white_spaces[1])

            Chrome_browser.find_element(
                by=By.XPATH, value=f"/html/body/div[5]/main/div[2]/div[2]/ul/li[2]/div/div[2]/div/div/form/table/tbody/tr[{i+1}]/td[3]/button").click()


user = input("inserisci nome utente:  ")
password = input("inserisci password:  ")

options = Options()
ua = UserAgent()
userAgent = ua.random
options.add_argument(f'user-agent={userAgent}')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
Chrome_browser = webdriver.Chrome(options=options)


Chrome_browser.maximize_window()
Chrome_browser.get(
    "https://id.heroku.com/login")

WebDriverWait(Chrome_browser, 10).until(
    EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))).click()

WebDriverWait(Chrome_browser, 10).until(
    EC.presence_of_element_located((By.ID, "email"))).send_keys(user)

WebDriverWait(Chrome_browser, 10).until(
    EC.presence_of_element_located((By.ID, "password"))).send_keys(password)

WebDriverWait(Chrome_browser, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/form/button"))).click()

WebDriverWait(Chrome_browser, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/form[2]/button"))).click()

WebDriverWait(Chrome_browser, 15).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/main/div[2]/div[2]/div[3]/div[1]/a"))).click()

WebDriverWait(Chrome_browser, 15).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/main/div[2]/div[2]/nav/div/div[7]/a"))).click()

WebDriverWait(Chrome_browser, 15).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/main/div[2]/div[2]/ul/li[2]/div/div[2]/div/button"))).click()

set_env()

Chrome_browser.quit()

"/html/body/div[5]/main/div[2]/div[2]/ul/li[2]/div/div[2]/div/div/form/table/tbody/tr/td[1]/div/input"

# pip install selenium faker colorama requests

import random
from selenium import webdriver # pip install selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from faker import Faker
import time
import requests
import os
import traceback
import colorama
from colorama import Fore, Style, Back

def cls():
    os.system("cls") if os.name=='nt' else os.system("clear")

def title(nt):
    os.system(f"title {nt}")

cls()
title("The best roblox account generator.")
# colorama shit
colorama.init(autoreset=True)

# Define color variables
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN
WHITE = Fore.WHITE
RESET = Style.RESET_ALL
BRIGHT = Style.BRIGHT
DIM = Style.DIM
BG_RED = Back.RED
BG_GREEN = Back.GREEN
BG_YELLOW = Back.YELLOW
BG_BLUE = Back.BLUE
BG_MAGENTA = Back.MAGENTA
BG_CYAN = Back.CYAN
BG_WHITE = Back.WHITE

# proxy list updater
updateornah = input(f"{CYAN}[?] Update Proxy list? [y/(n)]: {WHITE}").strip().lower() or 'n'
if updateornah.startswith('y'):
    upd = True
else:
    upd = False

cls()

if upd:
    print(f"{YELLOW}[~] Attempting to update...")
    os.system("scraper.py")
    
else:
    print(f"{RED}[!] Going without updating proxy.")

time.sleep(3)
cls()


fake = Faker() # make user/pass generator instance.
               # pip install faker
               

    
cls()

logo = """
 _ __         _       
' )  )    /  //       
 /--' __ /__// __ _., 
/  \_(_)/_)</_(_)/ /\_
   __                       
  /  )                   _/_
 /--/ _. _. __ . . ____  /  
/  (_(__(__(_)(_/_/ / <_<__ 
_________                              _____              
__  ____/_____________________________ __  /______________
_  / __ _  _ \_  __ \  _ \_  ___/  __ `/  __/  __ \_  ___/
/ /_/ / /  __/  / / /  __/  /   / /_/ // /_ / /_/ /  /    
\____/  \___//_/ /_/\___//_/    \__,_/ \__/ \____//_/     
                    -- by kz0x1 --                                      
        THE BEST account generator for Roblox  
            
"""

print(f"{GREEN}{logo}\n{WHITE}")
print(f"{RED}[!] WARNING: PROXY MODE IS VERY UNSTABLE.")
proxinp = input(f"{YELLOW}[?] Use Proxy? [(y)/n]: {WHITE}").strip().lower() or 'y'
if proxinp.startswith('y'):
    proxyyesno = True
    print(f"{GREEN}[~] Proxy enabled.")
else:
    proxyyesno = False
    print(f"{RED}[!] Continuing without proxy.")

PROXY_MODE = proxyyesno

def fetch_proxies_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            proxies = file.readlines()
            # Filter proxies with port 8080
            proxies = [proxy.strip() for proxy in proxies if proxy.strip().endswith(':8080')]
        return proxies
    except Exception as e:
        print(f"{RED}[!] Error reading proxies from file: {e}")
        return []

def create_driver_with_proxy(proxy=None):
    options = Options()
    if PROXY_MODE and proxy:
        options.add_argument(f'--proxy-server={proxy}')
    driver = webdriver.Chrome(service=Service(r".\chromedriver.exe"), options=options)
    return driver

def generate_random_username():
    return fake.user_name() + str(random.randint(1000, 99999))

def generate_random_password():
    return fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)

def save_account_info(username, password):
    with open("generated.txt", "a") as file:
        file.write(f"{username}:{password}\n")
    print(f"{GREEN}[+] Account info saved: {username}:{password}")

def get_random_proxy(proxies):
    return random.choice(proxies) if proxies else None

def create_account_with_retry(proxies):
    attempts = 10
    for attempt in range(attempts):
        proxy = get_random_proxy(proxies) if PROXY_MODE else None
        if PROXY_MODE and not proxy:
            print(f"{RED}[!] No proxies available. Exiting.")
            break
        
        print(f"{YELLOW}[~] Attempting to use proxy: {proxy}" if proxy else f"{YELLOW}[~] Attempting without proxy.")

        try:
            driver = create_driver_with_proxy(proxy)
            driver.get("https://www.roblox.com/CreateAccount")

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "MonthDropdown"))
            )

            month_dropdown = Select(driver.find_element(By.ID, "MonthDropdown"))
            random_value = random.randint(1, 12)
            month_dropdown.select_by_index(random_value)

            day_dropdown = Select(driver.find_element(By.ID, "DayDropdown"))
            day_dropdown.select_by_index(random_value)

            year_dropdown = Select(driver.find_element(By.ID, "YearDropdown"))
            year_dropdown.select_by_value(str(random.randint(1980, 2000)))

            time.sleep(2)

            username = generate_random_username()
            username_field = driver.find_element(By.ID, "signup-username")
            username_field.send_keys(username)

            password = generate_random_password()
            password_field = driver.find_element(By.ID, "signup-password")
            password_field.send_keys(password)

            male_button = driver.find_element(By.ID, "MaleButton")
            male_button.click()

            print(f"{GREEN}[+] Successfully filled out the form!")

            time.sleep(2)

            sign_up_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign Up']"))
            )
            sign_up_button.click()

            save_account_info(username, password)
            print(f"{YELLOW}[!] Account created successfully! [Please solve any captcha! We are working to automate captcha solving.]")

            time.sleep(9e9)
            driver.quit()

            break

        except Exception as e:
            print(f"{RED}[!] Error on attempt {attempt + 1}: {e}")
            traceback.print_exc()
            driver.quit()
            if attempt < attempts - 1:
                print(f"{YELLOW}[~] Retrying with another proxy..." if PROXY_MODE else "Retrying...")
                continue
            else:
                print(f"{RED}[-] All attempts failed. Exiting.")
                time.sleep(5)
                break

proxies = fetch_proxies_from_file("proxy.txt")

create_account_with_retry(proxies)

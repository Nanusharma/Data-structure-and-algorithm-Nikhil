from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
import string
import random
import time
from contextlib import contextmanager

def generate_passwords(count, length=15):
    chars = string.ascii_letters + string.digits + string.punctuation
    return [''.join(random.choices(chars, k=length)) for _ in range(count)]

@contextmanager
def create_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Edge(options=options)
    try:
        yield driver
    finally:
        driver.quit()

def perform_search(driver, query):
    driver.execute_script("window.open('https://www.bing.com/');")
    driver.switch_to.window(driver.window_handles[-1])
    
    try:
        search_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_field.send_keys(query)
        search_field.submit()
        
        time.sleep(random.uniform(4, 10))
    
    finally:
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

def main():
    search_strings = generate_passwords(34)
    
    with create_driver() as driver:
        driver.get('https://www.bing.com')
        
        for query in search_strings:
            perform_search(driver, query)

if __name__ == "__main__":
    main()






# #<input id="sb_form_q" class="sb_form_q" name="q" type="search" maxle ngth="1000" autocomplete="off" aria-labelledby="sb_form_c" autofocus aria-controls="sw_as" aria-autocomplete="both" aria-owns="sw_as" spellcheck="false" data-ms-editor="true" data-bm="41" aria-activedescendant="sa_5031">
# import time
# from selenium import webdriver
# import string
# import random
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium. webdriver.edge.service import Service as EdgeService


# def generate_password():
  
#   characters = string.ascii_letters + string.digits + string.punctuation

  
#   password = ''.join(random.choices(characters, k=15))
#   return password


# driver = webdriver.Edge()
# driver.get('https://www.bing.com')


# strings = [] 
# for i in range(34):
#   strings.append(generate_password())


# original_handle = driver.current_window_handle

# for string in strings:
  
#   driver.execute_script("window.open('https://www.bing.com/');")

  
#   driver.switch_to.window(driver.window_handles[-1])

 
#   search_fields = driver.find_elements("name", "q")

  
#   for search_field in search_fields:
#     search_field.send_keys(string)

 
#   for search_field in search_fields:
#     search_field.submit()

  
#   #time.sleep(4)
#   sleep_duration = random.uniform(4, 10)
#   time.sleep(sleep_duration)

  
#   driver.close()

  
#   driver.switch_to.window(original_handle)

# # Close the web driver
# driver.quit()

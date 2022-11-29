from selenium import webdriver
from selenium.webdriver.common.by import By

url1 = "https://www.humblebundle.com/"
url2 = "https://www.nautiljon.com/"
url3 = "https://www.youtube.com/"

def get_title(driver, url, i):
    driver.set_window_size(1600, 1200)
    driver.get(url)
    
    driver.implicitly_wait(2)
    title = driver.title
    print(f"Titre récupéré n°{i}: {title}")
    
    return title

def create_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    return webdriver.Chrome(
        options=chrome_options
    )



driver = create_chrome_driver()
    
url_list = [url1, url2, url3]
title_list = []
    
for url in url_list:
    title = get_title(driver, url, url_list.index(url)+1)
    title_list.append(title)
    
driver.quit()
    
print(f"Voici le titre le plus long : '{max(title_list, key=len)}'")

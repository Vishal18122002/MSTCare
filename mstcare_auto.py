def mstcare_auto():
    import os
    import time
    import json
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    options=webdriver.ChromeOptions()
    driver=webdriver.Chrome(options=options)

    with open("/Users/vishal/PycharmProjects/MSTSOFT/Fiserv_model/Pages/Mstcare/p101454.json","r") as file:
        data = json.load(file)

    html_path="file://"+ "/Users/vishal/PycharmProjects/MSTSOFT/Fiserv_model/Pages/Mstcare/login.html"
    driver.get(html_path)
    driver.fullscreen_window()

    time.sleep(2)

    driver.find_element(By.ID,"email").send_keys("vishal@mstcare.com")

    driver.find_element(By.ID,"password").send_keys("vishal@mstcare.com")

    time.sleep(1)

    driver.find_element(By.ID,"next").click()
    driver.fullscreen_window()
    time.sleep(2)
    driver.find_element(By.ID,"hover_2").click()
    time.sleep(1)
    driver.find_element(By.ID,"edit_2").click()
    time.sleep(2)
    general_2=driver.find_element(By.ID,"nav_general_2")
    general_2.click()
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'start' });", general_2)

    time.sleep(2)
    driver.find_element(By.ID,"auth_2").click()
    driver.fullscreen_window()
    time.sleep(2)

    driver.find_element(By.ID,"id").send_keys("1892-healthcare")
    driver.find_element(By.ID,"pass").send_keys("jdbqe3uj12")

    time.sleep(1)
    driver.find_element(By.ID,"next").click()

    driver.fullscreen_window()
    time.sleep(2)
    driver.find_element(By.ID,"auth").click()
    time.sleep(2)
    driver.find_element(By.ID,"searchbar").send_keys("P01370")
    time.sleep(0.5)
    driver.find_element(By.ID,"search").click()
    time.sleep(2)
    driver.find_element(By.ID,"pop").click()
    time.sleep(3)

    driver.get("file://"+"/Users/vishal/PycharmProjects/MSTSOFT/Fiserv_model/Pages/Mstcare/menu.html")
    driver.fullscreen_window()

    time.sleep(2)

    driver.find_element(By.ID,"hover").click()
    time.sleep(1)
    driver.find_element(By.ID,"edit").click()
    time.sleep(2)
    general=driver.find_element(By.ID,"nav_general")
    general.click()
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'start' });", general)
    time.sleep(2)
    driver.find_element(By.ID,"auth").click()
    driver.fullscreen_window()
    time.sleep(2)

    driver.find_element(By.ID,"id").send_keys("1892-healthcare")
    driver.find_element(By.ID,"pass").send_keys("jdbqe3uj12")

    time.sleep(1)
    driver.find_element(By.ID,"next").click()

    driver.fullscreen_window()
    time.sleep(2)
    driver.find_element(By.ID,"auth").click()
    time.sleep(2)
    driver.find_element(By.ID,"searchbar").send_keys("P01454")
    time.sleep(0.5)
    driver.find_element(By.ID,"search").click()
    time.sleep(2)
    driver.find_element(By.ID,"next").click()
    time.sleep(2)

    for key,value in data.items():
        if value ==True:
            driver.find_element(By.ID,key).click()
        else:
            driver.find_element(By.ID, key).send_keys(value)
        time.sleep(0.2)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.find_element(By.ID,"submit").click()
    time.sleep(5)




    driver.quit()



mstcare_auto()
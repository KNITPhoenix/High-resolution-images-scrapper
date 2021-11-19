#author:Shubham Pandey
#script for scrapping high resolution images from google
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import time
import os
import requests
import glob

fruits=["Lemon","Orange","Peach","Pears","Plums","tomato","Watermelons"]
category=["farm stand","farmer's market","fruit selling stand","fruit stand","market","market stand"]

#scrapping for images
for n in fruits:
    counter = 0
    for j in category:
        inp=n+" "+j    #what to search
        print("opening goole images with the given query")
        url="https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q="+inp+"&oq="+inp+"&gs_l=img"
        #url = "https://www.google.com/search?q="+inp+"&tbm=isch"   #constructing the url
        driver=webdriver.Chrome('C:/Users/spandey8/Downloads/chromedriver3.exe')
        header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
        driver.get(url)
        save_directory="C:/Users/spandey8/Desktop/CEDAR CUBS/task 1/scrape_attempt/"
        path = save_directory + n + "/"
        if not os.path.exists(path):
            os.mkdir(path)
        for _ in range(500):
            driver.execute_script("window.scrollBy(0,10000)")
        for i in driver.find_elements_by_css_selector("img.Q4LuWd"):
            hover = ActionChains(driver).move_to_element(i)
            action = ActionChains(driver)
            action.send_keys_to_element(i,Keys.RETURN).perform()
            time.sleep(1)
            try:
                path = save_directory + n + "/"
                img=driver.find_elements_by_css_selector("img.n3VNCb")[1].get_attribute("src")
                print(img)
                counter += 1
                new_filename = str(counter) + ".jpg"
                path += new_filename
                r=requests.get(img)
                open(path,'wb').write(r.content)
            except Exception as e:
                pass
        driver.close()

#removing all images less than 25kb
for n in fruits:
    path=save_directory+n+"/*"
    for i in glob.glob(path):
        if((os.path.getsize(i)/1024)<25):
            os.remove(i)
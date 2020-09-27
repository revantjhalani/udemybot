from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
#from selenium.webdriver.firefox.webdriver import FirefoxProfile
#profile = FirefoxProfile("/home/sotpurk/.mozilla/firefox/xxdnr3qf.selenium")
driver = webdriver.Chrome('chromedriver')
driver.set_window_size(1900,1000)
links = []
email = 'email'
password = 'password'
pagelink = "https://tutsnode.net/?s=hello"
def init():
    global email
    global password
    driver.get('https://www.udemy.com/join/login-popup/')
    time.sleep(3)
    emailsend = driver.find_element_by_xpath("//input[@name='email']")
    passwordsend = driver.find_element_by_xpath("//input[@name='password']")
    passwordsend.clear()
    emailsend.clear()
    emailsend.send_keys(email)
    passwordsend.send_keys(password)
    passwordsend.send_keys(Keys.RETURN)
    time.sleep(6)

def olink(link):
    global links
    driver.get(link)
    elements = driver.find_elements_by_css_selector("div.title h3 a")

    for element in elements:
        s = element.text
        try:
            m = re.match(r"[^[]*\[([^]]*)\]", s).groups()[0]
            #print(m)
        except: m = ''
        
        if m == '100% off': #to be changed 
            #print(element.text) 
            links.append(element.get_attribute("href"))
    



olink(pagelink)
pages = driver.find_element_by_css_selector("a[class='page-numbers']").text
for page in range(int(pages)-1) :
    #print(page)
    time.sleep(1)
    olink(driver.find_element_by_css_selector("a[class='next page-numbers']").get_attribute('href'))




ulinks = []
#print(links)
for link in links:
    if link.find('https://tutsnode.net/about/') == -1:
            
        driver.get(link)
        time.sleep(1)
        ulink = driver.find_element_by_xpath('//a[@rel="noopener"]').get_attribute('href')
        #print(ulink)
        ulinks.append(ulink)
init()

failed_links = []
print("Total Udemy Links fetched: " + str(len(ulinks)) )
for link in ulinks:
    driver.get(link)
    time.sleep(3)
    #try:driver.find_element_by_class_name("add-to-cart").click()
    #except:
    #    failed_links.append(link)
         
    try: driver.find_element_by_xpath('//button[@data-purpose="dismiss"]').click()
    except: pass
    #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "add-to-cart")))
    try:driver.find_element_by_class_name("add-to-cart").click()
    except: failed_links.append(link)

    time.sleep(2)
print("Failed:  ")
for flinks in failed_links:
    print(flinks)
#driver.quit()

# Before you use these codes, install selenium into your laptop using python. In your terminal, type "python3 pip -m install selenium" or "python3 pip install selenium" or "pip install selenium". For windows, type "python pip install selenium" or "pip install selenium". If it says installation successful, great! You are good to go
# If pip install did not work, try to troubleshoot on google, there are many resources out there that can help you with this issue
# Next, you have to install chromedriver on your laptop so that you can allow selenium to control chrome. Go to https://chromedriver.chromium.org/downloads and download your version of chrome
# Lastly, look for your chromedriver file in downloads and copy its location (it should look like Users/name/Downloads/chromedriver) and insert the location into the first variable


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Paste Chromedriver location below
Chromedriverlocation = 
# Insert the title of the book
Book = 


browser = webdriver.Chrome(Chromedriverlocation)
browser.get('https://www.bookdepository.com/')
try:
    search = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.NAME, "searchTerm"))
    )
    search.send_keys(Book)
    search.send_keys(Keys.ENTER)
except:
    time.sleep(1)

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[1])
browser.get('https://bookshop.org/')
try:
    search1 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "keywords"))
    )
    search1.send_keys(Book)
    search1.send_keys(Keys.ENTER)
except:
    time.sleep(1)

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[2])
browser.get('https://www.textbookrush.com/')
try:
    search2 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "txtHeaderSearch"))
    )
    search2.send_keys(Book)
    search2.send_keys(Keys.ENTER)
except:
    time.sleep(1)

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[3])
browser.get('https://www.barnesandnoble.com/')
try:
    search3 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="rhf_header_element"]/nav/div/div[3]/form/div/div[2]/div/input[1]'))
    )
    search3.send_keys(Book)
    search3.send_keys(Keys.ENTER)
except:
    time.sleep(1)

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[4])
browser.get('https://www.textbooks.com/')
try:
    search4 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='mftTxt']"))
    )
    search4.send_keys(Book)
    search4.send_keys(Keys.ENTER)
except:
    time.sleep(1)

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[5])
browser.get('https://booksrun.com/')
try:
    search5 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='main-search-form']/div/input"))
    )
    search5.send_keys(Book)
    search5.send_keys(Keys.ENTER)
except:
    time.sleep(1)

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[6])
browser.get('https://www.chegg.com/')
try:
    search6 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "chegg-searchbox"))
    )
    search6.send_keys(Book)
    search6.send_keys(Keys.ENTER)
except:
    time.sleep(1)

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[7])
browser.get('https://www.walmart.com/')
try:
    search7 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "global-search-input"))
    )
    search7.send_keys(Book)
    search7.send_keys(Keys.ENTER)
except:
    time.sleep(1)

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[8])
browser.get('https://www.facebook.com/marketplace/?ref=bookmark')
try:
    search8 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='mount_0_0_/9']/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/span/div/div/div/div/label/input"))
    )
    search8.send_keys(Book)
    search8.send_keys(Keys.ENTER)
except:
    time.sleep(1)

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[9])
browser.get('https://www.booksamillion.com/?id=7857917387282')
try:
    search9 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "query"))
    )
    search9.send_keys(Book)
    search9.send_keys(Keys.ENTER)
except:
    time.sleep(1)

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[10])
browser.get('https://www.biblio.com/')
try:
    search10 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "top-search"))
    )
    search10.send_keys(Book)
    search10.send_keys(Keys.ENTER)
except:
    time.sleep(1)

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[11])
browser.get('https://www.strandbooks.com/')
try:
    search11 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "search"))
    )
    search11.send_keys(Book)
    search11.send_keys(Keys.ENTER)
except:
    time.sleep(1)

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[12])
browser.get('https://www.alibris.com/')
try:
    search12 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "searchBox"))
    )
    search12.send_keys(Book)
    search12.send_keys(Keys.ENTER)
except:
    time.sleep(1)

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[13])
browser.get('https://www.valorebooks.com/')
try:
    search13 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "search-typeahead-in-page"))
    )
    search13.send_keys(Book)
    search13.send_keys(Keys.ENTER)
except:
    time.sleep(1)

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[14])
browser.get('https://www.powells.com/')
try:
    search14 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "keyword"))
    )
    search14.send_keys(Book)
    search14.send_keys(Keys.ENTER)
except:
    time.sleep(1)

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[15])
browser.get('https://www.thriftbooks.com/')
try:
    search16 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='GlobalSearch']/div/input"))
    )
    time.sleep(2)
    search16.send_keys(Book)
    time.sleep(2)
    search16.send_keys(Keys.ENTER)
except:
    time.sleep(1)

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[16])
browser.get('https://www.abebooks.com/?cm_sp=TopNav-_-PLP-_-Logo')
try:
    search17 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "header-searchbox-input"))
    )
    search17.send_keys(Book)
    search17.send_keys(Keys.ENTER)
except:
    time.sleep(1)

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[17])
browser.get('https://www.ebay.com/')
try:
    search18 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "gh-ac"))
    )
    search18.send_keys(Book)
    search18.send_keys(Keys.ENTER)
except:
    time.sleep(1)

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[18])
browser.get('https://www.amazon.com/ref=nav_logo')
try:
    search19 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search19.send_keys(Book)
    search19.send_keys(Keys.ENTER)
except:
    time.sleep(1)

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[19])
browser.get('https://www.betterworldbooks.com/')
try:
    search15 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "form-control input-lg nav-search-box aa-input"))
    )
    search15.send_keys(Book)
    search15.send_keys(Keys.ENTER)
except:
    time.sleep(1)

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[20])
browser.get('https://www.hpb.com/home?&size=25&#product-panel-home')
try:
    search15 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "keywords"))
    )
    search15.send_keys(Book)
    search15.send_keys(Keys.ENTER)
except:
    time.sleep(1)

browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[21])
browser.get('https://www.target.com/')
try:
    search15 = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "search"))
    )
    search15.send_keys(Book)
    search15.send_keys(Keys.ENTER)
except:
    time.sleep(1)


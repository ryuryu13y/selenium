from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
PROXY_IP = ("zproxy.lum-superproxy.io:22225" )

options = webdriver.ChromeOptions()
#options.add_argument("--proxy-server=%s" % PROXY_IP)
options.add_extension('./crx/twitter.crx')
driver = webdriver.Chrome(executable_path="./chromedriver.exe",chrome_options=options)

mail=("ryuryu13y+1@gmail.com")
pw=("ryusei13")

driver.get("https://lobi.co/signin?back=https%3A%2F%2Fweb.lobi.co%2F")

driver.find_element_by_xpath("//*[@id='input--email']").send_keys(mail)

driver.find_element_by_xpath("//*[@id='input--password']").send_keys(pw)

driver.find_element_by_class_name("button button--primary").click()

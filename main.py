from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
PROXY_IP = ("zproxy.lum-superproxy.io:22225" )

options = webdriver.ChromeOptions()
#options.add_argument("--proxy-server=%s" % PROXY_IP)
options.add_extension('./crx/twitter.crx')
driver = webdriver.Chrome(executable_path="./chromedriver.exe",chrome_options=options)

"""
print("プロキシ設定")
driver.get("chrome-extension://enhldmjbphoeibbpdhmjkchohnidgnah/options.html");
driver.findElement(By.id("url")).sendKeys(url);
driver.findElement(By.id("username")).sendKeys(username);
driver.findElement(By.id("password")).sendKeys(password);
driver.findElement(By.className("credential-form-submit")).click();
"""
driver.get("https://twitter.com")
a=input("a")
driver.get("https://twitter.com/search?f=tweets&vertical=default&q=%E3%82%AA%E3%83%BC%E3%83%96%E5%9E%A2&src=typd")

"""In order to make an infinite scrool through Javascript"""
lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
lenOfPage.click()

elements = driver.find_elements_by_css_selector(".ProfileTweet-actionButton.js-actionButton.js-actionFavorite")
elements.click()

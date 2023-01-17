from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

PATH = r"C:\Users\jjmik\Desktop\Coding Practice\Selenium python\chromedriver_win32 (2)\chromedriver.exe"

def try_until_done(command):
    while True:
        try:
            command
            break
        except:
            continue

class getTiktokUrls(webdriver.Chrome):

    def search_keyword(self, keyword):
        time.sleep(2)
        INXPATH = r'//*[@id="app"]/div[2]/div/div[1]/div/form/input'
        VIDEOS_XPATH = r'//*[@id="tabs-0-tab-search_video"]'
        FIRST_VID_X = r'//*[@id="app"]/div[3]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/div'
        SEARCH_BUTTON = r'//*[@id="app"]/div[2]/div/div[1]/div/form/button'
        ADD_MORE_VID = r'//*[@id="app"]/div[3]/div[2]/div[2]/div[2]/button'
    
        try_until_done(self.find_element(By.XPATH, INXPATH).send_keys(keyword))
        #input_field.send_keys(keyword)
        time.sleep(2)
        try_until_done(self.find_element(By.XPATH, SEARCH_BUTTON).click())
        time.sleep(6)
        try_until_done(self.find_element(By.XPATH, VIDEOS_XPATH).click())
        time.sleep(15)
        #try_until_done(self.find_element(By.XPATH, FIRST_VID_X).click())
        time.sleep(2)
        for _ in range(5):
            self.find_element(By.XPATH, ADD_MORE_VID).click()
            time.sleep(3)
        self.find_element(By.XPATH, FIRST_VID_X).click()
        time.sleep(8)


    def get_next_url(self):
        LOWER_XPATH = '//*[@id="app"]/div[3]/div[2]/div[2]/div[3]/div[1]/button[3]'
        last_url = self.current_url
        with open('currenturls.txt', 'a') as fd:
            fd.write(f'\n{last_url}')
        self.find_element(By.XPATH, LOWER_XPATH).click()
        time.sleep(7)


def main():
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    #browser = webdriver.Chrome(chrome_options=chrome_options)
    browser = getTiktokUrls(executable_path=PATH, chrome_options=chrome_options)
    browser.get("https://www.tiktok.com/")
    browser.search_keyword("World Cup")
    for _ in range(3):
        browser.get_next_url()
    #browser.get(r"https://www.tiktok.com/")
    #time.sleep(3)
    #for i in range(10):
    #    browser.get_next_url()

if __name__ == "__main__":
    main()
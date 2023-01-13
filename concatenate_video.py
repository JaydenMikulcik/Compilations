import glob
#import os.path
import os
from moviepy.editor import *
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
#import moviepy

PATH = r"C:\Users\jjmik\Downloads\chromedriver_win32 (1)\chromedriver.exe"
DOWNLOAD_PATH = r"C:\Users\jjmik\Downloads"
VIDEO_PATH = r"C:\Users\jjmik\Videos\CompilationVideos\VideosFolder"
TEST_URL = r"https://www.tiktok.com/@kagiristwins/video/7167763239156272390?is_copy_url=1&is_from_webapp=v1"

chrome_options = webdriver.ChromeOptions()

#prefs = {'profile.default_content_setting_values.automatic_downloads': 1}
#chrome_options.add_experimental_option("prefs", prefs)
#driver = webdriver.Chrome(options = chrome_options)

"""
import glob
import os.path
"""


class concat_video(webdriver.Chrome):

    
    def download_from_url(self, url):

        URL_PATH = r'//*[@id="url"]'
        SUBMIT_PATH = r'//*[@id="hero"]/div/div[2]/form/div/div[4]/button'
        DOWNLOAD_BUTTON = r'//*[@id="download"]/div/div/div[2]/div/a[1]'

        self.get('https://snaptik.app/en')
        time.sleep(4)
        self.find_element(By.XPATH, URL_PATH).send_keys(url)
        time.sleep(3)
        #submit_button = self.find_element(By.XPATH, SUBMIT_PATH)
        #print(submit_button.text)
        #submit_button.click()
        #TODO make it so only do when on new page
        time.sleep(6)
            
        while True:
            try:
                new_download_button = self.find_element(By.XPATH, DOWNLOAD_BUTTON)
                print(new_download_button.text)
                new_download_button.click()
                time.sleep(4)
                break
            except:
                continue
        #move_latest_video()

        time.sleep(15)


def move_latest_video():
    folder_path = DOWNLOAD_PATH
    file_type = r'\*.mp4'
    files = glob.glob(folder_path + file_type)
    max_file = max(files, key=os.path.getctime)
    max_file_list = max_file.split('\\')
    print(max_file)

    os.rename(max_file, os.path.join(VIDEO_PATH, max_file_list[-1]))

def concat_all_from_directory():
    clip_path = r"C:\Users\jjmik\Videos\CompilationVideos\VideosFolder"
    video_list = []
    for file in os.listdir("VideosFolder"):
        if file.endswith(".mp4"):
            file_path = os.path.join(clip_path, file)
            clip = VideoFileClip(file_path)
            video_list.append(clip)
    
    print(video_list)
    final_concat = concatenate_videoclips(video_list)
    final_concat.write_videofile("final_comp.mp4")
    #final_concat.ipython_display(width = 480)


def main():
    #concat_all_from_directory()
    #move_latest_video()
    #move_latest_video()
    #concat_all_from_directory()
    #return
    
    prefs = {'profile.default_content_setting_values.automatic_downloads': 1}
    chrome_options.add_experimental_option("prefs", prefs)
    #driver = webdriver.Chrome(options = chrome_options)

    browser = concat_video(executable_path=PATH, options=chrome_options)
    browser.get('https://snaptik.app/en')
    browser.download_from_url(TEST_URL)
    #browser.download_from_url(TEST_URL)
    #with open('currenturls.txt') as topo_file:
    #    for line in topo_file:
    #        if line != "\n":
    #            print(line) 


if __name__ == "__main__":
    main()


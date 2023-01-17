import os
import glob
import time
from selenium.webdriver.chrome.options import Options


import concatenate_video
import geturls

PATH = r"C:\Users\jjmik\Desktop\Coding Practice\Selenium python\chromedriver_win32 (2)\chromedriver.exe"
VIDEOS_PATH = r"C:\Users\jjmik\Videos\CompilationVideos\VideosFolder"


def main():
    #Reseting the enviorment
    open('currenturls.txt', 'w').close()
    for f in os.listdir(VIDEOS_PATH):
        os.remove(os.path.join(VIDEOS_PATH, f))
    if os.path.exists("final_comp.mp4"):
        os.remove("final_comp.mp4")
    return
    
    #Starting to get the urls to use
    chrome_options = Options()
    
    comp_word = input("Enter the Keyword for Compilation: ")
    
    chrome_options.add_argument("--disable-notifications")

    tiktokBrowser = geturls.getTiktokUrls(executable_path=PATH, chrome_options=chrome_options)
    tiktokBrowser.get("https://www.tiktok.com/")
    tiktokBrowser.search_keyword(comp_word)
    for _ in range(20):
        tiktokBrowser.get_next_url()
    tiktokBrowser.quit()
    

    #Starting to download the videos
    prefs = {'profile.default_content_setting_values.automatic_downloads': 1}
    chrome_options.add_experimental_option("prefs", prefs)
    #driver = webdriver.Chrome(options = chrome_options)

    downloadBrowser = concatenate_video.concat_video(executable_path=PATH, options=chrome_options)
    downloadBrowser.get('https://snaptik.app/en')
    
    with open('currenturls.txt') as topo_file:
        for url in topo_file:
            if url != "\n":
                downloadBrowser.download_from_url(url)
                concatenate_video.move_latest_video()

    downloadBrowser.quit()
    
    # Concatenating all the videos in the VideosFolder directiory
    concatenate_video.concat_all_from_directory()


if __name__ == "__main__":
    main()
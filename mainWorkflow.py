import time
from selenium.webdriver.chrome.options import Options


import concatenate_video
import geturls

PATH = r"C:\Users\jjmik\Downloads\chromedriver_win32 (1)\chromedriver.exe"


def main():
    chrome_options = Options()
    """
    comp_word = input("Enter the Keyword for Compilation: ")
    
    chrome_options.add_argument("--disable-notifications")

    tiktokBrowser = geturls.getTiktokUrls(executable_path=PATH, chrome_options=chrome_options)
    tiktokBrowser.get("https://www.tiktok.com/")
    tiktokBrowser.search_keyword(comp_word)
    for _ in range(2):
        tiktokBrowser.get_next_url()
    tiktokBrowser.quit()
    """


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
    concatenate_video.concat_all_from_directory()


if __name__ == "__main__":
    main()
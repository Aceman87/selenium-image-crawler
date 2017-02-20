import time
from crawler.BaseCrawler import BaseCrawler
from selenium import webdriver

class BingCrawler(BaseCrawler):

    def __init__(self, search_key='', **kwargs):
        super().__init__(search_key, **kwargs)

        # google search specific url parameters
        self.search_url_prefix = kwargs.get('search_url_prefix', 'https://www.bing.com/images/search?q=')
        self.search_url_postfix = kwargs.get('search_url_postfix', '')

        # show more options
        # options : 'id','class'
        self.show_more_find_type = kwargs.get('show_more_find_type', 'class')
        self.show_more_find_value = kwargs.get('show_more_find_value', 'expandButton')

        # image options
        self.preview_image_class = kwargs.get('preview_image_class', 'mimg')
        self.original_image_class = kwargs.get('original_image_class', 'iusc')

    def create_selenium_driver(self):
        driver = webdriver.Firefox()
        return driver

    def extract_pic_url(self, driver):
        """ extract all the raw pic url in list
        """
        original_tag_list = driver.find_elements_by_class_name(self.original_image_class)
        # original image

        for tag in original_tag_list:
            original_image_url = tag.get_attribute('href')
            preview_image_url = tag.find_element_by_class_name(self.preview_image_class).get_attribute('src')
            self.pic_url_list.append((preview_image_url, original_image_url))
        driver.quit()

    def load_page(self, driver):
        driver.get(self.target_url_str)
        try:
            doc_height = driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            # save a screenshot for debug
            #driver.save_screenshot('out.png')
            counter = 0
            while True:
                doc_height_new = driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                button_load_rest = driver.find_element_by_class_name(self.show_more_find_value)
                if button_load_rest and button_load_rest.is_displayed():
                    button_load_rest.click()
                    time.sleep(0.5)
                    doc_height_new = driver.execute_script(
                        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                if doc_height == doc_height_new:
                    button_load_rest = driver.find_element_by_class_name(self.show_more_find_value)
                    if button_load_rest is None:
                        break
                    else:
                        counter += 1
                        if counter > 10:
                            break
                else:
                    doc_height = doc_height_new
                    counter = 0
                time.sleep(0.1)

        except Exception as e:
            print(e)

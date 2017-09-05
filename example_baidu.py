#!/usr/bin/env python3
from crawler.BaiduCrawler import BaiduCrawler
from processor.LogProcessor import LogProcessor
from processor.DownloadProcessor import DownloadProcessor

if __name__ == '__main__':

    options = {
        # defines the directory where the images and the log will be saved
        'output_directory':  "./images"
    }
    w = BaiduCrawler(search_key='Apple')
    # w.append_processor(LogProcessor())
    w.append_processor(DownloadProcessor(output_directory=options['output_directory'], process_count=16))
    w.run()

#!/usr/bin/env python3
from crawler.GoogleCrawler import GoogleCrawler
from processor.LogProcessor import LogProcessor
from processor.DownloadProcessor import DownloadProcessor
from processor.ElasticSearchProcessor import ElasticSearchProcessor

if __name__ == '__main__':

    options = {
        # defines the directory where the images and the log will be saved
        'output_directory':  "./images"
    }
    w = GoogleCrawler(search_key='Apple')
    w.append_processor(LogProcessor())
    w.append_processor(DownloadProcessor(output_directory=options['output_directory']))
    # w.append_processor(ElasticSearchProcessor())
    w.run()

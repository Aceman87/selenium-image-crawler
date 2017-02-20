# selenium-image-crawler
Selenium Image Crawler

Reference source code : https://simply-python.com/2015/05/18/saving-images-from-google-search-using-selenium-and-python/

## Notes
* You need to install [PhantomJS](http://phantomjs.org/) headless browser and add the PhantomJS Executable to path.

## Features
* Google Image Searh and Yandex Image Search included
* BaseCrawler supplied for other search engines or websites
* GoogleCrawler and YandexCrawler extended from BaseCrawler
* BaseProcessor supplied for processing of each search item
* LogProcessor, DownloadProcessor and ElasticSearchProcessor extended from BaseProcessor
* DownloadProcessor, ElasticSearchProcessor : Pool class is used from multiprocessing library for parallelizing download
* example_*.py files are included for simple usage

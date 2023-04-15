
import json
import urllib.request
import os
import re
from selenium import webdriver

'''
This script extracts all URLs of JavaScript files from a given HAR file and saves them in a new folder. It also displays the list of JS files and their count.
To download the JS files, it uses a regular expression to filter out URLs that match the specified file format and downloads them using urllib.request.
In addition, it uses Selenium to loop through the URLs and download the files. The download status is displayed for each file.

A HAR (HTTP Archive) file is a log of all network requests made by a browser when loading a web page.
It contains detailed information such as the URL, request method, response status, headers, and timings.
Saving a HAR file can help in analyzing network performance, troubleshooting issues, and optimizing website performance.
HAR files can be saved using browser extensions or in the developer tools of a browser.
'''

# specify the path of the HAR file
har_file_path = 'network_log.har'

# read the HAR file and parse it as JSON
with open(har_file_path, 'r', encoding='utf-8') as f:
    har_data = json.load(f)

# extract the URLs of all JS files
js_urls = []
for entry in har_data['log']['entries']:
    url = entry['request']['url']
    content_type = entry['response']['content']['mimeType']
    if 'javascript' in content_type:
        js_urls.append(url)

# print the list of JS files and count of files
print('List of JS files:')
for i, url in enumerate(js_urls):
    print(f'{i+1}. {url}')
print(f'Total number of JS files: {len(js_urls)}')

# create a new folder to save the JS files in
if not os.path.exists('js_files'):
    os.makedirs('js_files')

# prompt to start the download

download_format_regex = re.compile(f'.*\.(js)$')
filtered_js_urls = list(filter(download_format_regex.match, js_urls))
print(f'Downloading {len(js_urls)} JS files...')
for url in filtered_js_urls:
    filename = os.path.basename(url)
    filepath = os.path.join('js_files', filename)
    try:
        urllib.request.urlretrieve(url, filepath)
        print(f'{filename} downloaded successfully.')
    except Exception as e:
        print(f'Error downloading {filename}: {e}')
    
# Selenium setup
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
driver = webdriver.Chrome(options=options)

# Loop through each JS file URL and download it with Selenium
for i, url in enumerate(js_urls):
    driver.get(url)
    content = driver.page_source
    filename = os.path.basename(url)
    filepath = os.path.join('js_files', filename)
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'{filename} downloaded successfully.')
    except Exception as e:
        print(f'Error downloading {filename}: {e}')
    
driver.quit()

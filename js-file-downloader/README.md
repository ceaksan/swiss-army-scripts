# JS Downloader

JS Downloader is a Python script that downloads all JavaScript files from a specified HAR file and saves them in a new folder. It also prints out the list of JS files and their count. It uses a regular expression to filter out the URLs of the JS files and then downloads them using urllib.request. Additionally, it uses Selenium to loop through the JS file URLs and download them as well. Finally, it prints out the status of each download.

## Requirements

- Python 3.x
- Selenium WebDriver for Chrome
- A HAR file from which to download JavaScript files

## Usage

1. Save the HAR file to be parsed in the same directory as the js_downloader.py script.
2. Open the terminal or command prompt and navigate to the directory containing the script and the HAR file.
3. Run the script using the command python js_downloader.py.
4. The script will prompt you to specify the file format of the files to be downloaded (optional). If left blank, it will download all JavaScript files.
5. The script will create a new folder called js_files in the current directory and save the downloaded files there.
6. The script will print out the status of each download.

### How to Generate a HAR File

1. Open Google Chrome.
2. Navigate to the webpage you want to generate a HAR file for.
3. Press F12 to open the Developer Tools.
4. Click on the "Network" tab.
5. Ensure that the "Preserve log" checkbox is checked.
6. Reload the page.
7. Wait for the page to finish loading.
8. Right-click on any request in the "Network" tab and select "Save all as HAR with content".
9. Save the HAR file to the desired location.

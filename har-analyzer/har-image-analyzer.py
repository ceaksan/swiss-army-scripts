from haralyzer import HarParser, HarPage
import pandas as pd
import matplotlib.pyplot as plt
import json

# Load the HAR file
with open('tr.wikipedia.org.har', 'r') as f:
    har_parser = HarParser(json.loads(f.read()))

# print(har_parser.har_data)
# print(har_parser.har_data.keys())
# print(har_parser.har_data['entries'])

# get list of entries
entries = har_parser.har_data['entries']
print(len(entries))
# 4

# Extract data from the HAR file
image_entries = [entry for entry in entries if entry['request']['url'].endswith(('.png', '.jpeg', '.jpg', '.gif', '.bmp'))]

# Create a DataFrame from the Image entries
df = pd.DataFrame(image_entries)

# Print the column names
print(df.columns)

# Print the summary statistics for numeric columns
print(df.describe())

# Get the number of Image requests
entry_count = len(image_entries)
print("Number of Image requests:", entry_count)

# Get the file names and sizes of the Image requests
Image_files = [(entry['request']['url'].split('/')[-1], entry['response']['content']['size']) for entry in image_entries]

# Print the Image file names and sizes
for Image_file in Image_files:
    print(Image_file[0], ":", Image_file[1], "bytes")
    
# Group the Image entries by file name
image_entries_by_file = {}
for entry in image_entries:
    file_name = entry['request']['url'].split('/')[-1]
    if file_name in image_entries_by_file:
        image_entries_by_file[file_name].append(entry)
    else:
        image_entries_by_file[file_name] = [entry]

# Analyze the data per file
for file_name, entries in image_entries_by_file.items():
    print("File:", file_name)
    print("Number of requests:", len(entries))
    print("Total size:", sum(entry['response']['content']['size'] for entry in entries), "bytes")
    print("Max loading time:", max(entries, key=lambda entry: entry['time'])['time'], "ms")
    print("Min loading time:", min(entries, key=lambda entry: entry['time'])['time'], "ms")
    print("Average loading time:", sum(entry['time'] for entry in entries) / len(entries), "ms")

# Get the total time taken for all the Image requests
total_time = sum(entry['time'] for entry in image_entries)
print("Total time taken for all Image requests:", total_time, "ms")

# Get the loading times for all the Image requests
loading_times = [entry['time'] for entry in image_entries]

# Calculate the total loading time and loading time per file
total_loading_time = sum(entry['time'] for entry in image_entries)
loading_time_by_file = {}
for entry in image_entries:
    file_name = entry['request']['url'].split('/')[-1]
    if file_name in loading_time_by_file:
        loading_time_by_file[file_name] += entry['time']
    else:
        loading_time_by_file[file_name] = entry['time']

# Calculate the percentage of total loading time each file accounts for
loading_time_percentages = {}
for file_name, loading_time in loading_time_by_file.items():
    loading_time_percentages[file_name] = loading_time / total_loading_time * 100

# Print the loading time percentages
for file_name, loading_time_percentage in loading_time_percentages.items():
    print(file_name, ":", loading_time_percentage, "%")


# Create a histogram of the loading times
plt.hist(loading_times, bins=20)
plt.xlabel('Loading Time (ms)')
plt.ylabel('Count')
plt.title('Distribution of Image Loading Times')
plt.show()

# Create a boxplot of the loading times
plt.boxplot([entry['time'] for entry in image_entries], vert=False)
plt.xlabel('Loading Time (ms)')
plt.title('Distribution of Image Loading Times')
plt.show()

# Get the Image request with the maximum loading time
max_loading_time = max(image_entries, key=lambda entry: entry['time'])
print("Image request with the maximum loading time:", max_loading_time['request']['url'], max_loading_time['time'], "ms")

# Get the Image request with the minimum loading time
min_loading_time = min(image_entries, key=lambda entry: entry['time'])
print("Image request with the minimum loading time:", min_loading_time['request']['url'], min_loading_time['time'], "ms")
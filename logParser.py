import csv
import re
from collections import Counter, defaultdict

# Function to read the log file and extract IPs and their associated data size
def read(filename):
    with open(filename, 'r') as f:
        log = f.read()

        # Regular expression pattern to match IP addresses
        ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        # Regular expression pattern to match the data size in the log
        data_pattern = r'" \d{3} (\d+) '

        # Find all IP addresses and data sizes in the log using the patterns
        ips_list = re.findall(ip_pattern,log)
        data_size = (re.findall(data_pattern, log))

        data = []
        # Combine IP addresses with their corresponding data size
        for i in range(len(ips_list)):
            data.append((ips_list[i],int(data_size[i])))

        return data

# Function to count frequency and total data for each IP address
def count_ips_data(data):
    combined_data = defaultdict(lambda: {'frequency': 0, 'data': 0})

    for ip,size in data:
        combined_data[ip]['frequency'] += 1             # Increment the frequency count for the IP
        combined_data[ip]['data'] += size               # Add the data size to the total for the IP

    return combined_data

# Function to write the final data to a CSV file
def write_csv(final_data):
    with open('Data Flow.csv','w') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header row to the CSV file
        header = ['IP', 'Frequency', 'Total Data (MB)']
        writer.writerow(header)
        # Write each IP and its associated frequency and data size to the CSV
        for ip,info in final_data.items():
            writer.writerow((ip, info['frequency'], info['data']))


if __name__ == '__main__':
    write_csv(count_ips_data(read('log_sample.txt')))
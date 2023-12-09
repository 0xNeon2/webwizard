import requests
import sys
import time
import random
import os

filename1 = 'API_KEY.txt'
filename2 = 'SEARCH_ENGINE_ID.txt'

script_directory = os.path.dirname(os.getcwd())
# Specify the relative path to the directory where the text files are located
api_files_directory = 'webwizard/package/sub_package/'
# Construct the full file path by joining the script directory and the text files directory
file_path1 = os.path.join(script_directory, api_files_directory,filename1)
# Read API_KEY and SEARCH_ENGINE_ID from separate files
file_path2 = os.path.join(script_directory, api_files_directory,filename2)

with open(file_path1, 'r') as api_file:
    API_KEY = api_file.read().strip()

with open(file_path2, 'r') as engine_file:
    SEARCH_ENGINE_ID = engine_file.read().strip()

# Define a function to perform the Google Custom Search with exponential backoff algorithm
def gsearch():
    try:
        dork = input("\n[-] Paste The Dork Search Query ==> ")
        amount = input("[-] Enter The Number Of Websites To Display ==> ")
        print("\n")
        print("========================================================================")
        print("\n")

        # Define the API parameters
        params = {
            'q': dork,
            'key': API_KEY,
            'cx': SEARCH_ENGINE_ID,
        }

        url = 'https://www.googleapis.com/customsearch/v1'
        max_retries = 5  # Maximum number of retries
        retry_delay = 1  # Initial retry delay in seconds

        for retry in range(max_retries):
            try:
                response = requests.get(url, params=params)
                response.raise_for_status()  # Raise an exception if the request is unsuccessful

                results = response.json()

                if 'items' in results:
                    # Display the links for the specified number of websites
                    for i in range(min(int(amount), len(results['items']))):
                        print(f"{i + 1}. {results['items'][i]['link']}")
                break  # Break out of the loop if successful

            except requests.exceptions.RequestException as e:
                print(f"Attempt {retry + 1} failed. Error: {e}")
                if retry < max_retries - 1:
                    # Calculate the next retry delay using exponential backoff with jitter
                    retry_delay = min(2 ** retry * random.uniform(0.5, 1.5), 60)
                    print(f"Retrying in {retry_delay:.2f} seconds...")
                    time.sleep(retry_delay)
                else:
                    print("Maximum number of retries reached. Exiting...")
                    sys.exit()

    except KeyboardInterrupt:
        print("\n")
        print("Terminating...!")
        time.sleep(0.5)
        sys.exit()

def spider():
    print("\n")
    print("\n=======================> Welcome to SPIDER <=======================\n")
    banner = ("""
  ______ ______  _ ______  _______ ______  
 / _____|_____ \| (______)(_______|_____ \ 
( (____  _____) ) |_     _ _____   _____) )
 \____ \|  ____/| | |   | |  ___) |  __  / 
 _____) ) |     | | |__/ /| |_____| |  \ \ 
(______/|_|     |_|_____/ |_______)_|   |_| 
                project-WebWizard(b)"""
)
    for col in banner:
        print(col, end="")
        sys.stdout.flush()
        time.sleep(0.0025)
    print("\n")
    gsearch()
    time.sleep(0.5)
    print("\n")
    print("=============================> Crawling Done <============================")

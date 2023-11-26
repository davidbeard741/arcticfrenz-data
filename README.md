# Arctic Frenz Discord Bot Data Repository

Welcome to the Arctic Frenz Data Repository - a specialized resource designed to enhance the Arctic Frenz Bot with extensive NFT analytics. Our repository features in-depth data on aspects like asset ownership duration, listing status, quantity, and rarity of NFTs. It is engineered to offer seamless integration with Discord, allowing community members to conduct ranking checks and access metadata with ease. Additionally, this repository empowers collections to leverage these insights to encourage and strengthen community engagement on Discord platforms.

<table align="center">
	<tr>
		<td>
			<img src="https://raw.githubusercontent.com/davidbeard741/arcticfrenz-data/main/images/IMG_3153.gif">
		</td>
	</tr>
	<tr>
		<td align="center">
			<a href="https://discord.gg/arcticfrenz">
				<img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white">
			</a>
			<a href="https://twitter.com/arcticfrenz">
				<img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white">
			</a> 
		</td>
	</tr>
</table>

---

## Part 1: How to Retrieve NFT Metadata for an Entire Collection

A structured guide designed to help you retrieve the metadata for each NFT in a collection.

### Step 1: Identify the Creator Address

<table align="center">
	<tr>
		<td>
			1. Visit <a href="https://magiceden.io">Magic Eden</a> and select an NFT from the collection you are interested in.
		</td>
	</tr>
	<tr>
		<td>
			2. Navigate to the NFT's detail page and locate its Mint Address, then proceed to <a href="https://solscan.io">Solscan</a>
			<img src="https://raw.githubusercontent.com/davidbeard741/arcticfrenz-data/main/images/3B369D54-BACD-4747-9AC7-9A5026257145.jpeg">
		</td>
	</tr>
	<tr>
		<td>
			3. In Solscan, click on the "Creators" tab. Look for the first listed address that shows a 0% share and is marked with a blue tick. 
			<img src="https://raw.githubusercontent.com/davidbeard741/arcticfrenz-data/main/images/0D636107-2D85-4DBD-849D-E19A2B647338.jpeg">
		</td>
	</tr>
	<tr>
		<td>
			4. Copy this Creator Address.
			<img src="https://raw.githubusercontent.com/davidbeard741/arcticfrenz-data/main/images/CC753005-3372-463E-97A9-D8E0710BC5A3.jpeg">
		</td>
	</tr> 
</table>

### Step 2: Acquire the Collection's Hash List

1. Visit <a href="https://tools.smithii.io/hashlist/solana">Smithii</a>, a tool for Hash List NFTs on the Solana blockchain.
2. Paste the Creator Address obtained from [Step 1](https://github.com/davidbeard741/arcticfrenz-data/blob/main/README.md#step-1-identify-the-creator-address) into the provided field.
3. Click 'Get hash list' to generate the list.
4. Please be patient, as generating the hash list may take a few minutes.
5. Once the list is available, copy or save the list for Part 1, Step 4.

### Step 3: Set Up Your Python Development Environment

Choose one of the following environments for your Python development needs:

- **Google Colab**: Utilize [Google Colab](https://colab.research.google.com) for a cloud-based Jupyter notebook experience that does not require any local setup.
- **JupyterLab**: For a more advanced setup, [JupyterLab](https://jupyter.org/) provides a comprehensive development environment to work with notebooks, code, and data.
- **Local Environment**: Set up your development environment locally on various operating systems:
  - [Windows Setup Guide](https://realpython.com/python-coding-setup-windows/)
  - [macOS Setup Guide](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-macos)
  - [Linux/Unix Setup Guide](https://itsfoss.com/python-setup-linux/)

### Step 4: Make a Python List

Open your development environment and create a variable named `nft_addresses` for a Python list. Paste your hash list from [Part 1, Step 2](https://github.com/davidbeard741/arcticfrenz-data/blob/main/README.md#step-2-acquire-the-collections-hash-list) into the Python list.

```PYTHON
nft_addresses = [
         # PASTE HASH LIST HERE  
]
```

### Step 5: Helius

<table align="center">
	<tr>
		<td>
			1. Visit <a href="https://dev.helius.xyz/dashboard/app">Helius</a>, a platform for Solana RPC nodes, APIs, webhooks, and infrastructure.
		</td>
	</tr>
	<tr>
		<td>
			2. Sign-in to Helius 
		</td>
	</tr>
	<tr>
		<td>
			3. Copy your free API key for Step 6.
			<img src="https://raw.githubusercontent.com/davidbeard741/arcticfrenz-data/main/images/1C21909B-7CF4-41A9-B6A7-8655DF609006.jpeg">
		</td>
	</tr>
</table>

### Step 6: API Key 

Open your development environment, create a variable named `apikey`. Paste your API Key from [Part 1, Step 5](https://github.com/davidbeard741/arcticfrenz-data#step-5-helius) into the variable 

```PYTHON
apikey = "INSERT YOUR API KEY BETWEEN THESE QUOTATION MARKS"
```

### Step 7: Make a Batched API Request

Below is the complete code. Execute it to generate a file named 'nft_metadata.json' that will include the metadata each NFT in the collection.

<details>
  <summary>CLICK TO EXPAND Python Script</summary>

```PYTHON
import requests
import json


nft_addresses = [
         # PASTE HASH LIST HERE  
]

apikey = "INSERT YOUR API KEY BETWEEN THESE QUOTATION MARKS"

url = f"https://api.helius.xyz/v0/token-metadata?api-key={apikey}"

def get_metadata(nft_addresses):
    batch_size = 80
    all_data = []

    for i in range(0, len(nft_addresses), batch_size):
        batch_addresses = nft_addresses[i:i + batch_size]
        payload = {
            "mintAccounts": batch_addresses,
            "includeOffChain": True,
            "disableCache": False
        }
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            batch_data = response.json()
            all_data.extend(batch_data)
            print(f"Batch {i // batch_size + 1} successfully retrieved.")
        else:
            print(f"Failed to retrieve metadata for batch {i // batch_size + 1}: {response.status_code}")
            print("Error message:", response.text)

    with open('nft_metadata.json', 'w') as file:
        json.dump(all_data, file, indent=4)
        print("All metadata written to nft_metadata.json")

get_metadata(nft_addresses)
```
</details>

### The Output JSON File

The example JSON below is truncated for illustrative purposes; the 'nft_metadata' output file will encompass all NFTs in the collection.

<details>
  <summary>CLICK TO EXPAND JSON Example</summary>

```JSON 
[
    {
        "account": "DYTo4wYJDA2tRkD3kMzthDY3rrnyWMgSFrBc3TtiSjQq",
        "onChainAccountInfo": {
            "accountInfo": {
                "key": "DYTo4wYJDA2tRkD3kMzthDY3rrnyWMgSFrBc3TtiSjQq",
                "isSigner": false,
                "isWritable": false,
                "lamports": 1461600,
                "data": {
                    "parsed": {
                        "info": {
                            "decimals": 0,
                            "freezeAuthority": "62q7i8DMds7SAPSjnShQKHjacZd29421XH4qnNad5xGK",
                            "isInitialized": true,
                            "mintAuthority": "62q7i8DMds7SAPSjnShQKHjacZd29421XH4qnNad5xGK",
                            "supply": "1"
                        },
                        "type": "mint"
                    },
                    "program": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA",
                    "space": 82
                },
                "owner": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA",
                "executable": false,
                "rentEpoch": 361
            },
            "error": ""
        },
        "onChainMetadata": {
            "metadata": {
                "tokenStandard": "NonFungible",
                "key": "MetadataV1",
                "updateAuthority": "6DMG9hv3eR8BXKH79sXGyQtfRSxXfNrkHEdc6nCsEjVK",
                "mint": "DYTo4wYJDA2tRkD3kMzthDY3rrnyWMgSFrBc3TtiSjQq",
                "data": {
                    "name": "Arctic Fox #41",
                    "symbol": "AFAF",
                    "uri": "https://m5brw73kei7uoysb7gxdomaxbdqobnz27j65nrq7ohbpgrktfjmq.arweave.net/Z0Mbf2oiP0diQfmuNzAXCODgtzr6fdbGH3HC80VTKlk",
                    "sellerFeeBasisPoints": 1500,
                    "creators": [
                        {
                            "address": "79iAsPyGDhQ7Sw5HcSkhYX9b3tzXp4phxjfPdo9xkmx1",
                            "verified": true,
                            "share": 0
                        },
                        {
                            "address": "2wBMxuAYKiVjQFGB48bhHPexNRyeHcDN1aaYT4WYv5r5",
                            "verified": true,
                            "share": 54
                        },
                        {
                            "address": "8XzUgMAhFZWERytRDNVBdL95LL5Ftox72EiSNzTu63QS",
                            "verified": true,
                            "share": 46
                        }
                    ]
                },
                "primarySaleHappened": true,
                "isMutable": true,
                "editionNonce": 255,
                "uses": {
                    "useMethod": "",
                    "remaining": 0,
                    "total": 0
                },
                "collection": {
                    "key": "EFjksSb2b897hvxuHXrnVoE2y66iufiJxtDSgFJZYQna",
                    "verified": true
                },
                "collectionDetails": null
            },
            "error": ""
        },
        "offChainMetadata": {
            "metadata": {
                "attributes": [
                    {
                        "traitType": "Arctic Animal",
                        "value": "Fox"
                    },
                    {
                        "traitType": "Endangered",
                        "value": "No"
                    },
                    {
                        "traitType": "Paw",
                        "value": "Left-Up"
                    },
                    {
                        "traitType": "Eyes",
                        "value": "Heterochromia"
                    },
                    {
                        "traitType": "Mouth",
                        "value": "Blep"
                    }
                ],
                "description": "An exclusive family, 69 #SolanaNFTs per collection. Liquidity adding for rewarding #ArcticFrenz.",
                "image": "https://arweave.net/p5C032iu3UQ4Lpr5cTNlcW8bVDrcVd872QChc3z8J-4?ext=png",
                "name": "Arctic Fox #41",
                "properties": {
                    "category": null,
                    "creators": [
                        {
                            "address": "2wBMxuAYKiVjQFGB48bhHPexNRyeHcDN1aaYT4WYv5r5",
                            "share": 54
                        },
                        {
                            "address": "8XzUgMAhFZWERytRDNVBdL95LL5Ftox72EiSNzTu63QS",
                            "share": 46
                        }
                    ],
                    "files": [
                        {
                            "type": "image/png",
                            "uri": "40.png"
                        }
                    ]
                },
                "sellerFeeBasisPoints": 1500,
                "symbol": "AFAF"
            },
            "uri": "https://m5brw73kei7uoysb7gxdomaxbdqobnz27j65nrq7ohbpgrktfjmq.arweave.net/Z0Mbf2oiP0diQfmuNzAXCODgtzr6fdbGH3HC80VTKlk",
            "error": ""
        },
        "legacyMetadata": null
    },
    {
      "_comment": "The file has been truncated for this example; the output JSON file nft_metadata will contain all NFTs in the collection",
    }
]
```
</details>

---

## Part 2: Calculating Rarity Scores for NFTs Based on Off-Chain Metadata

The concept of rarity in the context of NFTs pertains to the uniqueness and scarcity of certain traits within a collection. Rarity scores can significantly impact the perceived value and desirability of individual NFTs. This section outlines the process for calculating rarity scores using the off-chain metadata associated with each NFT.

### Steps to Calculate Rarity Scores

1. **List Traits**: Enumerate all distinct traits and their possible values from the `offChainMetadata` within the NFT dataset.
   
2. **Count Traits**: Tally the frequency of each trait value across the collection to determine how common or rare each trait is.

3. **Calculate Rarity Scores**: Assign a rarity score to each NFT by summing the inverse frequencies of its trait values. This score quantifies the rarity, with higher scores indicating rarer traits.

### Implementation

The following Python script performs the above steps. It processes the off-chain metadata to compute a rarity score for each NFT, then appends this score to the original dataset, and finally outputs the enriched dataset as a JSON file.

<details>
  <summary>CLICK TO EXPAND Python Script</summary>
	
```python
import json
import pandas as pd

# Define a function to compute the rarity score based on trait counts
def calculate_rarity_score(attributes, trait_counts_df):
    # The rarity score is the sum of inverses of trait counts
    score = sum(1 / trait_counts_df[(trait_counts_df['traitType'] == attr['traitType']) & 
                                    (trait_counts_df['value'] == attr['value'])]['count'].values[0]
                for attr in attributes if len(trait_counts_df[(trait_counts_df['traitType'] == attr['traitType']) & 
                                                              (trait_counts_df['value'] == attr['value'])]) > 0)
    return score

# Load the JSON data
file_path = 'nft_metadata.json'
with open(file_path, 'r') as file:
    nft_metadata = json.load(file)

# Normalize the data into a flat table
nft_df = pd.json_normalize(nft_metadata)

# Prepare the trait values and counts
attributes_list = nft_df.dropna(subset=['offChainMetadata.metadata.attributes'])['offChainMetadata.metadata.attributes'].tolist()
attributes_flat_list = [attr for sublist in attributes_list for attr in sublist]
attributes_df = pd.DataFrame(attributes_flat_list)
trait_counts = attributes_df.groupby(['traitType', 'value']).size().reset_index(name='count')

# Compute rarity scores for each NFT
nft_df['rarity_score'] = nft_df['offChainMetadata.metadata.attributes'].apply(
    lambda attrs: calculate_rarity_score(attrs, trait_counts) if isinstance(attrs, list) else None
)

# Append the rarity scores to the original data
for i, record in enumerate(nft_metadata):
    rarity_score = nft_df.loc[i, 'rarity_score']
    record['rarity_score'] = rarity_score if pd.notnull(rarity_score) else 0

# Save the enriched data to a new JSON file
updated_file_path = 'nft_metadata_with_rarity.json'
with open(updated_file_path, 'w') as file:
    json.dump(nft_metadata, file, indent=4)

print(f"Updated JSON file saved to {updated_file_path}")
```
</details>

### Rarity Score Implications
A lower frequency of a trait value indicates rarity, and hence, it contributes more significantly to the rarity score. The scoring system is designed such that the sum of the inverses of the trait frequencies for an NFT's traits yields its total rarity score. The end result is a comprehensive dataset where each NFT entry is supplemented with a rarity_score field, reflecting its uniqueness within the collection.

### Note on Rarity Score Calculation

In the rarity score calculation, it is possible for an NFT to have missing or undefined attributes. When such cases arise, the script is designed to handle these gracefully by assigning a default rarity score of 0. This ensures that every NFT has a defined rarity score when saved to the JSON file. By doing so, the dataset maintains consistency and allows for a meaningful comparison between NFTs, even if some have incomplete metadata. This approach also prevents potential errors during data processing and analysis that could occur due to undefined or missing values.

### Example Output
The output is an updated JSON file, nft_metadata_with_rarity.json, where each NFT entry now includes a rarity_score. Below is a truncated example of what an NFT entry might look like with an appended rarity score:

<details>
  <summary>CLICK TO EXPAND JSON Example</summary>

```JSON
[
    {
        "account": "DYTo4wYJDA2tRkD3kMzthDY3rrnyWMgSFrBc3TtiSjQq",
        "onChainAccountInfo": {
            "accountInfo": {
                "key": "DYTo4wYJDA2tRkD3kMzthDY3rrnyWMgSFrBc3TtiSjQq",
                "isSigner": false,
                "isWritable": false,
                "lamports": 1461600,
                "data": {
                    "parsed": {
                        "info": {
                            "decimals": 0,
                            "freezeAuthority": "62q7i8DMds7SAPSjnShQKHjacZd29421XH4qnNad5xGK",
                            "isInitialized": true,
                            "mintAuthority": "62q7i8DMds7SAPSjnShQKHjacZd29421XH4qnNad5xGK",
                            "supply": "1"
                        },
                        "type": "mint"
                    },
                    "program": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA",
                    "space": 82
                },
                "owner": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA",
                "executable": false,
                "rentEpoch": 361
            },
            "error": ""
        },
        "onChainMetadata": {
            "metadata": {
                "tokenStandard": "NonFungible",
                "key": "MetadataV1",
                "updateAuthority": "6DMG9hv3eR8BXKH79sXGyQtfRSxXfNrkHEdc6nCsEjVK",
                "mint": "DYTo4wYJDA2tRkD3kMzthDY3rrnyWMgSFrBc3TtiSjQq",
                "data": {
                    "name": "Arctic Fox #41",
                    "symbol": "AFAF",
                    "uri": "https://m5brw73kei7uoysb7gxdomaxbdqobnz27j65nrq7ohbpgrktfjmq.arweave.net/Z0Mbf2oiP0diQfmuNzAXCODgtzr6fdbGH3HC80VTKlk",
                    "sellerFeeBasisPoints": 1500,
                    "creators": [
                        {
                            "address": "79iAsPyGDhQ7Sw5HcSkhYX9b3tzXp4phxjfPdo9xkmx1",
                            "verified": true,
                            "share": 0
                        },
                        {
                            "address": "2wBMxuAYKiVjQFGB48bhHPexNRyeHcDN1aaYT4WYv5r5",
                            "verified": true,
                            "share": 54
                        },
                        {
                            "address": "8XzUgMAhFZWERytRDNVBdL95LL5Ftox72EiSNzTu63QS",
                            "verified": true,
                            "share": 46
                        }
                    ]
                },
                "primarySaleHappened": true,
                "isMutable": true,
                "editionNonce": 255,
                "uses": {
                    "useMethod": "",
                    "remaining": 0,
                    "total": 0
                },
                "collection": {
                    "key": "EFjksSb2b897hvxuHXrnVoE2y66iufiJxtDSgFJZYQna",
                    "verified": true
                },
                "collectionDetails": null
            },
            "error": ""
        },
        "offChainMetadata": {
            "metadata": {
                "attributes": [
                    {
                        "traitType": "Arctic Animal",
                        "value": "Fox"
                    },
                    {
                        "traitType": "Endangered",
                        "value": "No"
                    },
                    {
                        "traitType": "Paw",
                        "value": "Left-Up"
                    },
                    {
                        "traitType": "Eyes",
                        "value": "Heterochromia"
                    },
                    {
                        "traitType": "Mouth",
                        "value": "Blep"
                    }
                ],
                "description": "An exclusive family, 69 #SolanaNFTs per collection. Liquidity adding for rewarding #ArcticFrenz.",
                "image": "https://arweave.net/p5C032iu3UQ4Lpr5cTNlcW8bVDrcVd872QChc3z8J-4?ext=png",
                "name": "Arctic Fox #41",
                "properties": {
                    "category": null,
                    "creators": [
                        {
                            "address": "2wBMxuAYKiVjQFGB48bhHPexNRyeHcDN1aaYT4WYv5r5",
                            "share": 54
                        },
                        {
                            "address": "8XzUgMAhFZWERytRDNVBdL95LL5Ftox72EiSNzTu63QS",
                            "share": 46
                        }
                    ],
                    "files": [
                        {
                            "type": "image/png",
                            "uri": "40.png"
                        }
                    ]
                },
                "sellerFeeBasisPoints": 1500,
                "symbol": "AFAF"
            },
            "uri": "https://m5brw73kei7uoysb7gxdomaxbdqobnz27j65nrq7ohbpgrktfjmq.arweave.net/Z0Mbf2oiP0diQfmuNzAXCODgtzr6fdbGH3HC80VTKlk",
            "error": ""
        },
        "legacyMetadata": null,
        "rarity_score": 0.1473389390210555
    },
    {
      "_comment": "The file has been truncated for this example; the output JSON file nft_metadata_with_rarity will contain all NFTs in the collection with their rarity_score",
    }
]

```
</details>

---

## Part 3: Enhancing the Metadata of an Entire NFT Collection with Additional Data

### Step 1: Setting Up Your Python Development Environment

Refer to [Part 1, Step 3](https://github.com/davidbeard741/arcticfrenz-data#step-3-set-up-your-python-development-environment) for the setup instructions.

### Step 2: Web Scraping and Selenium WebDriver

This script employs Selenium WebDriver to automate web browser interactions for the purpose of collecting additional metadata about NFTs. It scrapes data from a specific website, focusing on extracting information about NFT holders and relevant timestamps. Subsequently, this data is used to update a JSON file. The following sections detail the key functionalities of the script:

#### Parsing Approach

**Owner Address Extraction:**
- The script scans the HTML content of a webpage to locate a specific table with a header titled 'Owner'. This identification is crucial as the table contains the NFT owner's address.
- Within this table, the script bypasses any 'measurement' rows (marked by the class 'ant-table-measure-row'). These rows are not visible to users and do not contain relevant data.
- The primary focus is on the first visible row following any measurement rows. This row holds the necessary information.
- The script then extracts the text within the 'a' tag found in the second 'td' (table data) element of this row. This text is the actual owner's address associated with the NFT.

**Timestamp Extraction:**
- Similar to the owner address extraction, the script identifies and parses a specific table on the webpage to extract timestamp data related to the NFT.
- The script navigates to the appropriate column (identified in the script) that contains timestamp information.
- It extracts the timestamp data from the first visible row, ensuring that it skips any non-relevant rows such as measurement rows.

<details>
  <summary>CLICK TO EXPAND Python Script</summary>

```shell
!apt update

!apt install chromium-chromedriver

!pip install selenium

!wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && apt install ./google-chrome-stable_current_amd64.deb
```


```shell
!Service('/usr/bin/chromedriver')
```


```python
import json
import random
import time
import logging
import sys
import os
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
import psutil


LOG_FILE = 'logfile.log'
FILE_ADDRESS = 'address.html'
FILE_TIME = 'time.html'


def setup_logger(log_file_path, logger_name='MyAppLogger'):
    logger = logging.getLogger(logger_name)
    logger.handlers = []
    logger.setLevel(logging.INFO)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger


def kill_chrome_and_chromedriver(logger):
    for proc in psutil.process_iter():
        if 'chrome' in proc.name().lower() or 'chromedriver' in proc.name().lower():
            try:
                proc.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass


def driversetup(logger):
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=selenium")
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("lang=en-US")
    options.add_argument("location=US")
    options.add_argument(f"--window-size={1920},{1080}")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--incognito")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.page_load_strategy = 'normal'

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    ]
    selected_user_agent = random.choice(user_agents)
    options.add_argument(f"user-agent={selected_user_agent}")

    caps = webdriver.DesiredCapabilities.CHROME
    caps['goog:loggingPrefs'] = {'browser': 'ALL'}
    service = webdriver.chrome.service.Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(options=options)
    driver.execute_cdp_cmd("Network.clearBrowserCookies", {})
    driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"Referer": "https://www.google.com/"}})
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
    return driver

def random_sleep(min_seconds, max_seconds):
    time.sleep(random.uniform(min_seconds, max_seconds))

def simulate_human_interaction(driver, logger):
    action = ActionChains(driver)
    body_element = driver.find_element(By.TAG_NAME, 'body')
    for _ in range(random.randint(1, 3)):
        action.send_keys_to_element(body_element, Keys.PAGE_DOWN).perform()
        random_sleep(0.5, 1.0)
        action.send_keys_to_element(body_element, Keys.PAGE_UP).perform()
        random_sleep(0.5, 1.0)
    action.move_to_element(body_element).perform()
    random_sleep(0.5, 1.0)
    action.move_by_offset(random.randint(0, 100), random.randint(0, 100)).perform()
    random_sleep(0.5, 1.0)


def extract_owner_address_from_file(file_path, logger):
    try:
        with open(FILE_ADDRESS, 'r') as file:
            html_content = file.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        tables = soup.find_all("table")

        for table in tables:
            if table.find("th", {"title": "Owner"}):
                visible_rows = table.select("tbody tr:not(.ant-table-measure-row)")
                if visible_rows:
                    owner_address_element = visible_rows[0].select_one("td:nth-of-type(2) a")
                    if owner_address_element:
                        address = owner_address_element.text.strip()
                        logger.info(f"Owner address found: {address}")
                        return address
                    else:
                        logger.error("Owner address not found in the table.")
                        return "Address not found"
                else:
                    logger.error("No visible rows found in the owner table.")
                    return "No rows in table"
    except Exception as e:
        logger.error(f"Error while extracting owner address: {e}")
        return f"Error: {e}"


def extract_time_from_file(file_path, logger):
    try:
        with open(file_path, 'r') as file:
            html_content = file.read()
        logger.info(f"Successfully read HTML content from '{file_path}'.")

        soup = BeautifulSoup(html_content, 'html.parser')
        time_column_index = 4
        logger.info("Parsing HTML to locate the time table.")

        table_count = 0
        for table in soup.find_all("table"):
            table_count += 1
            logger.info(f"Checking table {table_count} for visible rows.")
            visible_rows = table.select("tbody tr:not(.ant-table-measure-row)")
            if not visible_rows:
                logger.info(f"No visible rows found in table {table_count}. Checking next table if available...")
                continue

            logger.info(f"Table {table_count}: Visible rows found. Extracting time from the first row.")
            time_cell = visible_rows[0].select_one(f"td:nth-of-type({time_column_index})")
            if not time_cell:
                logger.info(f"Table {table_count}: Time cell not found in the table.")
                continue

            hold_time = time_cell.text.strip()
            logger.info(f"Table {table_count}: Hold Time successfully extracted: {hold_time}")
            return hold_time

        logger.info("Failed to find a table with visible rows containing time data.")
        return "No visible rows found in any time table"

    except Exception as e:
        logger.info(f"An unexpected error occurred while extracting hold time from '{file_path}': {e}")
        return f"Error: {e}"


def getholderaddress(url_holder, driver, logger):

    try:

        driver.get(url_holder)

        wait = WebDriverWait(driver, timeout=30)
        root = driver.find_element(By.ID, 'root')
        body = driver.find_element(By.TAG_NAME, 'body')

        wait.until(lambda d: driver.execute_script('return document.readyState') == 'complete')
        wait.until(lambda d: root.is_displayed())
        wait.until(lambda d: body.is_displayed())

        random_sleep(6, 7)

        simulate_human_interaction(driver, logger)

        root_html = driver.find_element(By.ID, 'root').get_attribute('outerHTML')
        with open(FILE_ADDRESS, 'w') as file:
            file.write(root_html)

        solana_address = extract_owner_address_from_file(FILE_ADDRESS, logger)
        logger.info(f"Holder Address: {solana_address}")

    except TimeoutException:
        logger.error("Timed out waiting for page to load")
        solana_address = "Error: Page did not load properly"
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        solana_address = "Error: Unexpected issue occurred"

    return solana_address


def get_hold_time(url_time, driver, logger):
    try:

        driver.get(url_time)

        wait = WebDriverWait(driver, timeout=30)
        root = driver.find_element(By.ID, 'root')
        body = driver.find_element(By.TAG_NAME, 'body')

        wait.until(lambda d: driver.execute_script('return document.readyState') == 'complete')
        wait.until(lambda d: root.is_displayed())
        wait.until(lambda d: body.is_displayed())

        random_sleep(8, 9)

        simulate_human_interaction(driver, logger)

        javascript = """
        var elements = document.querySelectorAll('span.sc-kDvujY.dxDyul');
        var targetElement = null;
        var count = 0;

        for (var i = 0; i < elements.length; i++) {
            if (elements[i].textContent.includes('Time')) {
                count++;
                if (count === 2) {
                    targetElement = elements[i];
                    break;
                }
            }
        }

        if (targetElement) {
            targetElement.click();
        } else {
            console.log('Second element not found');
        }
        """

        try:
            driver.execute_script(javascript)
        except Exception as e:
            logger.error(f"An error occurred: {e}")

        time.sleep(1)

        body_html = driver.find_element(By.TAG_NAME, 'body').get_attribute('outerHTML')

        with open(FILE_TIME, 'w') as file:
            file.write(body_html)

        hold_time = extract_time_from_file(FILE_TIME, logger)
        logger.info(f"Hold time extracted: {hold_time}")

    except TimeoutException as e:
        logger.info(f"TimeoutException encountered: {e}. The website might be unresponsive or the element locators might be incorrect.")
        hold_time = "Error: Timed out"
    except Exception as e:
        logger.info(f"Unexpected error encountered: {e}. Review the stack trace for details and check the website's structure.")
        hold_time = "Error: Unexpected issue occurred"
    finally:
        logger.info("Closing the web driver...")
        driver.close()
        logger.info("Web driver closed for holder address and time.")

    return hold_time


def process_item(item, driver, logger):
    account = item.get('account')
    if not account:
        logger.info("Account information not found in the item.")
        return

    url_holder = f"https://solscan.io/token/{account}#holders"
    url_time = f"https://solscan.io/token/{account}#txs"

    try:
        solana_address = getholderaddress(url_holder, driver, logger)
        hold_time = get_hold_time(url_time, driver, logger)
        update_json_data(item, solana_address, hold_time, logger)
        logger.info(f"Successfully processed account {account}.")
    except Exception as e:
        logger.error(f"Error processing {account}: {e}")


from datetime import datetime

def update_json_data(item, solana_address, hold_time_str, logger):

    hold_time_format = "%m-%d-%Y %H:%M:%S"
    hold_time = datetime.strptime(hold_time_str, hold_time_format)

    current_time = datetime.now()
    hold_time_unix = int(hold_time.timestamp())
    current_time_unix = int(current_time.timestamp())

    item['holder data'] = [
        {"holder": solana_address},
        {"when acquired": hold_time_unix},
        {"time checked": current_time_unix}
    ]


def find_start_index(nft_metadata):
    # Step 1: Prioritize items without 'holder data'
    for index, item in enumerate(nft_metadata):
        if 'holder data' not in item:
            return index

    # Step 2: Prioritize items with invalid 'holder' length
    for index, item in enumerate(nft_metadata):
        if 'holder data' in item:
            holder = item['holder data'][0]['holder']
            if len(holder) not in range(32, 45) and holder != "Magic Eden V2 Authority":
                return index

    # New Step 3: Prioritize if 'when acquired' is not a Unix epoch timestamp
    for index, item in enumerate(nft_metadata):
        if 'holder data' in item:
            when_acquired = item['holder data'][1]['when acquired']
            if not isinstance(when_acquired, int):
                return index

    # Step 4: Prioritize by oldest 'time checked'
    oldest_index = None
    oldest_time = float('inf')
    for index, item in enumerate(nft_metadata):
        if 'holder data' in item:
            time_checked = item['holder data'][2]['time checked']
            if time_checked < oldest_time:
                oldest_time = time_checked
                oldest_index = index

    return oldest_index if oldest_index is not None else len(nft_metadata)


def main():
    logger = setup_logger(LOG_FILE)

    logger.info("Starting new run. Appending to the existing logfile.")

    kill_chrome_and_chromedriver(logger)

    # Load existing data if available
    processed_data_file = 'nft_metadata_with_rarity_and_holder_data.json'
    if os.path.exists(processed_data_file):
        try:
            with open(processed_data_file, 'r') as file:
                nft_metadata = json.load(file)
            logger.info("Continuing from previously saved progress.")
        except Exception as e:
            logger.error(f"Error loading processed data: {e}")
            return
    else:
        try:
            with open('nft_metadata_with_rarity.json', 'r') as file:
                nft_metadata = json.load(file)
                logger.info("Starting from the beginning as no progress file found.")
        except Exception as e:
            logger.error(f"Error loading initial data: {e}")
            return

    # Determine where to start processing
    start_index = find_start_index(nft_metadata)
    end_index = min(start_index + 100, len(nft_metadata))

    for index in range(start_index, end_index):
        item = nft_metadata[index]
        logger.info(f"Processing item {index + 1}/{len(nft_metadata)} with account: {item.get('account', 'Unknown')}")
        driver = driversetup(logger)

        try:
            process_item(item, driver, logger)
        except Exception as e:
            logger.error(f"Error processing item with account {item.get('account', 'Unknown')}: {e}")
        finally:
            driver.quit()
            logger.info(f"WebDriver closed for item {index + 1}")

    try:
        with open(processed_data_file, 'w') as file:
            json.dump(nft_metadata, file, indent=4)
            logger.info("Progress saved.")
    except Exception as e:
        logger.error(f"An error occurred while saving the progress: {e}")

if __name__ == '__main__':
    main()

```

</details>

<details>
  <summary>CLICK TO EXPAND JSON Output</summary>

```json
[
    {
        "account": "DYTo4wYJDA2tRkD3kMzthDY3rrnyWMgSFrBc3TtiSjQq",
        "onChainAccountInfo": {
            "accountInfo": {
                "key": "DYTo4wYJDA2tRkD3kMzthDY3rrnyWMgSFrBc3TtiSjQq",
                "isSigner": false,
                "isWritable": false,
                "lamports": 1461600,
                "data": {
                    "parsed": {
                        "info": {
                            "decimals": 0,
                            "freezeAuthority": "62q7i8DMds7SAPSjnShQKHjacZd29421XH4qnNad5xGK",
                            "isInitialized": true,
                            "mintAuthority": "62q7i8DMds7SAPSjnShQKHjacZd29421XH4qnNad5xGK",
                            "supply": "1"
                        },
                        "type": "mint"
                    },
                    "program": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA",
                    "space": 82
                },
                "owner": "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA",
                "executable": false,
                "rentEpoch": 361
            },
            "error": ""
        },
        "onChainMetadata": {
            "metadata": {
                "tokenStandard": "NonFungible",
                "key": "MetadataV1",
                "updateAuthority": "6DMG9hv3eR8BXKH79sXGyQtfRSxXfNrkHEdc6nCsEjVK",
                "mint": "DYTo4wYJDA2tRkD3kMzthDY3rrnyWMgSFrBc3TtiSjQq",
                "data": {
                    "name": "Arctic Fox #41",
                    "symbol": "AFAF",
                    "uri": "https://m5brw73kei7uoysb7gxdomaxbdqobnz27j65nrq7ohbpgrktfjmq.arweave.net/Z0Mbf2oiP0diQfmuNzAXCODgtzr6fdbGH3HC80VTKlk",
                    "sellerFeeBasisPoints": 1500,
                    "creators": [
                        {
                            "address": "79iAsPyGDhQ7Sw5HcSkhYX9b3tzXp4phxjfPdo9xkmx1",
                            "verified": true,
                            "share": 0
                        },
                        {
                            "address": "2wBMxuAYKiVjQFGB48bhHPexNRyeHcDN1aaYT4WYv5r5",
                            "verified": true,
                            "share": 54
                        },
                        {
                            "address": "8XzUgMAhFZWERytRDNVBdL95LL5Ftox72EiSNzTu63QS",
                            "verified": true,
                            "share": 46
                        }
                    ]
                },
                "primarySaleHappened": true,
                "isMutable": true,
                "editionNonce": 255,
                "uses": {
                    "useMethod": "",
                    "remaining": 0,
                    "total": 0
                },
                "collection": {
                    "key": "EFjksSb2b897hvxuHXrnVoE2y66iufiJxtDSgFJZYQna",
                    "verified": true
                },
                "collectionDetails": null
            },
            "error": ""
        },
        "offChainMetadata": {
            "metadata": {
                "attributes": [
                    {
                        "traitType": "Arctic Animal",
                        "value": "Fox"
                    },
                    {
                        "traitType": "Endangered",
                        "value": "No"
                    },
                    {
                        "traitType": "Paw",
                        "value": "Left-Up"
                    },
                    {
                        "traitType": "Eyes",
                        "value": "Heterochromia"
                    },
                    {
                        "traitType": "Mouth",
                        "value": "Blep"
                    }
                ],
                "description": "An exclusive family, 69 #SolanaNFTs per collection. Liquidity adding for rewarding #ArcticFrenz.",
                "image": "https://arweave.net/p5C032iu3UQ4Lpr5cTNlcW8bVDrcVd872QChc3z8J-4?ext=png",
                "name": "Arctic Fox #41",
                "properties": {
                    "category": null,
                    "creators": [
                        {
                            "address": "2wBMxuAYKiVjQFGB48bhHPexNRyeHcDN1aaYT4WYv5r5",
                            "share": 54
                        },
                        {
                            "address": "8XzUgMAhFZWERytRDNVBdL95LL5Ftox72EiSNzTu63QS",
                            "share": 46
                        }
                    ],
                    "files": [
                        {
                            "type": "image/png",
                            "uri": "40.png"
                        }
                    ]
                },
                "sellerFeeBasisPoints": 1500,
                "symbol": "AFAF"
            },
            "uri": "https://m5brw73kei7uoysb7gxdomaxbdqobnz27j65nrq7ohbpgrktfjmq.arweave.net/Z0Mbf2oiP0diQfmuNzAXCODgtzr6fdbGH3HC80VTKlk",
            "error": ""
        },
        "legacyMetadata": null,
        "rarity_score": 0.1473389390210555,
        "holder data": [
            {
                "holder": "Ar3Tqj2DVr2WoLmKmG5aFo17Quh33zKWcCMUibKzrgK3"
            },
            {
                "when acquired": 1644640715
            },
            {
                "time checked": 1700666552
            }
        ]
    },
    {
        "_comment": "The file has been truncated for this example. The output JSON file will include all NFTs in the collection along with the respective holder's public keys and the timestamp indicating when they acquired the NFT."
    }
]
```

</details>

### Step 3: Automated Monitoring of NFT Holders within a Collection on a Recurring Schedule

1. **Create a YAML File**: Create a YAML file for the script, e.g., `main.yml`.

2. **Define the Workflow**:
   - **Trigger**: Use the `schedule` event to run at specific times.
   - **Jobs and Steps**: Define a job that runs the script. Include steps for setting up Python, installing dependencies, and executing the script.

3. **Handling Dependencies**:
   - **Chromedriver and Google Chrome**: The script uses Selenium with Chrome, Chrome and Chromedriver need to be set up in the environment.

4. **Handle Data and Logs**: Handle data storage and logging within the environment - adjust file paths. 

This YAML:
- Runs the workflow every 4 hours.
- Sets up the latest Ubuntu environment.
- Checks out the script.
- Sets up Python.
- Installs Chrome and Chromedriver.
- Installs the required Python packages.
- Runs Python script.

<details>
  <summary>CLICK TO EXPAND YAML File</summary>

```yaml
name: NAME Runner

on:
  schedule:
    - cron: '0 */4 * * *'  # Runs every 4 hours

jobs:
  run-script:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.8' 

    - name: Install Chrome and Chromedriver
      run: |
        sudo apt-get update
        sudo apt-get install -y google-chrome-stable
        CHROME_VERSION=$(google-chrome --version | grep -oE "[0-9]+\.[0-9]+\.[0-9]+")
        CHROMEDRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION")
        wget -N "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip" -P ~/
        unzip ~/chromedriver_linux64.zip -d ~/
        sudo mv -f ~/chromedriver /usr/local/share/
        sudo chmod +x /usr/local/share/chromedriver
        sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver

    - name: Install Python dependencies
      run: pip install selenium bs4 psutil

    - name: Run script
      run: python enhance_NAME_metadata.py

```

</details>

Ensure that the output file from **Part 3, Step 2** or from **Part 2** is in the directory. 

<details>
  <summary>CLICK TO EXPAND Python Script</summary>

```python

 # WIP

``` 

</details>

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

### Step 6: Make a Batched API Request 

Open your development environment, create a variable named `apikey`. Paste your API Key from [Part 1, Step 5](https://github.com/davidbeard741/arcticfrenz-data#step-5-helius) into the variable 

```PYTHON
apikey = "INSERT YOUR API KEY BETWEEN THESE QUOTATION MARKS"
```

Copy and paste the code below into your development environement. 

```PYTHON
import requests
import json

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

### Step 7: Run the Code

Below is the complete code. Execute it to generate a file named 'nft_metadata.json' that will include the metadata each NFT in the collection.

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

### The Output JSON File

The JSON is truncated for illustrative purposes; the 'nft_metadata' output file will encompass all NFTs in the collection.

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

---

## Part 2: Enhancing the Metadata of an Entire NFT Collection with Additional Data

### Step 1: Setting Up Your Python Development Environment

Refer to [Part 1, Step 3](https://github.com/davidbeard741/arcticfrenz-data#step-3-set-up-your-python-development-environment) for the setup instructions.

### Step 2: Fetching the Web Page

Start by briefly examining the structure of the HTML, which will enable effective navigation through the parse tree in subsequent steps.

```python
import requests

# The URL of the page you want to parse
URL = "[https://realpython.github.io/fake-jobs/](https://solana.fm/address/DYTo4wYJDA2tRkD3kMzthDY3rrnyWMgSFrBc3TtiSjQq?mode=lite&cluster=mainnet-solanafmbeta)"

page = requests.get(URL)

print(page.text)
```

### Step 3: Parsing HTML with Beautiful Soup

To work with the data from the fetched HTML page, we'll use [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/), a Python library that simplifies web scraping by converting HTML and XML documents into a parse tree. This tree is easy to navigate, which is helpful for data extraction and manipulation.

If you haven't installed Beautiful Soup yet, open your terminal and run the following command:

```shell
pip install beautifulsoup4
```

Save the body of the HTML to a file

```html
# Import the Requests library for making HTTP requests
import requests
# Import BeautifulSoup for parsing HTML
from bs4 import BeautifulSoup

# set the URL to parse
URL = "https://solana.fm/address/DYTo4wYJDA2tRkD3kMzthDY3rrnyWMgSFrBc3TtiSjQq?mode=lite&cluster=mainnet-solanafmbeta"

# Fetch the page
page = requests.get(URL)

# Parse the page content using BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')

# Find the body tag
body = soup.find('body')

# If the body tag was found, write its contents to a file
if body:
    with open("htmlbody.html", "w", encoding='utf-8') as f:
        f.write(str(body))
else:
    print("No body tag found in the HTML.")
```

Output saved as 'htmlbody.html': 

```html
<body>
    <div id="__next">
        <div>
            <div class="modal-backdrop fade disable-pointer-events"></div>
        </div>
        <div class="main-content pb-4 bg-blue-800">
            <nav class="flex navbar-background h-[60px] sticky top-0 z-40 p-3 py-3">
                <div class="container flex items-center md:px-0 false">
                    <div class="container hidden md:block">
                        <div class="flex justify-between gap-5 items-center">
                            <div class="flex w-8/12 items-center justify-start"><a class="hidden md:block pt-3"
                                    href="/"><span
                                        style="box-sizing:border-box;display:inline-block;overflow:hidden;width:initial;height:initial;background:none;opacity:1;border:0;margin:0;padding:0;position:relative;max-width:100%"><span
                                            style="box-sizing:border-box;display:block;width:initial;height:initial;background:none;opacity:1;border:0;margin:0;padding:0;max-width:100%"><img
                                                alt="" aria-hidden="true"
                                                src="data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27120%27%20height=%2736%27/%3e"
                                                style="display:block;max-width:100%;width:initial;height:initial;background:none;opacity:1;border:0;margin:0;padding:0" /></span><img
                                            alt="SolanaFM Explorer" data-nimg="intrinsic" decoding="async"
                                            src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"
                                            style="position:absolute;top:0;left:0;bottom:0;right:0;box-sizing:border-box;padding:0;border:none;margin:auto;display:block;width:0;height:0;min-width:100%;max-width:100%;min-height:100%;max-height:100%" /><noscript><img
                                                alt="SolanaFM Explorer" data-nimg="intrinsic" decoding="async"
                                                loading="lazy" src="/_next/static/media/solanafm-beta.be5d4b54.svg"
                                                srcset="/_next/static/media/solanafm-beta.be5d4b54.svg 1x, /_next/static/media/solanafm-beta.be5d4b54.svg 2x"
                                                style="position:absolute;top:0;left:0;bottom:0;right:0;box-sizing:border-box;padding:0;border:none;margin:auto;display:block;width:0;height:0;min-width:100%;max-width:100%;min-height:100%;max-height:100%" /></noscript></span></a>
                            </div>
                        </div>
                    </div>
                    <div class="w-full md:hidden">
                        <div class="w-full flex justify-between items-center py-2">
                            <div class="grow"><a class="" href="/"><span
                                        style="box-sizing:border-box;display:inline-block;overflow:hidden;width:initial;height:initial;background:none;opacity:1;border:0;margin:0;padding:0;position:relative;max-width:100%"><span
                                            style="box-sizing:border-box;display:block;width:initial;height:initial;background:none;opacity:1;border:0;margin:0;padding:0;max-width:100%"><img
                                                alt="" aria-hidden="true"
                                                src="data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%2740%27%20height=%2740%27/%3e"
                                                style="display:block;max-width:100%;width:initial;height:initial;background:none;opacity:1;border:0;margin:0;padding:0" /></span><img
                                            alt="SolanaFM Explorer" data-nimg="intrinsic" decoding="async"
                                            src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"
                                            style="position:absolute;top:0;left:0;bottom:0;right:0;box-sizing:border-box;padding:0;border:none;margin:auto;display:block;width:0;height:0;min-width:100%;max-width:100%;min-height:100%;max-height:100%" /><noscript><img
                                                alt="SolanaFM Explorer" data-nimg="intrinsic" decoding="async"
                                                loading="lazy"
                                                src="/_next/static/media/solanafm-icon-white.61bea9a0.svg"
                                                srcset="/_next/static/media/solanafm-icon-white.61bea9a0.svg 1x, /_next/static/media/solanafm-icon-white.61bea9a0.svg 2x"
                                                style="position:absolute;top:0;left:0;bottom:0;right:0;box-sizing:border-box;padding:0;border:none;margin:auto;display:block;width:0;height:0;min-width:100%;max-width:100%;min-height:100%;max-height:100%" /></noscript></span></a>
                            </div>
                            <div class="flex items-center"></div>
                        </div>
                    </div>
                    <div class="flex gap-10 whitespace-nowrap items-center">
                        <div class="hidden md:block"><a href="https://early.solana.fm" target="_blank"><button
                                    class="flex items-center gap-2 font-semibold h-12 w-[102px] py-3 px-2 hover:border-b-2 hover:border-b-primary hover:delay-100">
                                    <div class="relative w-full h-6 my-3"><span
                                            style="box-sizing:border-box;display:block;overflow:hidden;width:initial;height:initial;background:none;opacity:1;border:0;margin:0;padding:0;position:absolute;top:0;left:0;bottom:0;right:0"><img
                                                alt="Quantum Logo" class="rounded-lg shadow-lg aspect-auto"
                                                data-nimg="fill" decoding="async"
                                                src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"
                                                style="position:absolute;top:0;left:0;bottom:0;right:0;box-sizing:border-box;padding:0;border:none;margin:auto;display:block;width:0;height:0;min-width:100%;max-width:100%;min-height:100%;max-height:100%" /><noscript><img
                                                    alt="Quantum Logo" class="rounded-lg shadow-lg aspect-auto"
                                                    data-nimg="fill" decoding="async" loading="lazy" sizes="100vw"
                                                    src="/img/quantum-new-logo.svg"
                                                    srcset="/img/quantum-new-logo.svg 640w, /img/quantum-new-logo.svg 750w, /img/quantum-new-logo.svg 828w, /img/quantum-new-logo.svg 1080w, /img/quantum-new-logo.svg 1200w, /img/quantum-new-logo.svg 1920w, /img/quantum-new-logo.svg 2048w, /img/quantum-new-logo.svg 3840w"
                                                    style="position:absolute;top:0;left:0;bottom:0;right:0;box-sizing:border-box;padding:0;border:none;margin:auto;display:block;width:0;height:0;min-width:100%;max-width:100%;min-height:100%;max-height:100%" /></noscript></span>
                                    </div>
                                </button></a></div>
                        <div class="hidden md:block"><a class="text-white"
                                href="/openbook/8BnEgHoWFysVcuFFX7QztDmzuH8r5ZFvyP3sYwn1XTh6"><button
                                    class="flex items-center gap-2 font-semibold h-12 px-2 hover:border-b-2 hover:border-b-primary hover:delay-100">
                                    <div class="relative h-7 w-7"><span
                                            style="box-sizing:border-box;display:block;overflow:hidden;width:initial;height:initial;background:none;opacity:1;border:0;margin:0;padding:0;position:absolute;top:0;left:0;bottom:0;right:0"><img
                                                alt="Openbook Logo" data-nimg="fill" decoding="async"
                                                src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"
                                                style="position:absolute;top:0;left:0;bottom:0;right:0;box-sizing:border-box;padding:0;border:none;margin:auto;display:block;width:0;height:0;min-width:100%;max-width:100%;min-height:100%;max-height:100%" /><noscript><img
                                                    alt="Openbook Logo" data-nimg="fill" decoding="async" loading="lazy"
                                                    sizes="100vw" src="/_next/static/media/OB_Icon.b7f34424.svg"
                                                    srcset="/_next/static/media/OB_Icon.b7f34424.svg 640w, /_next/static/media/OB_Icon.b7f34424.svg 750w, /_next/static/media/OB_Icon.b7f34424.svg 828w, /_next/static/media/OB_Icon.b7f34424.svg 1080w, /_next/static/media/OB_Icon.b7f34424.svg 1200w, /_next/static/media/OB_Icon.b7f34424.svg 1920w, /_next/static/media/OB_Icon.b7f34424.svg 2048w, /_next/static/media/OB_Icon.b7f34424.svg 3840w"
                                                    style="position:absolute;top:0;left:0;bottom:0;right:0;box-sizing:border-box;padding:0;border:none;margin:auto;display:block;width:0;height:0;min-width:100%;max-width:100%;min-height:100%;max-height:100%" /></noscript></span>
                                    </div>Openbook
                                </button></a></div>
                        <div class="hidden md:block"><a class="text-white" href="/blocks"><button
                                    class="flex items-center gap-2 font-semibold h-12 px-2 hover:border-b-2 hover:border-b-primary hover:delay-100"><svg
                                        class="h-5 w-5 text-primary" fill="none" height="24" stroke="currentColor"
                                        stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
                                        <path d="M0 0h24v24H0z" fill="none" stroke="none"></path>
                                        <path d="M6 17.6l-2 -1.1v-2.5"></path>
                                        <path d="M4 10v-2.5l2 -1.1"></path>
                                        <path d="M10 4.1l2 -1.1l2 1.1"></path>
                                        <path d="M18 6.4l2 1.1v2.5"></path>
                                        <path d="M20 14v2.5l-2 1.12"></path>
                                        <path d="M14 19.9l-2 1.1l-2 -1.1"></path>
                                        <line x1="12" x2="14" y1="12" y2="10.9"></line>
                                        <line x1="18" x2="20" y1="8.6" y2="7.5"></line>
                                        <line x1="12" x2="12" y1="12" y2="14.5"></line>
                                        <line x1="12" x2="12" y1="18.5" y2="21"></line>
                                        <path d="M12 12l-2 -1.12"></path>
                                        <line x1="6" x2="4" y1="8.6" y2="7.5"></line>
                                    </svg>Blocks</button></a></div><button
                            class="flex rounded-[16px] w-[88px] h-[44px] bg-blue-700 p-2 items-center justify-center">
                            <div class="bg-blue-800 relative w-7 h-7 rounded-full border-4 border-blue-800"><span
                                    style="box-sizing:border-box;display:block;overflow:hidden;width:initial;height:initial;background:none;opacity:1;border:0;margin:0;padding:0;position:absolute;top:0;left:0;bottom:0;right:0"><img
                                        class="rounded-full" data-nimg="fill" decoding="async"
                                        src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"
                                        style="position:absolute;top:0;left:0;bottom:0;right:0;box-sizing:border-box;padding:0;border:none;margin:auto;display:block;width:0;height:0;min-width:100%;max-width:100%;min-height:100%;max-height:100%" /><noscript><img
                                            class="rounded-full" data-nimg="fill" decoding="async" loading="lazy"
                                            sizes="100vw" src="/img/account-icon.svg"
                                            srcset="/img/account-icon.svg 640w, /img/account-icon.svg 750w, /img/account-icon.svg 828w, /img/account-icon.svg 1080w, /img/account-icon.svg 1200w, /img/account-icon.svg 1920w, /img/account-icon.svg 2048w, /img/account-icon.svg 3840w"
                                            style="position:absolute;top:0;left:0;bottom:0;right:0;box-sizing:border-box;padding:0;border:none;margin:auto;display:block;width:0;height:0;min-width:100%;max-width:100%;min-height:100%;max-height:100%" /></noscript></span>
                            </div>
                            <div class="pl-4"><svg class="h-6 w-6" fill="none" height="24" stroke="currentColor"
                                    stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24"
                                    width="24" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M0 0h24v24H0z" fill="none" stroke="none"></path>
                                    <line x1="4" x2="20" y1="6" y2="6"></line>
                                    <line x1="4" x2="20" y1="12" y2="12"></line>
                                    <line x1="4" x2="20" y1="18" y2="18"></line>
                                </svg></div>
                        </button>
                    </div>
                </div>
            </nav>
            <div class="container my-4">
                <div
                    class="flex items-center bg-blue-700 rounded-xl relative transition-colors duration-300 border-2 border-blue-700 false w-full">
                    <div class="flex-grow input-group items-center searchbar--input px-3 mt-0 flex flex-row"><input
                            class="form-control outline-none w-full pl-2 placeholder:text-gray-500 bg-transparent h-14 placeholder:opacity-75 rounded-xl border-0"
                            placeholder="Search by address, transaction hash, block or token" type="text"
                            value="" /><span class="pl-3">
                            <div class="flex items-center rounded-lg">
                                <div class="flex-1 text-center bg-blue-800 px-4 py-2 rounded-lg"><span class=""
                                        style="opacity:0.3">F</span></div>
                            </div>
                        </span></div>
                </div>
            </div>
            <div class="mx-2 sm:mx-4 md:m-0"></div>
        </div>
        <footer class="w-auto container m-auto overflow-y-auto bg-blue-800">
            <div class="md:my-20 my-4 md:mx-8 p-4 flex md:flex-row flex-col gap-10 items-start justify-between"><a
                    href="/"><span
                        style="box-sizing:border-box;display:inline-block;overflow:hidden;width:initial;height:initial;background:none;opacity:1;border:0;margin:0;padding:0;position:relative;max-width:100%"><span
                            style="box-sizing:border-box;display:block;width:initial;height:initial;background:none;opacity:1;border:0;margin:0;padding:0;max-width:100%"><img
                                alt="" aria-hidden="true"
                                src="data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27155%27%20height=%2739%27/%3e"
                                style="display:block;max-width:100%;width:initial;height:initial;background:none;opacity:1;border:0;margin:0;padding:0" /></span><img
                            alt="SolanaFM" class="inline-block" data-nimg="intrinsic" decoding="async"
                            src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"
                            style="position:absolute;top:0;left:0;bottom:0;right:0;box-sizing:border-box;padding:0;border:none;margin:auto;display:block;width:0;height:0;min-width:100%;max-width:100%;min-height:100%;max-height:100%" /><noscript><img
                                alt="SolanaFM" class="inline-block" data-nimg="intrinsic" decoding="async"
                                loading="lazy" src="/_next/static/media/dark-explorer-logo.4bfba811.svg"
                                srcset="/_next/static/media/dark-explorer-logo.4bfba811.svg 1x, /_next/static/media/dark-explorer-logo.4bfba811.svg 2x"
                                style="position:absolute;top:0;left:0;bottom:0;right:0;box-sizing:border-box;padding:0;border:none;margin:auto;display:block;width:0;height:0;min-width:100%;max-width:100%;min-height:100%;max-height:100%" /></noscript></span></a>
                <div class="flex lg:flex-row flex-col lg:gap-24 gap-6 text-white">
                    <div class="flex flex-col gap-6">
                        <div>Developers</div>
                        <div class="flex flex-col gap-3 text-white">
                            <div><a href="https://docs.solana.fm" id="heap-documentation-footer" rel="noreferrer"
                                    target="_blank">Documentation</a></div>
                            <div><a href="https://solanafm.canny.io/changelog" id="heap-documentation-footer"
                                    rel="noreferrer" target="_blank">Changelog</a></div>
                        </div>
                    </div>
                </div>
            </div>
            <hr class="text-secondary" />
            <div
                class="py-6 flex lg:flex-row flex-col justify-between lg:items-center items-start gap-4 px-4 md:px-0 mx-0 border-gray-200 border-t border-opacity-30">
                <div class="flex flex-row gap-10 items-center">
                    <div class="text-xs text-gray-400">Copyright © 2022</div>
                </div>
                <div class="flex flex-row gap-3 items-center"><a
                        class="flex items-center justify-center bg-blue-700 text-white rounded-full w-10 h-10"
                        href="https://twitter.com/solanafm" rel="noreferrer" target="_blank"><i
                            class="w-5 h-5 m-auto text-center"><svg aria-hidden="true"
                                class="svg-inline--fa fa-twitter w-full h-full" data-icon="twitter" data-prefix="fab"
                                focusable="false" role="img" viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
                                <path
                                    d="M459.4 151.7c.325 4.548 .325 9.097 .325 13.65 0 138.7-105.6 298.6-298.6 298.6-59.45 0-114.7-17.22-161.1-47.11 8.447 .974 16.57 1.299 25.34 1.299 49.06 0 94.21-16.57 130.3-44.83-46.13-.975-84.79-31.19-98.11-72.77 6.498 .974 12.99 1.624 19.82 1.624 9.421 0 18.84-1.3 27.61-3.573-48.08-9.747-84.14-51.98-84.14-102.1v-1.299c13.97 7.797 30.21 12.67 47.43 13.32-28.26-18.84-46.78-51.01-46.78-87.39 0-19.49 5.197-37.36 14.29-52.95 51.65 63.67 129.3 105.3 216.4 109.8-1.624-7.797-2.599-15.92-2.599-24.04 0-57.83 46.78-104.9 104.9-104.9 30.21 0 57.5 12.67 76.67 33.14 23.72-4.548 46.46-13.32 66.6-25.34-7.798 24.37-24.37 44.83-46.13 57.83 21.12-2.273 41.58-8.122 60.43-16.24-14.29 20.79-32.16 39.31-52.63 54.25z"
                                    fill="currentColor"></path>
                            </svg></i></a><a
                        class="flex items-center justify-center bg-blue-700 text-white rounded-full w-10 h-10"
                        href="https://discord.gg/QqcBJcf274" rel="noreferrer" target="_blank"><i
                            class="w-5 h-5 m-auto text-center"><svg aria-hidden="true"
                                class="svg-inline--fa fa-discord w-full h-full" data-icon="discord" data-prefix="fab"
                                focusable="false" role="img" viewbox="0 0 640 512" xmlns="http://www.w3.org/2000/svg">
                                <path
                                    d="M524.5 69.84a1.5 1.5 0 0 0 -.764-.7A485.1 485.1 0 0 0 404.1 32.03a1.816 1.816 0 0 0 -1.923 .91 337.5 337.5 0 0 0 -14.9 30.6 447.8 447.8 0 0 0 -134.4 0 309.5 309.5 0 0 0 -15.14-30.6 1.89 1.89 0 0 0 -1.924-.91A483.7 483.7 0 0 0 116.1 69.14a1.712 1.712 0 0 0 -.788 .676C39.07 183.7 18.19 294.7 28.43 404.4a2.016 2.016 0 0 0 .765 1.375A487.7 487.7 0 0 0 176 479.9a1.9 1.9 0 0 0 2.063-.676A348.2 348.2 0 0 0 208.1 430.4a1.86 1.86 0 0 0 -1.019-2.588 321.2 321.2 0 0 1 -45.87-21.85 1.885 1.885 0 0 1 -.185-3.126c3.082-2.309 6.166-4.711 9.109-7.137a1.819 1.819 0 0 1 1.9-.256c96.23 43.92 200.4 43.92 295.5 0a1.812 1.812 0 0 1 1.924 .233c2.944 2.426 6.027 4.851 9.132 7.16a1.884 1.884 0 0 1 -.162 3.126 301.4 301.4 0 0 1 -45.89 21.83 1.875 1.875 0 0 0 -1 2.611 391.1 391.1 0 0 0 30.01 48.81 1.864 1.864 0 0 0 2.063 .7A486 486 0 0 0 610.7 405.7a1.882 1.882 0 0 0 .765-1.352C623.7 277.6 590.9 167.5 524.5 69.84zM222.5 337.6c-28.97 0-52.84-26.59-52.84-59.24S193.1 219.1 222.5 219.1c29.67 0 53.31 26.82 52.84 59.24C275.3 310.1 251.9 337.6 222.5 337.6zm195.4 0c-28.97 0-52.84-26.59-52.84-59.24S388.4 219.1 417.9 219.1c29.67 0 53.31 26.82 52.84 59.24C470.7 310.1 447.5 337.6 417.9 337.6z"
                                    fill="currentColor"></path>
                            </svg></i></a><a
                        class="flex items-center justify-center bg-blue-700 rounded-full text-white w-10 h-10"
                        href="https://www.linkedin.com/company/solanafm/" rel="noreferrer" target="_blank"><i
                            class="w-5 h-5 text-center"><svg aria-hidden="true"
                                class="svg-inline--fa fa-linkedin w-full h-full" data-icon="linkedin" data-prefix="fab"
                                focusable="false" role="img" viewbox="0 0 448 512" xmlns="http://www.w3.org/2000/svg">
                                <path
                                    d="M416 32H31.9C14.3 32 0 46.5 0 64.3v383.4C0 465.5 14.3 480 31.9 480H416c17.6 0 32-14.5 32-32.3V64.3c0-17.8-14.4-32.3-32-32.3zM135.4 416H69V202.2h66.5V416zm-33.2-243c-21.3 0-38.5-17.3-38.5-38.5S80.9 96 102.2 96c21.2 0 38.5 17.3 38.5 38.5 0 21.3-17.2 38.5-38.5 38.5zm282.1 243h-66.4V312c0-24.8-.5-56.7-34.5-56.7-34.6 0-39.9 27-39.9 54.9V416h-66.4V202.2h63.7v29.2h.9c8.9-16.8 30.6-34.5 62.9-34.5 67.2 0 79.7 44.3 79.7 101.9V416z"
                                    fill="currentColor"></path>
                            </svg></i></a><a
                        class="flex items-center justify-center bg-blue-700 rounded-full text-white w-10 h-10"
                        href="https://solanafm.substack.com/" rel="noreferrer" target="_blank"><i
                            class="relative w-4 h-4 text-center"><span
                                style="box-sizing:border-box;display:block;overflow:hidden;width:initial;height:initial;background:none;opacity:1;border:0;margin:0;padding:0;position:absolute;top:0;left:0;bottom:0;right:0"><img
                                    data-nimg="fill" decoding="async"
                                    src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"
                                    style="position:absolute;top:0;left:0;bottom:0;right:0;box-sizing:border-box;padding:0;border:none;margin:auto;display:block;width:0;height:0;min-width:100%;max-width:100%;min-height:100%;max-height:100%" /><noscript><img
                                        data-nimg="fill" decoding="async" loading="lazy" sizes="100vw"
                                        src="/_next/static/media/SubstackLogo.9cd51042.svg"
                                        srcset="/_next/static/media/SubstackLogo.9cd51042.svg 640w, /_next/static/media/SubstackLogo.9cd51042.svg 750w, /_next/static/media/SubstackLogo.9cd51042.svg 828w, /_next/static/media/SubstackLogo.9cd51042.svg 1080w, /_next/static/media/SubstackLogo.9cd51042.svg 1200w, /_next/static/media/SubstackLogo.9cd51042.svg 1920w, /_next/static/media/SubstackLogo.9cd51042.svg 2048w, /_next/static/media/SubstackLogo.9cd51042.svg 3840w"
                                        style="position:absolute;top:0;left:0;bottom:0;right:0;box-sizing:border-box;padding:0;border:none;margin:auto;display:block;width:0;height:0;min-width:100%;max-width:100%;min-height:100%;max-height:100%" /></noscript></span></i></a>
                </div>
            </div>
        </footer>
        <div style="position:fixed;z-index:9999;top:16px;left:16px;right:16px;bottom:16px;pointer-events:none"></div>
    </div>
    <script id="__NEXT_DATA__"
        type="application/json">{"props":{"pageProps":{}},"page":"/address/[...address]","query":{},"buildId":"1dJr2PshwetVJ5MiRophB","nextExport":true,"autoExport":true,"isFallback":false,"scriptLoader":[]}</script>
</body>
```

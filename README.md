# Arctic Frenz Discord Bot Data Repository

The Arctic Frenz Data Repository offers a comprehensive collection of NFT analytics tailored for the Arctic Frenz Bot. This includes detailed information on asset ownership duration, listing status, quantity, and rarity. The repository provides streamlined access to ranking checks and metadata, enriching the community experience. Furthermore, collections can harness this data to incentivize and bolster community interaction within Discord.

![Arctic Frenz Visualization](https://raw.githubusercontent.com/davidbeard741/arcticfrenz-data/main/images/IMG_3153.gif)

## Get NFT Metadata for the entire  Collection: A Step-by-Step Guide

### Step 1: Get Creator Address of the Collection 

- Find an NFT that is part of the collection on [Magic Eden](https://magiceden.io).

- Open the NFT's Mint Address in [Solscan](https://solscan.io).
![Magic Eden](https://raw.githubusercontent.com/davidbeard741/arcticfrenz-data/main/images/3B369D54-BACD-4747-9AC7-9A5026257145.jpeg)

- Click on the "Creators" tab and select the first address that appears, with a 0% and a blue tick. 
![Find Creator Address](https://raw.githubusercontent.com/davidbeard741/arcticfrenz-data/main/images/0D636107-2D85-4DBD-849D-E19A2B647338.jpeg)

- Copy the account's address
![Find Creator Address](https://raw.githubusercontent.com/davidbeard741/arcticfrenz-data/main/images/CC753005-3372-463E-97A9-D8E0710BC5A3.jpeg)

### Step 2: Get Collection's Hash List

- Go to [Smithii | Hash List NFT Solana](https://tools.smithii.io/hashlist/solana)
- Enter the Creator Address from Step 1
- Click on 'Get hash list'
- Wait! The hash list process will take a couple of minutes.
- Copy the hash list

### Step 3: Create a Python Development Environment using:

- [Google Colab](https://colab.research.google.com) notebooks are Jupyter notebooks that run in the cloud. The example below will use Google Colab.
- [JupyterLab](https://jupyter.org/) is the latest web-based interactive development environment for notebooks, code, and data.
- Local Environment on [Windows](https://realpython.com/python-coding-setup-windows/), on [macOS](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-macos), or on [Linux/Unix](https://itsfoss.com/python-setup-linux/) Systems.

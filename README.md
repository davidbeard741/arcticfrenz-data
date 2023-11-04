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

## How to Retrieve NFT Metadata for an Entire Collection

Below is a structured guide to assist you in fetching metadata for any NFT collection.

### Step 1: Identify the Creator Address

<table align="center">
	<tr>
		<td>
			1. Visit [Magic Eden](https://magiceden.io) and select an NFT from the collection you are interested in.
		</td>
	</tr>
	<tr>
		<td>
			2. Navigate to the NFT's detail page and locate its Mint Address, then proceed to [Solscan](https://solscan.io).
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
2. Paste the Creator Address obtained from Step 1 into the provided field.
3. Click 'Get hash list' to generate the list.
4. Please be patient, as generating the hash list may take a few minutes.
5. Once the list is available, copy or save the list for Step 4.

### Step 3: Set Up Your Python Development Environment

Choose one of the following environments for your Python development needs:

- **Google Colab**: Utilize [Google Colab](https://colab.research.google.com) for a cloud-based Jupyter notebook experience that does not require any local setup.
- **JupyterLab**: For a more advanced setup, [JupyterLab](https://jupyter.org/) provides a comprehensive development environment to work with notebooks, code, and data.
- **Local Environment**: Set up your development environment locally on various operating systems:
  - [Windows Setup Guide](https://realpython.com/python-coding-setup-windows/)
  - [macOS Setup Guide](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-macos)
  - [Linux/Unix Setup Guide](https://itsfoss.com/python-setup-linux/)

### Step 4: Get Metadata for each NFT in the Collection

```
# Code
```

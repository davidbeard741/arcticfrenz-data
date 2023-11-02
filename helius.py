import requests
import json

url = "https://api.helius.xyz/v0/token-metadata?api-key=<your-key>"
nft_addresses = [
    "BAAzgRGWY2v5AJBNZNFd2abiRXAUo56UxywKEjoCZW2",
    "8s6kQUZfdm7GSaThAcsmSs56wMinXrbk6SdNVngutrz5"
]  # Monkes

def get_metadata():
    payload = {
        "mintAccounts": nft_addresses,
        "includeOffChain": True,
        "disableCache": False
    }
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        print("metadata:", data)
    else:
        print(f"Failed to retrieve metadata: {response.status_code}")

get_metadata()
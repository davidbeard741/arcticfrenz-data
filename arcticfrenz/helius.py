import requests
import json

url = "https://mainnet.helius-rpc.com/?api-key=4fd44b3c-8002-413c-a2d6-e956976bf5c2"
nft_addresses = [
    "BAAzgRGWY2v5AJBNZNFd2abiRXAUo56UxywKEjoCZW2",
    "8s6kQUZfdm7GSaThAcsmSs56wMinXrbk6SdNVngutrz5"
]

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
        print("Metadata successfully retrieved. Writing to file.")
        with open('nft_metadata.json', 'w') as file:
            json.dump(data, file, indent=4)
            print("Data written to nft_metadata.json")

    else:
        print(f"Failed to retrieve metadata: {response.status_code}")

get_metadata()

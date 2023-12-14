import json
import re

def get_name(nft_name):
    try:
        return nft_name.rsplit(' ', 1)[0]
    except IndexError:
        return nft_name.split(' ', 1)[0]

def get_nft_number(nft_name):
    match = re.search(r'#(\d+)', nft_name)
    if match:
        return int(match.group(1))
    return 0

def rewrite_data(data):
  rewritten_data = []
  for item in data:
    nft_name = item["onChainMetadata"]["metadata"]["data"]["name"]
    nft_address = item["account"]
    rarity_score = item["rarity_score"]
    holder_data = {}
    if "holder data" in item:
        holder_data = {
            "holderAddress": item["holder data"][0]["holder"],
            "whenAcquired": item["holder data"][1]["when acquired"],
            "timeChecked": item["holder data"][2]["time checked"]
        }
    rewritten_data.append({
      "nftName": nft_name,
      "nftAddress": nft_address,
      "rarityScore": rarity_score,
      "holderData": holder_data,
    })
  return rewritten_data

with open("arcticfrenz/with_rarity_and_holder_data.json") as f:
  data = json.load(f)

naming = set([get_name(x["onChainMetadata"]["metadata"]["data"]["name"]) for x in data])
naming_order = sorted(list(naming))

rewritten_data = rewrite_data(data)
rewritten_data = sorted(rewritten_data, key=lambda x: (naming_order.index(get_name(x["nftName"])), get_nft_number(x["nftName"])))

with open("arcticfrenz/by-NFT.json", "w") as f:
  json.dump(rewritten_data, f, indent=4)

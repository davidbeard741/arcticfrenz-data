import json
import re
from datetime import datetime

with open('smb/by-NFT.json') as f:
    data = json.load(f)

holders = {}
for nft in data:
    holder_data = nft['holderData']
    if holder_data is None:
      continue
    holder_address = holder_data.get('holderAddress')  # Get the holderAddress
    if holder_address in ["Magic Eden V2 Authority", "4zdNGgAtFsW1cQgHqkiWyRsxaAgxrSRRynnuunxzjxue", "1BWutmTvYPwDtmw9abTkS4Ssr8no61spGAvW1X6NDix"]:
        continue
    if holder_data:
        holder_address = holder_data['holderAddress']
        if isinstance(holder_address, str):
            if not re.match(r'^[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{32,44}$', holder_address):
                continue
        if holder_address not in holders:
            holders[holder_address] = {
                "holderAddress": holder_address,
                "quantityNfts": 1,
                "holdingNfts": [{
                    "nftAddress": nft['nftAddress'],
                    "rarityScore": nft['rarityScore'],
                    "daysHeld": (datetime.utcnow() - datetime.utcfromtimestamp(holder_data['whenAcquired'])).days
                }]
            }
        else:
            holders[holder_address]['quantityNfts'] += 1
            holders[holder_address]['holdingNfts'].append({
                "nftAddress": nft['nftAddress'],
                "rarityScore": nft['rarityScore'],
                "daysHeld": (datetime.utcnow() - datetime.utcfromtimestamp(holder_data['whenAcquired'])).days
            })

result = sorted(holders.values(), key=lambda x: x["quantityNfts"], reverse=True)

with open('smb/by-holder.json', 'w') as f:
    json.dump(result, f, indent=4)

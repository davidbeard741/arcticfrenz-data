# `rank-holders_okay-bears.py`

### Date and Time Tuned (UTC):

2024-01-19 18:23:19

### Input:

`okay-bears/by-holder.json`: JSON file containing data on holders.

### Output:

`okay-bears/ranked-holders.json`: JSON file containing the ranked list of holders based on their calculated score.

### Collection Specific Values 

| Description | Value |
|---|---|
| **Weight given to the number of NFTs held** | 1.75 |
| **Weight given to rarity scores** | 0.045 |
| **Weight given to days held scores** | 1.8 |
| **Factor controlling the decay of score based on days held** | 0.1 |
| **The total number of NFTs owned by the individual with the largest NFT collection** | 148 |
| **The average rarity score of the owner who possesses the highest average rarity score** | 0.9998 |
| **The total duration held by the owner possessing the maximum cumulative duration of all NFTs they own** | 1171 |
| **Average Score of Holder's NFTs Owned** |  0.025958556595810135 |
| **Average Score of Holder's Rarity** | 0.025451811139761322 |
| **Average Score of Holder's Days Held** | 0.025959718851906736 |


### Script

```Python
import json
from datetime import date, datetime
import traceback
from math import exp
import numpy as np

try:
    with open('okay-bears/by-holder.json') as f:
        data = json.load(f)

    quantityNfts_weight = 1.75
    rarityScore_weight = 0.045
    daysHeld_weight = 1.8
    daysHeld_decay_factor = 0.1

    """
    print(f"Weight given to the number of NFTs held: {quantityNfts_weight}")
    print(f"Weight given to rarity scores: {rarityScore_weight}")
    print(f"Weight given to days held scores: {daysHeld_weight}")
    print(f"Factor controlling the decay of score based on days held: {daysHeld_decay_factor}")
    """

    max_nfts = max([holder["quantityNfts"] for holder in data])
    # print(f"The total number of NFTs owned by the individual with the largest NFT collection: {max_nfts}")

    avg_rarity_per_holder = [(holder["holderAddress"], sum(subnft["rarityScore"] for subnft in holder["holdingNfts"]) / holder["quantityNfts"]) for holder in data]
    rarity_sniper = max(avg_rarity_per_holder, key=lambda x: x[1])
    highest_rarity_average = rarity_sniper[1]
    # print(f"The average rarity score of the owner who possesses the highest average rarity score: {highest_rarity_average}")

    days_held_per_holder = [(holder["holderAddress"], sum(subnft["daysHeld"] for subnft in holder["holdingNfts"])) for holder in data]
    diamond_hands = max(days_held_per_holder, key=lambda x: x[1])
    hold_door = diamond_hands[1]
    # print(f"Th total duration held by the owner possessing the maximum cumulative duration of all NFTs they own : {hold_door}")

    today = date.today()

    def score_address(addr):
        holder_data = [holder for holder in data if holder["holderAddress"] == addr]
        if not holder_data:
            return 0

        holder_data = holder_data[0]

        nfts = holder_data["quantityNfts"]
        nfts_normalized = nfts / max_nfts
        nfts_weighted = nfts_normalized * quantityNfts_weight

        rarity_scores = [subnft["rarityScore"] for subnft in holder_data["holdingNfts"]]
        rarity_scores_log = [np.log(score + 1) for score in rarity_scores]
        rarity_score_average = sum(rarity_scores_log) / len(rarity_scores_log)
        rarity_score_normalized = rarity_score_average / np.log(highest_rarity_average + 1)
        rarity_score_weighted = rarity_score_normalized * rarityScore_weight

        days_held = sum([subnft["daysHeld"] for subnft in holder_data["holdingNfts"]])
        days_held_normalized = days_held / hold_door
        decay_factor = exp(-days_held_normalized * daysHeld_decay_factor)
        days_held_with_decay = days_held_normalized * decay_factor
        days_held_weighted = days_held_with_decay * daysHeld_weight
        # print(f"Address: {addr}, NFTs Weighted: {nfts_weighted}, Rarity Score Weighted: {rarity_score_weighted}, Days Held Weighted: {days_held_weighted}")
        scoreHold = (nfts_weighted + rarity_score_weighted + days_held_weighted)
        return scoreHold, # nfts_weighted, rarity_score_weighted, days_held_weighted

    # Review the calculated averages to consider adjustments to the weights assigned to the number
    # of NFTs (`quantityNfts_weight`), rarity score (`rarityScore_weight`), and holding duration
    # (`daysHeld_weight`). This evaluation will help in fine-tuning the scoring system for more
    # accurate assessments.

    """
    sum_nfts_weighted = 0
    sum_nfts_weighted = 0
    sum_rarity_score_weighted = 0
    sum_days_held_weighted = 0
    for holder in data:
        _, nfts_weighted, rarity_score_weighted, days_held_weighted = score_address(holder["holderAddress"])
        sum_nfts_weighted += nfts_weighted
        sum_rarity_score_weighted += rarity_score_weighted
        sum_days_held_weighted += days_held_weighted
    average_nfts_weighted = sum_nfts_weighted / len(data)
    average_rarity_score_weighted = sum_rarity_score_weighted / len(data)
    average_days_held_weighted = sum_days_held_weighted / len(data)
    print(f"Average Score of Holder's NFTs Owned: {average_nfts_weighted}")
    print(f"Average Score of Holder's Rarity: {average_rarity_score_weighted}")
    print(f"Average Score of Holder's Days Held: {average_days_held_weighted}")
    now_utc = datetime.utcnow()
    print(f"Date Tuned (UTC): {now_utc.strftime('%Y-%m-%d %H:%M:%S')}")
    """

    scored = []
    for holder in data:
        score = score_address(holder["holderAddress"])
        holder["holderScore"] = score
        scored.append(holder)

    ranked = sorted(scored, key=lambda x: x["holderScore"], reverse=True)

    with open('okay-bears/ranked-holders.json', 'w') as f:
      json.dump(ranked, f, indent=4)

except Exception as e:
    print(f"Error: {e}")
    traceback.print_exc()
```

import matplotlib.pyplot as plt
from datetime import datetime
import json

file_path = '/mnt/data/69.json'
with open(file_path, 'r') as file:
    nft_data = json.load(file)

def adjusted_plot_nft_ownership_histogram(nft_data, bins=30):
    
    def calculate_ownership_duration(acquired_timestamp):
        acquired_date = datetime.utcfromtimestamp(acquired_timestamp)
        current_date = datetime.now()
        return (current_date - acquired_date).days

    ownership_durations = []

    for nft in nft_data:
        holder_data_list = nft.get('holder data', [])
        
        holder = ""
        when_acquired = None
        for item in holder_data_list:
            if 'holder' in item:
                holder = item['holder']
            elif 'when acquired' in item:
                when_acquired = item['when acquired']
        
        if holder != "Magic Eden V2 Authority" and when_acquired:
            duration = calculate_ownership_duration(when_acquired)
            if duration >= 0:
                ownership_durations.append(duration)

    plt.style.use('dark_background')
    plt.figure(figsize=(12, 8))
    n, bins, patches_hist = plt.hist(ownership_durations, bins=bins, color='#0D47A1', edgecolor='#B3E5FC')

    max_bin_index = n.argmax()
    patches_hist[max_bin_index].set_facecolor('#FFC107')

    plt.title('Adjusted NFT Ownership Duration Distribution', fontsize=16, color='#E0E0E0')
    plt.xlabel('Length of Ownership (Days)', fontsize=14, color='#E0E0E0')
    plt.ylabel('Number of NFTs', fontsize=14, color='#E0E0E0')
    plt.xticks(fontsize=12, color='#E0E0E0')
    plt.yticks(fontsize=12, color='#E0E0E0')

    plt.text(0.5, 0.5, 'Arctic Frenz', fontsize=70, color='gray', alpha=0.2,
             ha='center', va='center', rotation=30, transform=plt.gca().transAxes)

    plt.grid(axis='y', alpha=0.65, color='#E0E0E0')

    plt.savefig('/mnt/data/adjusted_nft_ownership_histogram.png', format='png')

adjusted_plot_nft_ownership_histogram(nft_data)
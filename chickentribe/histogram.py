import matplotlib.pyplot as plt
from datetime import datetime
import json

file_path = '/mnt/data/69.json'
with open(file_path, 'r') as file:
    nft_data = json.load(file)

def plot_nft_ownership_histogram(nft_data, bins=30):
    
    def calculate_ownership_duration(acquired_timestamp, checked_timestamp):
        acquired_date = datetime.utcfromtimestamp(acquired_timestamp)
        checked_date = datetime.utcfromtimestamp(checked_timestamp)
        return (checked_date - acquired_date).days

    ownership_durations = []
    for nft in nft_data:
        holder_data = nft.get('holder data', [])
        when_acquired = next((item['when acquired'] for item in holder_data if 'when acquired' in item), None)
        time_checked = next((item['time checked'] for item in holder_data if 'time checked' in item), None)
        if when_acquired and time_checked:
            duration = calculate_ownership_duration(when_acquired, time_checked)
            if duration >= 0:
                ownership_durations.append(duration)

    plt.style.use('dark_background')

    plt.figure(figsize=(12, 8))
    n, bins, patches_hist = plt.hist(ownership_durations, bins=bins, color='#0D47A1', edgecolor='#B3E5FC')

    max_bin_index = n.argmax()
    patches_hist[max_bin_index].set_facecolor('#FFC107')

    plt.title('NFT Ownership Duration Distribution', fontsize=16, color='#E0E0E0')
    plt.xlabel('Length of Ownership (Days)', fontsize=14, color='#E0E0E0')
    plt.ylabel('Number of NFTs', fontsize=14, color='#E0E0E0')
    plt.xticks(fontsize=12, color='#E0E0E0')
    plt.yticks(fontsize=12, color='#E0E0E0')

    plt.text(0.5, 0.5, 'Arctic Frenz', fontsize=70, color='gray', alpha=0.2,
             ha='center', va='center', rotation=30, transform=plt.gca().transAxes)

    plt.grid(axis='y', alpha=0.65, color='#E0E0E0')

    plt.show()

plot_nft_ownership_histogram(nft_data)
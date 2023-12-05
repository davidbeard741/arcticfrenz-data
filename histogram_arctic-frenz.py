import matplotlib.pyplot as plt
from datetime import datetime
import json

file_path = 'arcticfrenz/nft_metadata_with_rarity_and_holder_data.json'

with open(file_path, 'r') as file:
    nft_data = json.load(file)

def plot_nft_ownership_histogram(nft_data, bins=30):
    
    def calculate_ownership_duration(acquired_timestamp):
        acquired_date = datetime.utcfromtimestamp(acquired_timestamp)
        current_date = datetime.utcnow()
        return (current_date - acquired_date).days

    def is_valid_unix_timestamp(timestamp):
        try:
            _ = datetime.utcfromtimestamp(int(timestamp))
            return True
        except (ValueError, OverflowError, TypeError):
            return False

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
        
        if holder != "Magic Eden V2 Authority" and when_acquired and is_valid_unix_timestamp(when_acquired):
            duration = calculate_ownership_duration(when_acquired)
            if duration >= 0:
                ownership_durations.append(duration)

    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 8))
    plt.subplots_adjust(bottom=0.25)
    
    n, bins, patches_hist = ax.hist(ownership_durations, bins=bins, color='#0D47A1', edgecolor='#B3E5FC')

    max_bin_index = n.argmax()
    patches_hist[max_bin_index].set_facecolor('#FFC107')

    ax.set_title('ChickenTribe\nNFT Ownership Duration Distribution', fontsize=16, color='#E0E0E0')
    ax.set_xlabel('Length of Ownership (Days)', fontsize=14, color='#E0E0E0')
    ax.set_ylabel('Number of NFTs', fontsize=14, color='#E0E0E0')
    ax.tick_params(axis='x', colors='#E0E0E0', labelsize=12)
    ax.tick_params(axis='y', colors='#E0E0E0', labelsize=12)

    ax.text(0.5, 0.5, 'Arctic Frenz', fontsize=70, color='gray', alpha=0.2,
             ha='center', va='center', rotation=30, transform=ax.transAxes)
		
    generation_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    footnote_text = f"Chart generated on: {generation_time}\nThis analysis did not include NFTs listed on Magic Eden."
    fig.text(0.05, 0.02, footnote_text, fontsize=10, color='#E0E0E0')  # Lowered text position relative to figure

    ax.grid(axis='y', alpha=0.65, color='#E0E0E0')

    plt.savefig('arcticfrenz/histogram-ownership-duration.png', format='png', bbox_inches='tight')  # Adjusted path for file saving

plot_nft_ownership_histogram(nft_data)

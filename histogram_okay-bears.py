import matplotlib.pyplot as plt
from datetime import datetime
import json
import numpy as np

file_path = 'okay-bears/by-NFT.json'
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
        holder_data = nft.get('holderData', {})
        holder = holder_data.get('holderAddress', "")
        when_acquired = holder_data.get('whenAcquired', None)
	      # "8Ew6iQXcTRHAUNNu3X9VBn1g1bJkXEZJ9gFD2AGKtdPB" is Mad Lads reserve for Scholarship Program
        if holder not in ["Magic Eden V2 Authority", "4zdNGgAtFsW1cQgHqkiWyRsxaAgxrSRRynnuunxzjxue", "1BWutmTvYPwDtmw9abTkS4Ssr8no61spGAvW1X6NDix", "8Ew6iQXcTRHAUNNu3X9VBn1g1bJkXEZJ9gFD2AGKtdPB" ] and when_acquired and is_valid_unix_timestamp(when_acquired):
            duration = calculate_ownership_duration(when_acquired)
            if duration >= 0:
                ownership_durations.append(duration)

    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 8))
    plt.subplots_adjust(bottom=0.25)

    n, bins, patches_hist = ax.hist(ownership_durations, bins=bins, color='#0D47A1', edgecolor='#B3E5FC')

    max_bin_indices = np.argsort(n)[-3:]
    colors = ['#FFC71F', '#CC9A05', '#997304']
    for i, index in enumerate(max_bin_indices[::-1]):
        patches_hist[index].set_facecolor(colors[i])

    ax.set_title('Okay Bears\nDistribution of NFT Ownership Durations', fontsize=16, color='#E0E0E0')
    ax.set_xlabel('Length of Ownership (Days)', fontsize=14, color='#E0E0E0')
    ax.set_ylabel('Number of NFTs', fontsize=14, color='#E0E0E0')

    ax.tick_params(axis='x', colors='#E0E0E0', labelsize=12)
    ax.tick_params(axis='y', colors='#E0E0E0', labelsize=12)

    ax.text(0.5, 0.5, 'Arctic Frenz', fontsize=70, color='gray', alpha=0.2,
             ha='center', va='center', rotation=30, transform=ax.transAxes)

    generation_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    footnote_text = f"Chart generated on: {generation_time}\nThis analysis did not include NFTs listed on Magic Eden and Tensor."
    fig.text(0.05, 0.1, footnote_text, fontsize=10, color='#E0E0E0')

    ax.grid(axis='y', alpha=0.65, color='#E0E0E0')

    save_path = 'okay-bears/histogram.png'

    try:
        plt.savefig(save_path, format='png', bbox_inches='tight')
        plt.close(fig)
    except Exception as e:
        print(f"Error saving file: {e}")

plot_nft_ownership_histogram(nft_data)

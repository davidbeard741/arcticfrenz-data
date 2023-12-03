import matplotlib.pyplot as plt
from datetime import datetime

def plot_dark_mode_nft_ownership_histogram(nft_data, bins=30):
    """
    Parameters:
    nft_data (list): List of NFT data.
    bins (int): Number of bins for the histogram.
    """
    # Helper function to calculate ownership duration in days
    def calculate_ownership_duration(acquired_timestamp, checked_timestamp):
        acquired_date = datetime.utcfromtimestamp(acquired_timestamp)
        checked_date = datetime.utcfromtimestamp(checked_timestamp)
        return (checked_date - acquired_date).days

    # Extracting ownership duration data
    ownership_durations = []
    for nft in nft_data:
        holder_data = nft.get('holder data', [])
        when_acquired = next((item['when acquired'] for item in holder_data if 'when acquired' in item), None)
        time_checked = next((item['time checked'] for item in holder_data if 'time checked' in item), None)
        if when_acquired and time_checked:
            duration = calculate_ownership_duration(when_acquired, time_checked)
            if duration >= 0:
                ownership_durations.append(duration)

    # Setting dark background
    plt.style.use('dark_background')

    # Plotting the histogram
    plt.figure(figsize=(12, 8))
    n, bins, patches_hist = plt.hist(ownership_durations, bins=bins, color='#0D47A1', edgecolor='#B3E5FC')

    # Highlighting the most common duration bin
    max_bin_index = n.argmax()
    patches_hist[max_bin_index].set_facecolor('#FFC107')

    # Adding labels and title
    plt.title('NFT Ownership Duration Distribution', fontsize=16, color='#E0E0E0')
    plt.xlabel('Length of Ownership (Days)', fontsize=14, color='#E0E0E0')
    plt.ylabel('Number of NFTs', fontsize=14, color='#E0E0E0')
    plt.xticks(fontsize=12, color='#E0E0E0')
    plt.yticks(fontsize=12, color='#E0E0E0')

    # Grid and style settings
    plt.grid(axis='y', alpha=0.75, color='#E0E0E0')

    # Show the plot
    plt.show()

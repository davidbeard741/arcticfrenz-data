import json
import matplotlib.pyplot as plt
from matplotlib import ticker
import matplotlib.font_manager as fm
import numpy as np
import math
from datetime import datetime
from matplotlib.ticker import NullFormatter

def custom_formatter(x, pos):
    if x >= 100:
        exponent = int(math.log10(x))
        mantissa = x / 10**exponent
        return f"{mantissa:.0f}e{exponent}"
    else:
        return "%d" % x

with open('smb/ranked-holders.json') as f:
    data = json.load(f)[:20]

data = [d for d in data if d is not None]

holders = []
for d in data:
    address = d.get('holderAddress')
    if address:
        holders.append(address[:4] + "..." + address[-4:])
    else:
        holders.append("Unknown")
        
metrics = [
    (d['quantityNfts'],
     sum(nft['rarityScore'] for nft in d['holdingNfts']),
     sum(nft['daysHeld'] for nft in d['holdingNfts']))
    for d in data
]
font1 = fm.FontProperties(size=12)
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(7, 8.4))
x = np.arange(len(holders))
width = 0.2
ticks = x + 0.9 * width
locator = ticker.FixedLocator(ticks)

ax.yaxis.set_major_locator(locator)
ax.set_yticklabels(holders, color='#ffffff', fontsize=10)
ax.set_ylabel('Holders', color='#E0E0E0', fontsize=16, fontweight=5)
ax.set_title('SMB Gen2\nTop Holders', fontsize=20, fontweight=5, color='#E0E0E0')
ax.tick_params(axis='y', color='#E0E0E0')
ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
ax.invert_yaxis()
ax.text(0.5, 0.5, 'Arctic Frenz', fontsize=70, color='gray', alpha=0.2,
          ha='center', va='center', rotation=30, transform=ax.transAxes)

ax1 = ax.twiny()
ax1.set_xscale('linear')
ax1.barh(x, [m[0] for m in metrics], width, color='#00e0ff', label='Quantity of NFTs Owned', edgecolor='#E0E0E0', alpha=0.8)
ax1.set_ylabel('Quantity of NFTs Owned', color='#00e0ff')
ax1.set_autoscalex_on(True)
ax1.xaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
ax1.tick_params(axis='y', labelcolor='#00e0ff')
ax1.tick_params(axis='x', which='both', labelcolor='#00e0ff', tickdir='in', direction='out', length=4, width=1, colors='#00e0ff', grid_color='#00e0ff', grid_alpha=0.5)
ax1.grid(axis='x', linestyle='--', alpha=0.5, color='#00e0ff')
ax1.yaxis.label.set_color('#00e0ff')

ax2 = ax.twiny()
ax2.set_xscale('linear')
ax2.barh(x + 1*width, [m[1] for m in metrics], width, color='#ff00a8', label='Cumulative Rarity Score\nAcross NFTs Owned', edgecolor='#E0E0E0', alpha=0.8)
ax2.set_ylabel('Cumulative Rarity Score\nAcross NFTs Owned', color='#ff00a8')
ax2.set_autoscalex_on(True)
ax2.xaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
ax2.tick_params(axis='y', labelcolor='#ff00a8')
ax2.tick_params(axis='x', labelcolor='#ff00a8', tickdir='out', direction='out', length=15, width=1, colors='#ff00a8', grid_color='#ff00a8', grid_alpha=0.5)
ax2.grid(axis='x', linestyle='--', alpha=0.5, color='#ff00a8')
ax2.yaxis.label.set_color('#ff00a8')

ax3 = ax.twiny()
ax3.set_xscale('log')
ax3.barh(x + 2*width, [m[2] for m in metrics], width, color='#fdff00', label='Cumulative Hold Duration\nin Days Across NFTs Owned', edgecolor='#E0E0E0', alpha=0.8)
ax3.set_ylabel('Cumulative Hold Duration\nin Days Across NFTs Owned', color='#fdff00')
ax3.tick_params(axis='y', labelcolor='#fdff00')
ax3.tick_params(axis='x', labelcolor='#fdff00', tickdir='out', direction='out', length=35, width=1, colors='#fdff00', grid_color='#fdff00', grid_alpha=0.5)
ax3.grid(axis='x', linestyle='--', alpha=0.5, color='#fdff00')
ax3.yaxis.label.set_color('#fdff00')
ax3.set_autoscalex_on(False)
ax3.xaxis.set_major_formatter(custom_formatter)
ax3.xaxis.set_minor_formatter(NullFormatter())
hold_durations = [m[2] for m in metrics]
min_hold_duration = min(hold_durations)
max_hold_duration = max(hold_durations)
buffer = max_hold_duration * 0.1
max_limit = max_hold_duration + buffer
ax3.set_xlim([min_hold_duration, max_limit])

legend_handles = []
legend_labels = []
for ax in [ax1, ax2, ax3]:
    handles, labels = ax.get_legend_handles_labels()
    legend_handles.extend(handles)
    legend_labels.extend(labels)
fig.legend(legend_handles, legend_labels, bbox_to_anchor=(0.98, 0.02), loc='lower right', title='Holders\' Stats', fontsize=10)

generation_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
footnote_text = f"Chart generated on:\n{generation_time}"
fig.text(-0.16, 1.17, footnote_text, fontsize=9, color='#E0E0E0', ha="left", va="top", transform=ax.transAxes, alpha=0.7)

fig.tight_layout()
plt.savefig('smb/top-holders.png', format='png', bbox_inches='tight')

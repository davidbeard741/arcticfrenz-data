import json
import os

MAX_FILE_SIZE = 500
OUTPUT_DIR = 'chickentribe/GPT/'
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

with open('chickentribe/ranked-holders.json') as f:
    data = json.load(f)

chunks = []
current_chunk = []

for item in data:
    if len(json.dumps(current_chunk + [item]).encode('utf-8')) / 1024 > MAX_FILE_SIZE:
        chunks.append(current_chunk)
        current_chunk = [item]
    else:
        current_chunk.append(item)

if current_chunk:
    chunks.append(current_chunk)

for i, chunk in enumerate(chunks):
    file_name = os.path.join(OUTPUT_DIR, f'output_{i}.json')
    with open(file_name, 'w') as f:
        json.dump(chunk, f, indent=4, sort_keys=True)
    file_size = os.path.getsize(file_name) / 1024
    print(f'{file_name} with size {file_size:.2f} KB')
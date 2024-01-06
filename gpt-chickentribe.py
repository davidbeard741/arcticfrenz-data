import json 
import math
import os
MAX_FILE_SIZE = 500
OUTPUT_DIR = 'chickentribe/GPT/'
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)
with open('chickentribe/ranked-holders.json') as f:
    data = json.load(f)
    
json_size = len(json.dumps(data).encode('utf-8')) / 1024
num_chunks = math.ceil(json_size / MAX_FILE_SIZE)  
chunk_size = len(data) // num_chunks  
chunk_end = chunk_size
chunks = []
current_chunk = []
for item in data:
    if (len(json.dumps(current_chunk + [item]).encode('utf-8')) / 1024) > MAX_FILE_SIZE:
        chunks.append(current_chunk)
        current_chunk = [item]
        chunk_end += chunk_size
    else:
        current_chunk.append(item)
chunks.append(current_chunk)
for i, chunk in enumerate(chunks):
    file_name = os.path.join(OUTPUT_DIR, f'output_{i}.json')
    
    with open(file_name, 'w') as f:
        json.dump(chunk, f)
    file_size = os.path.getsize(file_name) / 1024
    print(f'{file_name} with size {file_size:.2f} KB')
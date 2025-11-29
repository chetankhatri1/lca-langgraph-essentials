import json
import os

file_path = '/Users/chetan/Library/Mobile Documents/com~apple~CloudDocs/CK Learning/LangChain/lca-langgraph-essentials/python/L6_EmailAgent.ipynb'

with open(file_path, 'r') as f:
    nb = json.load(f)

count = 0
for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        new_source = []
        for line in cell['source']:
            if "state.get('classification', {})" in line:
                new_line = line.replace("state.get('classification', {})", "(state.get('classification') or {})")
                new_source.append(new_line)
                count += 1
            else:
                new_source.append(line)
        cell['source'] = new_source

with open(file_path, 'w') as f:
    json.dump(nb, f, indent=1)

print(f"Replaced {count} occurrences.")

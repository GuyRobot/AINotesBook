import json
import sys

data = []
fnames = sys.argv[1:]

for fname in fnames:
    with open(fname) as f:
        x = json.load(f)
        data.extend(x)

with open("merged.json", "w") as f:
    #unique_list = []
    #[unique_list.append(item) for item in data if item not in unique_list]
    json.dump(data, f, indent=4)
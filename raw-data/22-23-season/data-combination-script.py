"""
Header
"""
import json
import os

# Opening JSON file
cur_path = os.path.dirname(__file__)
main_file = open(cur_path + '\combined.json')
for i in range(28):
    relative_path = cur_path + '\loose\\' + str(i) + '.json'
    f = open(relative_path)

    data = json.load(f)

    print(data["d"]["total"])
    # main_file["array"]

    f.close()


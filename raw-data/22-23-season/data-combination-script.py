"""
This script opens all raw data and copies them to a single file.
there are 28 json files in the <../loose> folder. 
Author: Aren James Kerdokian
Date: 09/11/2023
"""
import json
import os

#obtain current path to create relative path
cur_path = os.path.dirname(__file__)

# stores all data when combined
all_data = {"rows": []}

for i in range(28):
    relative_path = cur_path + '\loose\\' + str(i) + '.json'  # path to the raw data
    f = open(relative_path)  # open raw data file

    data_dict = json.load(f)  # convert data to dict
    all_data["rows"].append(data_dict["d"]["rows"])  # append file data to all data 
    f.close()  # close data file

# Copies all data to the "combined.json file"
with open(cur_path + "\combined.json", "w") as outfile:
    json.dump(all_data, outfile)

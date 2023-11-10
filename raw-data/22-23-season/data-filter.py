"""
This script opens combined raw data and only keeps relevant data in the "combined-filtered.json" file.
Author: Aren James Kerdokian
Date: 09/11/2023
"""
import json
import os

# open file
cur_path = os.path.dirname(__file__)
f = open(cur_path + "\combined.json")  # open raw data file

# glo vars storing raw and filtered data
all_data_dict = json.load(f)
filtered_data_dict = {"rows": []}

# copies relevant data to filtered glo var
for i in range(len(all_data_dict["rows"])):  # for every game...
    new_row = {}

    # data fields that are relevant
    new_row["home-name"] = all_data_dict["rows"][i]["home-name"]
    new_row["away-name"] = all_data_dict["rows"][i]["away-name"]
    new_row["date-start-base"] = all_data_dict["rows"][i]["date-start-base"]
    new_row["date-start-timestamp"] = all_data_dict["rows"][i]["date-start-timestamp"]
    new_row["homeResult"] = all_data_dict["rows"][i]["homeResult"]
    new_row["awayResult"] = all_data_dict["rows"][i]["awayResult"]
    new_row["home-winner"] = all_data_dict["rows"][i]["home-winner"]
    new_row["away-winner"] = all_data_dict["rows"][i]["away-winner"]
    new_row["home-odds"] = all_data_dict["rows"][i]["odds"][0]["avgOdds"]
    new_row["away-odds"] = all_data_dict["rows"][i]["odds"][1]["avgOdds"]

    filtered_data_dict["rows"].append(new_row)

# close file
f.close()

# Copies all data to the "combined.json file"
with open(cur_path + "\combined-filtered.json", "w") as outfile:
    json.dump(filtered_data_dict, outfile)

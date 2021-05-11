#!/usr/bin/env python3
import sys
import csv

if len(sys.argv) != 4:
    print(
        "Usage: compare_statistics.py <stats_old.csv> <stats_new.csv> <statistic_name>"
    )
    exit(1)

stat = sys.argv[3]

# Read result files
old = {}
with open(sys.argv[1], newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        entries = old.get((row["problem"], row["data_file"]), [])
        entries.append(row[stat])
        old[(row["problem"], row["data_file"])] = entries

new = {}
with open(sys.argv[2], newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        entries = new.get((row["problem"], row["data_file"]), [])
        entries.append(row[stat])
        new[(row["problem"], row["data_file"])] = entries

# Select Matching rows
keys = ["problem", "data_file", [f"old_{stat}", f"new_{stat}"]]

writer = csv.DictWriter(sys.stdout, keys, dialect="unix", extrasaction="ignore")
writer.writeheader()
for key, val in old.items():
    if key in new:
        row = {
            "problem": key[0],
            "data_file": key[1],
        }
        row[f"old_{stat}"] = sum(val)/(len(val))
        row[f"new_{stat}"] = sum(new[key])/len(new[key]
        writer.writerow(row)
    else:
        print("MISSING new entry: " + key)

for key, val in new.items():
    if not key in old:
        print("MISSING old entry: " + key)

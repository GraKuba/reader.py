import sys
import json
import csv
import pickle

# GLOBAL VARIABLES

temporary_list = []
action = sys.argv[2]

# CLASSES


class Json:
    def __init__(self, file_out, file_type, argument):
        self.file_out = file_out
        self.file_type = file_type
        self.argument = argument


class Pickle:
    def __init__(self, file_out, file_type, argument):
        self.file_out = file_out
        self.file_type = file_type
        self.argument = argument


# CREATING OBJECTS

file_json = Json("file.json", json, "")
file_pickle = Pickle("file.pickle", pickle, "b")


# DOWNLOAD, READ AND WRITE THE FILE

if action == "json":
    f_out = file_json.file_out
    f_type = file_json.file_type
    f_arg = file_json.argument
elif action == "pickle":
    f_out = file_pickle.file_out
    f_type = file_pickle.file_type
    f_arg = file_pickle.argument
elif action == "csv":
    ...
else:
    print("Wrong command!")

with open("file.csv", 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        temporary_list.append(line)
if action == "csv":
    with open("file_2.csv", "w") as f:
        writer = csv.writer(f)
        for line in temporary_list:
            writer.writerow(line)
else:
    with open(f_out, "w"+f_arg) as f:
        f_type.dump(temporary_list, f)
    with open(f_out, "r"+f_arg) as f:
        text = f_type.load(f)
        print(text)

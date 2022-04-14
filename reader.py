import sys
import json
import csv
import pickle

# GLOBAL VARIABLES

temporary_list = []
file_in = sys.argv[1]
action = sys.argv[2]
location_x = int(sys.argv[3])
location_y = int(sys.argv[4])
command_change = sys.argv[5]

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

if action == "file.json":
    f_out = file_json.file_out
    f_type = file_json.file_type
    f_arg = file_json.argument
elif action == "file.pickle":
    f_out = file_pickle.file_out
    f_type = file_pickle.file_type
    f_arg = file_pickle.argument
elif action == "file.csv":
    ...
else:
    print("Wrong command!")

with open(file_in, 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        temporary_list.append(line)

temporary_list[location_x][location_y] = command_change

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

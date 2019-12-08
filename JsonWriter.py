import json
with open("myjson.json", "r+") as jsonReadFile:
    data = json.load(jsonReadFile)
    jsonReadFile.close()
print(data)
key=raw_input("Which key should be changed")
newvalue=raw_input("New Value")
data[key] = newvalue

with open("myjson.json", "w") as jsonWriteFile:
    json.dump(data, jsonWriteFile)
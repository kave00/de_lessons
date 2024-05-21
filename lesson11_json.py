import json

dictionary = {
    'name': 'BBB',
    'age': '14',
    'password': '545452s'
}

json_object = json.dumps(dictionary, indent=4)
print(json_object)

with open('sample.json', 'w') as file:
    file.write(json_object)

with open('sample.json') as file:
    json_object = json.load(file)

print(json_object)
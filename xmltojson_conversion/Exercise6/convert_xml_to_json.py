import xmltodict
import json

# Read XML data from the file
with open('data.xml', 'r') as xml_file:
    xml_data = xml_file.read()

# Parse XML data into a Python dictionary
xml_dict = xmltodict.parse(xml_data)

# Convert the Python dictionary to JSON
json_data = json.dumps(xml_dict, indent=4)

# Print the JSON data
print(json_data)

# Optionally, save the JSON data to a file
with open('data.json', 'w') as json_file:
    json_file.write(json_data)

import json

# Load the data from the JSON file
with open('content/FlexPwrTechRadar - 2024.1.json', 'r') as file:
    data = json.load(file)

# Sort the data by quadrant
sorted_data = sorted(data, key=lambda x: x['quadrant'])

# Save the sorted data back to the JSON file
with open('content/FlexPwrTechRadar - 2024.1.json', 'w') as file:
    json.dump(sorted_data, file, indent=2)
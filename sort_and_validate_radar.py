import json

# Load the data from the JSON file
with open('content/FlexPwrTechRadar - 2024.1.json', 'r') as file:
    data = json.load(file)

# Define the required fields and their valid values
required_fields = {
    'name': None,
    'ring': ['adopt', 'trial', 'assess', 'hold'],
    'quadrant': ['techniques', 'tools', 'platforms', 'languages & frameworks'],
    'isNew': ['TRUE', 'FALSE'],
    'description': None
}

# Check each item in the radar
for item in data:
    for field, valid_values in required_fields.items():
        if field not in item:
            print(f"Item {item['name']} does not have the required field {field}")
        elif valid_values is not None:
            # Convert the value to lowercase for comparison
            value = item[field].upper() if field == 'isNew' else item[field].lower()
            if value not in valid_values:
                print(f"Item {item['name']} has an invalid value for {field}: {item[field]}")
            else:
                # Replace the value with the correct case
                item[field] = value

# Sort the data by quadrant
sorted_data = sorted(data, key=lambda x: x['quadrant'])

# Save the sorted data back to the JSON file
with open('content/FlexPwrTechRadar - 2024.1.json', 'w') as file:
    json.dump(sorted_data, file, indent=2)

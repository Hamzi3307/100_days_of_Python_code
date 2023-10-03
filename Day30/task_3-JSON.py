import json 

# Writing JSON Files
# json.dump(new_data, file_to_write_data)

# with open("Day30\data.json", 'w') as file:
#     dict = {
#         'website' : {
#             'Email': 'mail@mail.com',
#             'Password': 'password@123'
#         }
#     }
#     json.dump(dict, file, indent=4)

# Reading JSON Files
# json.load(file_to_read_data)

# with open("Day30\data.json", 'r') as file:
#     data = json.load(file)
#     print(data)

# updating JSON Files
# file_data.update(new_data)

with open("Day30\data.json", 'r') as file:
    new_dict = {
        'Mobile App' : {
            'Email': 'yahoo@yahoo.in',
            'Password': 'hamzi3307'
        }
    }
    data = json.load(file)
    data.update(new_dict)
with open("Day30\data.json", 'w') as file:
    json.dump(data, file, indent=4)
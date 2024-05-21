import yaml


# write

# connections_db = [
#     {
#         'user_name': 'etl_user',
#         'password': '123'
#     },
#     {
#         'user_name': 'test_user',
#         'password': '456'
#     }
# ]
# with open(r'connections.yaml', 'w') as file:
#     documents = yaml.dump(connections_db, file)

with open(r'connections.yaml') as file:
    connections = yaml.load(file, Loader=yaml.FullLoader)
    print(connections)
    print(type(connections))
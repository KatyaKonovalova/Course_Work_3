from src import utils
dict_path = {}

for item in range(len(utils.getting_path_from())):
    item_for = utils.getting_path_from()[item]
    item_to = utils.getting_path_to()[item]
    print(f'{item_for} -> {item_to}')


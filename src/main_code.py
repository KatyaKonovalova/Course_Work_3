from src import functions

for item in range(len(functions.getting_path_from())):
    item_for = functions.getting_path_from()[item]
    item_to = functions.getting_path_to()[item]

for item_day in range(len(functions.formatted_date())):
    item_date = functions.formatted_date()[item_day]

for item_description in range(len(functions.getting_description())):
    item_d = functions.getting_description()[item_description]
    print(item_date, item_d)
    print(f'{item_for} -> {item_to}')



import os
import json
import operator
from datetime import datetime
list_of_completed_operations = []
list_path_from = []
list_path_to = []

with open(os.path.join('operations.json'), encoding='utf8') as file:
    all_operations = json.load(file)
    # print(all_operations)


for operation in all_operations:
    for key, value in operation.items():
        if key == 'state' and value == 'EXECUTED':
            list_of_completed_operations.append(operation)

sorted_operations = sorted(list_of_completed_operations, key=operator.itemgetter('date'), reverse=True)
result = sorted_operations[:5]
print(result)


def getting_path_from():

    for current_operation in result:
        path_from = current_operation.get('from')

        if path_from is None:
            path_from = 'Information is absent'
            list_path_from.append(path_from)
        else:
            card_number = path_from.split()[-1]
            formatted_number_from = str(
                card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:])
            formatted_number_from = '-'.join(formatted_number_from[i * 4:(i + 1) * 4] for i in range(4))
            path_from = path_from.split()[0] + ' ' + formatted_number_from
            list_path_from.append(path_from)

    print(list_path_from)

    return list_path_from

# getting_path_from()


def getting_path_to():

    for current_operation in result:
        path_to = current_operation.get('to')
        card_number = path_to.split()[-1]
        formatted_number = '**' + card_number[-4:]
        path_to = path_to.split()[0] + ' ' + formatted_number
        list_path_to.append(path_to)

    print(list_path_to)

    return list_path_to

# getting_path_to()


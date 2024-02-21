import os
import json
import operator
import functions

list_of_completed_operations = []
i = 0


def formatted_operations():
    with open(os.path.join('../src/operations.json'), encoding='utf8') as file:
        all_operations = json.load(file)
        return all_operations


def getting_sorted_operations(operations):
    '''Выборка списка словарей по значению EXECUTED, и из них вывод последних 5 операций'''

    for operation in operations:
        for key, value in operation.items():
            if key == 'state' and value == 'EXECUTED':
                list_of_completed_operations.append(operation)

    sorted_operations = sorted(list_of_completed_operations, key=operator.itemgetter('date'), reverse=True)
    result = sorted_operations[:5]
    return result


for current_operation in getting_sorted_operations(formatted_operations()):

    date_output = functions.formatted_date(current_operation.get('date'))
    description_output = current_operation.get('description')
    path_from_output = functions.getting_path_from(current_operation.get('from'))
    path_to_output = functions.getting_path_from(current_operation.get('to'))
    amount_output = current_operation.get('operationAmount').get('amount')
    name_output = current_operation.get('operationAmount').get('currency').get('name')

    print(date_output, description_output)
    if path_from_output == '':
        print(path_to_output)
    else:
        print(f'{path_from_output} -> {path_to_output}')

    print(amount_output, name_output, end='\n\n')

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


result_of_sorted_operations = getting_sorted_operations(formatted_operations())
print(result_of_sorted_operations)
result_formatted_date = functions.formatted_date(result_of_sorted_operations)
result_description = functions.getting_description(result_of_sorted_operations)
print(result_description)
result_path_from = functions.getting_path_from(result_of_sorted_operations)
result_path_to = functions.getting_path_to(result_of_sorted_operations)
result_operation_amount = functions.getting_operation_amount(result_of_sorted_operations)
result_operation_currency = functions.getting_operation_currency(result_of_sorted_operations)

while i < 5:

    print(result_formatted_date[i], result_description[i])
    print(f'{result_path_from[i]} -> {result_path_to[i]}')
    print(result_operation_amount[i], result_operation_currency[i], end='\n\n')

    i += 1

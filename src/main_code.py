from src import functions
i = 0

while i < 5:

    print(functions.formatted_date()[i], functions.getting_description()[i])
    print(f'{functions.getting_path_from()[i]} -> {functions.getting_path_to()[i]}')
    print(functions.getting_operation_amount()[i], functions.getting_operation_currency()[i], end='\n\n')

    i += 1






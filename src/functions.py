from datetime import datetime
list_path_from = []
list_path_to = []
list_date = []
list_description = []
list_operation = []
list_operation_amount = []
list_operation_currency = []
list_operation_name = []


def getting_path_from(data):
    """Вывод значений номеров карт/счетов откуда совершалась операция, в формате XXXX-XX**-****-XXXX"""

    for current_operation in data:
        path_from = current_operation.get('from')
        # print(path_from)
        if path_from is None:
            path_from = 'Information is absent'
            list_path_from.append(path_from)

        elif 'Счет' in path_from:
            card_number = path_from.split()[-1]
            formatted_number = '**' + card_number[-4:]
            path_from = path_from.split()[0] + ' ' + formatted_number
            list_path_from.append(path_from)

        elif 'Visa' in path_from:
            card_number = path_from.split()[-1]
            formatted_number_from = str(
                card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:])
            formatted_number_from = '-'.join(formatted_number_from[i * 4:(i + 1) * 4] for i in range(4))
            path_from = path_from.split()[0] + ' ' + path_from.split()[1] + ' ' + formatted_number_from
            list_path_from.append(path_from)
        else:
            card_number = path_from.split()[-1]
            formatted_number_from = str(
                card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:])
            formatted_number_from = '-'.join(formatted_number_from[i * 4:(i + 1) * 4] for i in range(4))
            path_from = path_from.split()[0] + ' ' + formatted_number_from
            list_path_from.append(path_from)

    return list_path_from


def getting_path_to(data):
    """Вывод номеров счетов куда совершалась операция, в формате **XXXX"""

    for current_operation in data:
        path_to = current_operation.get('to')
        card_number = path_to.split()[-1]
        formatted_number = '**' + card_number[-4:]
        path_to = path_to.split()[0] + ' ' + formatted_number
        list_path_to.append(path_to)

    return list_path_to


def formatted_date(data):
    """Вывод даты в формате день.месяц.год"""

    for current_operation in data:
        change_date = current_operation.get('date')
        datetime_obj = datetime.strptime(change_date, '%Y-%m-%dT%H:%M:%S.%f')
        date_result = datetime_obj.strftime("%d.%m.%Y")
        list_date.append(date_result)

    return list_date


def getting_description(data):
    """Вывод описания операции"""

    for current_operation in data:
        # description = current_operation.get('description')
        list_description.append(current_operation.get('description'))

    return list_description


def getting_operation_amount(data):
    """Вывод суммы операции"""

    for current_operation in data:
        operation_amount = current_operation.get('operationAmount')
        list_operation.append(operation_amount)
        list_operation_amount.append(operation_amount.get('amount'))

    return list_operation_amount


def getting_operation_currency(data):
    """Вывод валюты операции"""

    for current_operation in data:
        operation_amount = current_operation.get('operationAmount')
        list_operation.append(operation_amount)
        list_operation_currency.append(operation_amount.get('currency'))

    for money_name in list_operation_currency:
        list_operation_name.append(money_name.get('name'))

    return list_operation_name




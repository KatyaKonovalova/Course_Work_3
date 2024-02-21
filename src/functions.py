from datetime import datetime


def getting_path_from(path_from):
    """Вывод значений номеров карт/счетов откуда совершалась операция, в формате XXXX-XX**-****-XXXX"""

    if path_from is None:
        result_path_from = ''

    elif 'Счет' in path_from:
        card_number = path_from.split()[-1]
        formatted_number = '**' + card_number[-4:]
        result_path_from = path_from.split()[0] + ' ' + formatted_number

    elif 'Visa' in path_from:
        card_number = path_from.split()[-1]
        formatted_number_from = str(
            card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:])
        formatted_number_from = '-'.join(formatted_number_from[i * 4:(i + 1) * 4] for i in range(4))
        result_path_from = path_from.split()[0] + ' ' + path_from.split()[1] + ' ' + formatted_number_from

    else:
        card_number = path_from.split()[-1]
        formatted_number_from = str(
            card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:])
        formatted_number_from = '-'.join(formatted_number_from[i * 4:(i + 1) * 4] for i in range(4))
        result_path_from = path_from.split()[0] + ' ' + formatted_number_from

    return result_path_from


def getting_path_to(path_to):
    """Вывод номеров счетов куда совершалась операция, в формате **XXXX"""

    card_number = path_to.split()[-1]
    formatted_number = '**' + card_number[-4:]
    result_path_to = path_to.split()[0] + ' ' + formatted_number

    return result_path_to


def formatted_date(date):
    """Вывод даты в формате день.месяц.год"""

    datetime_obj = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    date_result = datetime_obj.strftime("%d.%m.%Y")

    return date_result



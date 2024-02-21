from src.functions import formatted_date
from src.functions import getting_path_from
from src.functions import getting_path_to


def test_formatted_date():

    assert formatted_date('2019-08-26T10:50:58.294041') == '26.08.2019'


def test_getting_path_from():

    assert getting_path_from(None) == ''
    assert getting_path_from('Visa Classic 2842878893689012') == 'Visa Classic 2842-87**-****-9012'
    assert getting_path_from('Maestro 7810846596785568') == 'Maestro 7810-84**-****-5568'
    assert getting_path_from('Счет 38611439522855669794') == 'Счет **9794'


def test_getting_path_to():

    assert getting_path_to('Счет 90424923579946435907') == 'Счет **5907'

import pytest
from src import main_code
from src import functions


def test_getting_description():

    assert functions.getting_description(main_code.formatted_operations()) == functions.getting_description(main_code.getting_sorted_operations(main_code.formatted_operations()))


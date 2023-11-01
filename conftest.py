import pytest
from rest import login

@pytest.fixture
def incorrect_word():
    return "Малоко"

@pytest.fixture
def correct_word():
    return "Молоко"

@pytest.fixture
def rest_login():
    return login()

@pytest.fixture
def rest_title():
    return "White cat"

@pytest.fixture
def rest_post_data():
    return "Как я провела лето.", "Рассказ о том, как я провела летние каникулы.", "Нормально."
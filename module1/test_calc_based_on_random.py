import pytest
from support_functions import *
from datetime import datetime
from calc import user_input


@pytest.mark.no_input
def test_no_input():
    assert user_input('') == 0


@pytest.mark.no_digits
def test_input_ascii_letters():
    _user_input = random_string_generator(string.ascii_letters)
    assert user_input(_user_input) == 0


@pytest.mark.no_digits
def test_input_punctuation():
    _user_input = random_string_generator(string.punctuation)
    assert user_input(_user_input) == 0


@pytest.mark.no_digits
def test_input_spaces():
    _user_input = random_string_generator(' ')
    assert user_input(_user_input) == 0


@pytest.mark.digits_only
def test_input_digits():
    time_now = datetime.now
    _user_input = six_digits_string(time_now)
    _user_input = shuffled_string(_user_input)
    assert user_input(_user_input) == checksum_six_digits(time_now)


@pytest.mark.with_digits
def test_input_ascii_letters_digits():
    time_now = datetime.now
    _user_input = random_string_generator(string.ascii_letters) + six_digits_string(time_now)
    _user_input = shuffled_string(_user_input)
    assert user_input(_user_input) == checksum_six_digits(time_now)


@pytest.mark.with_digits
def test_input_punctuation_digits():
    time_now = datetime.now
    _user_input = random_string_generator(string.punctuation) + six_digits_string(time_now)
    _user_input = shuffled_string(_user_input)
    assert user_input(_user_input) == checksum_six_digits(time_now)


@pytest.mark.with_digits
def test_input_spaces_digits():
    time_now = datetime.now
    _user_input = random_string_generator(' ') + six_digits_string(time_now)
    _user_input = shuffled_string(_user_input)
    assert user_input(_user_input) == checksum_six_digits(time_now)


@pytest.mark.with_digits
def test_input_all_char_digits():
    time_now = datetime.now
    _user_input = random_string_generator(string.ascii_letters + string.punctuation + ' ') + six_digits_string(time_now)
    _user_input = shuffled_string(_user_input)
    assert user_input(_user_input) == checksum_six_digits(time_now)

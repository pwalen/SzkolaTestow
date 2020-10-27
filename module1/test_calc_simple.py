import pytest
from calc import user_input

def test_no_input():
    assert user_input('') == 0


def test_input_ascii_letters():
    assert user_input('zwNFgAGvYfOsSPTexZurnUjKWlLokdiymbHDJEthQqBRpMXCaIVc') == 0


def test_input_punctuation():
    assert user_input('''"\`+[:<*_{~&|#(.,>@/-;$%])'!}^=?''') == 0


def test_input_spaces():
    assert user_input('                             ') == 0


def test_input_digits():
    assert user_input('25356478524741525') == 75


def test_input_ascii_letters_digits():
    assert user_input('VOhPN2lL2dkCav2usiZz551jYXWJGEy4UDBop35eRMT5x8AbrF47KcQ5wSn4t7Hq6Ifmg') == 75


def test_input_punctuation_digits():
    assert user_input('''7,835\+5:644-"/@*.)5{?;=2]_2^7|<5'&`(#5[%$!42>1~}''') == 75


def test_input_spaces_digits():
    assert user_input('2 5  555    25  73   6         8 7   1  4 4 24') == 75


def test_input_all_char_digits():
    assert user_input(
        ''' scRydp?Bj.l~b/IG}$  S 4!{P 4f  F7     Jt i m`=M5> vor"V Zh,#  -8nD7Ya+ 2  1K )|62 %QXx3]^& ke425z;('W T5 OAg5<  EC\LwuUHN:*q5 @_[''') == 75

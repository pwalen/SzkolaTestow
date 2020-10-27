import pytest
from calc import user_input


@pytest.mark.parametrize('_user_input, result',
                         [
                             ('', 0),
                             ('zwNFgAGvYfOsSPTexZurnUjKWlLokdiymbHDJEthQqBRpMXCaIVc', 0),
                             ('''"\`+[:<*_{~&|#(.,>@/-;$%])'!}^=?''', 0),
                             ('                             ', 0),
                             ('25356478524741525', 75),
                             ('VOhPN2lL2dkCav2usiZz551jYXWJGEy4UDBop35eRMT5x8AbrF47KcQ5wSn4t7Hq6Ifmg', 75),
                             ('''7,835\+5:644-"/@*.)5{?;=2]_2^7|<5'&`(#5[%$!42>1~}''', 75),
                             ('2 5  555    25  73   6         8 7   1  4 4 24', 75),
                             (
                                     ''' scRydp?Bj.l~b/IG}$  S 4!{P 4f  F7     Jt i m`=M5> vor"V Zh,#  -8nD7Ya+ 2  1K )|62 %QXx3]^& ke425z;('W T5 OAg5<  EC\LwuUHN:*q5 @_[''',
                                     75)
                         ]
                         )


def test_input(_user_input, result):
    assert user_input(_user_input) == result

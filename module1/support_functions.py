import random
import string

# ===== a random string generator (6-30 characters long) ======
def random_string_generator(ascii_characters):
    random_lenght = random.randint(6, 30)
    random_string = ''
    for _i in range(1, random_lenght):
        char = random.choice(ascii_characters)
        random_string += char
        _i += 1
    return random_string

# ===== a generator of a string of six unique digits from '123456789' ======
def six_digits_string(random_seed_number):
    digits_list = string.digits[1:]
    random_seed = random.seed(random_seed_number)
    random_digits_string = (''.join(random.sample(digits_list, len(digits_list)))[:6])
    return random_digits_string


# ===== a checksum calculator for selected six numbers ======
def checksum_six_digits(random_seed_number):
    random_seed = random.seed(random_seed_number)
    selected_digits_numbers = [int(x) for x in str(six_digits_string(random_seed_number))]
    return sum(selected_digits_numbers)

# ===== a string "shuffler" for mixing up digits, or digits with other letters or symbols ======
def shuffled_string(x):
    _shulled_string = ''.join(random.sample(x, len(x)))
    return _shulled_string

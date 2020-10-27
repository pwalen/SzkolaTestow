def user_input(_user_input):
    if _user_input == '':
        return 0
    else:
        result = 0
        for number in _user_input:
            if number.isdigit():
                result += int(number)
        return result

def check_pwd(input_string):
    if len(input_string) < 8 or len(input_string) > 20:
        return False
    dig_count = 0
    count_lower = 0
    count_upper = 0
    count_symbol = 0
    digits = [str(x) for x in range (0,10)]
    symbols = "~`!@#$%^&*()_+-="
    for i in input_string:
        if i in digits:
            dig_count +=1
        if i in symbols:
            count_symbol += 1
        if i == i.lower() and i not in digits and i not in symbols:
            count_lower += 1
        if i == i.upper() and i not in digits and i not in symbols:
            count_upper += 1

    if count_lower == 0 or count_upper == 0 or dig_count == 0 or count_symbol == 0:
        return False
    return True
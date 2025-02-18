def check_pwd(input_string):
    if len(input_string) < 8 or len(input_string) > 20:
        return False
    count_lower = 0
    digits = [str(x) for x in range (0,10)]
    symbols = "~`!@#$%^&*()_+-="
    for i in input_string:
        if i == i.lower() and i not in digits and i not in symbols:
            count_lower += 1

    if count_lower == 0:
        return False
    return True
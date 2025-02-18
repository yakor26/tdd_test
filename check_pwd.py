def check_pwd(input_string):
    if len(input_string) < 8 or len(input_string) > 20:
        return False
    return True
def create_phone_number(n):
    n = str(n).translate({ord(i): None for i in '[], '})
    n = '(' + n[:3] + ')' + ' ' + n[3:6] + '-' + n[6:]

    return n
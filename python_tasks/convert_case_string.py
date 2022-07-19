def to_underscore(string):
    new_str = ''
    string = str(string)
    for i in string:
        if i.isupper():
            new_str += '_' + i.lower()
        else:
            new_str += i
    if string[:1].isalpha():
        new_str = new_str[1:]
    return new_str

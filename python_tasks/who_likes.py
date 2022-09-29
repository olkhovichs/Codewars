def likes(names):
    len_names = len(names)
    if len_names == 0:
        return 'no one likes this'
    elif len_names == 1:
        return ''.join(names) + ' likes this'
    elif len_names == 2:
        return str(names[0] + ' and ' +names[1] + ' like this')
    elif len_names == 3:
        return str(names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this')
    elif len_names > 3:
        return str(names[0] + ', ' + names[1] + ' and ' + str(len(names) - 2) + ' others like this')
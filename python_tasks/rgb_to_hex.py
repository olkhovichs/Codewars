def rgb(r, g, b):
    rgb = [r, g, b]
    rgb = [0 if i < 0 else 255 if i > 255 else i for i in rgb]
    hex_col =  ['%02X' % i for i in rgb]
    return ''.join(hex_col)
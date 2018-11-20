def techdead(x,y):
    if y == 0:
        raise AssertionError ('y cannot be a zero')
    else:
        po = x * pow(x,y-1)
        return po

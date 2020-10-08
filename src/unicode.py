
__base = "0x0001F0"


def int2hex(i):
    return hex(i)[2:].rjust(2, '0')


def tile(i):
    hex = __base + int2hex(i)
    return chr(int(hex, 16))


def mahjong_tiles():
    return [tile(i) for i in range(0, 44)]

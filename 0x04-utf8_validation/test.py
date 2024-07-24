def validUTF8(data):

    skip = 0
    n = len(data)
    for i in range(n):
        if skip > 0:
            skip -= 1
            continue
        if type(data[i]) != int or data[i] < 0 or data[i] > 0x10ffff:
            return False
        span = 0
        if data[i] < 128:
            skip = 0
        elif data[i] & 0b1111000 == 0b11110000:
            span = 4
        elif data[i] & 0b1110000 == 0b11100000:
            span = 3
        elif data[i] & 0b1100000 == 0b11000000:
            span = 2
        else:
            return False
        if n - i >= span:
            continuation = list(map(
                lambda x: x & 0b11000000 == 0b10000000,
                data[i + 1: i + span],
            ))
            if not all(continuation):
                return False
            skip = span - 1
        else:
            return False
    return True

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))
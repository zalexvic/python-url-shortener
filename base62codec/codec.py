import string


def encode(ind):
    alphabet = string.ascii_letters + string.digits
    base = 62

    base62_digits = list()

    while ind > 0:
        digit = ind % base
        base62_digits.append(digit)
        ind //= base

    result = ""

    for digit in base62_digits:
        result += alphabet[digit]

    return result


def decode(pattern):
    alphabet = string.ascii_letters + string.digits
    base62_alphabet = {symbol: ind for ind, symbol in enumerate(alphabet)}

    base = 62
    base_pow = len(pattern) - 1

    result = 0

    for char in pattern:
        result += base62_alphabet[char] * base**base_pow
        base_pow -= 1

    return result



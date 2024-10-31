#!/usr/bin/python3
""" UTF-8 Validation """


def get_leading_set_bits(n):
    """ returns the number of leading set bits """
    s_bits = 0
    help = 1 << 7
    while help & n:
        s_bits += 1
        help = help >> 1
    return s_bits


def validUTF8(data):
    """ determines
    represents a valid UTF-8 encoding """
    bits_c = 0
    for i in range(len(data)):
        if bits_c == 0:
            bits_c = get_leading_set_bits(data[i])
            """ 1-byte
            format: 0xxxxxxx """
            if bits_c == 0:
                continue
            """ a character in UTF-8 can be 1 to 4 bytes long """
            if bits_c == 1 or bits_c > 4:
                return False
        else:
            """ checks if current byte has format
            10xxxxxx """
            if not (data[i] & (1 << 7) and not (data[i] & (1 << 6))):
                return False
        bits_c -= 1
    return bits_c == 0

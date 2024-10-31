#!/usr/bin/python3

'''Checks if a given data set represents a valid UTF-8 encoding'''


def validUTF8(data):
    remaining_bytes = 0

    for byte in data:
        byte = byte & 0xFF

        if remaining_bytes == 0:
            if (byte >> 5) == 0b110:  # 2-byte character
                remaining_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                remaining_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                remaining_bytes = 3
            elif (byte >> 7) == 0b0:  # 1-byte character (ASCII)
                remaining_bytes = 0
            else:
                return False  # Invalid lead byte
        else:
            # Check if byte is a valid continuation byte (10xxxxxx)
            if (byte >> 6) != 0b10:
                return False
            remaining_bytes -= 1

    return remaining_bytes == 0

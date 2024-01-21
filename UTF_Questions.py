# Imports
import random

print("Running UTF_Questions")


def getRandHex(lower=0, upper=0xFF):
    return "%02x" % random.randint(lower, upper)


def splitToPart(pattern, strng):
    return [strng[i:j] for i, j in zip(pattern, pattern[1:] + [None])]


def getHexBinary(stringHex):
    scale = 16  ## equals to hexadecimal
    num_of_bits = 24
    return bin(int(stringHex, scale))[2:].zfill(num_of_bits)


# string_hex = getRandHex(upper=0xFF)
string_hex = "0x09"
print(string_hex)
string_binary = getHexBinary(string_hex)


def getForm(string_binary):
    global string_first_section
    encode_form_1 = [0, 17]
    encode_form_2 = [0, 13, 18]
    encode_form_3 = [0, 8, 12, 18]
    encode_form_4 = [0, 3, 8, 12, 18]
    forms = [encode_form_1, encode_form_2, encode_form_3, encode_form_4]

    for form_num in range(len(forms)):
        string_first_section = splitToPart(forms[form_num], string_binary)
        print(string_first_section)
        int_first_section = int(string_first_section[0], 2)
        if int_first_section == 0:
            break

    if form_num == 0:
        binary_first = "0"+string_first_section[1]
        first_val = hex(int(binary_first, 2))
        print("Binary value '" + binary_first + "' = " + first_val)

        output_string = first_val


    if form_num == 1:
        binary_first = "110"+string_first_section[1]
        first_val = hex(int(binary_first, 2))
        print("Binary value '" + binary_first + "' = " + first_val)

        binary_second = "10"+string_first_section[2]
        second_val = hex(int(binary_second, 2))
        print("Binary value '" + binary_second + "' = " + second_val)

        output_string = first_val + ", " + second_val

    elif form_num == 2:
        binary_first = "1110"+string_first_section[1]
        first_val = hex(int(binary_first, 2))
        print("Binary value '" + binary_first + "' = " + first_val)

        binary_second = "10"+string_first_section[2]
        second_val = hex(int(binary_second, 2))
        print("Binary value '" + binary_second + "' = " + second_val)

        binary_third = "10"+string_first_section[3]
        third_val = hex(int(binary_third, 2))
        print("Binary value '" + binary_third + "' = " + third_val)

        output_string = first_val + ", " + second_val + ", " + third_val


    print("Serialised hex is '" + output_string + "'")



getForm(string_binary)
# print(getForm(string_binary))


def generateQ1():
    hexVal = getRandHex(upper=0x7F)
    print("because '" + hexVal + "' is below 7F, the UTF-8 serialization is: " + hexVal)

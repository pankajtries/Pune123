def manipulate_string(input_string):
    result_and = ""
    result_xor = ""

    for char in input_string:
        ascii_value = ord(char)
        binary_value = bin(ascii_value)[2:]
        manipulated_and = int(binary_value, 2) & 127
        manipulated_xor = int(binary_value, 2) ^ 127
        result_and += f"{manipulated_and:08b} "
        result_xor += f"{manipulated_xor:08b} "

    return result_and, result_xor

input_string = "\HelloWorld"
result_and, result_xor = manipulate_string(input_string)

print("Original String:", input_string)
print("AND Manipulation (Binary):", result_and)
print("XOR Manipulation (Binary):", result_xor)

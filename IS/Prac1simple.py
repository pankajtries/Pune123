input_string = input("Enter a string: ")
for char in input_string:
    a = ord(char)
    b = 127
    k = a & b
    j = a ^ b
    print("Converted value of", char, "in AND is:", bin(k)[2:], "and:",k)
    print("Converted value of", char, "in XOR is:", bin(j)[2:],"and:",j)

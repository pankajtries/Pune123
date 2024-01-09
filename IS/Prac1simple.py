input_string = "HelloWorld"
list= []
for char in input_string:
    list.append(char)

for i in list:
    a=ord(i)
    b=127
    k=a&b
    j=a^b
    print("Converted value of ",i," in AND is : ",bin(k))
    print("Converted value of ", i, " in XOR is : ", bin(j))

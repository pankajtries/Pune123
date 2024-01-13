import math
dec_cipher = []
msg = ""
k_indx = 0
msg_indx = 0

instring = input("Enter cipher text: ")
key = input("Enter key: ")

msg_len = float(len(instring))
msg_lst = list(instring)
col = len(key)
row = int(math.ceil(msg_len / col))
key_lst = sorted(list(key))

for _ in range(row):
    dec_cipher += [[None] * col]

for _ in range(col):
    curr_idx = key.index(key_lst[k_indx])
    for j in range(row):
        dec_cipher[j][curr_idx] = msg_lst[msg_indx]
        msg_indx += 1
    k_indx += 1

msg = ''.join(sum(dec_cipher, []))
print("Decrypted Message: {}".format(msg))

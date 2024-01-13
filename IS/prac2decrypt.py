import math

def decryptMessage(cipher, key):
    msg = ""
    k_indx = 0
    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)
    col = len(key)
    row = int(math.ceil(msg_len / col))
    key_lst = sorted(list(key))
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1
    msg = ''.join(sum(dec_cipher, []))
    return msg

# Input for Decryption
cipher_text = input("Enter the cipher text: ")
decryption_key = input("Enter the decryption key: ")
decrypted_text = decryptMessage(cipher_text, decryption_key)
print("Decrypted Message: {}".format(decrypted_text))

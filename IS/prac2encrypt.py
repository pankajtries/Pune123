import math
matrix=[]
cipher=""
kindex=0

instring=input("Enter plain text: ")
key=input("Enter key: ")

msglen=len(instring)
msglst=list(instring)
keylist=sorted(list(key))
col=len(key)
row=int(math.ceil(msglen/col))

fillnull=int((row*col)-msglen)
msglst.extend('_'*fillnull)

for i in range(0,len(msglst),col):
    matrix.append(msglst[i:i+col])


for j in range(col):
    currindex=key.index(keylist[kindex])
    cipher+=''.join([row[currindex] for row in matrix])
    kindex+=1

print(cipher)

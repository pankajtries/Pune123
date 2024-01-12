def bubble(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
import math
instring=input("Enter plain text: ")
key=input("Enter key: ")

matrix=[]
for i in key:
    matrix.append(i)

matrix1=[]
for i in instring:
    matrix1.append(i)

matrix2=[]

print(matrix1)
bubble(matrix)
print(matrix)
p=len(matrix1)/len(matrix)
if(p!=math.trunc(p)):
    p=math.trunc(p)+1
print(p)
n=len(matrix1)
for k in range(len(matrix)):
    list=[]
    for i in range(1,n,p):
        list.append(matrix1[i])
    matrix2.append(list)

print(matrix2)

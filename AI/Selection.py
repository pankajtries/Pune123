def sort(l):
    size=len(l)
    for i in range(size-1):
        min=i
        for j in range(i+1,size):
            if l[j] < l[min]:
                min=j
        l[i],l[min]=l[min],l[i]
        print(l)

def main():
    l=[]
    n = int(input("Enter no of students: "))
    for i in range(0, n):
        k = int(input("Enter percentage: "))
        l.append(k)
    print(l)
    sort(l)

main()

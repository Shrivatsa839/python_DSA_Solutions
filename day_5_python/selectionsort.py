def insertion(arr,size):
    for i in range(1,size):
        temp=arr[i]
        j=i-1
        while j>=0 and temp<=arr[j]:
            arr[j+1]=arr[j]
            j-=1
            arr[j+1]=temp
    return arr

size = int(input("enter size: "))
arr=[]
for i in range(0,size):
    arr.append(int(input()))
print(insertion(arr,size))
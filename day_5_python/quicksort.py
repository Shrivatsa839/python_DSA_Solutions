def quick(arr,low,high):
    if(low<high):
        part=partition(arr,low,high)

        quick(arr,low,part-1)
        quick(arr,low,high)
    return arr
def partition(arr,low,high):
    i=low
    j=i-1
    pivot=arr[high]
    while(i<=high-1):
        if(arr[i]<=pivot):
            j+=1

            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            i+=1
        else:
            i+=1
 
    temp=arr[j+1]
    arr[j+1]=arr[high]
    arr[high]=temp
    return j+1

size=int(input())
arr=[]
for i in range(0,size):
    arr.append(int(input()))
print(quick(arr,0,size-1))

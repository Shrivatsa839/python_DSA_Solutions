def Subset(arr, index, subset):

    if index == len(arr):
        print(subset)
        return
    
    subset.append(arr[index])
    Subset(arr, index + 1, subset)
    subset.pop()
    Subset(arr, index + 1, subset)

arr = [1, 2, 3]
Subset(arr, 0, [])
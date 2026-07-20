arr=[1,2,3]
def subset(index,result):
    if index == len(arr):
        print(result)
        return
    subset(index+1, result +[arr[index]])
    subset(index+1,result)
    
result=[]
subset(0,result)
##### IMP #####
arr=[1,2,3,4]
for i in range(0,5):
    for j in range(i+1,5):
        for k in range(i,j): # OR print(arr[i:j])
            print(arr[k], end="") #
        print()
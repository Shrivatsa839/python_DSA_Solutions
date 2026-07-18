def LinearSearch(arr,key):
    for i in range(0,len(arr)):
        if arr[i]==key:
            return i
    return -1

#driver code
li=[8,5,1,9,75,69,35,60,24,13,90]
key=int(input("enter a key to search"))
result=LinearSearch(li,key)
if(result==-1):print("key not found")
else:print(f'key found at {result+1}')














# class LinearSearch:
#     def search(self, arr, index, searchkey):
#         if index == len(arr):
#             print("Element not found")
#             return

#         if arr[index] == searchkey:
#             print("Element found at index", index)
#             return
        
#         self.search(arr, index + 1, searchkey)

# arr = [0, 9, 17, 27, 56, 68, 78, 98, 100]
# searchkey = int(input("Enter the number to search: "))
# obj = LinearSearch()
# obj.search(arr, 0, searchkey)
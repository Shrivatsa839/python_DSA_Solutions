class Binary:

    def BinarySearch(self, arr, low, high, searchkey):

        if low > high:
            print("Element not found")
            return
        
        mid = (low + high) // 2

        if arr[mid] == searchkey:
            print("Element found at index", mid)
            return
        
        elif arr[mid] < searchkey:
            self.BinarySearch(arr, mid + 1, high, searchkey)
        else:
            self.BinarySearch(arr, low, mid - 1, searchkey)

arr = [0, 9, 17, 27, 56, 68, 78, 98, 100]
searchkey = int(input("Enter number to search: "))
obj = Binary()
obj.BinarySearch(arr, 0, len(arr) - 1, searchkey)
# string = input("Enter a string: ")
# visited = ""
# for i in range(len(string)):
#     if string[i] not in visited:
#         count = 1
#         for j in range(i + 1, len(string)):
#             if string[i] == string[j]:
#                 count += 1
#         print(string[i], ":", count)
#         visited = visited + string[i]

dict1={}

string1=input()
for char in string1:
    if char in dict1:
        dict1[char]+=1
    else:
        dict1[char]=1
arr=[]
for key in dict1.keys():
    arr.append(key)
    arr.sort()
for keys in arr:
    print(keys,end=":")
    print(dict1.get(keys)) 


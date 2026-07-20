coins=[10,5,2,1]
amount=25
result=[]
for i in coins:
    while amount >=i:
        result.append(i)
        amount-=i
        print(result)
        print(len(result))
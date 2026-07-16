str1="shrivatsa khandare"
var1=0
var2=0
vowels=" a e i o u A E I O U"
for i in str1:
    if i not in vowels:
        var1+=1
    else:
        var2+=1
print("vowels count =",var2)
print("consonents count =",var1)


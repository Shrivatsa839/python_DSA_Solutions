s = "I Love JAVA"

stack = []

for ch in s:
    if ch != " ":
        stack.append(ch)

result = ""

for ch in s:
    if ch == " ":
        result = result + " "
    else:
        result = result + stack.pop()

print("String :", s)
print("Reversed String :", result)
s = "ab#bc#defghijk####"

hashes = ""
letters = ""

for ch in s:
    if ch == "#":
        hashes = hashes + "#"
    else:
        letters = letters + ch

result = hashes + letters

print(result)
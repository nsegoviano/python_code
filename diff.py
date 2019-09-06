def search_list(a, b):
    result = []
    for i in a:
        if i in b:
            result.append(i)
    return result

a = "SPAM"
b = "SAM"
f = search_list(a, b)
print(f)


def first_chars(x):
    spec_chars = ["#", ",", ".", ";", ":", "!"]
    text = x
    list = text.split(" ")
    first_char = []
    for s in list:
        first_char.append(s[0])
        temp = [*s]
        for i in temp:
            if i in spec_chars:
                first_char[ -1] += i
    return first_char

txt = input("Vad är din text?\n")
list = first_chars(txt)
res = " ".join(list)
print("Här kommer dina första bokstaver")
print("\n")
print(list)
print("\n")
print(res)
exit()
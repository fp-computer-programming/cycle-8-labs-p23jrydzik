# author: JHR 12/07/22

# the function
def count_a(word):
    letters = len(word)
    times = 0
    acount = 0
    while letters >= acount and times < letters:
        if "a" in word[times] or "A" in word[times]:
            acount += 1
        else:
            pass
        times += 1
    return acount

# test cases
print(count_a("abrAcadabra"))
print(count_a("aaaaaAAAAA"))
print(count_a("the first letter is nowhere to be found in this string"))
print(count_a("apple"))
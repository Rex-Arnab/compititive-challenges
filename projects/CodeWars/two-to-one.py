
# Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters,
#? each taken only once - coming from s1 or s2.

#! Examples
#* a = "xyaabbbccccdefww"
#* b = "xxxxyyyyabklmopq"
#* longest(a, b) -> "abcdefklmopqwxy"

#* a = "abcdefghijklmnopqrstuvwxyz"
#* longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

def longest(s1, s2):
    # your code
    c = sorted(s1)+sorted(s2)
    c = sorted(c)
    my_list = []
    for i in c:
        if i not in my_list:
            my_list.append(i)
    return "".join(my_list)
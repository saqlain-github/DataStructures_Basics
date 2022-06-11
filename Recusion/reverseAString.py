def reverse(str):
    return str[::-1]

def reverse_loop(str):
    tmp = ""
    for i in str:
        tmp = i+tmp
    return tmp


print(reverse_loop("abcde"))
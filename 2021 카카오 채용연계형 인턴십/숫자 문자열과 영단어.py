s = input()
alpha = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
         'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

def isString(str):
    if '0' <= str <= '9':
        return False
    else:
        return True

if s.isdigit():
    print(s)
    exit(0)
else:
    word = ''
    res = ''
    idx = 0
    while idx < len(s):
        if isString(s[idx]):
            while alpha.get(str(word)) not in alpha.values():
                word += s[idx]
                #print(word)
                idx += 1
                if idx == len(s):
                    break
                #print(str(alpha.get(str(word))))
            res += str(alpha.get(str(word)))
            word = ''
            idx -= 1
        else:
            res += s[idx]
        idx += 1
    print(res)

# words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# for i in range(len(words)):
#     s = s.replace(words[i], str(i))
#     print(s)
# print(s)
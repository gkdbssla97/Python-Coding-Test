#20:20 ~
survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
pick = [0, 3, 2, 1, 0, 1, 2, 3]
kakao = {'R': 0, 'T': 0, 'C': 0, 'F': 0,
         'J': 0, 'M': 0, 'A': 0, 'N': 0}
res = ''
def score(grade, character):
    if 1 <= grade <= 3:
        kakao[character[0]] += pick[grade]
    elif 5 <= grade <= 7:
        kakao[character[1]] += pick[grade]
for i in range(len(choices)):
    score(choices[i], survey[i])

if kakao['R'] >= kakao['T']:
    res += 'R'
else:
    res += 'T'
if kakao['C'] >= kakao['F']:
    res += 'C'
else:
    res += 'F'
if kakao['J'] >= kakao['M']:
    res += 'J'
else:
    res += 'M'
if kakao['A'] >= kakao['N']:
    res += 'A'
else:
    res += 'N'
print(res)

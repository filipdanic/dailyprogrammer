notation = list(''.join(raw_input().split()))
score = 0

for i in range(len(notation)):
    if notation[i] == 'X':
        notation[i] = 10
    elif notation[i] == '-':
        notation[i] = 0
    elif notation[i] == '/':
        continue
    else:
        notation[i] = int(notation[i])

for x in range(len(notation)):
    ball = notation[x]
    if len(notation) - 3 <= x:
        if ball == '/':
            score += (10 - notation[x-1])
        else:
            score += ball
        continue
    elif ball == 10:
        score += ball
        score += notation[x+1]
        if notation[x+2] == '/':
            score += (10 - notation[x+1])
        else:
            score += notation[x+2]
    elif ball == '/':
        score += (10 - notation[x-1])
        score += notation[x+1]
    else:
        score += ball

print score

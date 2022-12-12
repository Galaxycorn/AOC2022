#Thanks to my friend for helping me a lot here
def move_head(head, move):
    match(move):
        case 'R':
            head[0] += 1
        case 'L':
            head[0] -= 1
        case 'U':
            head[1] += 1
        case 'D':
            head[1] -= 1
            
def move_tail(tail, head):
    if tail[0] - 1 <= head[0] <= tail[0] + 1 and tail[1] - 1 <= head[1] <= tail[1] + 1:
        return
    if tail[0] == head[0]:
        if tail[1] < head[1]:
            tail[1] += 1
        elif tail[1] > head[1]:
            tail[1] -= 1
    elif tail[1] == head[1]:
        if tail[0] < head[0]:
            tail[0] += 1 
        elif tail[0] > head[0]:
            tail[0] -= 1
    else:
        if tail[0] > head[0] and tail[1] > head[1]:
            tail[0] -= 1
            tail[1] -= 1
        if tail[0] < head[0] and tail[1] > head[1]:
            tail[0] += 1
            tail[1] -= 1
        if tail[0] < head[0] and tail[1] < head[1]:
            tail[0] += 1
            tail[1] += 1
        if tail[0] > head[0] and tail[1] < head[1]:
            tail[0] -= 1
            tail[1] += 1
            

with open('DayNine/input.txt', 'r') as f:
    knots = [[0, 0] for _ in range(10)]
    headQ1 = [knots[1].copy()]
    headQ2 = [knots[9].copy()]
    for line in f.readlines():
        line = line.removesuffix('\n')
        move, lenght = line.split(' ')
        for _ in range(int(lenght)):
            move_head(knots[0], move)
            for k in range(1, len(knots)):
                move_tail(knots[k], knots[k-1])
            if knots[1] not in headQ1:
                headQ1.append(knots[1].copy())
            if knots[9] not in headQ2:
                headQ2.append(knots[9].copy())
        
        
print('Question 1 :', len(headQ1))#6256
print('Question 2 :', len(headQ2))#2665
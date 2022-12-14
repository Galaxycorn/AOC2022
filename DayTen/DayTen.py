#Part 1
cycle = 0
X = 1
sumX = 0
strengthRound = 0

def strength(cycle, X, lastX, instru):
    if cycle % 2 == 0 and instru == 'noop':
        sumX = X*cycle
    elif cycle % 2 == 1:
        X -= lastX
        sumX = X*(cycle-1)
    else:
        X -= lastX
        sumX = X*cycle
    return sumX
   
with open('DayTen/input.txt', 'r') as f:
    for line in f.readlines():
        line = line.replace('\n', '')
        if line[:4] == 'addx':
            cycle += 2
            X += int(line[5:])
            lastX = int(line[5:])
        if line[:4] == 'noop':
            cycle += 1
        if cycle >= 20+(40*strengthRound):
            sumX += strength(cycle, X, lastX, line[:4])
            strengthRound += 1    
          
#print('Question 1 :', sumX)

#Part 2
#Took me way more time to understand how to do it correctly 
#I had to rework completly how I did part 1 too, to make it work easier

data = [1]
with open('DayTen/input.txt', 'r') as f:
    for line in f.readlines():
        line = line.replace('\n', '')
        instru = line.split(' ')
        last_X = data[-1]
        data.append(last_X)
        if instru[0] == 'addx':
            data.append(last_X + int(instru[1]))


def draw(cycle):
    CRT = [[False for _ in range(40)] for _ in range(6)]
    for index, spritePos in enumerate(cycle): #Index = number of cycle and spritePos the value of the middle of the sprite
        y, x = index // 40, index % 40
        if spritePos - 1 <= x <= spritePos + 1:
            CRT[y][x] = True
    print("\n".join("".join("#" if c else " " for c in row) for row in CRT))
    
print('Question 2 : ')
draw(data)
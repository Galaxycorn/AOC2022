import re
import math

def parseMonkeys(f):
    monkeys = [[] for _ in range(15)]
    operation = [[] for _ in range(7)]
    test, targetTrue, targetFalse = [], [], []
    for line in f.readlines():
        line = line.replace('\n', '')
        if 'Monkey' in line:
            currentMonkey = re.findall('\d', line)
        if 'Starting items' in line:
            items = re.findall('\d+', line)
            monkeys[0].append(currentMonkey)
            monkeys[1].append(items)
        if 'Operation' in line:
            operation[0].append(line[23])
            operation[1].append(line[24:])
        if 'Test' in line:
            test.append(line[21:])
        if 'If true' in line:
            targetTrue.append(line[29:])
        if 'If false' in line:
            targetFalse.append(line[30:])
                    
    return monkeys, operation, test, targetTrue, targetFalse
            
def part1(monkeys, operation, test, targetTrue, targetFalse):
    counter = [[0] for _ in range(8)]
    for i in range(20):
        for k in range(8):
            for j in monkeys[1][k]:
                j = int(j)
                counter[k][0] += 1
                if operation[0][k] == '+':
                    j += int(operation[1][k])
                if operation[0][k] == '*':
                    if operation[1][k] == ' old':
                        j *= j
                    else:      
                        j *= int(operation[1][k])
                j = j // 3
                if int(j) % int(test[k]) == 0:
                    monkeys[1][int(targetTrue[k])].append(j)
                else: 
                    monkeys[1][int(targetFalse[k])].append(j)
                monkeys[1][k] = []
    return counter

def part2(monkeys, operation, test, targetTrue, targetFalse):
    counter = [[0] for _ in range(8)]
    for i in range(10000):
        for k in range(8):
            for j in monkeys[1][k]:
                j = int(j)
                counter[k][0] += 1
                if operation[0][k] == '+':
                    j += int(operation[1][k])
                if operation[0][k] == '*':
                    if operation[1][k] == ' old':
                        j *= j
                    else:      
                        j *= int(operation[1][k])
                j = j % 9699690 #Had to find how to do it because I cound't see it otherwise
                if int(j) % int(test[k]) == 0:
                    monkeys[1][int(targetTrue[k])].append(j)
                else: 
                    monkeys[1][int(targetFalse[k])].append(j)
                monkeys[1][k] = []
    return counter


with open("DayEleven/input.txt") as f:
   monkeys, operation, test, targetTrue, targetFalse = parseMonkeys(f)

counterP1 = part1(monkeys, operation, test, targetTrue, targetFalse)
max1 = max(counterP1)
counterP1.remove(max1)
max2 = max(counterP1)           
print(max1, max2)

with open("DayEleven/input.txt") as f:
   monkeys, operation, test, targetTrue, targetFalse = parseMonkeys(f)  
counterP2 = part2(monkeys, operation, test, targetTrue, targetFalse)
max3 = max(counterP2)
counterP2.remove(max3)
max4 = max(counterP2)           
print(max3, max4)
            
print('Question 1 : ', max1[0]*max2[0]) #61503
print('Question 2 : ', max3[0]*max4[0]) #14081365540
        
        
            
        
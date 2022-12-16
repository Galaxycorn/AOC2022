import re

def parseMonkeys(f):
    monkeys = [[] for _ in range(25)]
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
            
with open("DayEleven/input.txt") as f:
   monkeys, operation, test, targetTrue, targetFalse = parseMonkeys(f)
   
for i in range(20):
    for k in range(7):
        for j in monkeys[1][k]:
            if operation[0][k] == '+':
                j = j + operation[1][k]
            else: 
                j = j * operation[1][k]
            j = j // 3
            if j % test[k]:
                monkeys[1][targetTrue[k]].append(monkeys[1][k])
            else: 
                monkeys[1][targetFalse[k]].append(monkeys[1][k])
            monkeys[1][k] = []
            
   
        
            
print(monkeys[0][1], monkeys[1][1])
print(operation[0][1], operation[1][1])
print(test[1])
print(targetTrue[1])
print(targetFalse[1])

        
        
            
        
from collections import defaultdict

path = []
dictio = defaultdict(int)
with open("DaySeven/input.txt") as f:
    for line in f.readlines():
        line = line.replace("\n", "")
        if line[:7] == "$ cd ..":
            path.pop()
        elif line[:4] == "$ cd":
            path.append(line[5:])
        elif line[0].isdigit():
            size = line.split()
            for i in range(len(path)):
                dictio["/".join(path[:i + 1])] += int(size[0])

print('Solution 1 : ', sum(v for v in dictio.values() if v < 100000)) #2104783
print('Solution 2 : ', min(v for v in dictio.values() if dictio['/'] - v <= 40000000))        
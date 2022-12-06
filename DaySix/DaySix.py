marker = ""
counter = 0
counterMarker = 0
stop = False
#Part 1
with open("DaySix/input.txt") as file:
    buffer = file.readline()
    while True:
        for i in range(counter, counter + 4):
            marker += buffer[i]
        for j in range(4):
            if marker[j] in marker[(1+j):]:
                break
            else:
                counterMarker += 1
        if counterMarker == 4:
            break
        counter += 1
        counterMarker = 0
        marker = ""
print("Solution 1 : ", counter + 4) #1651    
#Part 2
counter = 0
counterMessage = 0
message = ""

with open("DaySix/input.txt") as file:
    buffer = file.readline()
    while True:
        for i in range(counter, counter + 14):
            message += buffer[i]
        for j in range(14):
            if message[j] in message[(1+j):]:
                break
            else:
                counterMessage += 1
        if counterMessage == 14:
            break
        counter += 1
        counterMessage = 0
        message = ""
    
print("Solution 2 : ", counter + 14) #3837
        

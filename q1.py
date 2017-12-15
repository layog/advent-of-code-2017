inFile = open("in.txt", "r")

number = inFile.readline().strip()
inFile.close()
ans = 0
for index in range(len(number)):
    if number[index] == number[(index+1) % (len(number))]:
        ans += int(number[index])

print ans

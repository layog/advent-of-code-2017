# Reading the number
inFile = open("in.txt", "r")
number = inFile.readline().strip()
inFile.close()

ans = 0
for index in range(len(number)):
    # OK simply add half the number of the digits
    if number[index] == number[(index+ len(number)/2) % (len(number))]:
        ans += int(number[index])

print ans

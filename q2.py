ans = 0
with open("in.txt", "r") as inFile:
    for line in inFile:
        nums = map(int, (line.strip()).split())
        ans += (max(nums) - min(nums))
print ans

num = int((raw_input("Input: ")).strip())

n = (pow(4*num - 3, 0.5) - 1)/2.0

n = int(n)

done_nums = 1 + (n) * (n+1)
remaining_nums = num - done_nums

if n%2 == 0:
    deltaX = deltaY = -n/2
    deltaX += min(remaining_nums, n+1)
    remaining_nums -= n+1
    deltaY += max(0, remaining_nums)
else:
    deltaX = deltaY = -(n-1)/2 + n
    deltaX -= min(remaining_nums, n+1)
    remaining_nums -= n+1
    deltaY -= max(0, remaining_nums)

print abs(deltaX) + abs(deltaY)

ans = 0
with open("in.txt", "r") as inFile:
    for line in inFile:
        nums = map(int, (line.strip()).split())
        for first_index in range(0, len(nums)-1):
        	done = False
        	for second_index in range(first_index+1, len(nums)):
        		num1, num2 = nums[first_index], nums[second_index]
        		num1, num2 = max(num1, num2), min(num1, num2)
        		if num1%num2 == 0:
        			ans += num1/num2
        			done=True
        			break
        	if done:
        		continue
print ans

def get_bitwise_max(num1, num2):
    max_num1 = True
    orig_num1 = num1
    orig_num2 = num2
    while num1 or num2:
        if (num1 & 0b001) == (num2 & 0b001):
            pass
        elif (num1 & 0b001):
            max_num1 = True
        else:
            max_num1 = False

        num1 = num1 >> 1
        num2 = num2 >> 1
    if max_num1:
        return orig_num1
    return orig_num2


ans = 0
with open("in.txt", "r") as inFile:
    for line in inFile:
        nums = map(int, (line.strip()).split())

        # Let's loop over first number first and then second
        for first_index in range(0, len(nums)-1):
            done = False
            for second_index in range(first_index+1, len(nums)):
                num1, num2 = nums[first_index], nums[second_index]
                max_num = get_bitwise_max(num1, num2)
                num1, num2 = max_num, (num2 + num1 - max_num)
                
                quotient = 0
                while num1 > 0:
                    num1 -= num2
                    quotient += 1

                # If divides perfectly
                if not num1:
                    ans += quotient
                    done = True
                    break
            if done:
                continue
print ans

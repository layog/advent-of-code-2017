from q10_2 import complete_hash

string_input = "xlqgujun"

filled_count = 0

for x in range(128):
    this_string_input = list(string_input + "-" + str(x))
    this_string_input = [ord(letter) for letter in this_string_input]
    this_string_hash = complete_hash(this_string_input)

    filled_count += (bin(int(this_string_hash, 16))[2:]).count('1')

print filled_count
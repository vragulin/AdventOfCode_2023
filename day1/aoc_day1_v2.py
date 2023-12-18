input = """
# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# 		"""
# lines = input.split('\n')

path = r'data/input_day1.txt'
# path = r'C:\Users\vragu\OneDrive\Desktop\Proj\PyLearning\AdventOfCode\data\input_test_2.txt'
lines = open(path, 'r').read().split('\n')

digits_list = list("0123456789")
digit_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

sum_all_nums = 0
for line in lines:

	nums = []
	for i in range(len(line)):
		if line[i] in digits_list:  # check if the character is a digit
			nums.append(line[i])
		else:  # check if the last n characters spell a number
			for j, d in enumerate(digit_words):
				if i >= (len(d) - 1):
					if line[i - len(d) + 1:i + 1] == d:
						nums.append(str(j + 1))
						break
	if len(nums) > 0:
		first_digit = int(nums[0])
		last_digit = int(nums[-1])
		calibration_val = 10 * first_digit + last_digit
		print(line, " : ", calibration_val)
		sum_all_nums += calibration_val

print(f"\nSum of All Values: {sum_all_nums}")

input = """
		"""
lines = input.split('\n')

digits_list = list("0123456789")

sum_all_nums = 0
for line in lines:
	nums = []
	for c in line:
		if c in digits_list:
			nums.append(c)

	if len(nums) > 0:
		first_digit = int(nums[0])
		last_digit = int(nums[-1])
		calibration_val = 10 * first_digit +last_digit
		print(line, " : ", calibration_val)
		sum_all_nums += calibration_val

print(f"\nSum of All Values: {sum_all_nums}")
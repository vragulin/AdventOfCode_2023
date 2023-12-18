from pathlib import Path

data_dir = r'C:\Users\vragu\OneDrive\Desktop\Proj\PyLearning\AdventOfCode\day2'
# f = 'input_test1.txt'
f = 'input.txt'

lines = open(str(Path(data_dir) / f), 'r').read().split('\n')

powers = []
for line in lines:
	print(line)
	tokens = line.split(' ')
	game = int(tokens[1].replace(":",""))
	token_num = 2
	game_is_good = True
	min_cubes = {'red': 0, 'green': 0, 'blue': 0}
	while token_num < len(tokens) - 1:
		n = int(tokens[token_num])
		color = tokens[token_num + 1].replace(",","").replace(";","")
		min_cubes[color] = max(min_cubes[color], n)
		token_num += 2

	power = min_cubes['red'] * min_cubes['green'] * min_cubes['blue']
	powers.append(power)

print(powers)
print(sum(powers))
from pathlib import Path

data_dir = r'C:\Users\vragu\OneDrive\Desktop\Proj\PyLearning\AdventOfCode\day2'
# f = 'input_test1.txt'
f = 'input.txt'

max_cubes = {'red': 12, 'green': 13, 'blue': 14}

# path = r'C:\Users\vragu\OneDrive\Desktop\Proj\PyLearning\AdventOfCode\data\input_test_2.txt'
lines = open(str(Path(data_dir) / f), 'r').read().split('\n')

good_games = []
for line in lines:
	print(line)
	tokens = line.split(' ')
	game = int(tokens[1].replace(":",""))
	token_num = 2
	game_is_good = True
	while token_num < len(tokens) - 1:
		n = int(tokens[token_num])
		color = tokens[token_num + 1].replace(",","").replace(";","")
		if n > max_cubes[color]:
			game_is_good = False
			break
		else:
			token_num += 2

	if game_is_good:
		good_games.append(game)


print(good_games)
print(sum(good_games))
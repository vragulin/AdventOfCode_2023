from typing import Callable
import math


class Node:
	next: tuple["Node"]


with open("input1.txt") as src:
	route, __, *nodes = map(str.strip, src)
	[*route] = map(int, route.translate(str.maketrans("LR", "01")))

for n in nodes:
	exec(n[:6] + "Node()")

for n in nodes:
	exec(n.replace(" =", ".next ="))


def n_routes(
		pos: Node = 'AAA',
		condition: Callable = lambda n: n == 'ZZZ',
) -> int:
	count = 1
	while True:
		for d in route:
			pos = pos.next[d]
		if condition(pos):
			break
		count += 1
	return count


print("part one answer:", n_routes() * len(route))

starts = [v for k, v in locals().items() if k.endswith("A")]
ends = [v for k, v in locals().items() if k.endswith("Z")]
counts = [n_routes(n, lambda n: n in ends) for n in starts]

print("part two answer:", math.lcm(*counts) * len(route))

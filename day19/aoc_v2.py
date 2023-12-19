# https://topaz.github.io/paste/#XQAAAQDhBAAAAAAAAAAFGovjf455l+am3pmC2uxAtGaKh/ytZNRoxZSvWje2mxpTJGA7+4OIOclwP6cYcgbwBhlnxeaFoM9/Iwd+ywUpIHUb3xSUG87fj2X52H65twZk4nhUuAu4uIGWzJU7mwZVepzjSAMXlh9ZtnL9lq1pJ4TalmDFQjGRwtmMxIRJ3L9oG8IB+aVMywF62Td/2l6mcRpw165YWc7EpRH6+azG0YC4M2EdiVsDI+oXGBsysk4YejABcDt0NlRiKbMm6g4d+twwckQhtJuA18wCGUXFrMffAZECXyq7ZkIdQeuFkRFigGZNWBxg0mn3c/Rk1T9bVetoW1wivfnpMgYa/6gpYpwDi14ebaU4wWmvtzAWC4jKnMuMkdRqB4xhO0gkSLd43RJMAsxEi+BNz1hISdc0iIsd3OAS+Ra3UE+KLp8rr6wZ3DRYWH5IkGq3GgIEvdAfk3LSS8SpY5kik0qK2lNv0bETj6Sh0zBs+TPgbx/ZY6i0ovzcadWHCohXC7/q3pLIEGof7AGLSVUhn9Q4UqtydI3A0AQ3oyge08zwhvD9dzk7D4toikNUfZmn4ailqFmkD7ObSYXpahRwyfFVmV4LRfWtJrOtndUWS/hYNJldHDzGvozaHWSqIuYbydnT0QK1TcADXxMvHGsfLuAmTxNQiACqalSvoz3ZkRLyrZ1E5vlB1Xps9XgsNOg/watISnPn5Ged8K5Slv/r6YLm
from math import prod
import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent


def f1(k, xmas):
	if k in ("R", "A"):
		return k == "A"
	for p in d[k].split(","):
		match p.split(":"):
			case cond, dest:
				if eval(f"{xmas[cond[0]]}{cond[1:]}"):
					return f1(dest, xmas)
			case dest,:
				return f1(dest, xmas)


def f2(k, lims):
	if k in ("R", "A"):
		if k == "R":
			return 0
		return prod(max(0, lims[f"{k}<"] - lims[f"{k}>"] - 1) for k in "xmas")
	o = 0
	for p in d[k].split(","):
		match p.split(":"):
			case cond, dest:
				ck = cond[:2]
				cv = (min, max)[cond[1] == ">"](int(cond[2:]), lims[ck])
				o += f2(dest, lims | {ck: cv})
				ck, cv = f"{ck[0]}{'<>'[ck[1] == '<']}", cv + (-1, 1)[ck[1] == ">"]
				lims[ck] = cv
			case dest,:
				o += f2(dest, lims)
	return o


PROD = True
fname = "input1.txt" if PROD else "example1.txt"
puzzle_input = (PUZZLE_DIR / fname).read_text().strip()
a, b = puzzle_input.split("\n\n")
d = {k: v[:-1] for k, v in (l.split("{") for l in a.splitlines())}
xs = (eval(l.replace("{", "dict(").replace("}", ")")) for l in b.splitlines())
print(sum(sum(x.values()) for x in xs if f1("in", x)))
print(f2("in", {f"{c}{o}": (0, 4001)[o == "<"] for c in "xmas" for o in "<>"}))

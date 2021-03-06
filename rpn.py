#!/usr/bin/env python3
import sys
from termcolor import colored, cprint

def calculate(arg):
	stack = []

	tokens = arg.split()

	for token in tokens:
		try:
			stack.append(int(token))
		except ValueError:
			val2 = stack.pop()
			val1 = stack.pop()
			if token == '+':
				result = val1 + val2
			elif token == '-':
				result = val1 - val2
			elif token == '^':
				result = 1
				for x in val2:
					result = result * val1 
			elif token == '*':
				result = val1 * val2
			stack.append(result)
	if len(stack) > 1:
		raise ValueError("Too many arguments on the stack")

	return(stack[0])


def main():
	while True:
		try:
			result = calculate(input('rpn calc> '))
			#print_red_on_cyan(result)
			#print(result)
			cprint(result,'green','on_red')
		except ValueError:
			pass


if __name__ == '__main__':
	main()


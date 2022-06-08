# The Basics Lessons of Python

[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=F7313B&background=4CFFA200&lines=The+basics+lessons+of+Python)](https://git.io/typing-svg)

## Tools

![Sublime Text](https://img.shields.io/badge/sublime_text-%23575757.svg?style=for-the-badge&logo=sublime-text&logoColor=important) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white) ![Google](https://img.shields.io/badge/google-4285F4?style=for-the-badge&logo=google&logoColor=white)

## Description

*I have encountered such a problem that I do not remember or do not know many built-in Python functions.
Therefore, I have created a small repository for many built-in language tools*

- Relevant topics:
	- Functions
	- OOP
	- List
	- Generators
	- String manipulation


## Example

```python
class Plan:

	def __init__(self, name, salary):
		self.v1 = name
		self.v2 = salary

	def __str__(self):
		return f'User name is {self.v1} and his/her salary\'s {self.v2}\n'

	def __repr__(self):
		return f'User (name={self.v1}, salary={self.v2})\n'

val = Plan('Duck', 7000)

print(val.__str__() + val.__repr__())

```
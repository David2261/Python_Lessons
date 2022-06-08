# UTF-8

"""
Лямбда функция - это анонимные функции, которые содержат
	только одно выражение.

lambda args(аргументы): тело функции

"""

List = [1, 4, 2, 5, 6, 8]

# list(map(lambda x: x*2, List))
# [2, 8, 4, 10, 12, 16]

# С лямбда функцией
def multiplyBy(n):
	return lambda x: x*n

# Без неё
def multiplyBy_2(x):
	def temp(n):
		return x*n
	return temp


double = multiplyBy(2)
triple = multiplyBy(3)
times10 = multiplyBy(10)

print(f'Удваение {double(7)} \nУтроение {triple(81)} \nУдесятерение {times10(64)}\n')

# Удваение 14
# Утроение 243
# Удесятерение 640
import sys
import time
from itertools import islice

"""
Функция range() - возращает объект типа range,
		тем самым уменьшая использования места.
Происходит это из-за того, что range() хранит значения start, stop, step.
Всё остальное вычисляет по мере необходимости.
"""
print(f"5 is {sys.getsizeof(range(5))} B")
print(f"500 is {sys.getsizeof(range(500))} B")

# Итератор - это объект, класс которого имеет методы:
# 			 __next__ и __iter__.
# Генератор - это функция, которая возвращает объект типа итератор.
# Вместо return пишется yeild



def timing(f):
	def wrap(*args, **kwargs):
		time_1 = time.time()
		ret = f(*args, **kwargs)
		time_2 = time.time()
		print(
			"{:s} function took {:3f} ms".format(
				f.__name__,
				(time_2 - time_1)
				* 1000.0)
			)
		return ret
	return wrap

@timing
def use_generator():
	return list(islice((time.sleep(x)), 1))

@timing
def use_list():
	return list(islice([time.sleep(x) for x in range(3)], 1))

print(f"With generator: {use_generator()} \nWithout him {use_list()}")


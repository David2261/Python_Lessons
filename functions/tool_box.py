from functools import lru_cache, partial, \
		reduce, singledispatch


# Кэширование
@lru_cache()
def factorial(n):
	return n * factorial(n-1) if n else 1

# factorial(7)
# 5040


# Функция partial() - используется для частичного
# 		использования определенной функции.

def partial(func, *args, **keywords):
	
	def newfunc(*fargs, **fkeywords):
		new_key_words = {**keywords, **fkeywords}
		return func(*args, *fargs, **new_key_words)

	newfunc.func = func
	newfunc.args = args
	newfunc.keywords = keywords
	return newfunc

fact = partial(factorial)
# Бонусы - экономия времени и памяти
# fact(10)
# 3628800


# Функция reduce() - аккумулирует (суммирует) значения
# 		к итерируемой (данной) последовательности
# Т.е. содержит 2 аргумента:
# 		1 - сумма предыдущих значний
# 		2 - последовательность следующих значений

reduce(lambda x, y: x+y, range(1,6))
# 15


# Диспетчеризация - это центрадизация управления
@singledispatch
def fun(arg, verbose=False):
	if verbose:
		print("Let me just say,", end=" ")
	print(arg)

# Декоратор register - добавляет декорированные функции в список
@fun.register
def _(arg: int, verbose=False):
	if verbose:
		print("Сила в количестве, правда же", end=" ")
	print(arg)


@fun.register
def _(arg: list, verbose=False):
	if verbose:
		print("Перебрать это:")
	for i, elem in enumerate(arg):
		print(i, elem)




from functools import lru_cache



# Кэширование
@lru_cache()
def factorial(n):
	return n * factorial(n-1) if n else 1

print(factorial(7))
# 5040
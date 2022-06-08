


"""
~ Метод __repr__ - выдает текстовое или строковое представление
	сущности или объекта.

~ Метод __str__ - выдает тоже самое, но она предназначена
	для читаемости версии, возможность отслеживания и отображения
	информации об объекте.

"""


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

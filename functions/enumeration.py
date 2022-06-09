

"""
Функция enumerate() - перебирает последовательность [
	список, кортеж, строку и словарь	
], параллельно отслеживая индекс элемента в последовательности 

Принимаемые значения:
	- итерируемый объект
	- начальное значение счетчика
"""


COLOUR = ["Black", "Purple", "Brown", "Yellow", "Blue"]


list(enumerate(COLOUR))
# [(0, 'Black'), (1, 'Purple'), (2, 'Brown'), (3, 'Yellow'), (4, 'Blue')]

# ~~~~~~~~~~~~~~~~~~~ #

list(enumerate(COLOUR, 10))
# [(10, 'Black'), (11, 'Purple'), (12, 'Brown'), (13, 'Yellow'), (14, 'Blue')]


colour = {
	"Black": 0,
	"Purple": 2,
	"Brown": 4,
	"Yellow": 9,
	"Blue": 1
}

list(enumerate(colour.items()))
# [(0, ('Black', 0)), (1, ('Purple', 2)), (2, ('Brown', 4)), (3, ('Yellow', 9)), (4, ('Blue', 1))]




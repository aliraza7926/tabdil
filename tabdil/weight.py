


# this function converts sort of weight units (tons,kilograms,gerams) to milligrams
def milli_gram(weight_unit):
	unit_name = weight_unit[0].lower()
	number = 1
	if unit_name == 'ton':
		number = 1000 * 1000 * 1000
	elif unit_name == 'kg':
		number = 1000 * 1000
	elif unit_name == 'g':
		number = 1000
	elif unit_name == 'mg':
		pass
	else:
		raise ValueError('unknown unit name {!r}'.format(unit_name))
	unit_number = weight_unit[1]
	return unit_number * number
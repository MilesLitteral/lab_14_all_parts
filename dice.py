roll1 = int(raw_input('What is your first roll?\n>'))
roll2 = int(raw_input('What is your second roll?\n>'))

if roll1 == 1 and roll2 == 1:
	print('Snake Eyes')
elif roll1 == 2 and roll2== 2:
	print('Hard Four')
elif roll1 == 1 and roll2 == 3 or roll1 == 3 and roll2 == 1:
	print('Easy Four')
else:
	print('I don\'t know that roll yet')

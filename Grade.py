grade = raw_input('input your grade\n>')

if int(grade) < 60:
	print('You failed')
if int(grade) == 100 or int(grade) >= 90:
  print('your number grade is ' + grade)
  print('A')
elif int(grade) == 89 or int(grade) >= 80:
	print('your number grade is ' + grade)
	print('Your leter grade is B')
elif int(grade) == 79 or int(grade) >= 70:
	print('your number grade is ' + grade)
	print('Your leter grade is C')
elif int(grade) == 69 or int(grade) >= 60:
	print('your number grade is ' + grade)
	print('Your leter grade is D')
else:
	print('your number grade is ' + grade)
	print('your letter grade is F')

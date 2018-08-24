result_str = " ";
for row in range(0,6):
	for column in range(0,6):
		if(column == 1 or (row == 5 and column != 0 and column < 5)):
			result_str = result_str + "*"
		else:
			result_str = result_str + "\n"
			result_str = result_str + "\n"
			print(result_str);
current_row = int(input("enter the row of the current position"))
current_column = int(input("enter the column of the current position"))
new_row = int(input("enter the row of the new position"))
new_column = int(input("enter the column of the new position"))
if(current_row <= 0 or current_row > 8):
	print("are you sure you are playing chess?")
if(new_row == current_row) or (new_column == current_column):
	print("the move is possible")

if(current_row == current_column):
	print("yes")
elif(current_row != current_column):
	print("no")
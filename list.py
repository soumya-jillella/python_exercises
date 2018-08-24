names = ["githa","ramu","hyma","ramu"]
for a in range(len(names)):
	print(f"range the loop for the {a+1} time...")
	names.remove("ramu")
	print(names)
	if not "ramu" in names:
		print(f"Found ramu is not in the list {a+1} ")
		break




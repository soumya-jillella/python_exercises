number = int(input("enter the number of lines:"))
word_list = []

for i in range(1,number+1):
	words = input(f"the number of lines:{i}")
	word_list.extend(words.split())

print(word_list)
for j in word_list:
	count = word_list.count(j)
	word_list.append(word_list)

print(count)







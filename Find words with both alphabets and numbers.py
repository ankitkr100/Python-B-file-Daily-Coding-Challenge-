str1 = "Emma25 is Data scientist50 and AI Expert"
print("the original string is:" + str1)

res = []
# split string on whitespace
temp = str1.split()

# Words with both alphabets and numbers
# isdigit() for numbers + isalpha() for alphabets
# use any() to check each charecters

for item in temp:
	if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
		res.append(item)

print("Displaying words with alphabets and numbers")
for i in res:
	print(i)

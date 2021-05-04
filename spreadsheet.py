from openpyxl import Workbook

#Setting up the Workbook and creating a new spreadsheet
workbook = Workbook()
sheet = workbook.active

# Creating a list of first 10 letter in the alphabet
letters = ["A","B","C","D","E","F","G","H","I","J"]

# init my counter
count = 1

# row loop
for i in range(10):
	#column loop
	for letter in letters:
		#placing count into index ex. A1, A2... J9, J10
		sheet[letter + str(i+1)] = count
		# Increment count by 1
		count = count + 1
		
#Saving workbook 
workbook.save(filename="spreadsheet.xlsx")
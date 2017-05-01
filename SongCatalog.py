import sys

#string -> integer/output
#ensure the input is one of the options if not prints "invalid option" and recalls menu
def valid_selction(selection,file_name):
	selection = selection.strip()  #removes potential white space

	if len(selection) == 1:    #checks input if a length of one
		try:
			selection = int(selection)
			if selection > 4 or selection < 0:
				print ("\nInvalid Option\n")
				main(file_name)
			else:
				return selection
		except:
			print ("\nInvalid Option\n")
			main(file_name)
	else:
		print ("\nInvalid Option\n")
		main(file_name)

#string -> output
#thats a file name and prints out all of the options excluding blank lines
# and cites error lines
def print_catalog(file_name):
	file = open("{}.txt".format(file_name), "r")
	line_number = 0
	problem_lines = []

	for line in file:
		line_number += 1
		line = line.strip()
		if len(line) == 0: #if the line is blank do nothing
			pass
		else:
			testing = len(line.split("--")) 
			if testing != 3: #if there arent three segments as expected
				problem_lines.append(line_number)
			else:
				print("{}--{}".format(line_number - 1,line) )

	if len(problem_lines) != 0:    #if there are lines that were an issues
		print ("\nCatalog input errors:")
		for i in problem_lines:
			print ("line {}: malformed song information".format(i))
#print_catalog("songs")

#-> outputs
#Body of the funtion
def main(file_name):
	print ("Song Catalog\n\t1) Print Catalog\n\t2) Song Information\n\t3) Sort\n\t4) Add Songs\n\t0) Quit")
	input_selection = input("Enter selection: ")
	selection = valid_selction(input_selection,file_name)
	if selection == 1:
		print_catalog(file_name)

print (main("{}".format(sys.argv[1])))

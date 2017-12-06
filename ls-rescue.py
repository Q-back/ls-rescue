import sys, argparse

class ListedItem():
	source = ""
	content = ""

	def __init__(self, content, source):
		self.content = content
		self.source = source

def read_files(file1, file2):
	ls1_filepath = file1
	ls2_filepath = file2
	
	ls1_file = open(ls1_filepath, "r")
	ls2_file = open(ls2_filepath, "r")
	
	ls1_file_content = ls1_file.read()
	ls2_file_content = ls2_file.read()
	
	ls1 = ls1_file_content.split()
	ls2 = ls2_file_content.split()

	ls1_file.close()
	ls2_file.close()
	return (ls1, ls2)

def format_output(analized):
	analized_items = ""
	if args.l:
		i = 1
		for item in analized:
			analized_items += "\n"
			if args.show_sources:
				analized_items += item.source + " --> "			
			analized_items += "("+str(i)+") " + item.content
			i+=1
	else:
		for item in analized:
			analized_items += item.content+" "
	return analized_items

try:
	description = "Find differences between two ls outputs"
	parser = argparse.ArgumentParser(description=description)
	parser.add_argument("-l", action="store_true", help="Print result in list format")
	parser.add_argument("-s", "--show-sources", action="store_true", dest="show_sources", 
		help="Show source file next to every output item. Works only when -l used.")
	parser.add_argument("--same", action="store_true", 
		help="Print items that occur in both ls outputs instead of items that are different")
	parser.add_argument("-f", "--file", nargs=2, 
		help="Use files instead of standard input. Example: ls-rescue -f file1.txt path/to/file2.txt")
	args = parser.parse_args()

	ls1_filepath = ""
	ls2_filepath = ""

	if args.file:

		ls1_filepath = args.file[0]
		ls2_filepath = args.file[1]

		files_readed = read_files(args.file[0], args.file[1])
		ls1 = files_readed[0]
		ls2 = files_readed[1]
	if not args.file:
		ls1 = input("Enter first ls output: ").split()
		ls2 = input("Enter second ls output: ").split()
	
	modified = []
	modified_control = []
	same = []
	same_control = []
	# Not optimal. I'll have to change it
	for listed_item in ls1:
		if not listed_item in ls2:
			modified_control.append(listed_item) #Quick solution, not good.
			modified.append(ListedItem(listed_item, ls1_filepath))
		else:
			if not listed_item in same_control: #Probably that check is not needed
				same_control.append(listed_item) #Quick solution, not good.
				same.append(ListedItem(listed_item, ls1_filepath))

	for listed_item in ls2:
		if not listed_item in ls1 and not listed_item in modified_control:
			modified_control.append(listed_item) #Quick solution, not good.
			modified.append(ListedItem(listed_item, ls2_filepath))
		else:
			if not listed_item in same_control:
				same_control.append(listed_item) #Quick solution, not good.
				same.append(ListedItem(listed_item, ls2_filepath))

	if args.same:
		same_items = format_output(same)
		print(str( len(same) ) + " SAME ITEMS: " + same_items)
	else:
		modified_items = format_output(modified)
		print(str( len(modified) ) + " MODIFIED ITEMS: " + modified_items)

except KeyboardInterrupt:
	print("\nInterrupted by user. Exit.")
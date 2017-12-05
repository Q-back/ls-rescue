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

try:
	description = "Find differences between two ls outputs"
	parser = argparse.ArgumentParser(description=description)
	parser.add_argument("-l", action="store_true", help="Print result in list format")
	parser.add_argument("-s", "--show-sources", action="store_true", dest="show_sources", help="Show source file next to every output item. Works only when -l used.")
	parser.add_argument("-f", "--file", nargs=2, help="Use files instead of standard input. Example: ls-rescue -f file1.txt path/to/file2.txt")
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
	# Not optimal. I'll have to change it
	for listed_item in ls1:
		if not listed_item in ls2:
			modified.append(ListedItem(listed_item, ls1_filepath))
	
	for listed_item in ls2:
		if not listed_item in ls1 and not listed_item in modified:
			modified.append(ListedItem(listed_item, ls2_filepath))
	
	modified_items = ""

	if args.l:
		i = 1
		for item in modified:
			modified_items += "\n"
			if args.show_sources:
				modified_items += item.source + " --> "			
			modified_items += "("+str(i)+") " + item.content
			i+=1
	else:
		for item in modified:
			modified_items += item.content+" "
	print(str( len(modified) ) + " MODIFIED ITEMS: " + modified_items)

except KeyboardInterrupt:
	print("\nInterrupted by user. Exit.")
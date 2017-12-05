import sys, argparse

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
	description = ""
	parser = argparse.ArgumentParser(description=description)
	parser.add_argument("-l", action="store_true", help="Print result in list format")
	parser.add_argument("-f", "--file", nargs=2, help="Use files instead of standard input. Example: ls-rescue -f file1.txt path/to/file2.txt")
	args = parser.parse_args()
	if args.file:
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
			modified.append(listed_item)
	
	for listed_item in ls2:
		if not listed_item in ls1 and not listed_item in modified:
			modified.append(listed_item)
	
	modified_items = ""

	if args.l:
		i = 1
		for item in modified:
			modified_items += "\n("+str(i)+") " + item
			i+=1
	else:
		for item in modified:
			modified_items += item+" "
	print(str( len(modified) ) + " MODIFIED ITEMS: " + modified_items)

except KeyboardInterrupt:
	print("\nInterrupted by user. Exit.")
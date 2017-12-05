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
	return (ls1, ls2)


description = ""
parser = argparse.ArgumentParser(description=description)
parser.add_argument("file1", default=None, help="first file with ls output", type=str)
parser.add_argument("file2", default=None, help="second file with ls output", type=str)
parser.add_argument("-f", "--file", action="store_true", help="Use files instead of standard input")
args = parser.parse_args()
if args.file and args.file1 and args.file2:
	files_readed = read_files(args.file1, args,file2)
	ls1 = files_readed[1]
	ls2 = files_readed[2]
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

ls1_file.close()
ls2_file.close()

modified_items = ""
for item in modified:
	modified_items += item+" "
print("MODIFIED ITEMS: "+modified_items)

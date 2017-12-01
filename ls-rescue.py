import sys

ls1_filepath = sys.argv[1]
ls2_filepath = sys.argv[2]

ls1_file = open(ls1_filepath, "r")
ls2_file = open(ls2_filepath, "r")

ls1_file_content = ls1_file.read()
ls2_file_content = ls2_file.read()

ls1 = ls1_file_content.split()
ls2 = ls2_file_content.split()

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


#Turns wiki files into chatterbot readable yaml files




import csv
import time
import re 
#read the orignal wiki file
choice = raw_input( "Enter tsv filename to transfer to .yaml Chatterbot file: ")
#choose the output file name
name = raw_input( "Enter a name for the file that will be out put (no extensions): ")
tsv_file = open(choice)
read_tsv = csv.reader(tsv_file, delimiter="\t")
question = ""
f = open(name + ".yaml", "a")
f.write("categories:\n- conversations\nconversations:\n")
for row in read_tsv:
	#print(row[1] + row [5])
	
	
	if row[1] == question:
		f.write(re.sub(r'[^A-Za-z0-9 ]+', '',row[5]))
		print(row[5])
	else:
		f.write("\n" + "- - " + (re.sub(r'[^A-Za-z0-9 ]+', '',row[1]))+"\n")
		f.write("  - " +(re.sub(r'[^A-Za-z0-9 ]+', '',row[5])))
		print("Question Updated for: " + question)
		print(row [1])
		print(row[5])
		
	
	question = row[1]
	
	#time.sleep(1)
	
	



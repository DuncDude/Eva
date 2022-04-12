# makes a mouse clicknig scheme from the mouse_log txt made by the mouse logger

#open file read lines
file1 = open('mouse_log.txt', 'r') 
Lines = file1.readlines() 


#make new file to pre progrma the commands
convert = open('converted.txt', 'w) 


#count = 0
# Strips the newline character 
#for line in Lines: 
#    print("Line{}: {}".format(count, line.strip())) 
#go through each line
for i in Lines:
	#interpet the numbers as an x and y
	x_cord = i.split(':')[0]
	y_cord = i.split(':')[len(i)]
			   
			   
	convert.write('	console.log("moving...");\n')
	convert.write("	robot.moveMouse(" + x_cord +',' + y_cord + ');\n")
	convert.write("	robot.mouseClick();\n")
	convert.write('	console.log("Clicking")\n')
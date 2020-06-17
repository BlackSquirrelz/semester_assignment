import sys  ## necessary for command line arguments

## get the filename
filename = sys.argv[1]

## define a path for the output files
outfile_path = './'

## open a file for reading
infile = open(filename, 'r')
	
## create a name for the output file
outfilename_1 = outfile_path + filename + '.tokenized.txt'
## open the output file for writing
outfile_a = open(outfilename_1, 'w')
	
## for each line in the input file
for line in infile:

	# split the line into a list of strings
	line_list = line.split()

	# for each word in the line
	for word in line_list:
		
		# remove a comma or dot at the end of the word
#		if (word[-1] == ',') or (word[-1] == '.'):
#			word = word[0:-1]

			# write output to the first file
			outfile_a.write(word)
			outfile_a.write('\n')
							
## close the files
infile.close()
outfile_a.close()

	

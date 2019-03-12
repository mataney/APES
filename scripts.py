directory = "/home/matan/Dropbox/Research/development/APES/testdata/"


with open(directory + "onefile/"+ "test.txt.tgt", "r") as source: 
	lines = source.readlines()
	for i, line in enumerate(lines):
		with open(directory + str(i) + ".targets", "w") as destination:
			destination.write(line)


with open(directory + "onefile/"+ "test.txt.pred", "r") as source: 
	lines = source.readlines()
	for i, line in enumerate(lines):
		with open(directory + str(i) + ".decodes", "w") as destination:
			destination.write(line)

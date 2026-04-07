with open ("logwithouterrors.txt", "r") as f:
	for line in f:
		line = line.strip()
		if "ERROR" in line:
			print (line)
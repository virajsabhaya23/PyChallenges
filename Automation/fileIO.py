f = open('inputFile.txt', 'r')
counter = 0
for line in f:
    line_split = line.split()
    if line_split[2] == "P":
        print(str(counter) + line)
        counter = counter+1
f.close()

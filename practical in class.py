samplearray = ["ECE","WRE","IT","AE","ICE","ME","EC","CE","GE","SE"]
arraylem = len(samplearray)
newarray = []

for index in range(arraylem):
    allelement = samplearray[index]
    newarray.append(allelement.lower())  # Corrected: added parentheses to call the lower method

for secondIndex in range(len(newarray)):
    print(newarray[secondIndex])

    
import sys

data = sys.argv[1:16]

print data

# Fill the data with 0x00
for x in range(len(data),16):
	data.append(0x00)

print data
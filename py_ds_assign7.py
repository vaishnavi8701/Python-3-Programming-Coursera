#assignment 7.1

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    print(line.upper().rstrip())

#assignment 7.2

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count=0
z=0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count+=1
    x=line.find('0')
    y=line[x:x+6]
    y=float(y)
    z+=y
#print(count,z)
a=float(z/count)
print("Average spam confidence: {0:.12f}".format(a))

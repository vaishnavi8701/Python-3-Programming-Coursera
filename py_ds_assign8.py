#assignment 8.4

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    l=list((line.split()))
    for i in l:
        if i not in lst:
            lst.append(i)
lst.sort()
print(lst)
    
#assignment 8.5

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
ls=[]
l=[]

fh = open(fname)
count=0
for line in fh:
    ls=line.split()
    count=0
    for i in ls:
        if "From" in ls:
            if(count==0):
                 l.append(ls[1])
                 count+=1
            
for i in l:
    print(i)
print("There were", len(l), "lines in the file with From as the first word")

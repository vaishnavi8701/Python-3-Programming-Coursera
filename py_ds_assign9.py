name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
ls=[]
l=[]


count=0
for line in handle:
    ls=line.split()
    count=0
    for i in ls:
        if "From" in ls:
            if(count==0):
                
                 l.append(ls[1])
                 count+=1
            
counter=0

for i in l: 
        curr_frequency = l.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i 
  
    
   
print(num,counter)

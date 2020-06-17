import re

def r_line(file,line_number):
    with open(file,'r') as fp:
        for i, line in enumerate(fp):
            if i == line_number and re.search('ERROR',line):
                return (line+"----").replace('\n','')
            elif i == line_number:
                return line
f = open("logfile.txt", "r")
fa= open("input.txt","a")
count = 0
index = []
for line in f:
    if re.search('ERROR',line):
        index.append(count)
    count = count+1    
print(r_line('logfile.txt',8))               
for i in range(len(index)):
    
    if index[i]>=3:
        for x in range(index[i]-3,index[i]+1):
            fa.write("\n")
            #print(r_line('logfile.txt',x))  
            fa.write(r_line('logfile.txt',x))
                    
    elif index[i]==0:        
        fa.write(r_line('logfile.txt',x))
        fa.write("\n")
        
    elif index[i]==1:            
        for x in range(index[i]-1,index[i]+1):
            fa.write(r_line('logfile.txt',x))
            fa.write("\n")
         
    elif index[i]==2:            
        for x in range(index[i]-2,index[i]+1):
            fa.write(r_line('logfile.txt',x))
            fa.write("\n")
          
   

lines_seen = set() # holds lines already seen
outfile = open('outputfile.txt', "w")
for line in open('input.txt', "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
fa.close()
outfile.close()            
f.close()

#print(r_line('logfile.txt',11))
fName=input("Enter the FileName:")
outDict={}
with open(fName,'r') as f:
    for line in f:
        words=line.split()
        for i in words:
            if i.lower() in outDict:
                outDict[i.lower()]+=1
            else:
                outDict[i.lower()]=1
print(outDict)
f=open("output.txt","w")
for x,y in outDict.items():
    f.write("{} {}\n".format(x,y))
f.close()


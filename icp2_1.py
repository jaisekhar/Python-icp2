inpList=[]
outList=[]
numElem=int(input("Enter the Number of Elements should be in Input List:"))
for i in range(numElem):
    tempElem=float(input("Enter Number {} for Input List:".format(i+1)))
    inpList.append(tempElem)
outList=[i*0.453592 for i in inpList]
print("Input list(lbs): {}\nOutput List(kgs): {}".format(inpList,outList))
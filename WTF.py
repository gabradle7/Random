#Assign students to either group 1 or 2.  Alternate in the placement of the students.  There are 457 students.  Hint: Evens and odds
def placement(student):
    x=range(1,int(student))
    for i in x:
        if i%2==0:
            return 1
        else:
            return 2 
print(placement(457))
#for i in range(457):
  #  print(i)
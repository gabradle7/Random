#Assign students to either group 1 or 2.  Alternate in the placement of the students.  There are 457 students.  Hint: Evens and odds
def placement(student):
    count=0
    
    if student%2==0:
        return student
    else:
        return "Odd"
print(placement(457))
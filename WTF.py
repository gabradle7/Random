#Assign students to either group 1 or 2.  Alternate in the placement of the students.  There are 457 students.  Hint: Evens and odds
# def placement(student):
#     x=range(1,int(student))
#     for i in x:
#         if i%2==0:
#             return 1
#         else:
#             return 2 
# print(placement(457))
# #for i in range(457):
#   #  print(i)

# def placement(student):
#     groups = [0] * student
#     for i in range(student):
#         if i % 2 == 0:
#             groups[i] = 1
#         else:
#             groups[i] = 2
#     return groups

# groups = placement(457)
# print(groups)


def placement(student):
    group1_count = 0
    group2_count = 0
    groups = []
    for i in range(1, student+1):
        if i % 2 == 0:
            groups.append(1)
            group1_count += 1
        else:
            groups.append(2)
            group2_count += 1
    return groups, group1_count, group2_count

groups, group1_count, group2_count = placement(457)
print("Group 1 count:", group1_count)
print("Group 2 count:", group2_count)

from random import randint
import random

# bugs to report:
# Group 5: repeated sequence of numbers - Solved
# Sol panel: repeated sequence of numbers - Figured out, need to implement.

# assign a list with all the people

# assign parent SOl
students = []
downthedrive = []
for i in range(0, 25):
    students.append(i)
    downthedrive.append(i)
print(students)

parentsol = []
for i in range(0, 13):
    # print(students)
    b = random.choice(students)
    # print(b)
    # Code is buggy, repeated numbers
    # Found the Bug: randint is not eliminating numbers as we go through them.
    # using random,choice, the bug was resolved
    for j in range(0, len(students) - 1):
        # print(j)
        if b == students[j]:
            students.pop(j)
        elif b == students[-1]:
            students.pop(-1)
    # print(parentsol)
    # print(students)
    parentsol.append(b)
# print("Parent SOL: ", parentsol)



# assign someone down the drive
dtd = random.choice(downthedrive)
print("Down the Drive: ", dtd)

# eliminates number for whoever got assigned down the drive
for j in range(0, len(downthedrive) - 1):
    if dtd == downthedrive[j]:
        downthedrive.pop(j)
    elif dtd == downthedrive[-1]:
        downthedrive.pop(-1)

# assign floater SOL under parent SOL
floatersol = []
for i in range(0, 3):
    c = random.choice(parentsol)
    for j in range(0, len(parentsol) - 1):
        if c == parentsol[j]:
            parentsol.pop(j)
        elif c == parentsol[-1]:
            parentsol.pop(-1)
    for j in range(0, len(students) - 1):
        # print(j)
        if c == students[j]:
            students.pop(j)
        elif c == students[-1]:
            students.pop(-1)
    floatersol.append(c)
print("Parent SOL: ", parentsol)
print("Floater SOL: ", floatersol)
# print(students)

# assign 4 people in SOL panel
# parent SOL is buggy because numbers might repeat, are u stupid? Fix it.
solpanel = []
for i in range(0,4):
    solpanel.append(random.choice(parentsol))
print("SOL panel: ", solpanel)

# assign pairs of groups:
# There are 5 groups
grpup1 = []
parentsol_copy = []
for i in range(0, len(parentsol)):
    parentsol_copy.append(parentsol[i])
# Notes: when copying a list, don't use len-1 because then the last number of the list does not Copy over!!

for i in range(0,2):
    a = random.choice(parentsol_copy)
    grpup1.append(a)
    for j in range(0,len(parentsol_copy) - 1):
        if a == parentsol_copy[j]:
            parentsol_copy.pop(j)
        elif a == parentsol_copy[-1]:
            parentsol_copy.pop(-1)
print("group 1: ", grpup1)

group2 = []
for i in range(0,2):
    a = random.choice(parentsol_copy)
    group2.append(a)
    for j in range(0,len(parentsol_copy) - 1):
        if a == parentsol_copy[j]:
            parentsol_copy.pop(j)
        elif a == parentsol_copy[-1]:
            parentsol_copy.pop(-1)
print("group 2: ", group2)

group3 = []
for i in range(0,2):
    a = random.choice(parentsol_copy)
    group3.append(a)
    for j in range(0,len(parentsol_copy) - 1):
        if a == parentsol_copy[j]:
            parentsol_copy.pop(j)
        elif a == parentsol_copy[-1]:
            parentsol_copy.pop(-1)
print("group 3: ", group3)

group4 = []
for i in range(0,2):
    a = random.choice(parentsol_copy)
    group4.append(a)
    for j in range(0,len(parentsol_copy) - 1):
        if a == parentsol_copy[j]:
            parentsol_copy.pop(j)
        elif a == parentsol_copy[-1]:
            parentsol_copy.pop(-1)
print("group 4: ", group4)

#group 5 is kinda buggy, take care of that ASAP
print("group 5: ", parentsol_copy)


# assign 3 people in front row under parent SOL
#make a copy of parentsol to make it easier to eliminate
copy_parentsol = []
for i in range (0, len(parentsol)-1):
    copy_parentsol.append(parentsol[i])
front_row = []
for i in range(0,3):
    k = random.choice(copy_parentsol)
    #print(k)
    front_row.append(k)
    for j in range(0,len(copy_parentsol) - 1):
        if k == copy_parentsol[j]:
            copy_parentsol.pop(j)
        elif k == copy_parentsol[-1]:
            copy_parentsol.pop(-1)
print("Front row: ", front_row)

# assign 8 people in check-in tables
checkin_tables = []
for i in range(0,8):
    k = random.choice(parentsol)
    checkin_tables.append(k)
    for j in range (0, len(parentsol) - 1):
        if k == parentsol[j]:
            parentsol.pop(j)
        elif k == parentsol[-1]:
            parentsol.pop(-1)
print("Check-in tables: ", checkin_tables)
# assign 5 people in tunnel of awesomeness under parent SOL
# 3/5 of tunnel of awesomenesss are the floater SOL's
print("Tunnel of Awesomeness: ", floatersol, parentsol)


# assign 1 person in front row under student SOL
print("In front row: ", random.choice(students))

# assign student SOL
print("Student SOL: ", students)

students_copy = []
for i in range(0, len(students) - 1):
    students_copy.append(students[i])
# assign 8 greeters

greeters = []
for i in range(0,8):
    k = random.choice(students_copy)
    #print(k)
    greeters.append(k)
    for j in range(0,len(students_copy) - 1):
        if k == students_copy[j]:
            students_copy.pop(j)
        elif k == students_copy[-1]:
            students_copy.pop(-1)
print("Greeters: ", greeters)

# assign 4 people in tunnel of awesomeness under student SOL
print("Tunnel of Awesomeness: ", students_copy)

#assign 4 people on stage
# This should alternate between groups, as one person from each group should be present on stage and one above
# First: assign groups from student SOL's
# Most of the code uses same logic as the ones above
yellow_list = []
for i in range(0, 2):
    yellow = random.choice(students)
    yellow_list.append(yellow)
    for j in range(0, len(students) - 1):
        if yellow == students[j]:
            students.pop(j)
        elif yellow == students[-1]:
            students.pop(-1)

orange_list = []
for i in range(0, 2):
    orange = random.choice(students)
    orange_list.append(orange)
    for j in range(0, len(students) - 1):
        if orange == students[j]:
            students.pop(j)
        elif orange == students[-1]:
            students.pop(-1)

purple_list = []
for i in range(0, 2):
    purple = random.choice(students)
    purple_list.append(purple)
    for j in range(0, len(students) - 1):
        if purple == students[j]:
            students.pop(j)
        elif purple == students[-1]:
            students.pop(-1)

green_list = []
for i in range(0, 2):
    green = random.choice(students)
    green_list.append(green)
    for j in range(0, len(students) - 1):
        if green == students[j]:
            students.pop(j)
        elif green == students[-1]:
            students.pop(-1)

blue_list = []
for i in range(0, 2):
    blue = random.choice(students)
    blue_list.append(blue)
    for j in range(0, len(students) - 1):
        if blue == students[j]:
            students.pop(j)
        elif blue == students[-1]:
            students.pop(-1)

peach_list = []
for i in range(0, 2):
    peach = random.choice(students)
    peach_list.append(peach)
    for j in range(0, len(students) - 1):
        if peach == students[j]:
            students.pop(j)
        elif peach == students[-1]:
            students.pop(-1)

print("Yellow Group: ", yellow_list)
print("Orange Group: ", orange_list)
print("Purple Group: ", purple_list)
print("Green  Group: ", green_list)
print("Blue Group:   ", blue_list)
print("Peach Group:  ", peach_list)

# assigning 4 people on stage
# choice 1
print("On Stage: ", random.choice(yellow_list), random.choice(blue_list), random.choice(green_list),random.choice(orange_list))
# choice 2
# We will implement choice 2 later on if needed

# Code is essentially completed, now to print out the data in a clear concise manner, and to recheck everything
# Priority number 1: Ensure all the numbers are correct and not repeated when not needed
# SOL panel is still buggy.


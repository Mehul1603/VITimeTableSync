#Reading File
with open("text_copied.txt","r") as f:
    text = f.readlines();


'''
each row is 31 lines (except the top one that is only 2 lines)

si no
newline
class group
newline
course
newline
type of course
newline
ltpjc
newline
category
course option
newline
class nbr
newline
slot
newline
newline
venue
newline
faculty name
newline
newline
faculty school
newline
registered/updated date and time
newline
attendance date
attendance type
newline
status & ref no
'''

#Courses = [[Name, Slot, Location]]
courses = list()

del text[0:2]
number_of_courses=len(text)//31
x=0
for i in range(number_of_courses):
    name = text[x+4][0:-1]
    slot = text[x+15][0:-1]
    location = text[x+18][0:-1]
    courses += [[name, slot, location]]
    x+=31
print(courses)

from datetime import datetime, timedelta
d = datetime.now()
tomorrow = datetime(d.year, d.month, d.day, 10)+timedelta(days=1)
start = tomorrow.isoformat()
end = (tomorrow + timedelta(hours=1)).isoformat()

print(end)
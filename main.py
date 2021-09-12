#Import the canvas class
from canvasapi import Canvas
from canvasapi import paginated_list
import datetime
import mysql.connector
#from datetime import datetime

#Creating the database

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="starwars22"
)

print(mydb)


# Canvas API URL
API_URL = "https://canvas.tamu.edu"
# Canvas API Key
API_KEY = '15924~nW2EvffEOj6QyTFmdgDoeNK4gReKGbXlKgzqjgIgQhNL6Ivc3a8VuM6CJ7Wf2n7A'

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)


Chem107 = canvas.get_course(110495)
Chem117 = canvas.get_course(113161)
ENGR102 = canvas.get_course(114893)
MATH151 = canvas.get_course(113716)
#CLEN181 = canvas.get_course(11501)

#print(ENGR102)

chem107_tasks = Chem107.get_assignments()
chem117_tasks = Chem117.get_assignments()
engr_tasks = ENGR102.get_assignments()
math_tasks = MATH151.get_assignments()
#clen_tasks = CLEN181.get_assignments()



#for task in chem107_tasks:
#    print(task.__getattribute__("due_at"))

#for task in chem117_tasks:
#    print(task.__getattribute__("due_at"))

#for task in math_tasks:
 #   print(task.__getattribute__("due_at"))


ChemLab = {}
ChemLecture = {}
Engineering = {}
MathLecture = {}
MathLab = {}
Clen = []

for z in chem107_tasks:
    task = str(z)
    time = z.__getattribute__("due_at")
    ChemLecture[task] = time

for a in chem117_tasks:
    task = str(a)
    time = a.__getattribute__("due_at")
    ChemLab[task] = time

for j in engr_tasks:
    task = str(j)
    time = j.__getattribute__("due_at")
    Engineering[task] = time


for h in math_tasks:
    task = str(h)
    time = h.__getattribute__("due_at")
    MathLecture[task] = time



#labs = course.get_modules()

print(ChemLab)
print(ChemLecture)
print(Engineering)
print(MathLecture)


def difficultyAssigner(x):
    date_now = datetime.datetime.now()
    for key, value in x.items():
        print(value)



difficultyAssigner(Engineering)



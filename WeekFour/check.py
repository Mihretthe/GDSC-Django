open("Exam.txt","w")
open("Exam.txt","w")
open("Exam.txt","r")

from datetime import datetime, timedelta
import os

time = datetime.now()


dir = os.listdir()
current = datetime.now()

def check_last_24(file):
    mod_time = datetime.fromtimestamp(os.path.getmtime(file))
    time_diff = current - mod_time 
      
    return time_diff.total_seconds() <= 24 * 60 * 60


def collect():
    return os.listdir()
    
def update(dir):
    for file in dir:
        edit = open(file, "a")
        edit.write(str(datetime.date(datetime.now())))

# new = "last24"

# if not os.path.exists(new):
#     os.mkdir(new)


files = collect()
print(files)

update(files)



        
        


2023-12-122023-12-12
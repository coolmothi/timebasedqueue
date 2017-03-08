from datetime import datetime
import random
import copy

num_tasks=20
def get_time():
    time= str(datetime.now())
    time = time[0:16]
    time =time.replace(":","-")
    time = time.replace(" ","-")
    print time

def gen_random_time():
    #function that generates random minutes in the range next five minutes

    cmin = datetime.now().minute
    time = str(datetime.now().date())+"-"
    chour = datetime.now().hour
    if (60-cmin) < 7:
        chour= chour+1

    cmin = (cmin+1 + random.randint(1, 6))%60

    return time+str(chour)+"-"+"%02d"%cmin

def gen_taskid():
    task_id="task_"
    rand = random.randint(500,600)
    return task_id+str(rand)

def gen_task():

    task=gen_taskid()+","
    task = task+gen_random_time()
    return task

def gen_task_file():
    #function that generates 20 random tasks
    global num_tasks
    fp = open("taskdata.csv", "w")
    for i in range(num_tasks):
        fp.write(gen_task()+"\n")




def get_tasks_fromfile(filename, curtime):

    try:
        fp=open(filename,"r")
    except Exception,e:
        print "No such File found"

    cmin= int(curtime[14:16])
    global  num_tasks
    tasks = []
    t=1
    while t<=num_tasks:
        line=fp.readline()
        task_time = line.rsplit(",")
        task_id= task_time[0]
        time = task_time[1]
        tmin= int(time[14:16])
        minute=0
        if tmin < cmin:
            minute= 60-cmin+tmin
        else:
            minute = tmin-cmin

        task=[task_id,time,minute,False]

        tasks.append(task)
        t +=1

    stasks=sorted(tasks,key=lambda l:l[2])
    return stasks


def schedule(tasks, given_time):
    gmin=int(given_time[14:16])
    prev_min=gmin
    t=1
    while t <= num_tasks:
        for task in tasks:
            if task[3] == False:
                ctime= str(datetime.now())
                cmin=datetime.now().minute
                if cmin-prev_min == 1:
                    print "-----------After One Minute----------"
                    prev_min=cmin

                if cmin< gmin:
                    temp = 60-gmin+cmin
                else:
                    temp=cmin-gmin

                if(temp == task[2]):
                    task[3]=True
                    print "current time= "+ctime[0:16]+"  "+" Event :"+task[0]+"  Processed"
                    t += 1



print "20 random tasks are generated and placed automatically onto the file \"taskdata.csv\" please give same file as input"

filename=raw_input("Enter File name:   ")

gtime = str(datetime.now())

gtime=gtime[0:16]

print "the current time "+gtime+" is considered for input"

gen_task_file()

tasks = copy.deepcopy(get_tasks_fromfile(filename,gtime))

schedule(tasks,gtime)





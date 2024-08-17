import time
#help(time)
#include <stdio.h>

def format_time(hour,minute,second):
    print(f"Time: {hour:02d}:{minute:02d}:{second:02d}")


purpose = input("Add your Purpose of Work: ")
work_time = input("Add your Work Time (minutes): ")
work_time = int(work_time)
break_time = input("Break Time(minutes): ")
break_time = int(break_time)

print(purpose, work_time, break_time)
print(type(purpose),type(work_time),type(break_time))

work_time = work_time*60

while work_time>0:
    #print(work_time)
    hour = int(work_time/3600)
    remainder = work_time % 3600 # remainder
    minutes = int(remainder/60)
    seconds = remainder % 60
    format_time(hour, minutes,seconds)
    work_time-=1
    time.sleep(1)


import time
from module1 import format_time
from pygame import mixer
from datetime import datetime
import pandas as pd
mixer.init()

# returns current date and time
now = datetime.now() #geeks of geeks


def format_date():
    now = datetime.now()
    now = now.strftime("%Y-%m-%d")
    return now

def play_alarm(work_time):
    while work_time>0:
        #print(work_time)
        hour = int(work_time/3600)
        remainder = work_time % 3600 # remainder
        minutes = int(remainder/60)
        seconds = remainder % 60
        format_time(hour, minutes,seconds)
        work_time-=1
        time.sleep(1)

    mixer.music.load("alarm.wav")
    mixer.music.set_volume(0.7)
    mixer.music.play()

def give_value():
    work_dict = {"Purpose":[],"Work":[],"Break":[]}
    while True:
        purpose = input("Add your Purpose of Work (Press 'q' to quit): ")
        
        if purpose == 'q' or purpose=="Q":
            break

        work_time = input("Add your Work Time (minutes): ")
        work_time = float(work_time)
        break_time = input("Break Time(minutes): ")
        break_time = float(break_time)

        work_dict["Purpose"].append(purpose)
        work_dict["Work"].append(work_time)
        work_dict["Break"].append(break_time)


        work_time = int(work_time*60)
        play_alarm(work_time)
        print("\n")
        break_time = int(break_time*60)
        play_alarm(break_time)
    date = format_date()
    date = str(date)
    df = pd.DataFrame(work_dict,columns=work_dict.keys())
    df.to_csv(f"{date}.csv")



give_value()


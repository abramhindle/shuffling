#!/usr/bin/env python3
import random
import datetime
videos = ["Chungus","Friday","Dogs","Cats","PythonTutorial","MathVideo","Rickroll"]
offset = 2

def days_since_epoch(now=None):
    if now is None:
        now = datetime.datetime.utcnow()
    return (now - datetime.datetime(1970,1,1)).days

def day_seed(now=None,offset=offset):
    if now is None:
        now = datetime.datetime.utcnow()    
    return days_since_epoch(now + datetime.timedelta(days=offset))

def week_seed(n,now=None,offset=offset):
    return day_seed(now,offset)//n

def week_seed_and_day(n, now=None, offset=2):
    day = day_seed(now,offset)
    week = day // n
    return (week, day, day - week*7)

def video_of_day(videos,now=None,offset=offset):
    n = len(videos)
    week,day,nday = week_seed_and_day(n,now,offset)
    random.seed(week)
    videos_copy = list(videos)
    random.shuffle(videos_copy)
    return videos_copy[nday]

print(video_of_day(videos))

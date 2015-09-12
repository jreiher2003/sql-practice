#
# Database access functions for the web forum.
# 

import datetime
import time
import bleach
import sqlite3

## Database connection
# DB = []


## Get posts from database.
def GetAllPosts():
    DB = sqlite3.connect("forum.db")
    c = DB.cursor()
    c.execute("SELECT time, content FROM posts ORDER BY time DESC")
    posts = ({'content': str(row[1]), 'time': str(row[0])} for row in c.fetchall())
    # posts.sort(key=lambda row: row['time'], reverse=True)
    DB.close()
    return posts

## Add a post to the database.
def AddPost(content):
    DB = sqlite3.connect("forum.db")
    c = DB.cursor()
    t = str(datetime.datetime.now().ctime())
    # f = time.strptime('%d','%b')   
    # DB.append((t, content))
    print t
    clean = bleach.clean(content, strip=True)
    # print f
    c.execute("INSERT INTO posts (content, time) VALUES (?,?)", (clean,t))
    DB.commit()
    DB.close()

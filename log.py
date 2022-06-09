
import os,sys,time


x = "lukman"
y = "kill"


def login():

    user = raw_input("Username : ")
    pasw = raw_input("Password : ")
    if user ==x and pasw ==y:
       print "Access Killer"
       time.sleep(2)
       os.system("python2 Killer.py")
    else:
       print  "Access Back"
       time.sleep(2)
       os.system("python2 log.py")
if __name__ == "__main__":
      login()

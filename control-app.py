import psutil,os
from threading import Timer
from datetime import datetime  
from datetime import timedelta  

apps=[]
endTime=0

def KillApps():
    for pid in psutil.process_iter() :#(process.pid for process in psutil.process_iter() if process.name()=="firefox.exe"):
        for appName in apps:
            if appName in pid.name().lower():
                print('\nmaster kill:')
                print('\tpid')
                pid.kill()
                break
    print('here')
    
    if datetime.now()<endTime:
        Timer(5, KillApps).start()

try :
    h = int(input('\n\n\nset how much hours do you want to deep work ? \n'))
except :
    h=0
try :
    m = int(input('minutes ? \n'))
except :
    m=0
try :
    s = int(input('and seconds ? \n'))
except :
    s=0

endTime=datetime.now()+timedelta(hours=h,minutes=m,seconds=s)

i=input('\n\n\ndo you want to add a program to kill ?\n')

while 'y' in i.lower() :
    i=''
    while i=='' :
        i=input('\n\nenter part of your app (better to say the whole name) ?\n')
    apps+=[i.lower()]

    i=input('\n\ndo you want to add a program to kill ?\n')

Timer(3, KillApps).start()
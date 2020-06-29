import psutil,os

for pid in psutil.process_iter() :#(process.pid for process in psutil.process_iter() if process.name()=="firefox.exe"):
    if 'telegram' in pid.name().lower():
        print(pid)
        pid.kill()
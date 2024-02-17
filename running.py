import subprocess
import os
from threading import Thread
#from apscheduler.schedulers.blocking import BlockingScheduler
import time

dir = "/home/ubuntu/pemilu/"

def code1():
    os.system('sudo ' + 'python3  ' + dir + 'code_1.py')

def code2():
    os.system('sudo ' + 'python3  ' + dir + 'code_2.py')

def code3():
    os.system('sudo ' + 'python3  ' + dir + 'code_3.py')

def code4():
    os.system('sudo ' + 'python3  ' + dir + 'code_4.py')

def code5():
    os.system('sudo ' + 'python3  ' + dir + 'code_5.py')

def running():
    Thread(target = code1).start()
    Thread(target = code2).start()
    Thread(target = code3).start()
    Thread(target = code4).start()
    Thread(target = code5).start()


running()

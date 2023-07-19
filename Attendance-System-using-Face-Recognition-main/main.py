import subprocess
import time
def run_script1():
    # Code for your program
    subprocess.run(['python', 'Attendance.py'])

def run_script2():
    # Code for your program
    subprocess.run(['python', 'msg_gui.py'])
    run_script1()
while True:
    # Run your program
    run_script2()

    # Sleep for a particular interval of time
    time.sleep(3600)  # Sleep for 1 hour
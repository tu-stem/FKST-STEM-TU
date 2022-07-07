from mistyPy.Robot import Robot
import time
from misty_ide_comm.ide_comm import IdeComm

comm = IdeComm()

def main():
    misty = Robot()

    print('log start')
    comm.send_message('stream start')
    
    for x in range(4):
        misty.drive_time(10,0,5000)
        time.sleep(5)
        misty.drive_time(0,20,5000)
        time.sleep(5)
    
    print('log stop')
    comm.send_message('stream stop')

    comm.shutdown()

if __name__ == '__main__':
    comm.start(main)
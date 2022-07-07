from mistyPy.Robot import Robot
import time
from misty_ide_comm.ide_comm import IdeComm

comm = IdeComm()

def main():
    misty = Robot()

    print('log hello')
    comm.send_message('stream hello')

    misty.move_arms(30, 20)
    misty.move_arms(-30, -20)
    misty.speak("Hello World, I'm misty!")
    misty.run_skill()

    print('log goodbye')
    comm.send_message('stream goodbye')

    comm.shutdown()

if __name__ == '__main__':
    comm.start(main)

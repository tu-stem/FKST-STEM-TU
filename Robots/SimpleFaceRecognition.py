from mistyPy.Robot import Robot
from mistyPy.Events import Events

misty = Robot()

def FaceRec(data):
 msg='Hi'+' '+data['message']['label']
 misty.speak(msg)
misty.register_event(event_name='Face_Recognition_event', event_type=Events.FaceRecognition, callback_function=FaceRec, keep_alive=False)

misty.keep_alive()
#!/usr/bin/env python
import roslib
#roslib.load_manifest('my_package')
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int16

def callback(data):
    #Aquie va lo de los angulos y pa publicacion
    #print(data.data)
    res = data.data
    res = 1450-res
    pil =((180.0/1100.0)*float(res))+90
    dire.publish(int(pil))
    #print(int(pil))
    
def listener():
    global dire
    dire = rospy.Publisher('AutoModelMini/manual_control/steering',Int16, queue_size = 10)
    rospy.init_node('Convert', anonymous=True)
    rospy.Subscriber("Angulo", Int16, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
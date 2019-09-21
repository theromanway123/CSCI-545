#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def publish_topic():
    
    
    # Create a ROS publisher that publishes to the topic 'sensor_reading'. It should give a String message, with a queue size of 10
    ### START CODE HERE ###
	publisher = rospy.Publisher('sensor_reading',String,queue_size=10)	
	### END CODE HERE ###

    # Create a node 'ros_node_publisher'
    ### START CODE HERE ###
	rospy.init_node('ros_node_publisher',anonymous=True)		
	### END CODE HERE ###
        
    # Set a publishing rate of 10 hz (10 messages per second)
	### START CODE HERE ###
	rate = rospy.Rate(10) #10hz
	### END CODE HERE ###

	while not rospy.is_shutdown():
        # Write string formatted as 'Y <time>' where time is the ros time since start
        # We always return a Y as the message, meaning the obstacle is always detected
		### START CODE HERE ###
		publish_str = "Y  %s" % rospy.get_time()
		### END CODE HERE ###

        # Log and publish the information to the 'sensor_reading' topic
		### START CODE HERE ###
		rospy.loginfo(publish_str)
		publisher.publish(publish_str)
		### END CODE HERE ###    

if __name__ == '__main__':
    try:
        publish_topic()
    except rospy.ROSInterruptException as e:
        print('ROS exception {0}'.format(e))
        pass

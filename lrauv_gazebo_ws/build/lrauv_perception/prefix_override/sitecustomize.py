import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/vampweeknd/lrauv_gazebo_ws/install/lrauv_perception'

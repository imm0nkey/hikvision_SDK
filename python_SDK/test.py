import HKIPcamera

import numpy as np
import cv2

ip = str('192.168.1.64')  # 摄像头IP地址，要和本机IP在同一局域网
name = str('admin')  # 管理员用户名
pw = str('itsc123456')  # 管理员密码

HKIPcamera.init(ip, name, pw)
while True:
    fram = HKIPcamera.getframe()
    cv2.imshow('frame', np.array(fram))
    if cv2.waitKey(24) & 0xff == 27:
        break

HKIPcamera.release()

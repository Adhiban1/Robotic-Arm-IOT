# Robotic-Arm-IOT

## Project by
### Students:
Adhiban Siddarth .V (Reg.No: 510418107001),

Sathish .S (Reg.No: 510418107002),

Surya .M (Reg.No: 510418107003)

Arunai Engineering College,

Thiruvannamalai.

### Supervisor: 
Mr. V. Velmurugan. A.P, 

Arunai Engineering College,

Thiruvannamalai.

## ABSTRACT
A robotic arm sometimes referred to as an industrial robot, is a device that runs in an equivalent way to a human arm, with several joints that either move along an axis or can rotate in certain directions. Some robotic arms are anthropomorphic and try and imitate the exact movements of human arms. They are, in most cases programmable and used to perform specific tasks, most commonly for manufacturing, fabrication, and industrial applications. Robotic arms were originally designed to help in mass production factories, most famously in the manufacturing of cars. They were also implemented to mitigate the risk of injury for workers, undertake monotonous tasks, and free workers to concentrate on the more complex production elements.

*Keywords* — 6 DOF, Robotic arm, IoT, Servo motor.

## App
App folder contains `app.py`, `data.json`, `details.txt` and `icon.ico` files.

`app.py` opens Robotic Arm App. Any one can easily control the Robotic Arm using this app easily, there is no need of knowing coding.

`data.json` stored the positions of robotic arm.

### details.txt
{"IP": "192.168.4.1", "port": 80, "base": 0, "sholder": 135, "elbow": 135, "wristR": 0, "wristU": 45, "gripper": 150, "s1From": -24, "s1To": 24, "s2From": 0, "s2To": 24, "s3From": 0, "s3To": 24, "s4From": 0, "s4To": 180, "s5From": 0, "s5To": 180, "s6From": 90, "s6To": 150, "x": 0, "y": 0, "z": 12, "length": 12 }

`IP` : Enter the IP address of ESP32 here.

## Test App
Test app is used to test the Correct allignment of Robotic arm Servo motors

## ESP32 Code
ESP32 Code folder contains C++ code. Load this code to ESP32.

## Project files
This folder contains `PROJECT.pdf`, `Report.pdf` and `slide.pptx`.
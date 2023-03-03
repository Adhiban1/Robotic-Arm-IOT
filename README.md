# DESIGN AND IMPLEMENTATION OF AN AUTOMATED ROBOTIC ARM USING IOT

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

---

# Documentation
## details.txt:
```json
{
"IP": "192.168.4.1",
"port": 80,
"base": 0,
"sholder": 135,
"elbow": 135,
"wristR": 0,
"wristU": 45,
"gripper": 150,
"s1From": -24,
"s1To": 24,
"s2From": 0,
"s2To": 24,
"s3From": 0,
"s3To": 24,
"s4From": 0,
"s4To": 180,
"s5From": 0,
"s5To": 180,
"s6From": 90,
"s6To": 150,
"x": 0,
"y": 0,
"z": 12,
"length": 12
}
```
|Parameter|Description|
|---|---|
|`IP`|IP address of ESP32|
|`port`|ESP32 port|
|`base`|Initial angle of `base` servo motor|
|`sholder`|Initial angle of `sholder` servo motor|
|`elbow`|Initial angle of `elbow` servo motor|
|`wristR`|Initial angle of `wristR` servo motor|
|`wristU`|Initial angle of `wristU` servo motor|
|`gripper`|Initial angle of `gripper` servo motor|
|`s1From`|Minimum angle for `base` servo motor|
|`s1To`|Maximum angle for `base` servo motor|
|`s2From`|Minimum angle for `sholder` servo motor|
|`s2To`|Maximum angle for `sholder` servo motor|
|`s3From`|Minimum angle for `elbow` servo motor|
|`s3To`|Maximum angle for `elbow` servo motor|
|`s4From`|Minimum angle for `wristR` servo motor|
|`s4To`|Maximum angle for `wristR` servo motor|
|`s5From`|Minimum angle for `wristU` servo motor|
|`s5To`|Maximum angle for `wristU` servo motor|
|`s6From`|Minimum angle for `gripper` servo motor|
|`s6To`|Maximum angle for `gripper` servo motor|
|`x` `y` `z`|Initial coordinate position|
|`length`|`Length of the arm` from base servo motor to wristU servo motor|
## App (app.py)
Importing packages
```python
from tkinter import *
import socket
import json
from math import *
from time import sleep
import sys
```
Reading data from `details.txt`
```python
with open("details.txt", "r") as f:
    details = json.loads(f.read())
```
Reading data from `data.json`
```python
with open("data.json", "r") as f:
    data = json.loads(f.read())
```
initializing the values
```python
x = details["x"]
y = details["y"]
z = details["z"]
l = details["length"]

base = details["base"]
sholder = details["sholder"]
elbow = details["elbow"]
wristR = details["wristR"]
wristU = details["wristU"]
gripper = details["gripper"]

baseList = data["baseList"]
sholderList = data["sholderList"]
elbowList = data["elbowList"]
wristRList = data["wristRList"]
wristUList = data["wristUList"]
gripperList = data["gripperList"]

sock = socket.socket()
host = details["IP"]  # ESP32 IP in local network
port = details["port"]  # ESP32 Server Port
```
Functions:
|Functions|Description|
|---|---|
|storeData|It will store servo motor angles to `data.json`|
|formula|It will do inverse kinematics converting `x`, `y`, `z` coordinates to servo motor angles|
|display|It will show the coordinates and othe details in tkinter window|
|check|It checks whether `x`, `y`, `z` goes out of range or not|
|update|It will update the x,y,z coordinates in tkinter window|
|connect|It will connect to ESP32|
|disconnect|It will disconnect ESP32|
|send|It will send servo motor angles to ESP32|
|xf|It will change `x` value when ever the `x slide` is changed in tkinter|
|move|It will move Robotic arm to the position where we set x,y,z|
|record|It will store that x,y,z coordinates to `data.json`|
|clear|It will make empty `data.json`|
|default|It will move Robotic Arm to its default position|
|automate|It will get all coordinates from `data.json` and move Robotic Arm to that coordinates in continous loop|

from tkinter import *
import socket
import json
from math import *
from time import sleep
import sys

with open("details.txt", "r") as f:
    details = json.loads(f.read())

with open("data.json", "r") as f:
    data = json.loads(f.read())


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


def storeData():
    global data, baseList, sholderList, elbowList, wristRList, wristUList, gripperList
    data = {
        "baseList": baseList,
        "sholderList": sholderList,
        "elbowList": elbowList,
        "wristRList": wristRList,
        "wristUList": wristUList,
        "gripperList": gripperList,
    }
    with open("data.json", "w") as f:
        f.write(json.dumps(data))


correct_range = True


def formula():
    global x, y, z, base, sholder, elbow, wristU
    try:
        if x == 0:
            x = 0.001
        if y == 0:
            y = 0.001
        if z == 0:
            z = 0.001
        base = acos(x / sqrt(pow(x, 2) + pow(y, 2)))
        sholder = acos(sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2)) / (2 * l)) + acos(
            sqrt(pow(x, 2) + pow(y, 2)) / sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2))
        )
        elbow = pi - 2 * acos(sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2)) / (2 * l))
        wristU = 3 * pi / 2 - sholder - elbow

        base *= 180 / pi
        sholder *= 180 / pi
        elbow *= 180 / pi
        elbow = 180 - elbow
        wristU *= 180 / pi

        s5.set(wristU)
    except ValueError:
        l3.configure(text="ValueError", fg="#FF0000")


def display(a):
    l3.configure(text=a)


def check():
    global x, y, z, base, sholder, elbow, wristU, correct_range
    if (
        1 < sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2)) < 24
        and 0 <= elbow <= 120
        and 0 <= base <= 180
        and 0 <= sholder <= 180
        and 0 <= wristU <= 180
    ):
        l3.configure(text="CORRECT RANGE", fg="#00FF00")
        correct_range = True
    else:
        l3.configure(text="OUT OF RANGE", fg="#FF0000")
        correct_range = False


def update():
    l2.configure(
        text=f"X: {x:3.3f}, Y: {y:3.3f}, Z: {z:3.3f}\nWristR: {wristR:3d}, WristU: {wristU:3.3f}, Gripper: {gripper:3d}"
    )


def connect():
    try:
        sock.connect((host, port))
        l1.configure(text="---CONNECTED---", fg="#00FF00")
        formula()
        update()
    except TimeoutError:
        l1.configure(text="TimeOutError", fg="#FF0000")


def send():
    sock.send(
        f"{int(base):3d}{int(sholder):3d}{int(elbow):3d}{wristR:3d}{int(wristU):3d}{gripper:3d}".encode(
            "utf-8"
        )
    )


def xf(a):
    global x
    x = float(a)
    formula()
    update()
    check()


def yf(a):
    global y
    y = float(a)
    formula()
    update()
    check()


def zf(a):
    global z
    z = float(a)
    formula()
    update()
    check()


def wristRf(a):
    global wristR
    wristR = int(a)
    update()


def wristUf(a):
    global wristU
    wristU = float(a)
    update()


def gripperf(a):
    global gripper
    gripper = int(a)
    update()


win = Tk()
win.geometry("650x550")
win.iconbitmap("icon.ico")
win.title("Automated Robotic Arm using IoT")

l1 = Label(text="", font=("TimesNewRoman", 12, "italic", "bold"))
l1.pack()

b1 = Button(
    text="Connect", command=connect, font=("TimesNewRoman", 12, "bold"), bg="#FFFF00"
)
b1.pack()


def disconnect():
    sock.close()
    # l1.configure(text="---DISCONNECTED---", fg="#FF0000")
    sys.exit()


Button(
    text="Disconnect",
    command=disconnect,
    font=("TimesNewRoman", 12, "bold"),
    bg="#FF0000",
).pack(padx=5, pady=5)

l2 = Label(text="", font=("TimesNewRoman", 20, "bold"))
l2.pack()

scale_length = 450

s1 = Scale(
    from_=details["s1From"],
    to=details["s1To"],
    orient=HORIZONTAL,
    length=scale_length,
    command=xf,
    resolution=0.001,
    font=("TimesNewRoman", 12, "bold"),
    fg="#00FF00",
)
s1.set(details["x"])
s1.pack()

s2 = Scale(
    from_=details["s2From"],
    to=details["s2To"],
    orient=HORIZONTAL,
    length=scale_length,
    resolution=0.001,
    command=yf,
    font=("TimesNewRoman", 12, "bold"),
    fg="#00FF00",
)
s2.set(details["y"])
s2.pack()

s3 = Scale(
    from_=details["s3From"],
    to=details["s3To"],
    orient=HORIZONTAL,
    length=scale_length,
    resolution=0.001,
    command=zf,
    font=("TimesNewRoman", 12, "bold"),
    fg="#00FF00",
)
s3.set(details["z"])
s3.pack()

s4 = Scale(
    from_=details["s4From"],
    to=details["s4To"],
    orient=HORIZONTAL,
    length=scale_length,
    command=wristRf,
    font=("TimesNewRoman", 12, "bold"),
    fg="#00FF00",
)
s4.set(details["wristR"])
s4.pack()

s5 = Scale(
    from_=details["s5From"],
    to=details["s5To"],
    orient=HORIZONTAL,
    resolution=0.001,
    length=scale_length,
    command=wristUf,
    font=("TimesNewRoman", 12, "bold"),
    fg="#00FF00",
)
s5.set(details["wristU"])
s5.pack()

s6 = Scale(
    from_=details["s6From"],
    to=details["s6To"],
    orient=HORIZONTAL,
    length=scale_length,
    command=gripperf,
    font=("TimesNewRoman", 12, "bold"),
    fg="#00FF00",
)
s6.set(details["gripper"])
s6.pack()

f2 = Frame(win)
f2.pack()


def move():
    if correct_range:
        send()
        display("MOVE")
        l3.configure(fg="#FF00FF")


def record():
    if correct_range:
        global baseList, sholderList, elbowList, wristRList, wristUList, gripperList, base, sholder, elbow, wristR, wristU, gripper
        baseList.append(base)
        sholderList.append(sholder)
        elbowList.append(elbow)
        wristRList.append(wristR)
        wristUList.append(wristU)
        gripperList.append(gripper)
        display(f"RECORDED [ {len(baseList)} ]")
        l3.configure(fg="#FF00FF")
        storeData()


def clear():
    global baseList, sholderList, elbowList, wristRList, wristUList, gripperList
    baseList = []
    sholderList = []
    elbowList = []
    wristRList = []
    wristUList = []
    gripperList = []
    display("CLEAR")
    l3.configure(fg="#FF00FF")
    storeData()


def default():
    global x, y, z, base, sholder, elbow, wristR, wristU, gripper

    x = details["x"]
    y = details["y"]
    z = details["z"]
    wristR = details["wristR"]
    gripper = details["gripper"]

    formula()

    s1.set(details["x"])
    s2.set(details["y"])
    s3.set(details["z"])
    s4.set(details["wristR"])
    s6.set(details["gripper"])
    display("DEFAULT")
    l3.configure(fg="#FF00FF")


def automate():
    global baseList, sholderList, elbowList, wristRList, wristUList, gripperList
    for _ in range(3):
        for base, sholder, elbow, wristR, wristU, gripper in zip(
            baseList, sholderList, elbowList, wristRList, wristUList, gripperList
        ):
            sock.send(
                f"{int(base):3d}{int(sholder):3d}{int(elbow):3d}{wristR:3d}{int(wristU):3d}{gripper:3d}".encode(
                    "utf-8"
                )
            )
            sleep(2.5)
    display("Automation process completed")
    l3.configure(fg="#FF00FF")


Button(
    f2,
    text="RECORD",
    command=record,
    font=("TimesNewRoman", 12, "bold"),
    bg="#0000FF",
    fg="#FFFFFF",
).pack(side=LEFT, padx=5, pady=5)

Button(
    f2,
    text="CLEAR",
    command=clear,
    font=("TimesNewRoman", 12, "bold"),
    bg="#0000FF",
    fg="#FFFFFF",
).pack(side=LEFT, padx=5, pady=5)

Button(
    f2,
    text="AUTOMATE",
    command=automate,
    font=("TimesNewRoman", 12, "bold"),
    bg="#0000FF",
    fg="#FFFFFF",
).pack(side=LEFT, padx=5, pady=5)

Button(
    f2,
    text="DEFAULT",
    command=default,
    font=("TimesNewRoman", 12, "bold"),
    fg="#FFFFFF",
    bg="#0000FF",
).pack(side=LEFT, padx=5, pady=5)

Button(
    f2,
    text="MOVE",
    command=move,
    font=("TimesNewRoman", 12, "bold"),
    bg="#0000FF",
    fg="#FFFFFF",
).pack(side=LEFT, padx=5, pady=5)

f3 = Frame(win)
f3.pack()

l3 = Label(f3, text="", font=("TimesNewRoman", 12, "bold"))
l3.pack()

win.mainloop()

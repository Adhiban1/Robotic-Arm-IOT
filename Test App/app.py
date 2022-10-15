import socket
from time import sleep
from tkinter import *
import json

win = Tk()
win.geometry("600x500")
win.iconbitmap("icon.ico")
# win.resizable(False, False)
win.title("Robotic Arm App")
l1 = Label(text="", font=("TimesNewRoman", 12, "italic", "bold"))
l1.pack()

with open("details.txt", "r") as f:
    details = json.loads(f.read())

base = details["base"]
sholder = details["sholder"]
elbow = details["elbow"]
wristR = details["wristR"]
wristU = details["wristU"]
gripper = details["gripper"]

baseList = []
sholderList = []
elbowList = []
wristRList = []
wristUList = []
gripperList = []

sock = socket.socket()
host = details["IP"]  # ESP32 IP in local network
port = details["port"]  # ESP32 Server Port


def update():
    l2.configure(
        text=f"Base: {base:3d}, Sholder: {sholder:3d}, Elbow: {elbow:3d}\nWristR: {wristR:3d}, WristU: {wristU:3d}, Gripper: {gripper:3d}"
    )


def connect():
    try:
        sock.connect((host, port))
        l1.configure(text="---CONNECTED---", fg="#00FF00")
        update()
    except TimeoutError:
        l1.configure(text="TimeOutError", fg="#FF0000")


b1 = Button(
    text="Connect", command=connect, font=("TimesNewRoman", 12, "bold"), bg="#FFFF00"
)
b1.pack()


def send():
    sock.send(
        f"{base:3d}{sholder:3d}{elbow:3d}{wristR:3d}{wristU:3d}{gripper:3d}".encode(
            "utf-8"
        )
    )


def basef(a):
    global base
    base = int(a)
    update()


def sholderf(a):
    global sholder
    sholder = int(a)
    update()


def elbowf(a):
    global elbow
    elbow = int(a)
    update()


def wristRf(a):
    global wristR
    wristR = int(a)
    update()


def wristUf(a):
    global wristU
    wristU = int(a)
    update()


def gripperf(a):
    global gripper
    gripper = int(a)
    update()


l2 = Label(
    text=f"Base: {base:3d}, Sholder: {sholder:3d}, Elbow: {elbow:3d}\nWristR: {wristR:3d}, WristU: {wristU:3d}, Gripper: {gripper:3d}",
    font=("TimesNewRoman", 20, "bold"),
)
l2.pack()

s1 = Scale(
    from_=details["s1From"],
    to=details["s1To"],
    orient=HORIZONTAL,
    length=300,
    command=basef,
    font=("TimesNewRoman", 12, "bold"),
    fg="#00FF00",
)
s1.set(details["base"])
s1.pack()
s2 = Scale(
    from_=details["s2From"],
    to=details["s2To"],
    orient=HORIZONTAL,
    length=300,
    command=sholderf,
    font=("TimesNewRoman", 12, "bold"),
    fg="#00FF00",
)
s2.set(details["sholder"])
s2.pack()
s3 = Scale(
    from_=details["s3From"],
    to=details["s3To"],
    orient=HORIZONTAL,
    length=300,
    command=elbowf,
    font=("TimesNewRoman", 12, "bold"),
    fg="#00FF00",
)
s3.set(details["elbow"])
s3.pack()
s4 = Scale(
    from_=details["s4From"],
    to=details["s4To"],
    orient=HORIZONTAL,
    length=300,
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
    length=300,
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
    length=300,
    command=gripperf,
    font=("TimesNewRoman", 12, "bold"),
    fg="#00FF00",
)
s6.set(details["gripper"])
s6.pack()
f2 = Frame(win)
f2.pack()


def display(a):
    l3.configure(text=a)


def move():
    send()
    display("MOVE")


def record():
    global baseList, sholderList, elbowList, wristRList, wristUList, gripperList, base, sholder, elbow, wristR, wristU, gripper
    baseList.append(base)
    sholderList.append(sholder)
    elbowList.append(elbow)
    wristRList.append(wristR)
    wristUList.append(wristU)
    gripperList.append(gripper)
    display(f"RECORDED [ {len(baseList)} ]")


def clear():
    global baseList, sholderList, elbowList, wristRList, wristUList, gripperList
    baseList = []
    sholderList = []
    elbowList = []
    wristRList = []
    wristUList = []
    gripperList = []
    display("CLEAR")


def default():
    global base, sholder, elbow, wristR, wristU, gripper
    base = details["base"]
    sholder = details["sholder"]
    elbow = details["elbow"]
    wristR = details["wristR"]
    wristU = details["wristU"]
    gripper = details["gripper"]
    s1.set(details["base"])
    s2.set(details["sholder"])
    s3.set(details["elbow"])
    s4.set(details["wristR"])
    s5.set(details["wristU"])
    s6.set(details["gripper"])
    display("DEFAULT")


def automate():
    global baseList, sholderList, elbowList, wristRList, wristUList, gripperList
    for _ in range(3):
        for base, sholder, elbow, wristR, wristU, gripper in zip(
            baseList, sholderList, elbowList, wristRList, wristUList, gripperList
        ):
            sock.send(
                f"{base:3d}{sholder:3d}{elbow:3d}{wristR:3d}{wristU:3d}{gripper:3d}".encode(
                    "utf-8"
                )
            )
            sleep(2.5)
    display("Automation process completed")


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
l3 = Label(f3, text="", font=("TimesNewRoman", 12, "bold"), fg="#FF0000")
l3.pack()
win.mainloop()

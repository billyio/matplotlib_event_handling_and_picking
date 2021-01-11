import numpy as np
import matplotlib.pyplot as plt 

def motion(event):
    global gco
    if gco is None:
        return
    x = event.xdata
    y = event.ydata
    gco.set_data(x,y)
    plt.draw()

def onpick(event):
    global gco
    gco = event.artist
    plt.title(gco)

def release(event):
    global gco
    gco = None

def read_coordinate(file_path):
    file = open(file_path, 'r') 
    lines = file.readlines()
    coordinates = []
    for i in range(len(lines)):
        coord = lines[i].replace('\n', '')
        coord = list(map(int, coord.split(', ')))
        coordinates.append(coord)
    return coordinates

def plot_coordinates(coordinates):
    for i in range(len(coordinates)):
        x, y = coordinates[i][0], coordinates[i][1]
        plt.plot(x, y, "o", markersize=12)

gco = None
plt.figure()

coordinates = read_coordinate("sample/correspondence_A.txt")
plot_coordinates(coordinates)

plt.connect('motion_notify_event', motion)
plt.connect('pick_event', onpick)
plt.connect('button_release_event', release)
plt.show()

# gco = None
# plt.figure()

# plt.plot(0,0,"o",pickradius=15)
# plt.plot(1,0,"o",picker=15)
# plt.plot(5,0,"o",picker=15)
# plt.plot(5,5,"o",picker=15)
# plt.plot(5,10,"o",picker=15)

# plt.connect('motion_notify_event', motion)
# plt.connect('pick_event', onpick)
# plt.connect('button_release_event', release)
# plt.show()
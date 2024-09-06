from tkinter import * # Import tkinter
import math
#import gift_wrapping

def add(event):
    points.append([event.x, event.y])
    repaint()

def remove(event):
    for [x, y] in points:
        if distance(x, y, event.x, event.y) <= 10:
            points.remove([x, y])
    repaint()

def distance(x, y, x1, y1):
    return ((x - x1) * (x - x1) + (y - y1) * (y - y1)) ** 0.5

def repaint():
    canvas.delete("point")
    if len(points) > 0:
        #
        #
        #
        H = getConvexHull(points) # call GiftWrapping getConvexHull
        #
        #
        #
        canvas.create_polygon(H, fill = "gray", tags = "point")

    for [x, y] in points:
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, tags = "point")
    
def displayInstructions():
    instructions = ["INSTRUCTIONS", "Add:", "Left Click", "Remove:", "Right Click"]
    x = 20
    y = 20
    canvas.create_rectangle(x, y, x + 160, y + 80)
    canvas.create_text(x + 10 + 40, y + 20, text = instructions[0], justify = CENTER)
    for i in range(1, len(instructions), 2):
        canvas.create_text(x + 10 + 40, y + 20 + (i + 1) * 10, text = instructions[i], justify = RIGHT)
        canvas.create_text(x + 80 + 40, y + 20 + (i + 1) * 10, text = instructions[i + 1], justify = RIGHT)
        
def right_side_of_line(p0, p1, p2):
    return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1]) < 0

def getConvexHull(points: list) -> list:
    # gift wrapping algorithm
    hull = []
    h0 = points[0]
    for point in points:
        if point[0] > h0[0]:
            h0 = point
        elif point[0] >= h0[0] and point[1] < h0[1]:
            h0 = point
    hull.append(h0)
    t0 = h0

    while True:
        i = 0
        t1 = points[0]
        while t1 == t0 and i < len(points):
            t1 = points[i]
            i += 1
        for point in points:
            if right_side_of_line(t0, t1, point):
                t1 = point
        if t1 == h0:
            break
        hull.append(t1)
        t0 = t1
    return hull

window = Tk() # Create a window
window.title("Convex Hull") # Set title

width = 500
height = 150
radius = 2
canvas = Canvas(window, bg = "white", width = width, height = height)
canvas.pack()

# Create a 2-D list for storing points
points = []

displayInstructions()

canvas.bind("<Button-1>", add)
canvas.bind("<Button-3>", remove)


window.mainloop() # Create an event loop

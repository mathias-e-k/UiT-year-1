from tkinter import *
import random
import math



class Ball:
    # ball_list = []
    def __init__(self, canvas):
        self.ball_list = []
        self.canvas = canvas
        self.canvas_width = int(self.canvas["width"])
        self.canvas_height = int(self.canvas["height"])

    def create_ball(self):
        self.ball_list.append(canvas.create_oval(0, 0, 4, 4, fill="#" + "%06x" % random.randint(0, 0xFFFFFF), tags="ball"))
        self.canvas.move(self.ball_list[-1], random.randint(0-2, self.canvas_width-2), random.randint(0-2, self.canvas_height-2))

        self.canvas.after(100, self.create_ball)
    
    def delete(self, id):
        self.ball_list.remove(id)
        print(len(self.ball_list), id)
        self.canvas.delete(id)

    def get_ball_list(self):
        return self.ball_list
    
    def get_ball_position(self, id):
        return self.canvas.coords(id)
       
class Player:
    def __init__(self, canvas, ball) -> None:
        self.size = 6
        self.canvas = canvas
        self.ball = ball
        self.id = canvas.create_oval(0, 0, self.size, self.size, fill="white")
        self.canvas_width = int(self.canvas["width"])
        self.canvas_height = int(self.canvas["height"])
        self.canvas.move(self.id, random.randint(0-2, self.canvas_width-2), random.randint(0-2, self.canvas_height-2))
        self.target = -1
        self.target_distance = 999

        self.speed = 3

        self.xspeed = 0
        self.yspeed = 0
        self.angle = 0
        print(self.id)

    def move(self):
        self.canvas.move(self.id, self.xspeed, self.yspeed)
        previous_target_distance = self.target_distance
        self.find_target_distance()
        if previous_target_distance / self.target_distance  < 1:
            self.ball.delete(self.target)
            self.find_closest()
        self.canvas.after(20, self.move)

    def find_target_distance(self) -> int:
        self_coords = self.canvas.coords(self.id)
        x1, y1 = self_coords[0], self_coords[1]
        xpos = x1 + self.size//2
        ypos = y1 + self.size//2
        coords = self.ball.get_ball_position(self.target)
        if len(coords) == 0:
            self.canvas.after(100, self.find_closest)
            return
        ball_xpos = coords[0]+2
        ball_ypos = coords[1]+2
        self.target_distance = math.dist((xpos, ypos), (ball_xpos, ball_ypos))

    def find_closest(self):
        x1, y1, x2, y2 = self.canvas.coords(self.id)
        xpos = x1 + self.size//2
        ypos = y1 + self.size//2
        distance = 999
        for ball_id in self.ball.get_ball_list():
            coords = self.ball.get_ball_position(ball_id)
            ball_xpos = coords[0]+2
            ball_ypos = coords[1]+2
            new_distance = math.dist((xpos, ypos), (ball_xpos, ball_ypos))
            if new_distance < distance:
                distance = new_distance
                self.angle = math.atan2((ball_ypos-ypos), (ball_xpos-xpos))
                self.target = ball_id
                self.target_distance = distance
        self.xspeed = self.speed * math.cos(self.angle)
        self.yspeed = self.speed * math.sin(self.angle)



if __name__ == "__main__":
    root = Tk()
    root.title = "Game"
    root.resizable(0,0)
    root.wm_attributes("-topmost", 1)

    canvas = Canvas(root, width=300, height=300, bd=0, highlightthickness=0)
    canvas.pack()

    
    ball = Ball(canvas)
    ball.create_ball()
    for i in range(10):
        player = Player(canvas, ball)
        player.canvas.after(i, player.find_closest)
        player.canvas.after(i+1, player.move)
    root.mainloop()
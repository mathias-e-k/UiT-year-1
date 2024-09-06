# Koden fungerer som beskrevet i oppgaven

# PS: på oppgave 13 fikk jeg ikke plass til å skrive inn hele f string, så jeg skriver den her:
# f"You got {numbers[number]} {fruits[fruit]}{'s' if number != 0 else ''}"

import random as r
import tkinter as tk
import tkinter.messagebox
import math

class Shape():
    def __init__(self, color, fill, x, y):
        self._color = color
        self._fill = fill
        self._x = x
        self._y = y

    def __str__(self):
        return f"SHAPE: color={self._color} fill={self._fill} x={self._x} y={self._y}"

    
class Circle(Shape):
    def __init__(self, color, fill, x, y, radius):
        super().__init__(color,fill, x, y)
        self._radius = radius        

    def point_is_inside(self, x, y) -> bool: # returns True if x, y is inside circle
        center_x = self._x + self._radius
        center_y = self._y + self._radius
        if math.dist((center_x, center_y), (x, y)) < self._radius:
            return True
        else:
            return False
        
    
    def __str__(self):
        return f"CIRCLE: color={self._color} fill={self._fill} x={self._x} y={self._y} radius={self._radius}"
        

    def draw(self, canvas:tk.Canvas):
        canvas.create_oval(self._x, self._y, self._x + 2*self._radius, self._y + 2*self._radius, fill=self._fill)
        canvas.create_text(self._x, self._y,text=self)

class Rectangle(Shape):
    def __init__(self, color, fill, x, y, height, length):
        super().__init__(color,fill, x, y)
        self._height = height
        self._length = length

    def point_is_inside(self, x, y) -> bool: # returns True if x, y is inside rectangle
        center_x = self._x + self._length / 2
        center_y = self._y + self._height / 2
        h_distance = ((x - center_x) * (x - center_x)) ** 0.5
        v_distance = ((y - center_y) * (y - center_y)) ** 0.5
        if h_distance <= self._length / 2 and v_distance <= self._height / 2:
            return True
        return False

    def __str__(self):
        return f"RECTANGLE: color={self._color} fill={self._fill} x={self._x} y={self._y} height={self._height} length={self._length}"
        

    def draw(self,canvas:tk.Canvas):
        canvas.create_rectangle(self._x, self._y, self._x+self._height, self._y+self._length, fill=self._fill)
        canvas.create_text(self._x, self._y,text=self)
               
        
class MyGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.shape_list = []
        self.window.title("Draw shapes")
        self.window.configure(background="White")

        self.canvas_frame = tk.Frame(self.window)
        self.canvas_frame.pack()

        self.canvas = tk.Canvas(self.canvas_frame, bg="white", height=500, width=600)
        self.canvas.pack()

        self.bottom_frame = tk.Frame(self.window)
        self.bottom_frame.pack()

        # the radiobuttons for fill color
        self.color = tk.StringVar() # shared by the color radiobuttons
        self.color.set("red")
        self.rb_red = tk.Radiobutton(self.bottom_frame, text = "red", bg = "red", variable = self.color, value = "red")
        self.rb_red.pack(side="left")
        self.rb_blue = tk.Radiobutton(self.bottom_frame, text = "blue", bg = "blue", variable = self.color, value = "blue")
        self.rb_blue.pack(side="left")
        self.rb_green = tk.Radiobutton(self.bottom_frame, text = "green", bg = "green", variable = self.color, value = "green")
        self.rb_green.pack(side="left")

        
        # the radiobuttons for shape type
        self.shape_type = tk.StringVar()
        self.shape_type.set("Circle")
        self.rb_circle = tk.Radiobutton(self.bottom_frame, text = "Circle", bg = "white", variable = self.shape_type, value = "Circle")
        self.rb_circle.pack(side="left")
        self.rb_rectangle = tk.Radiobutton(self.bottom_frame, text = "Rectangle", bg = "white", variable = self.shape_type, value = "Rectangle")
        self.rb_rectangle.pack(side="left")
        
        # label for amount of shapes
        self.label_text = tk.StringVar()
        self.label_text.set("0")
        self.label_amt_shapes = tk.Label(self.bottom_frame, textvariable=self.label_text)
        self.label_amt_shapes.pack(side="left")

        self.canvas.bind("<Button-1>", self.processMouseEvent)
        
        self.window.mainloop()

    def repaint(self):
        self.canvas.delete("all")
        for shape in self.shape_list:
            shape.draw(self.canvas) # be figuren om å tegne seg selv
       
    # is the point x, y inside any existing shape?
    def inside_any(self,x,y):
        for shape in self.shape_list:
            if shape.point_is_inside(x,y):
                return shape
        return None      
    
    # create or delete shape 
    def processMouseEvent(self,event):
        existing_shape = self.inside_any(event.x,event.y)
        if existing_shape == None:
            if self.shape_type.get() == "Circle":
                circle = Circle(color="black", fill=self.color.get(), x=event.x, y=event.y, radius=r.randint(20, 40))
                circle.draw(self.canvas)
                self.shape_list.append(circle)
            if self.shape_type.get() == "Rectangle":
                rectangle = Rectangle(color="black", fill=self.color.get(), x=event.x, y=event.y, height=r.randint(20, 40), length=r.randint(20, 40))
                rectangle.draw(self.canvas)
                self.shape_list.append(rectangle)            
            
        else:
            if isinstance(existing_shape, Circle):
                delete = tkinter.messagebox.askyesno(message="Delete this Circle?")
            if isinstance(existing_shape, Rectangle):
                delete = tkinter.messagebox.askyesno(message="Delete this Rectangle?")
            
            if delete:
                self.shape_list.remove(existing_shape)

        self.label_text.set(len(self.shape_list))
        self.repaint()

   
if __name__ == "__main__":
    my_gui = MyGUI()
    

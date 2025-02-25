# -*- coding: utf-8 -*-

"""
    @Author 坦克手贝塔
    @Date 2022/1/18 18:32
"""
from tkinter.filedialog import *
from tkinter.colorchooser import *

WIDTH = 900
HEIGHT = 450


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.canvas = Canvas(root, width=WIDTH, height=HEIGHT*0.9, bg="white")
        self.master = master
        # id of the last drawing
        self.last_draw = 0
        # position x and position y
        self.x = 0
        self.y = 0
        self.draw_flag = False
        self.pen_color = "#ff0000"
        self.pack()
        self.create_widget()

    def create_widget(self):
        # canvas
        self.canvas.pack()
        # button
        # start button
        btn_start = Button(root, text="start", name="start")
        btn_start.pack(side="left", padx="10")
        # pen button
        btn_pen = Button(root, text="pen", name="pen")
        btn_pen.pack(side="left", padx="10")
        # rectangle button
        btn_rectangle = Button(root, text="rectangle", name="rectangle")
        btn_rectangle.pack(side="left", padx="10")
        # clear button
        btn_clear = Button(root, text="clear", name="clear")
        btn_clear.pack(side="left", padx="10")
        # eraser button
        btn_eraser = Button(root, text="eraser", name="eraser")
        btn_eraser.pack(side="left", padx="10")
        # line button
        btn_line = Button(root, text="line", name="line")
        btn_line.pack(side="left", padx="10")
        # arrow button
        btn_arrow = Button(root, text="arrow", name="arrow")
        btn_arrow.pack(side="left", padx="10")
        # color button
        btn_color = Button(root, text="color", name="color")
        btn_color.pack(side="left", padx="10")
        # bind events for buttons
        self.master.bind_class("Button", "<1>", self.event_manager)
        self.master.bind("<ButtonRelease-1>", self.stop_draw)

    def event_manager(self, event):
        button_name = event.widget.winfo_name()
        print(button_name)
        if button_name == "line":
            self.canvas.bind("<B1-Motion>", self.my_line)
        elif button_name == "arrow":
            self.canvas.bind("<B1-Motion>", self.my_arrow)
        elif button_name == "rectangle":
            self.canvas.bind("<B1-Motion>", self.my_rectangle)
        elif button_name == "pen":
            self.canvas.bind("<B1-Motion>", self.my_pen)
        elif button_name == "eraser":
            self.canvas.bind("<B1-Motion>", self.my_eraser)
        elif button_name == "clear":
            self.canvas.delete("all")
        elif button_name == "color":
            color = askcolor(color=self.pen_color, title="choose pen color")
            self.pen_color = color[1]

    def stop_draw(self, event):
        self.draw_flag = False
        self.last_draw = 0

    def start_draw(self, event):
        self.canvas.delete(self.last_draw)
        if not self.draw_flag:
            self.draw_flag = True
            self.x = event.x
            self.y = event.y

    def my_line(self, event):
        self.start_draw(event)
        self.last_draw = self.canvas.create_line(self.x, self.y, event.x, event.y, fill=self.pen_color)

    def my_arrow(self, event):
        self.start_draw(event)
        self.last_draw = self.canvas.create_line(self.x, self.y, event.x, event.y, arrow=LAST, fill=self.pen_color)

    def my_rectangle(self, event):
        self.start_draw(event)
        self.last_draw = self.canvas.create_rectangle(self.x, self.y, event.x, event.y, outline=self.pen_color)

    def my_pen(self, event):
        self.start_draw(event)
        self.canvas.create_line(self.x, self.y, event.x, event.y, fill=self.pen_color)
        self.x = event.x
        self.y = event.y

    def my_eraser(self, event):
        self.start_draw(event)
        self.canvas.create_rectangle(event.x-4, event.y-4, event.x+4, event.y+4, fill="white", outline="white")
        self.x = event.x
        self.y = event.y


if __name__ == "__main__":
    root = Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}+200+300")
    root.title("Simple Paint")
    app = Application(master=root)
    root.mainloop()

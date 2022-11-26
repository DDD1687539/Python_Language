# Coder: Lee
# Time:  2022/11/16 23:17


import math
import random
from math import sin, cos
from tkinter import Tk, Canvas


class Heart:
    def __init__(self):
        self.all_point_list = set()   # 生成原始坐标集
        self.frame_point_list = set()   # 每一帧的坐标

        self.get_points()   # 得到所有的点

    def count_point(self, value, enlarge=10.0):
        x = 16 * (sin(value) ** 3)
        y = -(13 * cos(value) - 5 * cos(2 * value) - 2 * cos(3 * value) - cos(4 * value))
        x = enlarge * x
        y = enlarge * y
        return int(x), int(y)

    def get_outside(self):
        """
        得到外型的原始边
        """
        for _ in range(500):
            rand_value = random.uniform(0, 2 * math.pi)
            self.all_point_list.add(self.count_point(rand_value))

    def fill_shape(self):
        """
        得到外型轮廓
        """
        large_ = random.uniform(0, 1)
        for _ in range(500):
            rand_value = random.uniform(0, 2 * math.pi)
            self.all_point_list.add(self.count_point(rand_value, enlarge=10 + large_))

    def get_points(self):
        self.get_outside()
        for _ in range(8):
            self.fill_shape()

    def animate(self, frame):
        """
        利用周期函数对爱心进行周期性放大缩小以达到模拟跳动的目的
        并且将爱心移动到canvas中间
        """
        for point in self.all_point_list:
            new_x = period(frame) * point[0] + 400
            new_y = period(frame) * point[1] + 300
            self.frame_point_list.add((new_x, new_y))

    def render(self, canvas, frame):
        self.animate(frame)   # 得到当前这一帧的动态坐标
        for point in self.frame_point_list:
            canvas.create_rectangle(
                point[0], point[1], point[0] + 4, point[1] + 4, fill="#ff2121")


def period(t):
    """周期性跳动"""
    larger = abs(1/2 * sin(t)) + 0.5
    if larger <= 0.8:
        larger = 0.8
    return larger


frame = 0

def draw(main, render_canvas, heart):
    global frame
    render_canvas.delete("all")
    heart.render(render_canvas, frame)
    frame += 1/12 * math.pi
    heart.frame_point_list = set()
    main.after(60, draw, main, render_canvas, heart)


if __name__ == "__main__":
    root = Tk()
    canvas = Canvas(root, width=800, height=600, background="black")
    canvas.pack()
    heart = Heart()
    draw(root, canvas, heart)
    root.mainloop()
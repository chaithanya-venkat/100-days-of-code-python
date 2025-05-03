# import colorgram as cg

# color_list = cg.extract('DamienHirstPainting.jpg', 100)

# rgbcolors = []
# for color in color_list:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgbcolors.append(new_color)

# print(rgbcolors)

import turtle
import random

color_list = [(208, 161, 82), (54, 89, 131), (143, 90, 40), (140, 26, 48), (223, 207, 105), (132, 177, 203), (47, 55, 103), (158, 46, 84), (169, 160, 39), (128, 189, 143), (83, 20, 45), (36, 43, 69), (187, 93, 105), (186, 140, 171), (84, 122, 181), (59, 39, 30), (88, 157, 90), (78, 153, 165), (195, 79, 72), (160, 202, 219), (45, 74, 78), (80, 73, 43), (59, 130, 120), (221, 182, 166), (218, 176, 188), (166, 207, 163), (179, 188, 212), (147, 38, 35), (48, 72, 69), (45, 65, 61)]

tim = turtle.Turtle()
turtle.colormode(255)
tim.penup()
tim.setpos([-250, -250])



for i in range(10):
    for j in range(10):
        tim.pencolor(random.choice(color_list))
        tim.dot(20)
        tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.right(180)






screen = turtle.Screen()
screen.exitonclick()

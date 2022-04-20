# import colorgram
# rgb_colors = []
# colors= colorgram.extract("image.jpg", 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(print(rgb_colors)
import turtle as turtle_module
import  random
import  random
color_list=[  (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]
turtle_module.colormode(255)
t = turtle_module.Turtle()
t.penup()
t.ht()
t.setheading(225)

t.fd(250)
t.setheading(0)
t.speed(0)
number_of_dot = 100
for dot_count in range(1, number_of_dot+1):
    t.dot(20,random.choice(color_list) )

    t.fd(50)
    if dot_count% 10 == 0:
        t.setheading(90)
        t.fd(50)
        t.setheading(180)
        t.fd(500)
        t.setheading(0)







































screen = turtle_module.Screen()

screen.exitonclick()
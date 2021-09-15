from turtle import Turtle, Screen

tim = Turtle()
tim.shape('turtle')
tim.color('green')

import random

colors = ['firebrick', 'pink', 'lavender', 'deep pink', 'orange', 'chartreuse',
          'purple', 'gray', 'dark blue']
def draw_shape(num_of_sides):
    angle = 360 / num_of_sides

    for _ in range(num_of_sides):

        tim.fd(100)
        tim.right(angle)



for i in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(i)


s = Screen()
s.exitonclick()

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

# import turtle
# a = turtle.Turtle()
# a.getscreen().bgcolor("blue")

# # a.penup()
# # a.goto(-200,100)
# # a.pendown()

# a.speed(25)

# a.left(90)
# a.forward(200)
# a.right(90)
# a.forward(50)
# a.right(90)
# a.forward(200)
# a.left(90)
# a.forward(50)
# a.right(90)
# a.forward(25)
# a.right(90)
# a.forward(150)
# a.right(90)
# a.forward(25)
# a.right(90)
# a.forward(50)
# a.end_fill()

# # def star(turtle, size):
# # 	if size <= 10:
# # 		return
# # 	else:
# # 		turtle.begin_fill()
# # 		for i in range(5):
# # 			turtle.forward(size)
# # 			star(turtle,size/3)
# # 			turtle.left(216)
# # 			turtle.end_fill()

# #star(a,360)
# turtle.done()
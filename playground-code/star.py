import turtle as t

screen = t.Screen()
screen.colormode(255)

r = 0
g = 0
b = 0

for i in range(100):
    t.right(125)
    t.fd(100)
    t.pencolor(r,g,b)
    t.fd(100)

    r = r + 1

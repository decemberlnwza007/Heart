import turtle as graph

def curve():
    for i in range(200):
        graph.left(1)
        graph.forward(1)

screen = graph.Screen()
screen.bgcolor("#8BD3E6") 

graph.shape("turtle")
graph.color("red")
graph.speed(10)

graph.begin_fill()

graph.left(90)

graph.right(45)
graph.forward(113)
curve()
graph.right(120)
curve()
graph.forward(113)

graph.begin_fill()

screen.mainloop()

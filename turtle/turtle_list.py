import turtle as tt

edge_length = 100
colors = ["coral", "gold", "brown", "red", "green", "blue", "yellow",\
    "purple", "orange", "cyan", "pink", "magenta", "goldenrod", "black"]

tt.color( colors[1], colors[-2] )
tt.hideturtle()

# tt.begin_fill()

tt.right(120)
tt.forward(edge_length)

tt.left(160)
tt.forward(edge_length)

tt.left(140)
tt.forward(edge_length - 5)

tt.left(140)
tt.forward(edge_length)

tt.showturtle()

# tt.end_fill()
tt.done()
import turtle as tt 

tt.color('red', 'pink')
tt.begin_fill()

n_sides = 7
side_length = 600.0 / n_sides
tt.forward(side_length)
while abs(round(tt.xcor(), 3)) != 0.000 or abs(round(tt.ycor(), 3)) != 0.000 :
    tt.left(360.0 / n_sides)
    tt.forward(side_length)

tt.end_fill()
tt.done()


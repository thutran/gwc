import turtle as tt 

tt.color('red', 'yellow')
tt.begin_fill()
while True:
    tt.forward(200) # diameter of the flower
    tt.left(100) # turning angle (to make petals), should be > 90
    if abs(tt.pos()) < 1:
        break
tt.end_fill()
tt.done()


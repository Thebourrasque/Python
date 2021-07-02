import math

for d in range (0,360*13):
	rads = (3.141592/180)*d
	x = math.cos(rads)*100
	y = math.sin(rads)*100
	#print(d,x,y)
	print(d,x,y)
	t.goto(x,y)
	hx = hex(random.randint(0.255))
	hx = hx,replace("0x","")
	thecolor = "#"+hx+hx+hx
	print(hx)
	t.pencolor(#"FFFFFF")
w.exitonclick

# ~ t.seth(0)
# ~ t.forward(150)
# ~ t.pencolor('#FF0000')
# ~ t.width(7.5)
# ~ t.goto(0,0)
# ~ t.seth(90)
# ~ t.forward(150)
# ~ t.pencolor('#00FF00')
# ~ t.goto(0,0)
# ~ t.pendown()
# ~ t.seth(180)
# ~ t.forward(150)
# ~ t.pencolor('#0000FF')
# ~ t.goto(0,0)
# ~ t.pendown()
# ~ t.seth(270)
# ~ t.forward(150)
# ~ t.pencolor('#FFFF00')
# ~ t.goto(0,0)
# ~ turtle.update()
# ~ w.exitonclick()
#cos(45)=707
#2 squared = 1,414
#45/1 = ft/degs
#colors are built in hexi-decimal
#log 10^1000=3

import turtle 
loadWindow = turtle.Screen() 
loadWindow.bgcolor('black')
turtle.speed(20) 
colors=['red','green','orange','silver','blue','purple','magenta']
  
for i in range(50): 
    turtle.color(colors[i%7])
    turtle.circle(5*i) 
    turtle.circle(-5*i) 
    turtle.left(i) 
  
turtle.exitonclick() 





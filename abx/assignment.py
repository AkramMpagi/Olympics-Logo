import turtle

def draw_circle(x, y, color, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.color(color)
    turtle.circle(radius)
    print(f"Drawing circle at position ({x}, {y}) with color {color} and radius {radius}")

def draw_olympic_logo(colors):
    turtle.setup(width=800, height=600)
    turtle.speed(2)

    positions = [(-110, 0), (0, 0), (110, 0), (-55, -100), (55, -100)]
    for i in range(len(colors)):
        draw_circle(positions[i][0], positions[i][1], colors[i], 100)

    turtle.hideturtle()
    turtle.done()

colors = ["blue", "black", "red", "yellow", "green"]
draw_olympic_logo(colors)

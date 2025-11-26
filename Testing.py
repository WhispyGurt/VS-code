11/26/25
import turtle
import random


# --- Setup ---
snek = turtle.Turtle()
turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Snek")
wn.bgcolor("lightgreen")
fruit=turtle.Turtle()
move_distance = 5
move_delay = 50 

#Score
score = 0
font_setup = ("Times new roman", 20, "bold")


score_turtle = turtle.Turtle()
score_turtle.color("#2A7D4F")
score_turtle.penup()
score_turtle.goto(350,350)
score_turtle.speed(0)




# Game functions
fruit.penup
fruit.hideturtle
fruit.goto(10, 30)
fruit.showturtle


# --- Collision Functions ---
def draw_and_log(drawer, distance):
    """
    Draws a line segment and logs points along it for collision detection.
    Assumes the pen is already down.
    """
    global fruit
    start_pos = drawer.position()
    drawer.forward(distance)
    end_pos = drawer.position()




    # Log points every 3 pixels for good accuracy
    steps = int(distance / 3)
    if steps == 0:
        steps = 1  # Ensure at least start and end are logged




    fruit.append(start_pos)
    fruit.append(end_pos)




    # Add intermediate points
    if steps > 1:
        x_step = (end_pos[0] - start_pos[0]) / steps
        y_step = (end_pos[1] - start_pos[1]) / steps
        for i in range(1, steps):
            inter_x = start_pos[0] + i * x_step
            inter_y = start_pos[1] + i * y_step
            fruit.append((inter_x, inter_y))




def check_collision():
    """Checks if snek is close to any logged wall point and resets if so."""
    global fruit, START_POS, COLLISION_DISTANCE
    player_pos = snek.position()
    for wall_pos in fruit:
        if snek.distance(wall_pos) <= COLLISION_DISTANCE:
            # --- COLLISION DETECTED! ---
            snek.hideturtle()
            snek.penup()
            snek.goto(0,0)
            snek.showturtle()
            return True  # Stop checking
    return False


def update_score():
    global score
    score+=1
    score_turtle.clear()
    score_turtle.write("Score:"+str(score), font=font_setup)


#--- Movement Functions ---


def h2():
    snek.left(45)




def h3():
    snek.right(45)




def h4():
    wn.bye()


def move_forward():
    snek.forward(MOVE_DISTANCE)
    wn.ontimer(move_forward, MOVE_DELAY)






# --- Event Listeners ---
wn.onkey(h2, "Right")
wn.onkey(h3, "Left")
wn.onkey(h2, "d")
wn.onkey(h3, "a")
wn.onkey(h4, "q")




# --- Start Game ---
move_forward()  # Start moving!
wn.listen()
wn.mainloop()







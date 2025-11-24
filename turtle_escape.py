import turtle
import random
import time

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("GET OUT!")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
maze_maker = turtle.Turtle()
wall_length = 20
width = 5
maze_maker.pensize(3)
maze_maker.speed(0)
maze_maker.hideturtle()
maze_maker.penup()
maze_maker.goto(-10, 5)
maze_maker.pendown()
tess.penup()
tess.goto(-10, 0)


barrier_drawer = turtle.Turtle()
barrier_drawer.color("red")
barrier_drawer.pensize(3)
barrier_drawer.penup()
barrier_drawer.hideturtle()
barrier_drawer.speed(0)



# Timer Variables
GAME_DURATION = 40  # Game duration in seconds
start_time = 0
game_over = False
timer_turtle = turtle.Turtle()  # Turtle to display the timer


# Set up the timer display turtle
timer_turtle.penup()
timer_turtle.hideturtle()
timer_turtle.goto(50, 180)  # Position the timer display


# --------------Timer Functions-----------
def update_timer():
    global start_time, game_over
    if game_over:
        return

    elapsed_time = int(time.time() - start_time)
    remaining_time = GAME_DURATION - elapsed_time
    timer_turtle.clear()
    timer_turtle.write(f"Time: {remaining_time}", font=("Arial", 20, "normal"))

    if remaining_time <= 0:
        game_over = True
        end_game()
    else:
        # Call this function again after 1000ms (1 second)
        wn.ontimer(update_timer, 1000)

def end_game():
    # Attempt to play an explosion sound if the playsound package is installed;
    # otherwise just close the window without raising an error.
    try:
        from playsound import playsound
        playsound("loud-explosion-425457.mp3")
    except Exception:
        pass
    wn.bye()
    # Flag to ensure the 10-second sound plays only once
    ten_second_sound_played = False

    # Redefine update_timer to add a 10-second warning sound
    def update_timer():
        global start_time, game_over, ten_second_sound_played
        if game_over:
            return

        elapsed_time = int(time.time() - start_time)
        remaining_time = GAME_DURATION - elapsed_time
        timer_turtle.clear()
        timer_turtle.write(f"Time: {remaining_time}", font=("Arial", 20, "normal"))

        # Play a sound once when there are 10 seconds remaining
        if remaining_time == 10 and not ten_second_sound_played:
            ten_second_sound_played = True
            try:
                playsound("loud-explosion-425457.mp3")
            except Exception:
                pass

        if remaining_time <= 0:
            game_over = True
            end_game()
        else:
            wn.ontimer(update_timer, 1000)

# Define gap characteristics
gap_size = 20  # Gap length
gap_probability = 0.5  # probability (50%)

#Create a list of random iteration numbers for barriers
num_barriers = 5
barrier_indices = random.sample(range(30), num_barriers)



## Bulding with gaps :)

for i in range(30):
    current_segment_length = wall_length - 10

    # 1. Is there space to draw two walls and a gap
    if current_segment_length > gap_size + 10 and random.random() < gap_probability:

        # Calculate the remaining space after subtracting the gap
        remaining_wall = current_segment_length - gap_size

        # 2. Randomly decide where to start the gap
        # The gap can start anywhere from 0 up to 'remaining_wall' distance from the corner
        gap_start_position = random.randint(5, int(remaining_wall) - 5)

        # Draw Wall Segment 1
        maze_maker.forward(gap_start_position)

        # Create the Gap
        maze_maker.penup()
        maze_maker.forward(gap_size)
        maze_maker.pendown()

        # Draw Wall Segment 2 (The ending piece)
        wall_end_position = current_segment_length - gap_start_position - gap_size
        maze_maker.forward(wall_end_position)

    else:
        # If no gap, draw full wall
        maze_maker.forward(current_segment_length)

    # Check if the current iteration 'i' is one of our "right numbers"
    if i in barrier_indices:
        # Get the maze_maker's current state (position and direction)
        current_pos = maze_maker.position()
        current_heading = maze_maker.heading()
        
        # Position the barrier_drawer
        barrier_drawer.goto(current_pos)
        barrier_drawer.setheading(current_heading)
        
        # Move "into" the path (which is to the left of the drawing direction)
        barrier_drawer.left(90)
        
      

        barrier_drawer.pendown()
        barrier_drawer.forward(20)
        barrier_drawer.penup()

    maze_maker.right(90)
    wall_length += 10


def h1():
    tess.forward(10)

def h2():
    tess.left(45)

def h3():
    tess.right(45)

def h4():
    wn.bye()

def h5():
    tess.goto(0, 0)
    wn.bye()


wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")
wn.ontimer(h5, 40000)

start_time = time.time()
update_timer()  
wn.listen()
wn.mainloop()
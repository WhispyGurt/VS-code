'''import turtle

turtle.setup(400,500)                # Determine the window size
wn = turtle.Screen()                 # Get a reference to the window
wn.title("Handling keypresses!")     # Change the window title
wn.bgcolor("lightgreen")             # Set the background color
tess = turtle.Turtle()               # Create our favorite turtle
maze_maker = turtle.Turtle()
wall_length = 20 
width = 5 
maze_maker.pensize(1.1)
maze_maker.speed(0)
maze_maker.penup()
maze_maker.goto(-10,5)
maze_maker.pendown()

#build the maze
for i in range(30):
   maze_maker.forward(wall_length-10)
   maze_maker.right(90)
   wall_length+=10



# The next four functions are our "event handlers".
def h1():
   tess.forward(10)

def h2():
   tess.left(45)

def h3():
   tess.right(45)

def h4():
    wn.bye()                        # Close down the turtle window

# These lines "wire up" keypresses to the handlers we've defined.
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")

# Now we need to tell the window to start listening for events,
# If any of the keys that we're monitoring is pressed, its
# handler will be called.
wn.listen()
wn.mainloop()'''

'''import turtle
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
maze_maker.speed(2)
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
    wn.bye()


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
wn.mainloop()'''

'''import turtle
from playsound import playsound
import os # Used to get the current working directory for relative paths

# Install playsound if you haven't already: pip install playsound

# Get the path to your sound file (replace 'your_sound.wav' with your actual file)
# It's recommended to place the sound file in the same directory as your Python script.
sound_file_path = os.path.join(os.getcwd(), 'playsound/loud-explosion-425457.mp3.wav') 

# Create a Turtle screen and turtle object
wn = turtle.Screen()
t = turtle.Turtle()

# Example: Play a sound when the turtle moves
def move_and_play():
    t.forward(50)
    playsound(sound_file_path, block=False) # block=False allows the program to continue while sound plays

# Bind a key to trigger the sound and movement
wn.listen()
wn.onkey(move_and_play, "space")

wn.mainloop()'''

import turtle
import random
import time

# --- Setup ---
turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("GET OUT!")
wn.bgcolor("lightgreen") 

#-----setup-----
BACKGROUND_IMAGE = "background.gif"

# set up the screen
wn = turtle.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic(BACKGROUND_IMAGE) 

wn.setup(width=1.0, height=1.0)

# --- Player Turtle (tess) ---
tess = turtle.Turtle()
tess.penup()
START_POS = (-10, 0)  # Define a constant for the start position
tess.goto(START_POS)

# --- Maze Drawing Turtles ---
maze_maker = turtle.Turtle()
wall_length = 20
width = 10
maze_maker.pensize(3)
maze_maker.speed(0)
maze_maker.hideturtle()
maze_maker.penup()
maze_maker.goto(-10, 5)
maze_maker.pendown() # Pen is down before the loop starts

barrier_drawer = turtle.Turtle()
barrier_drawer.color("red")
barrier_drawer.pensize(3)
barrier_drawer.penup()
barrier_drawer.hideturtle()
barrier_drawer.speed(0)

# --- Collision Detection Variables ---
wall_points = []  # List to store all wall coordinates
COLLISION_DISTANCE = 2  # How close tess can get to a wall point

# --- Timer Variables ---
GAME_DURATION = 40
start_time = 0
game_over = False
timer_turtle = turtle.Turtle()
timer_turtle.penup()
timer_turtle.hideturtle()
timer_turtle.goto(50, 180)
ten_second_sound_played = False  # Flag for 10-second sound

# --- Timer Functions ---
def end_game():
    """Stops the game, plays a sound, and closes the window."""
    global game_over
    game_over = True  # Set the flag to stop the timer
    try:
        from playsound import playsound
        playsound("loud-explosion-425457.mp3")
    except Exception:
        pass
    wn.bye()  # Close the window

def update_timer():
    """Updates the on-screen timer and checks for end-game conditions."""
    global start_time, game_over, ten_second_sound_played
    if game_over:
        return

    elapsed_time = int(time.time() - start_time)
    remaining_time = GAME_DURATION - elapsed_time
    timer_turtle.clear()
    timer_turtle.write(f"Time: {remaining_time}", font=("Arial", 20, "normal"))

    # Play a sound once when there are 10 seconds remaining
    if remaining_time <= 10 and not ten_second_sound_played:
        ten_second_sound_played = True
        try:
            from playsound import playsound
            playsound("loud-explosion-425457.mp3")
        except Exception:
            pass

    if remaining_time <= 0:
        end_game()  # Call the single end_game function
    else:
        wn.ontimer(update_timer, 1000)  # Schedule next update

# --- Collision Functions ---
def draw_and_log(drawer, distance):
    """
    Draws a line segment and logs points along it for collision detection.
    Assumes the pen is already down.
    """
    global wall_points
    start_pos = drawer.position()
    drawer.forward(distance)
    end_pos = drawer.position()

    # Log points every 3 pixels for good accuracy
    steps = int(distance / 3)
    if steps == 0:
        steps = 1  # Ensure at least start and end are logged

    wall_points.append(start_pos)
    wall_points.append(end_pos)

    # Add intermediate points
    if steps > 1:
        x_step = (end_pos[0] - start_pos[0]) / steps
        y_step = (end_pos[1] - start_pos[1]) / steps
        for i in range(1, steps):
            inter_x = start_pos[0] + i * x_step
            inter_y = start_pos[1] + i * y_step
            wall_points.append((inter_x, inter_y))

def check_collision():
    """Checks if Tess is close to any logged wall point and resets if so."""
    global wall_points, START_POS, COLLISION_DISTANCE
    player_pos = tess.position()
    for wall_pos in wall_points:
        if tess.distance(wall_pos) <= COLLISION_DISTANCE:
            # --- COLLISION DETECTED! ---
            tess.hideturtle()
            tess.penup()
            tess.goto(START_POS)  # Send back to start
            tess.showturtle()
            return True  # Stop checking
    return False

# --- Maze Generation 
gap_size = 20
gap_probability = 0.5
num_barriers = 5
barrier_indices = random.sample(range(30), num_barriers)

for i in range(30):
    current_segment_length = wall_length - 10

    if current_segment_length > gap_size + 10 and random.random() < gap_probability:
        gap_start_position = random.randint(5, int(current_segment_length - gap_size) - 5)

        # Draw Wall Segment 1
        draw_and_log(maze_maker, gap_start_position) 

        # Create the Gap
        maze_maker.penup()
        maze_maker.forward(gap_size)
        maze_maker.pendown()  # Put pen down for segment 2

        # Draw Wall Segment 2
        wall_end_position = current_segment_length - gap_start_position - gap_size
        draw_and_log(maze_maker, wall_end_position)

    else:
        # If no gap, draw full wall
        draw_and_log(maze_maker, current_segment_length)

    # --- Barrier Drawing 
    if i in barrier_indices:
        current_pos = maze_maker.position()
        current_heading = maze_maker.heading()
        
        barrier_drawer.goto(current_pos)
        barrier_drawer.setheading(current_heading)
        barrier_drawer.left(90)
        
        barrier_drawer.pendown()
        draw_and_log(barrier_drawer, 20)
        barrier_drawer.penup()

    maze_maker.right(90)
    wall_length += 10

# --- Movement Functions ---
def h1():
    """Move forward 10 steps, checking for collisions at each step."""
    
    # Move 1 pixel at a time, 10 times.
    for _ in range(10):
        tess.forward(1)
        

        if check_collision():
            break # Stop moving forward if you hit a wall

def h2():
    tess.left(45)

def h3():
    tess.right(45)

def h4():
    wn.bye()

def h5():
    pass

# --- Event Listeners ---
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "q")


# --- Start Game ---
start_time = time.time()
update_timer()  # Start the main timer loop
wn.listen()
wn.mainloop()

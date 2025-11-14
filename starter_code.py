import turtle as trtl
import random
import time

# ------------- constants and globals -------------
APPLE_IMAGE = "pear.gif"
BACKGROUND_IMAGE = "background.gif"
letter_list = list("asdfjklbceghimnopqrtuvwxyz")
current_letter = ""
apple = trtl.Turtle()
pear = trtl.Turtle()

# Timer Variables
GAME_DURATION = 30 # Game duration in seconds
start_time = 0
game_over = False
timer_turtle = trtl.Turtle() # Turtle to display the timer

# set up the screen
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic(BACKGROUND_IMAGE)
wn.addshape(APPLE_IMAGE)
apple.penup()
apple.hideturtle()

# Set up the timer display turtle
timer_turtle.penup()
timer_turtle.hideturtle()
timer_turtle.goto(300, 280) # Position the timer display

#--------------Timer Functions-----------
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
    apple.clear()
    apple.hideturtle()
    timer_turtle.goto(0, 0)
    timer_turtle.write("Game Over made by Oscar and Nahum!", align="center", font=("Arial", 50, "bold"))
    # Unbind keys to stop input
    for letter in "abcdefghijklmnopqrstuvwxyz":
        wn.onkeypress(None, letter)

# ------------- functions students will complete -------------
def generate_random_letter():
    global current_letter, letter_list
    if len(letter_list)==0:
        return "DONE, made by Oscar and Nahum" # Return empty string if no letters left
    else:
        number_of_letters = len(letter_list)
        slot = random.randint(0,number_of_letters-1)
        current_letter=letter_list.pop(slot)
        return current_letter

def get_random_xy():
    x = random.randint(-250, 250)
    y = random.randint(50, 250)
    return (x,y)

def draw_apple_and_letter():
    # Move the apple to a random position, give it a random letter, and draw that letter on the apple.
    # Uses generate_random_letter() and get_random_xy().
    global current_letter, game_over
    if game_over:
        return
    apple.clear() # erase old letter
    apple.shape(APPLE_IMAGE)
    apple.showturtle()
    current_letter = generate_random_letter()
    if current_letter == "": # Check for empty string, not None
        apple.hideturtle()
        return ("no letters left")
    location = get_random_xy()
    apple.goto(location[0], location[1])
    apple.write(current_letter, font=("Arial", 74, "bold"))
    return

def drop_apple():
    # Make the apple fall straight down and then draw a new apple and letter.
    global apple, game_over
    if game_over:
        return
    xcoord = apple.xcor()
    ycoord = apple.ycor()
    apple.goto(xcoord, ycoord-250)
    apple.clear()
    apple.hideturtle()
    apple.teleport(xcoord, ycoord)
    draw_apple_and_letter()

# ------------- key handling -------------
def handle_key(letter_pressed):
    global current_letter, game_over
    if game_over:
        return
    if letter_pressed == current_letter:
        drop_apple()
    else:
        # Handle incorrect key press (optional: add score penalty, etc.)
        pass

# Bind keys dynamically
for letter in "abcdefghijklmnopqrstuvwxyz":
    wn.onkeypress(lambda l=letter: handle_key(l), letter)

# ------------- main program -------------

# Start the timer and first apple drawing
start_time = time.time()
update_timer() # Start the timer updates
draw_apple_and_letter()
wn.listen()
trtl.done()

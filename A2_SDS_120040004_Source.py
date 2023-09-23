import turtle
import time
import random

GAME_DIMENSION = 500
GAME_MARGIN = 80
STYLE = ('Arial', 12, 'normal')
SQUARE_SIZE = 1
SNAKE_HEAD = 'blue'
SNAKE_BODY = ('black', 'yellow')
MONSTER_COLOR = 'red'

g_time, g_contact, g_motion = 0, 0, 'Paused'
g_snake_x, g_snake_y = 0, -GAME_MARGIN//2
g_monster_x, g_monster_y = 0, -GAME_MARGIN//2
g_key = ''
g_stop = True
g_last_motion = 'Paused'
g_food = []
g_food_dict = {}
g_snake_body = []
g_repeat = 0
g_last_food = None
g_end, g_snake_end, g_monster_end = False, False, False

# To set the screen display of the game
def set_screen():
    global g_screen
    g_screen = turtle.Screen()
    g_screen.tracer(0)
    g_screen.setup(width = GAME_DIMENSION+2*GAME_MARGIN, height = GAME_DIMENSION+3*GAME_MARGIN)
    g_screen.mode('standard')
    g_screen.title('Snake game')

# To set the border for the status area and motion area
def set_border():
    border = turtle.Turtle()
    border.penup()
    border.goto(-GAME_DIMENSION//2, (GAME_DIMENSION//2)+(GAME_MARGIN//2))
    border.pendown()
    border.color('black')
    border.pensize(2)
    for i in range(2):
        border.forward(GAME_DIMENSION)
        border.right(90)
        border.forward(GAME_DIMENSION+GAME_MARGIN)
        border.right(90)
    border.goto(-GAME_DIMENSION//2, (GAME_DIMENSION//2)-(GAME_MARGIN//2))
    border.forward(GAME_DIMENSION)
    border.hideturtle()

# To display a brief introduction of the game
def set_intro():
    global g_intro
    g_intro = turtle.Turtle()
    g_intro.penup()
    g_intro.goto(-GAME_DIMENSION//2, (GAME_DIMENSION//2)-(GAME_MARGIN//2)-120)
    g_intro.write('''
    Welcome to the snake game! 
    Please use the four arrow keys to move the snake
    Consume all the numbers without being caught by the monster 
    to win the game
    Click on the screen to start the game...
    ''', align = 'left', font = STYLE)
    g_intro.hideturtle()

# To display the status of the game
def set_status():
    global g_status
    g_status = turtle.Turtle()
    g_status.hideturtle()
    g_status.penup()
    g_status.goto(-GAME_DIMENSION//2, (GAME_DIMENSION//2)-10)
    g_status.write('    Contact: %d     Time: %d     Motion: %s '%(g_contact, g_time, g_motion), 
                    align = 'left', font = ('Arial', 14, 'normal'))

# To set the head of the snake
def set_snake():
    global g_snake, g_snake_x, g_snake_y
    g_snake = turtle.Turtle('square')
    g_snake.turtlesize(SQUARE_SIZE, SQUARE_SIZE, 1)
    g_snake.penup()
    g_snake.goto(0, -GAME_MARGIN//2)
    g_snake.color(SNAKE_HEAD)
    g_snake_x = g_snake.xcor()
    g_snake_y = g_snake.ycor()

# To add the body of the snake and store it in a list 
def set_snake_body():
    global g_snake_body, g_repeat
    repeat = g_food_dict.get((g_snake_x, g_snake_y-5), None)
    if len(g_snake_body) == 0:
        repeat = 5
    else:
        g_repeat += repeat

    for i in range(repeat):
        snake_body = turtle.Turtle('square')
        snake_body.turtlesize(SQUARE_SIZE, SQUARE_SIZE, 1)
        snake_body.color(SNAKE_BODY[0], SNAKE_BODY[1])
        snake_body.penup()
        if len(g_snake_body) < 5:
            snake_body.goto(0, -GAME_MARGIN//2)
        else: 
            snake_body.goto(g_snake_body[-1].pos())
        g_snake_body.append(snake_body)

# To set the monster
def set_monster():
    global g_monster, g_monster_x, g_monster_y
    g_monster = turtle.Turtle('square')
    g_monster.turtlesize(SQUARE_SIZE, SQUARE_SIZE, 1)
    g_monster.color(MONSTER_COLOR)
    g_monster.penup()
    while turtle.distance(g_monster) < 200:
        g_monster_x = random.randint(-(GAME_DIMENSION//2-((SQUARE_SIZE*20)-5)), GAME_DIMENSION//2-((SQUARE_SIZE*20)-5))
        g_monster_y = random.randint(-((GAME_DIMENSION//2)+(GAME_MARGIN//2))+((SQUARE_SIZE*20)-5), (GAME_DIMENSION//2)-(GAME_MARGIN//2)-120)
        g_monster.goto(g_monster_x, g_monster_y)
    turtle.hideturtle()   

# To set the foods and store them in a dictionary and a list
def set_food():
    global g_food_dict, g_food
    for i in range(9):
        food = turtle.Turtle()
        food.penup()
        while True:
            x = random.choice(range(-(GAME_DIMENSION//2)+10, (GAME_DIMENSION//2)-10, int(20*SQUARE_SIZE)))
            y = random.choice(range(-((GAME_DIMENSION//2)+(GAME_MARGIN//2))+5, (GAME_DIMENSION//2)-(GAME_MARGIN//2)-15, int(20*SQUARE_SIZE)))
            if ((x,y) not in g_food_dict and (x,y) != (0, -(GAME_MARGIN//2)-5)):
                break
        food.goto(x, y)
        food.write(i+1, align = 'center', font = STYLE)
        food.hideturtle()
        g_food.append(food)
        g_food_dict[(x,y)] = i+1
        time.sleep(0.1)

# To update the time every second
def update_time():
    global g_time
    g_time += 1
    g_screen.ontimer(update_time, 1000)

# To be bind to a keyboard event input and assign 'Up' to a variable
def up():
    global g_key
    g_key = 'Up'

# To be bind to a keyboard event input and assign 'Down' to a variable
def down():
    global g_key
    g_key = 'Down'

# To be bind to a keyboard event input and assign 'Right' to a variable
def right():
    global g_key
    g_key = 'Right'

# To be bind to a keyboard event input and assign 'Left' to a variable
def left():
    global g_key
    g_key = 'Left'

# To be bind to a keyboard event input and assign 'space' to a variable
def pause():
    global g_key, g_stop
    g_key = 'space'
    if (g_motion == 'Paused' and g_last_motion != 'Paused'):
        g_stop = False
    else: g_stop = True

# To get the keyboard event given by the player
# up(), down(), left(), right(), pause() functions should be defined before calling this function
def update_motion():
    turtle.listen()
    turtle.onkey(up, 'Up')
    turtle.onkey(down, 'Down')
    turtle.onkey(left, 'Left')
    turtle.onkey(right, 'Right')
    turtle.onkey(pause, 'space')
    turtle.hideturtle()
    g_screen.ontimer(update_motion, 300)

# To move the head of the snake
# body_motion() and snake_food_collide() function should be defined before calling this function
def snake_motion():
    global g_snake_x, g_snake_y, g_motion, g_key, g_last_motion, g_repeat, g_last_food, g_snake_end
    motion_dict = {'Up': (g_snake_x, g_snake_y+(20*SQUARE_SIZE)), 
                    'Down': (g_snake_x, g_snake_y-(20*SQUARE_SIZE)), 
                    'Right': (g_snake_x+(20*SQUARE_SIZE), g_snake_y), 
                    'Left': (g_snake_x-(20*SQUARE_SIZE), g_snake_y)}
    valid_move = []

    if g_end: 
        if g_food == []:
            if g_last_food == 0:
                g_snake_end = True
                return
        if ((abs(g_monster_x-g_snake_x) < (20*SQUARE_SIZE)) and (abs(g_monster_y-g_snake_y) < (20*SQUARE_SIZE))):
            g_snake_end = True
            return

    if g_snake_y != ((GAME_DIMENSION//2)-(GAME_MARGIN//2)-10):
        valid_move.append('Up')
    if g_snake_y != -((GAME_DIMENSION//2)+(GAME_MARGIN//2))+10:
        valid_move.append('Down')
    if g_snake_x != (GAME_DIMENSION//2)-10:
        valid_move.append('Right')
    if g_snake_x != -(GAME_DIMENSION//2)+10:
        valid_move.append('Left')

    if g_key == 'space':
        if not g_stop: 
            g_key = g_last_motion
        else: 
            g_motion = 'Paused'
    elif g_key in valid_move:
        g_motion = g_key
        g_last_motion = g_key
        g_snake.goto(motion_dict[g_key])
        body_motion()
        g_snake_x = g_snake.xcor()
        g_snake_y = g_snake.ycor()
        if (g_snake_x, g_snake_y-5) in g_food_dict:
            g_last_food = g_food_dict[(g_snake_x, g_snake_y-5)] + 1
            snake_food_collide()
        if g_food == []:
            g_last_food -= 1

    if g_repeat > 0:
        snake_speed = 400
        g_repeat -= 1
    else: snake_speed = 300
    g_screen.ontimer(snake_motion, snake_speed)

# To move the body of the snake
def body_motion():
    for i in range(len(g_snake_body)-1, 0, -1):
        x = g_snake_body[i-1].xcor()
        y = g_snake_body[i-1].ycor()
        g_snake_body[i].goto(x, y)
    g_snake_body[0].goto(g_snake_x, g_snake_y)

# To move the monster
# snake_monster_collide() function should be defined before calling this function
def monster_motion():
    global g_monster_x, g_monster_y, g_monster_end
    distance_x = abs(g_monster_x-g_snake_x)
    distance_y = abs(g_monster_y-g_snake_y)
    motion_dict = {'Up': (g_monster_x, g_monster_y+(20*SQUARE_SIZE)), 
                    'Down': (g_monster_x, g_monster_y-(20*SQUARE_SIZE)), 
                    'Right': (g_monster_x+(20*SQUARE_SIZE), g_monster_y), 
                    'Left': (g_monster_x-(20*SQUARE_SIZE), g_monster_y)}
    valid_move = []

    if g_end: 
        if g_food == []:
            if g_last_food == 0:
                g_monster_end = True
                return
        if ((abs(g_monster_x-g_snake_x) < (20*SQUARE_SIZE)) and (abs(g_monster_y-g_snake_y) < (20*SQUARE_SIZE))):
            g_monster_end = True
            return

    if g_monster_y+(20*SQUARE_SIZE) <= (GAME_DIMENSION//2)-(GAME_MARGIN//2)-10:
        valid_move.append('Up')
    if g_monster_y-(20*SQUARE_SIZE) >= -((GAME_DIMENSION//2)+(GAME_MARGIN//2))+10:
        valid_move.append('Down')
    if g_monster_x+(20*SQUARE_SIZE) <= (GAME_DIMENSION//2)-10:
        valid_move.append('Right')
    if g_monster_x-(20*SQUARE_SIZE) >= -(GAME_DIMENSION//2)+10:
        valid_move.append('Left')
    
    while True:
        move = random.choice(valid_move)
        if (g_end and (abs(g_monster_x-g_snake_x) < (20*SQUARE_SIZE)) and (abs(g_monster_y-g_snake_y) < (20*SQUARE_SIZE))):
            break
        if (distance_x > abs(motion_dict[move][0]-g_snake_x)) or (distance_y > abs(motion_dict[move][1]-g_snake_y)):
            break
    monster_speed = random.randint(250, 500)
    g_monster.goto(motion_dict[move])
    g_monster_x = g_monster.xcor()
    g_monster_y = g_monster.ycor()
    snake_monster_collide()
    g_screen.ontimer(monster_motion, monster_speed)

# To remove the food if the snake passes through it
# set_snake_body() function should be defined before calling this function
def snake_food_collide():
    global g_food
    for i in g_food:
        if i.pos() == (g_snake_x, g_snake_y-5):
            i.clear()
            g_food.remove(i)
    set_snake_body()

# To add g_contact by 1 if the snake and monster collided
def snake_monster_collide():
    global g_contact
    for body in g_snake_body:
        (x,y) = body.pos()
        if ((abs(g_monster_x-x) < (20*SQUARE_SIZE)) and (abs(g_monster_y-y) < (20*SQUARE_SIZE))):
            g_contact += 1
            break

# To clone the monster and the snake so the monster will stay on the top
def clone():
    global g_monster, g_snake
    old_snake = g_snake
    g_snake = g_snake.clone()
    old_snake.hideturtle()

    old_monster = g_monster
    g_monster = g_monster.clone()
    old_monster.hideturtle()

    g_screen.ontimer(clone, 200)

# To end the game if the player has either win or lose
# end_game_status() function should be defined before calling this function
def end_game():
    global g_end
    if (g_food == []) or ((abs(g_monster_x-g_snake_x) < (20*SQUARE_SIZE)) and (abs(g_monster_y-g_snake_y) < (20*SQUARE_SIZE))):
        g_end = True

    if (g_end and g_snake_end and g_monster_end):
        end_game_status()
        return
    g_screen.ontimer(end_game, 200)

# To display if the player wins or loses the game
def end_game_status():
    end = turtle.Turtle()
    end.penup()
    end.hideturtle()
    end.goto(g_snake_x, g_snake_y)
    if (g_food == [] and g_last_food == 0):
        end.write('Winner', align = 'center', font = STYLE)  

    elif ((abs(g_monster_x-g_snake_x) < (20*SQUARE_SIZE)) and (abs(g_monster_y-g_snake_y) < (20*SQUARE_SIZE))):
        end.write('Game over', align = 'center', font = STYLE)

# To display the screen at the beginning before the game starts
def beginning():
    set_screen()
    set_border()
    set_intro()
    set_snake_body()
    set_snake()
    set_monster()
    set_status()
    g_screen.update()

# To display the screen after the game starts
# p_x: The x coordinate of the position of the mouse click (float)
# p_y: The y coordinate of the position of the mouse click (float)
def on_timer(p_x, p_y):
    g_screen.onscreenclick(None)
    g_intro.clear()
    set_food()
    update_time()
    update_motion()
    snake_motion()
    monster_motion()
    clone()
    end_game()
    while not (g_end and g_snake_end and g_monster_end):
        g_status.clear()
        set_status()
        g_screen.update()

# To play the game
def main():
    beginning()
    g_screen.onscreenclick(on_timer)
    g_screen.mainloop()

if __name__ == "__main__":
	main()
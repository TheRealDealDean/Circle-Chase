import math, timer, button
from pygame import init, font, time, event, key, draw, display, quit
from pygame.event import get
from pygame import K_UP, K_LEFT, K_RIGHT, K_DOWN, K_SPACE, QUIT, KEYDOWN
from sys import exit
init()
font.init()
width = 1200
height = 600
screen = display.set_mode((width, height))

done = False

is_red = True

gameTimer = timer.Timer(100, 550, 100, 50)

restartButton = button.Button('Restart', (178, 34, 34), (255, 0, 0), 550, 275, 100, 50)

timerFont = font.SysFont('timesnewroman', 26, False, False, None)

buttonFont = font.SysFont('timesnewroman', 24, False, False, None)

speed = 3

xp = 1100 #Variable for X coordinate of Player Circle
yp = 300 #Variable for Y coordinate of Player Circle

r = 13

xf = 100
yf = 300

col_right = width - r
col_bott = height - r

color2 = (0, 0, 255)

clock = time.Clock()
def calculate_delta(): 
        dx = xp - xf
        dy = yp - yf
        return (dx, dy)
                #Function to Calculate the DELTA (Change) in position for the Player Circle
def calculate_vector_length(v):
        dx = v[0]
        dy = v[1]
        length = math.sqrt(dx**2 + dy**2)
        return length
                #Function to Calculate the length of the straight line between the Player Circle and the AI Circle (The Hypotenuse)
def normalize_vector(v):
        dx = v[0]
        dy = v[1]
        length = calculate_vector_length(v)
        if length == 0:
                length = 1
        xn = dx/length
        yn = dy/length
        normalized_vector = (xn, yn)
        return normalized_vector
                #Function to Normalize the Vector (straight line between the Player and AI)
def calculate_speed_vector(ndv, speed):
        dx = ndv[0]
        dy = ndv[1]
        svx = dx*speed
        svy = dy*speed
        speed_vector = (svx, svy) 
        return speed_vector
                #Function to Calculate the speed_vector (how fast the position changes and in which direction)
def ai_position_update(sv, ai_p):
        dx = sv[0]
        dy = sv[1]
        current_x = ai_p[0]
        current_y = ai_p[1]
        new_x = math.floor(current_x + dx)
        new_y = math.floor(current_y + dy)
        new_position = (new_x, new_y)
        return new_position
                #Function to update the position of the AI Circle after previous calculations have been made
def detect_circle_collision():
        (dx, dy) = calculate_delta()
        length = calculate_vector_length((dx, dy))
        if length <= (r*2):
                collision = True
        else:
                collision = False
        return collision
                #Function to detect whether or not the AI Circle and Player Circle are colliding with each other

while True:
        for e in event.get():
                        if e.type == QUIT:
                                quit(); exit();
                                done = True
        done = False

        is_red = True

        gameTimer = timer.Timer(100, 550, 100, 50)

        restartButton = button.Button('Restart', (178, 34, 34), (255, 0, 0), 550, 275, 100, 45)

        speed = 3

        xp = 1100 #Variable for X coordinate of Player Circle
        yp = 300 #Variable for Y coordinate of Player Circle

        r = 13

        xf = 100
        yf = 300

        col_right = width - r
        col_bott = height - r

        color2 = (0, 0, 255)
        
        while not done:
                for e in event.get():
                        if e.type == QUIT:
                                quit(); exit();
                                done = True
                        if e.type == KEYDOWN and e.key == K_SPACE:
                                is_red = not is_red

                gameTimer.increaseCount()
                
                pressed = key.get_pressed()
                if pressed[K_UP]: yp -= 5
                if pressed[K_DOWN]: yp += 5
                if pressed[K_LEFT]: xp -= 5
                if pressed[K_RIGHT]: xp += 5

                delta = calculate_delta()
                nv = normalize_vector(delta)
                sv = calculate_speed_vector(nv, speed)
                new_p = ai_position_update(sv, (xf, yf))
                xf = new_p[0]
                yf = new_p[1]
                #print(detect_circle_collision())

                if detect_circle_collision() == True:
                        done = True
                
                if is_red: color2 = (0, 0, 255)
                else: color2 = (255, 0, 0)

                if is_red: color = (255, 0, 0)
                else: color = (0, 0, 255)

                screen.fill((0, 0, 0))
                
                if xp <= r: xp = r
                if yp <= r: yp = r
                if xp >= col_right: xp = col_right
                if yp >= col_bott: yp = col_bott
                        
                draw.circle(screen, color, (xp, yp), r)

                draw.circle(screen, color2, (xf, yf), r)

                timerString = timerFont.render(gameTimer.render(), True, (255, 255, 255))
                screen.blit(timerString, (0, 0))
                
                display.flip()
                clock.tick(60)

        while done:
                for e in event.get():
                        if e.type == QUIT:
                                quit(); exit();

                screen.fill((0, 0, 0))
                
                screen.blit(timerString, (0, 0))
                
                restartButton.mouseButtonOverlap()
                restartButton.renderButton(screen, buttonFont)
                restartButton.buttonClicked()
                
                if restartButton.clicked:
                        done = False
                display.flip()



#Add: Timer/Scorekeeper, "Game Over", Start Over + Message, Obstacles(?)

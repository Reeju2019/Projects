import math
import pygame
from pygame import mixer as mx
import random
import time


# Initialize the pygame
pygame.init()

# Create te screen
display_width = 786
display_height = 512
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Space Invader')
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

#Background
#image
bg = pygame.image.load('space.png')
# Sound
mx.music.load('background.wav')
mx.music.play(-1)

# title and Icon
pygame.display.set_caption("Space Invader")
# icon should be  of 32X32 pixel size
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)

#player
playerimg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 440
pchange = 0

#enemy
enemyimg = []
enemyX = []
enemyY = []
echangeX = []
echangeY = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('alien.png'))
    enemyX.append(random.randint(0, 300))
    enemyY.append(random.randint(0, 300))
    echangeX.append(3)
    echangeY.append(30)

#bullet
bulletimg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 390
bchangeY = 20
bstate = 'ready'

#Score
score = 0
font = pygame.font.Font("comic.ttf", 32)
textX = 10
textY = 10
pause = False

def text_objects(text, font):
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()

def game_over():
    font = pygame.font.Font("comic.ttf", 64)
    tmp = font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(tmp, (200, 250))
    
def show_score(x, y):
    tmp = font.render("Score: " + str(score), True, (255, 128, 0))
    screen.blit(tmp, (x, y))

def player(x, y):
    screen.blit(playerimg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))
    
def bullet(x, y):
    global bstate
    bstate = 'fire'
    screen.blit(bulletimg, (x+24, y+40))

def isCol(x1, y1, x2, y2):
    distance = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))
    if distance <22:
        return True
    return False

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.fill(white)
        # background
        screen.blit(bg, (0, 0))
        largeText = pygame.font.Font("comic.ttf",64)
        TextSurf, TextRect = text_objects("Space Invader", largeText)
        TextRect.center = ((display_width/2),(display_height/2 -150))
        screen.blit(TextSurf, TextRect)
        
        button("PLAY",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)


def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False
    

"""
This function has the parameters of:

msg: What do you want the button to say on it.

x: The x location of the top left coordinate of the button box.

y: The y location of the top left coordinate of the button box.

w: Button width.

h: Button height.

ic: Inactive color (when a mouse is not hovering).

ac: Active color (when a mouse is hovering).
"""
def button(msg,x,y,w,h,ic,ac,action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != 'quitgame':
            game_loop()       
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
        if click[0] == 1 and action == 'quitgame':
            quitgame()

    smallText = pygame.font.SysFont("comic.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def paused():

    largeText = pygame.font.SysFont("comic.ttf",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    screen.blit(TextSurf, TextRect)
    

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)
        

        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)
    
def crash():
    
    global display_hieght, display_width
    largeText = pygame.font.SysFont("comic.ttf",115)
    TextSurf, TextRect = text_objects("Alien Wins", largeText)
    TextRect.center = ((display_width/2),(display_height/2 - 200))
    screen.blit(TextSurf, TextRect)
    

    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)
        

        button("Play Again",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()

# Game Loop
def game_loop():
    global bg, running, screen, pchange, bulletX, playerX, bulletY, playerimg, pause
    global playerY, echangeX, echangeY, bstate, score, textX, textY, enemyimg
    running = True
    #background = GRAY
    while running:
        # rgb(RED, GREEN, BLUE)
        screen.fill((0, 0, 0))
        # background
        screen.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # if keystroke is pressed or not
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pchange = -4
                if event.key == pygame.K_RIGHT:
                    pchange = 4
                if event.key == pygame.K_SPACE:
                    if bstate is 'ready':
                        mx.Sound('laser.wav').play()
                        bulletX = playerX
                        bullet(bulletX, bulletY)
                if event.key == pygame.K_p:
                    pause = True
                    paused()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    pchange = 0

        playerX += pchange

        if playerX <= 0:
            playerX = 0
        elif playerX >= 700:
            playerX = 700

        for i in range(num_of_enemies):
            # Game over
            if enemyY[i] > 350:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                crash()
                break
            enemyX[i] += echangeX[i]
            if enemyX[i] <= 0:
                echangeX[i] = 5
                enemyY[i] += echangeY[i]
            elif enemyX[i] >= 700:
                echangeX[i] = -5
                enemyY[i] += echangeY[i]
            # Collision
            col = isCol(enemyX[i], enemyY[i], bulletX, bulletY)
            if col:
                mx.Sound('explosion.wav').play()
                bulletY = 400
                bstate = 'ready'
                score += 1
                print(score)
                enemyX[i] = random.randint(0, 700)
                enemyY[i] = random.randint(0, 300)
            enemy(enemyX[i], enemyY[i], i)

        # Bullet movement
        if bulletY <= 0:
            bulletY = 400
            bstate = 'ready'
        if bstate is 'fire':
            bullet(bulletX, bulletY)
            bulletY -= bchangeY

        player(playerX, playerY)
        show_score(textX, textY)
        # TO Update the display
        pygame.display.update()


game_intro()
game_loop()


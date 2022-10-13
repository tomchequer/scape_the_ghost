import pygame, random
import pygame.freetype
import time


#constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (136, 8, 8)
VEL = 2
OPPONENT_SPEED = 1

def get_random_start():
    random.seed(int(time.time()))
    opponents_loc = {0: [random.randint(0, 500), random.randint(0, 500)]}
    return opponents_loc


pwidth = 15
pheight = 15
pradius = 15
gradius = 20
gwidth = 20
sradius = 10
swidth = 10

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('fuk man')

run = True

playerX, playerY = SCREEN_WIDTH/2, SCREEN_HEIGHT/2

#creating ghosts
opponents_loc = get_random_start()

scoreball_x, scoreball_y = random.randint(0,500), random.randint(0,500)
score, score_board, level = 0,0 ,1

sysfont = pygame.font.get_default_font()
font = pygame.font.SysFont(None, 48)
img = font.render(f'score: {score_board}', True, RED)
rect = img.get_rect()

while run:

    player = (playerX, playerY)
    screen.fill(BLACK)
    img = font.render(f'score: {score_board} level: {level}', True, RED)
    screen.blit(img, (20, 20))

    pygame.time.delay(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and playerX > 0 + pwidth:
        playerX -= VEL
    if keys[pygame.K_RIGHT] and playerX < 500 -  pwidth:
        playerX += VEL
    if keys[pygame.K_UP] and playerY > 0 + pheight:
        playerY -= VEL
    if keys[pygame.K_DOWN] and playerY < 500 -  pheight:
        playerY += VEL


    difx = abs(scoreball_x) - abs(playerX)
    dify = abs(scoreball_y) - abs(playerY)

    if abs(difx) < 20 and abs(dify) < 20:
        scoreball_x = random.randint(0,500)
        scoreball_y = random.randint(0,500)
        score += 1
        score_board +=1
        
    
    #spawning score coin
    pygame.draw.circle(screen, RED, (scoreball_x,  scoreball_y), radius=sradius, width=swidth)

    #spwaning player
    pygame.draw.circle(screen, WHITE, (playerX, playerY), radius=pradius, width=pwidth)

    #OPPONENT
    pygame.draw.circle(screen, WHITE, (opponents_loc[0]), radius=gradius, width=gwidth)
    
    currdisx = opponents_loc[0][0]-player[0]
    currdisy = opponents_loc[0][1] -player[1]
    if currdisx > 0:
        opponents_loc[0][0] -=OPPONENT_SPEED 
    else:
        opponents_loc[0][0] +=OPPONENT_SPEED
    if currdisy > 0:
        opponents_loc[0][1] -=OPPONENT_SPEED
    else:
        opponents_loc[0][1] +=OPPONENT_SPEED
        
    if abs(currdisx) < 25 and abs(currdisy) < 25: 
        pygame.quit()

    if score >= 5:
        VEL += 0.25
        OPPONENT_SPEED += 0.25
        level +=1
        score = 0
    pygame.display.update()

pygame.quit()
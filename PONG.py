# -TODO-
#   + SOLVED + Prevent paddle top/bottom sides hitting the ball
#   - Better visuals?
#   + SOLVED + Randomized start velocity
#   + SOLVED + Prevent ball from getting stuck in paddle
#   - Slowly increased difficulty with higher score

# Import pygame library and initialize the game engine
import pygame
import random

pygame.init()

# Open new window, caption it "Pong"
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Pong")

# Here's the variable that runs our game loop
doExit = False

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# Variables hold paddle position & color
# These go above game loop
p1x = 20
p1y = 200
p2x = 660
p2y = 200
p1Color = 100
p2Color = 100
p1Speed = 0
p2Speed = 0

# Ball variables
bVxStart = random.randint(0,1)
bVyStart = random.randint(0,1)
bx = 350 # X position
by = 250 # Y position

# Random starting velocity, decides beginning player confirm as well


if bVxStart == 0:
    bVx = 5 # X velocity (horizontal speed)
    p1Confirm = True
    p2Confirm = False

    
if bVxStart == 1:
    bVx = -5 # X velocity (horizontal speed)
    p2Confirm = True
    p1Confirm = False

    
if bVyStart == 0:
    bVy = 5 # X velocity (vertical speed)
    
if bVyStart == 1:
    bVy = -5 # X velocity (vertical speed)


# Score variables
p1Score = 0
p2Score = 0

while not doExit: #GAME LOOP----------------------------------------------------

    # Event queue stuff
    clock.tick(60)

    for event in pygame.event.get(): # Check if user did something
        if event.type == pygame.QUIT: # Check if user clicked close
            doExit = True # Flag that we are done so we exit the game loop
    
    # Game logic will go here-----------------------------------------------------
    
    if p1Confirm == True:
        p1Color = 100
    else:
        p1Color = 255
 
    if p2Confirm == True:
        p2Color = 100
    else:
        p2Color = 255


    # Move paddles, don't let them go off screen
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and p1y > 3:
        p1y-=5
    if keys[pygame.K_s] and p1y < 397:
        p1y+=5
    if keys[pygame.K_i] and p2y > 3:
        p2y-=5
    if keys[pygame.K_k] and p2y < 397:
        p2y+=5

    # Reflect ball off of paddles, change score, check if inside paddle, increase speed by score
    if bx <= p1x + 20 and bx >= p1x and by + 20 > p1y and by < p1y + 100 and p2Confirm == True:
        bVx *= -1
        if p2Confirm == True:
            p1Score += 1
            p2Confirm = False
            p1Confirm = True
        if bx < p1x + 18:
            bx = p1x + 20
            bVx = 5

    if bx >= p2x - 20 and bx <= p2x and by + 20 > p2y and by < p2y + 100 and p1Confirm == True:
        bVx *= -1
        if p1Confirm == True:
            p2Score += 1
            p1Confirm = False
            p2Confirm = True
        if bx > p2x - 18:
            bx = p2x - 20
            bVx = -5

    # Ball movement
    bx += bVx
    by += bVy

    # Reflect ball of sides of screen, set score to 0 for 1 player, allow other player to recieve points for their next hit
    if bx < 0:
        bVx *= -1
        p1Score = 0
        p1Confirm = True
        p2Confirm = False
    if bx + 20 > 700:
        bVx *= -1
        p2Score = 0
        p2Confirm = True
        p1Confirm = False
    if by < 0 or by + 20 > 500:
        bVy *= -1
    if bx < -5 or by < -5:
        bx = p1x+20
        by = p1y+40
        bVx = 5
    if bx > 685 or by > 530:
        bx = p2x
        by = p2y+40
        bVx = -5
        
    # Render section will go here ------------------------------------------------
    screen.fill((0,0,0)) # Wipe screen black

    # Draw a rectangle
    pygame.draw.rect(screen, (p1Color,p1Color,p1Color), (p1x, p1y, 20, 100), 1)
    pygame.draw.rect(screen, (p2Color,p2Color,p2Color), (p2x, p2y, 20, 100), 1)

    # Draw a ball
    pygame.draw.ellipse(screen, (255,255,255), (bx, by, 20, 20), 1)

    # Draw line down the middle
    pygame.draw.line(screen, (255, 255, 255), [349, 0], [349, 500], 5)

    # Display Scores
    font = pygame.font.Font(None, 74) # Use default font
    text = font.render(str(p1Score), 1, (255, 255, 255))
    screen.blit(text, (250,10))
    text = font.render(str(p2Score), 1, (255, 255, 255))
    screen.blit(text, (420,10))
    
    # Show Controls
    font = pygame.font.Font(None, 20) # Use default font
    text = font.render(str("Player 1 Controls: W / S"), 1, (100, 100, 100))
    screen.blit(text, (8,480))
    text = font.render(str("Player 2 Controls: I / K"), 1, (100, 100, 100))
    screen.blit(text, (550,480))

    # Update the screen
    pygame.display.flip()


# END GAME LOOP ----------------------------------------------------------------

pygame.quit() # When game is done close down pygame
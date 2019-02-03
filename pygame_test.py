#thanks "Tech With Tim" on YouTube
#ON EPISODE 3
import pygame
#initialize pygame:
pygame.init()
#make a window:
win = pygame.display.set_mode((500, 500))
#change title:
pygame.display.set_caption("First Game")
#make a rectangle:
x = 50
y = 50
width = 40
height = 60
#velocity:
vel = 5
run = True
isJump = False
jumpCount = 10
while run:
    #timer:
    pygame.time.delay(100)
    #sense events:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #gets what key is pressed:
    keys = pygame.key.get_pressed()
    if keys [pygame.K_LEFT]:
        if x > 0:
            x = x - vel
    if keys [pygame.K_RIGHT]:
        if x < 460:
            x = x + vel
    if keys [pygame.K_UP]:
        if y > 0:
            y-=vel
    if not(isJump):
        if keys [pygame.K_DOWN]:
            if y < 440:
                y+=vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        #JUMPING:
        if jumpCount >= -10:
            #** is power
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) / 2 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    #changes background color:
    win.fill((0, 0, 0))
    #draws a rectangle- can be more shapes
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    #must refresh display:
    pygame.display.update()
#allows you to quit:
pygame.quit()

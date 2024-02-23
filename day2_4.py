import pygame
pygame.init()
window= pygame.display.set_mode((500,500))
pygame.display.set_caption("game1")
x = 250
y = 250
width = 50
height = 50
velocity = 20
jump = False
JUMP_COUNT_MAX = 10
jumpcount = JUMP_COUNT_MAX         
run = True
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        print("left")
        x -= velocity
    elif keys[pygame.K_RIGHT]:
        print("right")
        x += velocity
    elif keys[pygame.K_UP]:
        print("up")
        y -= velocity
    elif keys[pygame.K_DOWN]:
        print("down")
        y += velocity
    elif keys[pygame.K_SPACE]:
        jump = True
    elif keys[pygame.K_SPACE]:
        jump = True

    if jump:
        if jumpcount >= -JUMP_COUNT_MAX:
            if jumpcount < 0:
                sign = -1
            else:
                sign = 1
            y -= sign * jumpcount**2
            jumpcount -=1
        else:
            jump = False
            jumpcount =JUMP_COUNT_MAX
            
    print(x,y)
    window.fill("black")
    pygame.draw.rect(window,(238,189,34),(x,y,width,height))
    pygame.display.update()
pygame.quit()    

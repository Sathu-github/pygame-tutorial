import pygame
pygame.init()
window= pygame.display.set_mode((500,500))
pygame.display.set_caption("game1")
x = 250
y = 250
width = 50
height = 50
velocity = 20
run = True

while run :
    pygame.time.delay(100)
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
    print(x,y)
    window.fill("black")
    pygame.draw.rect(window,(255,0,0),(x,y,width,height))
    pygame.display.update()
pygame.quit()        

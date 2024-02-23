import pygame
pygame.init()
window= pygame.display.set_mode((500,500))
pygame.display.set_caption("game1")
x = 250
y = 250
width = 50
height = 50
vel = 20
run = True
left, right, up, down = False, False, False, False
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                up = True
                left, right, down = False, False, False
            if event.key == pygame.K_s:
                down = True
                left, right, up = False, False, False
            if event.key == pygame.K_a:
                left = True
                up, right, down = False, False, False
            if event.key == pygame.K_d:
                right = True
                left, up, down = False, False, False
    if left:
        x -= vel
    if right:
        x += vel
    if up:
        y -= vel
    if down:
        y += vel

    if x > 500:
        x = 0
    elif x < 0:
        x = 500
    elif y < 0:
        y = 500
    elif y > 500:
        y = 0

    print(x,y)
    window.fill("black")
    pygame.draw.rect(window,(255,0,0),(x,y,width,height))
    pygame.display.update()
pygame.quit()       

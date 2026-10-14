import pygame
import random

pygame.init()

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Hardkorowa gra o kwadracie")
clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 24)

score = 0

enemy_speed = 1

player = pygame.Rect(50,50, 50,50)

x = random.randint(0, 400)
y = random.randint(0, 400)

apple = pygame.Rect(x,y, 20,20)

enemy = pygame.Rect(200,200, 50,50)

speed = 5

running = True
while running:
    clock.tick(60) / 1000
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if score > 5:
        enemy_speed += 0.001
        speed += 0.0001
    if score > 10:
        enemy_speed += 0.001
        speed += 0.0001
    if score > 20:
        enemy_speed += 0.001     
        speed += 0.0001

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y += speed


    player.clamp_ip(window.get_rect())       

    if enemy.x < player.x:
        enemy.x += enemy_speed
    if enemy.x > player.x:
        enemy.x -= enemy_speed
    if enemy.y < player.y:
        enemy.y += enemy_speed
    if enemy.y > player.y:
        enemy.y -= enemy_speed

    if apple.colliderect(player):
        apple.x = random.randint(0,400)
        apple.y = random.randint(0,400)
        score += 1
        print(f"Punkty: {score}")

    if enemy.colliderect(player):
        print("Koniec gry")
        exit()    

    window.fill((30, 30, 60))
    pygame.draw.rect(window, (255,255,255), player)
    pygame.draw.rect(window, (255,0,255), apple)
    pygame.draw.rect(window, (255,0,0), enemy)
    text = font.render(f"Punkty: {score}", True, (255, 255, 255))
    window.blit(text,(10,10))
    pygame.display.flip()
    
pygame.quit()
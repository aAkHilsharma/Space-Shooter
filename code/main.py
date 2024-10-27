import pygame
from os.path import join
from random import randint
# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('SpaceShip')

running = True

# surface
surf = pygame.Surface((100, 200))
surf.fill('orange')
x = 100

# importing an image
player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))

meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH/2,WINDOW_HEIGHT/2))

laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20,WINDOW_HEIGHT - 20))

star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_positons = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]

player_speed = 0.4
player_direction = -1

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # draw the game
    # fill the window with red color
    display_surface.fill('darkgrey')
    for pos in star_positons:
        display_surface.blit(star_surf, pos)
    
    if player_rect.right > WINDOW_WIDTH - 10 or player_rect.left < 10:
        player_direction *= -1
    
    player_rect.right += player_direction * player_speed
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(player_surf, player_rect)
    display_surface.blit(laser_surf, laser_rect)

    pygame.display.update()

pygame.quit()

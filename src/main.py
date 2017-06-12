import os
from sys import exit

import pygame
from pygame.locals import *

import settings
from object.factory import GameObjectFactory
from view.main_view import MainView


# Initial Game
pygame.init()
pygame.display.set_caption('StarCraft')

shoot_frequency = 0
player_down_index = 16
clock = pygame.time.Clock()

main_view = MainView(settings)
sprite_family = GameObjectFactory(settings)
player = sprite_family.create_player()
bullet1_img = sprite_family.bullet1_img

# Start Game
running = True
while running:
    # Set max fps is 60
    clock.tick(60)

    # Draw the background
    main_view.screen.fill(0)
    main_view.screen.blit(main_view.background, (0, 0))

    # Draw the assortment of game object
    ### Draw player
    if not player.is_hit:
        main_view.screen.blit(player.image[player.img_index], player.rect)
        # make dynamic effect by changing img_index
        player.img_index = shoot_frequency // 8
    else:
        player.img_index = player_down_index // 8
        main_view.screen.blit(player.image[player.img_index], player.rect)
        player_down_index += 1
        if player_down_index > 47:
            running = False

    ### Draw bullet which shoot by player
    if not player.is_hit:
        if shoot_frequency % 15 == 0:
            #bullet_sound.play()
            player.shoot(bullet1_img)

        shoot_frequency += 1
        if shoot_frequency >= 15:
            shoot_frequency = 0

    # Move bullet
    for bullet in player.bullets:
        bullet.move()
        if bullet.rect.bottom < 0:
            player.bullets.remove(bullet)

    # Show on the screen
    player.bullets.draw(main_view.screen)


    # Update display
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # keyboard listener
    key_pressed = pygame.key.get_pressed()
    if not player.is_hit:
        if key_pressed[K_w] or key_pressed[K_UP]:
            player.moveUp()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            player.moveDown()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            player.moveLeft()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            player.moveRight()

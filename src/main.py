import os
import random
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
enemy_frequency = 0
score = 0
player_down_index = 16
clock = pygame.time.Clock()

main_view = MainView(settings)
sprite_family = GameObjectFactory(settings)
player = sprite_family.create_player()
enemy = sprite_family.create_enemy()
enemies1 = pygame.sprite.Group()
enemies_down = pygame.sprite.Group()

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
        player.draw(main_view, player.img_index)
        # make dynamic effect by changing img_index
        player.img_index = shoot_frequency // 8
    else:
        player.img_index = player_down_index // 8
        player.draw(main_view, player.img_index)
        player_down_index += 1
        if player_down_index > 47:
            running = False

    ### Draw bullet which shoot by player
    #### Create bullet
    if not player.is_hit:
        if shoot_frequency % 15 == 0:
            #bullet_sound.play()
            player.shoot()

        shoot_frequency += 1
        if shoot_frequency >= 15:
            shoot_frequency = 0

    #### Move bullet
    for bullet in player.bullets:
        bullet.move()
        if bullet.rect.bottom < 0:
            player.bullets.remove(bullet)

    #### Show on the screen
    player.bullets.draw(main_view.screen)

    ### Draw enemy
    #### Create enemy
    if enemy_frequency % 50 == 0:
        enemy1_pos = [random.randint(0, settings.SCREEN_WIDTH - enemy.rect.width), 0]
        enemy1 = sprite_family.create_enemy(enemy1_pos)
        enemies1.add(enemy1)
    enemy_frequency += 1
    if enemy_frequency >= 100:
        enemy_frequency = 0

    #### Move enemy
    for enemy in enemies1:
        enemy.move()
        # Judge if player is_hit
        if pygame.sprite.collide_circle(enemy, player):
            enemies_down.add(enemy)
            enemies1.remove(enemy)
            player.is_hit = True
            #game_over_sound.play()
            break
        if enemy.rect.top > settings.SCREEN_HEIGHT:
            enemies1.remove(enemy)

    #### Add enemy_donw into Group to render animation
    enemies1_down = pygame.sprite.groupcollide(enemies1, player.bullets, 1, 1)
    for enemy_down in enemies1_down:
        enemies_down.add(enemy_down)

    #### Show on the screen
    ##### Draw enemy
    enemies1.draw(main_view.screen)

    ##### Draw enemy down
    for enemy_down in enemies_down:
        if enemy_down.down_index == 0:
            #enemy1_down_sound.play()
            pass
        if enemy_down.down_index > 7:
            enemies_down.remove(enemy_down)
            score += 1000
            continue
        enemy_down.draw(main_view, enemy_down.down_index // 2)
        enemy_down.down_index += 1


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

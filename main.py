# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-07-22 22:09:30
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-04 20:40:13

import pygame
import random

import my_source.__myglobal as myglobal
import my_source.__player as player
import my_source.__enemy as enemy
import my_source.__explosion as explosion
import my_source.__powerup as powerup
import my_source.__ui as ui

##### Collision #####
### Collision of Player and Enemies ###
def collide_player(player, enemies, explosions, powerups):
    if not (player.status["death_flag"] or player.status["reborn_flag"]):
        hits = pygame.sprite.spritecollide(player, enemies, True, pygame.sprite.collide_rect_ratio(0.8))
        for hit in hits:
            player.property["health_point"] -= hit.property["damage_point"]
            myglobal.score += hit.property["score"] / 2
            hit.collide_animation(hit.rect.center, explosions, powerups)
            if player.property["health_point"] <= 0:
                player.property["health_point"] = 0
                player.collide_animation(hit.rect.center, explosions)

### Collision of Player and Power_ups ###
def collide_powerup(player, powerups):
    hits = pygame.sprite.spritecollide(player, powerups, True, pygame.sprite.collide_rect_ratio(1.2))
    for hit in hits:
        hit.power_up(player)

### Collision of Bombs and Enemies ###
def collide_bomb(bombs, enemies, explosions, powerups):
    hits = pygame.sprite.groupcollide(enemies, bombs, True, False, pygame.sprite.collide_circle)
    for hit in hits:
        hit.collide_animation(hit.rect.center, explosions, powerups)
        myglobal.score += hit.property["score"] / 2

### Collision of Bullets and Enemies ###
def collide_shot(bullets, enemies, explosions, powerups):
    hits = pygame.sprite.groupcollide(enemies, bullets, False, True, pygame.sprite.collide_rect_ratio(1.2))
    for hit in hits:
        bullet_explosion  = explosion.Explosion(hit.rect.center, myglobal.IMAGE["BULLET_EXPLOSION"])
        explosions.add(bullet_explosion)
        hit.property["health_point"] -= 50
        if hit.property["health_point"] <= 0:
            myglobal.score += hit.property["score"]
            hit.collide_animation(hit.rect.center, explosions, powerups)

##### Add Enemies #####
def add_enemy(blocks, planes):
    now = pygame.time.get_ticks()
    if (now - myglobal.last_time) > myglobal.enemy_time:
        if len(blocks) < 10:
            enemy_block = enemy.Block(random.randint(1,4))
            blocks.add(enemy_block)
        if len(planes) < 5:
            enemy_plane = enemy.Plane(random.randint(1,3), random.randint(1,3))
            planes.add(enemy_plane)
        if myglobal.enemy_time > 300:
            myglobal.enemy_time -= 50
        myglobal.last_time = now

if __name__ == '__main__':
    ##### Game Initial #####
    ### Setting Initial ###
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    pygame.init()
    screen = pygame.display.set_mode(myglobal.SIZE["SCREEN"])
    pygame.display.set_caption("Shooting_Stars")
    clock = pygame.time.Clock()

    ### Classes Initial ###
    my_ui = ui.UiStart()
    my_bullets = pygame.sprite.Group()
    my_bombs = pygame.sprite.Group()
    my_powerups = pygame.sprite.Group()
    my_explosions = pygame.sprite.Group()
    enemy_bullets = pygame.sprite.Group()
    enemy_blocks = pygame.sprite.Group()
    enemy_planes = pygame.sprite.Group()

    ### Set Mode ####
    if myglobal.joystick_flag:
        try:
            pygame.joystick.init()
            my_joystick = pygame.joystick.Joystick(0)
            my_joystick.init()
        except:
            myglobal.joystick_flag = False

    ##### Main #####
    ### Main Initial ###
    game_flag = True

    ### Main Loop ###
    while game_flag:
        clock.tick(myglobal.FPS)

        ##### Start #####
        if myglobal.scene_flag == 1:
            ### Start Initial ###
            if myglobal.scene_flag != myglobal.last_scene_flag:
                my_ui = ui.UiStart()

            ### Set Status ###
            myglobal.last_scene_flag = myglobal.scene_flag

            ### Get Input ###
            # Get List
            event_list = pygame.event.get()
            for event in event_list:
            # Quit
                if event.type == pygame.QUIT:
                    game_flag = False
            # Keyboard DOWN
                if not myglobal.joystick_flag:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game_flag = False
                        if event.key == pygame.K_SPACE:
                            myglobal.scene_flag = 2
            # Joystick DOWN
                else:
                    if event.type == pygame.JOYBUTTONDOWN:
                        if my_joystick.get_button(6):
                            game_flag = False
                        if my_joystick.get_button(0):
                            myglobal.scene_flag = 2

            ### Render ###
            my_ui.render(screen)
            pygame.display.flip()

        ##### Game #####
        elif myglobal.scene_flag == 2:
            ### Game Initial ###
            if myglobal.scene_flag != myglobal.last_scene_flag:
                my_player = player.Player(3, random.randint(1,4))
                my_ui = ui.UiGame(my_player)
                for i in range(7):
                    enemy_block = enemy.Block(random.randint(1,4))
                    enemy_blocks.add(enemy_block)
                for i in range(3):
                    enemy_plane = enemy.Plane(random.randint(1,3), random.randint(1,3))
                    enemy_planes.add(enemy_plane)

            ### Set Status ###
            myglobal.last_scene_flag = myglobal.scene_flag

            ### Get Input ###
            # Get List
            event_list = pygame.event.get()
            for event in event_list:
            # Quit
                if event.type == pygame.QUIT:
                    game_flag = False
            # Keyboard DOWN
                if not myglobal.joystick_flag:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game_flag = False
                        if event.key == (pygame.K_LCTRL or pygame.K_RCTRL):
                            my_player.bomb(my_bombs)
            # Joystick DOWN
                else:
                    if event.type == pygame.JOYBUTTONDOWN:
                        if my_joystick.get_button(6):
                            game_flag = False
                        if my_joystick.get_button(1):
                            my_player.bomb(my_bombs)
            # Keyboard Control
            if not myglobal.joystick_flag:
                key_state = pygame.key.get_pressed()
                if key_state[pygame.K_UP]:
                    my_player.status["move_y"] = -1.0
                if key_state[pygame.K_DOWN]:
                    my_player.status["move_y"] = 1.0
                if not (key_state[pygame.K_UP] or key_state[pygame.K_DOWN]):
                    my_player.status["move_y"] = 0.0
                if key_state[pygame.K_LEFT]:
                    my_player.status["move_x"] = -1.0
                if key_state[pygame.K_RIGHT]:
                    my_player.status["move_x"] = 1.0
                if not (key_state[pygame.K_LEFT] or key_state[pygame.K_RIGHT]):
                    my_player.status["move_x"] = 0.0
                if key_state[pygame.K_SPACE]:
                    my_player.status["shot_flag"] = True
                else:
                    my_player.status["shot_flag"] = False
            # Joystick Control
            else:
                if abs(my_joystick.get_axis(0)) > 0.3:
                    my_player.status["move_x"] = my_joystick.get_axis(0)
                else:
                    my_player.status["move_x"] = 0
                if abs(my_joystick.get_axis(1)) > 0.3:
                    my_player.status["move_y"] = my_joystick.get_axis(1)
                else:
                    my_player.status["move_y"] = 0
                my_player.status["shot_flag"] = my_joystick.get_button(0)

            ### Update Game ###
            # Add Enemy
            add_enemy(enemy_blocks, enemy_planes)
            # Collision Detection and Response
            collide_player(my_player, enemy_blocks, my_explosions, my_powerups)
            collide_player(my_player, enemy_planes, my_explosions, my_powerups)
            collide_player(my_player, enemy_bullets, my_explosions, my_powerups)
            collide_bomb(my_bombs, enemy_blocks, my_explosions, my_powerups)
            collide_bomb(my_bombs, enemy_planes, my_explosions, my_powerups)
            collide_bomb(my_bombs, enemy_bullets, my_explosions, my_powerups)
            collide_shot(my_bullets, enemy_blocks, my_explosions, my_powerups)
            collide_shot(my_bullets, enemy_planes, my_explosions, my_powerups)
            collide_powerup(my_player, my_powerups)
            # Update All
            my_player.update(my_bullets, my_bombs)
            my_bullets.update()
            my_bombs.update()
            enemy_blocks.update()
            enemy_planes.update(enemy_bullets)
            enemy_bullets.update()
            my_explosions.update()
            my_powerups.update()
            my_ui.update(my_player)

            ### Render ###
            my_ui.render_background(screen)
            enemy_blocks.draw(screen)
            enemy_planes.draw(screen)
            my_bombs.draw(screen)
            my_player.render(screen)
            my_explosions.draw(screen)
            my_bullets.draw(screen)
            enemy_bullets.draw(screen)
            my_powerups.draw(screen)
            my_ui.render(screen)
            pygame.display.flip()

        ##### Over #####
        else:
            ### Over Initial ###
            if myglobal.scene_flag != myglobal.last_scene_flag:
                my_player.kill()
                my_ui = ui.UiOver()
                my_bullets.empty()
                my_bombs.empty()
                my_powerups.empty()
                my_explosions.empty()
                enemy_bullets.empty()
                enemy_blocks.empty()
                enemy_planes.empty()
                myglobal.score = 0

            ### Set Status ###
            myglobal.last_scene_flag = myglobal.scene_flag

            ### Get Input ###
            # Get List
            event_list = pygame.event.get()
            for event in event_list:
            # Quit
                if event.type == pygame.QUIT:
                    game_flag = False
            # Keyboard DOWN
                if not myglobal.joystick_flag:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game_flag = False
                        if event.key == pygame.K_SPACE:
                            myglobal.scene_flag = 1
            # Joystick DOWN
                else:
                    if event.type == pygame.JOYBUTTONDOWN:
                        if my_joystick.get_button(6):
                            game_flag = False
                        if my_joystick.get_button(0):
                            myglobal.scene_flag = 1

            ### Render ###
            my_ui.render(screen)
            pygame.display.flip()
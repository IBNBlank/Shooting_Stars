# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-07-22 19:02:52
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-07-28 22:18:59

import pygame
import random

import my_source._myglobal as myglobal
import my_source._bullet as bullet
import my_source._explosion as explosion

##### Property Define ######
### Player One ###
PLAYER_ONE_PROPERTY = {
    "HEALTH_POINT": 200,
    "MOVE_SPEED": 10,
    "ATTACK_SPEED": 200,
    "BOMB_NUMBER": 3
}
### Player Two ###
PLAYER_TWO_PROPERTY = {
    "HEALTH_POINT": 100,
    "MOVE_SPEED": 20,
    "ATTACK_SPEED": 200,
    "BOMB_NUMBER": 3
}
### Player Three ###
PLAYER_THREE_PROPERTY = {
    "HEALTH_POINT": 100,
    "MOVE_SPEED": 10,
    "ATTACK_SPEED": 100,
    "BOMB_NUMBER": 3
}
### Player Four ###
PLAYER_FOUR_PROPERTY = {
    "HEALTH_POINT": 200,
    "MOVE_SPEED": 20,
    "ATTACK_SPEED": 100,
    "BOMB_NUMBER": 1
}

##### Player Class ######
class Player(pygame.sprite.Sprite):
    def __init__(self, life=3, kind=random.randint(1,4)):
        pygame.sprite.Sprite.__init__(self)
        ##### Choose Kind #####
        if kind == 1:
            ### Property ###
            self.property = {
                "full_hp": PLAYER_ONE_PROPERTY["HEALTH_POINT"],
                "health_point": PLAYER_ONE_PROPERTY["HEALTH_POINT"],
                "move_speed": PLAYER_ONE_PROPERTY["MOVE_SPEED"],
                "attack_speed": PLAYER_ONE_PROPERTY["ATTACK_SPEED"],
                "bomb_number": PLAYER_ONE_PROPERTY["BOMB_NUMBER"],
                "life_number": life,
                "score": 0
            }
            ### Image ###
            self.IMAGE = {
                "ORIGIN": pygame.transform.scale(
                    myglobal.IMAGE["PLAYER_ONE"]["ORIGIN"].convert(),
                    myglobal.SIZE["PLAYER_ONE"]),
                "BLANK": pygame.transform.scale(
                    myglobal.IMAGE["PLAYER_ONE"]["BLANK"].convert(),
                    myglobal.SIZE["PLAYER_ONE"]),
                "LIFE": pygame.transform.scale(
                    myglobal.IMAGE["PLAYER_ONE"]["ORIGIN"].convert(),
                    myglobal.SIZE["PLAYER_ONE_LIFE"])
            }
        elif kind == 2:
            ### Property ###
            self.property = {
                "full_hp": PLAYER_TWO_PROPERTY["HEALTH_POINT"],
                "health_point": PLAYER_TWO_PROPERTY["HEALTH_POINT"],
                "move_speed": PLAYER_TWO_PROPERTY["MOVE_SPEED"],
                "attack_speed": PLAYER_TWO_PROPERTY["ATTACK_SPEED"],
                "bomb_number": PLAYER_TWO_PROPERTY["BOMB_NUMBER"],
                "life_number": life,
                "score": 0
            }
            ### Image ###
            self.IMAGE = {
                "ORIGIN": pygame.transform.scale(
                    myglobal.IMAGE["PLAYER_TWO"]["ORIGIN"].convert(),
                    myglobal.SIZE["PLAYER_TWO"]),
                "BLANK": pygame.transform.scale(
                    myglobal.IMAGE["PLAYER_TWO"]["BLANK"].convert(),
                    myglobal.SIZE["PLAYER_TWO"]),
                "LIFE": pygame.transform.scale(
                    myglobal.IMAGE["PLAYER_TWO"]["ORIGIN"].convert(),
                    myglobal.SIZE["PLAYER_TWO_LIFE"])
            }
        elif kind == 3:
            ### Property ###
            self.property = {
                "full_hp": PLAYER_THREE_PROPERTY["HEALTH_POINT"],
                "health_point": PLAYER_THREE_PROPERTY["HEALTH_POINT"],
                "move_speed": PLAYER_THREE_PROPERTY["MOVE_SPEED"],
                "attack_speed": PLAYER_THREE_PROPERTY["ATTACK_SPEED"],
                "bomb_number": PLAYER_THREE_PROPERTY["BOMB_NUMBER"],
                "life_number": life,
                "score": 0
            }
            ### Image ###
            self.IMAGE = {
                "ORIGIN": pygame.transform.scale(
                    myglobal.IMAGE["PLAYER_THREE"]["ORIGIN"].convert(),
                    myglobal.SIZE["PLAYER_THREE"]),
                "BLANK": pygame.transform.scale(
                    myglobal.IMAGE["PLAYER_THREE"]["BLANK"].convert(),
                    myglobal.SIZE["PLAYER_THREE"]),
                "LIFE": pygame.transform.scale(
                    myglobal.IMAGE["PLAYER_THREE"]["ORIGIN"].convert(),
                    myglobal.SIZE["PLAYER_THREE_LIFE"])
            }
        else:
            ### Property ###
            self.property = {
                "full_hp": PLAYER_FOUR_PROPERTY["HEALTH_POINT"],
                "health_point": PLAYER_FOUR_PROPERTY["HEALTH_POINT"],
                "move_speed": PLAYER_FOUR_PROPERTY["MOVE_SPEED"],
                "attack_speed": PLAYER_FOUR_PROPERTY["ATTACK_SPEED"],
                "bomb_number": PLAYER_FOUR_PROPERTY["BOMB_NUMBER"],
                "life_number": life,
                "score": 0
            }
            ### Image ###
            self.IMAGE = {
                "ORIGIN": pygame.transform.scale(
                    myglobal.IMAGE["PLAYER_FOUR"]["ORIGIN"].convert(),
                    myglobal.SIZE["PLAYER_FOUR"]),
                "BLANK": pygame.transform.scale(
                    myglobal.IMAGE["PLAYER_FOUR"]["BLANK"].convert(),
                    myglobal.SIZE["PLAYER_FOUR"]),
                "LIFE": pygame.transform.scale(
                    myglobal.IMAGE["PLAYER_FOUR"]["ORIGIN"].convert(),
                    myglobal.SIZE["PLAYER_FOUR_LIFE"])
            }

        ##### Status #####
        self.status = {
            "shot_flag": False,
            "death_flag": False,
            "reborn_flag": False,
            "move_x": 0,
            "move_y": 0,
            "death_time": 0,
            "reborn_time": 0,
            "last_shot_time": 0,
            "last_blink_time": 0,
            "blink_image": 0
        }

        ##### Initial #####
        self.image = self.IMAGE["ORIGIN"]
        self.image.set_colorkey(myglobal.COLOR["BLACK"])
        self.status["blink_image"] = self.IMAGE["BLANK"]
        self.status["blink_image"].set_colorkey(myglobal.COLOR["BLACK"])
        self.rect = self.image.get_rect()
        self.rect.centerx = myglobal.SIZE["SCREEN"][0] / 2
        self.rect.bottom = myglobal.SIZE["SCREEN"][1] - 50

    ##### Shot Bomb #####
    def bomb(self, bombs):
        if not self.status["death_flag"]:
            if self.property["bomb_number"] > 0:
                my_bomb_1 = bullet.MyBomb(self.rect.centerx - 200)
                my_bomb_2 = bullet.MyBomb(self.rect.centerx)
                my_bomb_3 = bullet.MyBomb(self.rect.centerx + 200)
                bombs.add(my_bomb_1)
                bombs.add(my_bomb_2)
                bombs.add(my_bomb_3)
                self.property["bomb_number"] -= 1

    ##### Shot Bullet #####
    def shot(self, bullets):
        my_bullet = bullet.MyBullet((self.rect.centerx, self.rect.top))
        bullets.add(my_bullet)

    ##### Collision Response #####
    def collide_animation(self, center, explosions):
        my_explosion = explosion.Explosion(center, myglobal.IMAGE["MY_EXPLOSION"])
        explosions.add(my_explosion)
        self.rect.center = (-400, -400)
        self.property["health_point"] = self.property["full_hp"]
        self.property["life_number"] -= 1
        if self.property["life_number"] <= 0:
            myglobal.scene_flag = 3
        else:
            self.status["death_flag"] = True
            self.status["death_time"] = pygame.time.get_ticks()

    ##### Update #####
    def update(self, bullets, bombs):
        ### Over Detection ###
        if myglobal.scene_flag == 2:
            ### Death Detection ###
            if self.status["death_flag"]:
                ### Death ###
                now = pygame.time.get_ticks()
                if (now - self.status["death_time"]) > 600:
                    self.status["death_flag"] = False
                    self.status["reborn_flag"] = True
                    self.rect.centerx = myglobal.SIZE["SCREEN"][0] / 2
                    self.rect.bottom = myglobal.SIZE["SCREEN"][1] - 50
                    my_bomb = bullet.MyBomb(self.rect.centerx)
                    bombs.add(my_bomb)
                    self.status["reborn_time"] = now
                    self.status["last_blink_time"] = now
            else:
                ### Move ###
                if myglobal.joystick_flag:
                    self.rect.x += self.property["move_speed"] * self.status["move_x"]
                    self.rect.y += self.property["move_speed"] * self.status["move_y"]
                else:
                    if self.status["move_x"] != 0 or self.status["move_y"] != 0:
                        direction = (self.status["move_x"]**2 + self.status["move_y"]**2) ** 0.5
                        self.rect.x += self.property["move_speed"] * self.status["move_x"] / direction
                        self.rect.y += self.property["move_speed"] * self.status["move_y"] / direction
                if self.rect.left <= 0:
                    self.rect.left = 0
                if self.rect.right >= myglobal.SIZE["SCREEN"][0]:
                    self.rect.right = myglobal.SIZE["SCREEN"][0]
                if self.rect.top <= 30:
                    self.rect.top = 30
                if self.rect.bottom >= myglobal.SIZE["SCREEN"][1]:
                    self.rect.bottom = myglobal.SIZE["SCREEN"][1]

                ### Shot ###
                if self.status["shot_flag"]:
                    now = pygame.time.get_ticks()
                    if (now - self.status["last_shot_time"]) > self.property["attack_speed"]:
                        self.shot(bullets)
                        self.status["last_shot_time"] = now

                ### Reborn ###
                if self.status["reborn_flag"]:
                    now = pygame.time.get_ticks()
                    if (now - self.status["reborn_time"]) > 2000:
                        self.status["reborn_flag"] = False
                        self.image = self.IMAGE["ORIGIN"]
                        self.image.set_colorkey(myglobal.COLOR["BLACK"])
                        old_center = self.rect.center
                        self.rect = self.image.get_rect()
                        self.rect.center = old_center
                    else:
                        if (now - self.status["last_blink_time"]) > 100:
                            temp = self.image.copy()
                            self.image = self.status["blink_image"]
                            self.status["blink_image"] = temp
                            old_center = self.rect.center
                            self.rect = self.image.get_rect()
                            self.rect.center = old_center
                            self.status["last_blink_time"] = now

    ##### Render #####
    def render(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
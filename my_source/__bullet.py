# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-07-22 22:12:24
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-04 20:41:51

import pygame
import random

import my_source.__myglobal as myglobal
import my_source.__explosion as explosion

##### Bullet Class ######
### My Bullet ###
class MyBullet(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        ### Property ###
        self.property = {
            "move_speed": 30,
            "damage_point": 50
        }

        ### Image ###
        self.IMAGE = {
            "ORIGIN": pygame.transform.scale(
                myglobal.IMAGE["BULLET"]["MY_BULLET"]["BULLET"].convert(),
                myglobal.SIZE["MY_BULLET"]),
            "SHOT_LIGHT": pygame.transform.scale(
                myglobal.IMAGE["BULLET"]["MY_BULLET"]["SHOT_LIGHT"].convert(),
                myglobal.SIZE["MY_SHOT_LIGHT"])
        }

        ### Music ###
        self.MUSIC = {
            "SOUND": pygame.mixer.Sound(myglobal.MUSIC["MY_SHOT"])
        }

        ### Status ###
        self.status = {
            "move_x": random.uniform(-2, 2),
            "move_y": self.property["move_speed"],
            "start_time": 0
        }

        ##### Initial #####
        self.image = self.IMAGE["SHOT_LIGHT"]
        self.image.set_colorkey(myglobal.COLOR["BLACK"])
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.MUSIC["SOUND"].set_volume(0.1)
        self.MUSIC["SOUND"].play()
        self.status["start_time"] = pygame.time.get_ticks()

    ##### Collision Response #####
    def collide_animation(self, center, explosions):
        bullet_explosion = explosion.Explosion(center, myglobal.IMAGE["BULLET_EXPLOSION"])
        explosions.add(bullet_explosion)

    ##### Update #####
    def update(self):
        ### Move ###
        self.rect.x += self.status["move_x"]
        self.rect.y -= self.status["move_y"]
        if (self.rect.left >= myglobal.SIZE["SCREEN"][0] or
            self.rect.right <= 0 or self.rect.bottom <= 0):
            self.kill()

        ### Update Image ###
        now = pygame.time.get_ticks()
        if (now - self.status["start_time"]) > 20:
            if (now - self.status["start_time"]) < 60:
                self.image = self.IMAGE["ORIGIN"]
                self.image.set_colorkey(myglobal.COLOR["BLACK"])
                old_center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = old_center

### Enemy Bullet ###
class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        ### Property ###
        self.property = {
            "move_speed": 15,
            "damage_point": 50,
            "score": 0
        }

        ### Image ###
        self.IMAGE = {
            "ORIGIN": pygame.transform.scale(
                myglobal.IMAGE["BULLET"]["ENEMY_BULLET"]["BULLET"].convert(),
                myglobal.SIZE["ENEMY_BULLET"]),
            "SHOT_LIGHT": pygame.transform.scale(
                myglobal.IMAGE["BULLET"]["ENEMY_BULLET"]["SHOT_LIGHT"].convert(),
                myglobal.SIZE["ENEMY_SHOT_LIGHT"])
        }

        ### Music ###
        self.MUSIC = {
            "SOUND": pygame.mixer.Sound(myglobal.MUSIC["ENEMY_SHOT"])
        }

        ### Status ###
        self.status = {
            "move_x": random.uniform(-5, 5),
            "move_y": self.property["move_speed"],
            "start_time": 0
        }

        ##### Initial #####
        self.image = self.IMAGE["SHOT_LIGHT"]
        self.image.set_colorkey(myglobal.COLOR["BLACK"])
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.MUSIC["SOUND"].set_volume(0.1)
        self.MUSIC["SOUND"].play()
        self.status["start_time"] = pygame.time.get_ticks()

    ##### Collision Response #####
    def collide_animation(self, center, explosions, powerups):
        bullet_explosion = explosion.Explosion(center, myglobal.IMAGE["BULLET_EXPLOSION"])
        explosions.add(bullet_explosion)

    ##### Update #####
    def update(self):
        ### Move ###
        self.rect.x += self.status["move_x"]
        self.rect.y += self.status["move_y"]
        if (self.rect.left >= myglobal.SIZE["SCREEN"][0] or
            self.rect.right <= 0 or self.rect.bottom <= 0):
            self.kill()

        ### Update Image ###
        now = pygame.time.get_ticks()
        if (now - self.status["start_time"]) > 20:
            if (now - self.status["start_time"]) < 60:
                self.image = self.IMAGE["ORIGIN"]
                self.image.set_colorkey(myglobal.COLOR["BLACK"])
                old_center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = old_center

### My Bomb ###
class MyBomb(pygame.sprite.Sprite):
    def __init__(self, rectx):
        pygame.sprite.Sprite.__init__(self)
        ### Property ###
        self.property = {
            "move_speed": 10
        }

        ### Image ###
        self.IMAGE = {
            "ORIGIN": pygame.transform.scale(
                myglobal.IMAGE["BULLET"]["MY_BOMB"],
                myglobal.SIZE["MY_BOMB"])
        }

        ### Status ###
        self.status = {
            "move_y": self.property["move_speed"]
        }

        ##### Initial #####
        self.image = self.IMAGE["ORIGIN"]
        self.image.set_colorkey(myglobal.COLOR["BLACK"])
        self.rect = self.image.get_rect()
        self.rect.centerx = rectx
        self.rect.top = myglobal.SIZE["SCREEN"][1]

    ##### Update #####
    def update(self):
        ### Move ###
        self.rect.y -= self.status["move_y"]
        if self.rect.bottom <= 0:
            self.kill()
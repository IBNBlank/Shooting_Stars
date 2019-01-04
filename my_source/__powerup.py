# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-07-26 18:58:58
# @Last Modified by:   IBNBlank
# @Last Modified time: 2019-01-04 20:41:33

import pygame
import random

import my_source.__myglobal as myglobal

##### Property #####
POWER_UP_PROPERTY = {
    "move_speed": 20
}

### New Power_up ###
def random_powerup(center):
    rate = random.randint(1, 8)
    if rate == 1 or rate == 2:
        power_up = AtkUp(center)
    elif rate == 3 or rate == 4:
        power_up = HpUp(center)
    elif rate == 5 or rate == 6:
        power_up = SpeedUp(center)
    elif rate == 7 :
        power_up = BombUp(center)
    else:
        power_up = LifeUp(center)
    return power_up

##### Power_up Classes #####
### Attack Up ###
class AtkUp(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)

        ### Property ###
        self.property = {
            "move_speed": POWER_UP_PROPERTY["move_speed"]
        }

        ### Image ###
        self.IMAGE = {
            "ORIGIN": pygame.transform.scale(
                    myglobal.IMAGE["POWER_UP"]["ATK_UP"].convert(),
                    myglobal.SIZE["POWER_UP"])
        }

        ### Music ###
        self.MUSIC = {
            "SOUND": pygame.mixer.Sound(myglobal.MUSIC["POWER_UP"])
        }

        ### Status ###
        self.status = {
            "move_x": 0,
            "move_y": 0,
            "angle": random.uniform(-1, 1)
        }

        ##### Initial #####
        direction = (self.status["angle"]**2 + 1) ** 0.5
        self.status["move_x"] = self.property["move_speed"] * self.status["angle"] / direction
        self.status["move_y"] = self.property["move_speed"] / direction
        self.image = self.IMAGE["ORIGIN"]
        self.image.set_colorkey(myglobal.COLOR["BLACK"])
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.MUSIC["SOUND"].set_volume(2)

    ##### Power Up #####
    def power_up(self, player):
        if player.property["attack_speed"] >= 100:
            player.property["attack_speed"] -= 50
        self.MUSIC["SOUND"].play()

    ##### Update #####
    def update(self):
        ### Move ###
        self.rect.x += self.status["move_x"]
        self.rect.y += self.status["move_y"]
        if self.rect.right >= myglobal.SIZE["SCREEN"][0]:
            self.rect.right = myglobal.SIZE["SCREEN"][0]
            self.status["move_x"] = -1 * abs(self.status["move_x"])
        if self.rect.left <= 0:
            self.rect.left = 0
            self.status["move_x"] = abs(self.status["move_x"])
        if self.rect.bottom >= myglobal.SIZE["SCREEN"][1]:
            self.rect.bottom = myglobal.SIZE["SCREEN"][1]
            self.status["move_y"] = -1 * abs(self.status["move_y"])
        if self.rect.top <= 0:
            self.rect.top = 0
            self.status["move_y"] = abs(self.status["move_y"])

### Health Point Up ###
class HpUp(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)

        ### Property ###
        self.property = {
            "move_speed": POWER_UP_PROPERTY["move_speed"]
        }

        ### Image ###
        self.IMAGE = {
            "ORIGIN": pygame.transform.scale(
                    myglobal.IMAGE["POWER_UP"]["HP_UP"].convert(),
                    myglobal.SIZE["POWER_UP"])
        }

        ### Music ###
        self.MUSIC = {
            "SOUND": pygame.mixer.Sound(myglobal.MUSIC["POWER_UP"])
        }

        ### Status ###
        self.status = {
            "move_x": 0,
            "move_y": 0,
            "angle": random.uniform(-1, 1)
        }

        ##### Initial #####
        direction = (self.status["angle"]**2 + 1) ** 0.5
        self.status["move_x"] = self.property["move_speed"] * self.status["angle"] / direction
        self.status["move_y"] = self.property["move_speed"] / direction
        self.image = self.IMAGE["ORIGIN"]
        self.image.set_colorkey(myglobal.COLOR["BLACK"])
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.MUSIC["SOUND"].set_volume(2)

    ##### Power Up #####
    def power_up(self, player):
        if player.property["health_point"] <= 250:
            player.property["health_point"] += 50
        else:
            player.property["health_point"] = 300
        self.MUSIC["SOUND"].play()

    ##### Update #####
    def update(self):
        ### Move ###
        self.rect.x += self.status["move_x"]
        self.rect.y += self.status["move_y"]
        if self.rect.right >= myglobal.SIZE["SCREEN"][0]:
            self.rect.right = myglobal.SIZE["SCREEN"][0]
            self.status["move_x"] = -1 * abs(self.status["move_x"])
        if self.rect.left <= 0:
            self.rect.left = 0
            self.status["move_x"] = abs(self.status["move_x"])
        if self.rect.bottom >= myglobal.SIZE["SCREEN"][1]:
            self.rect.bottom = myglobal.SIZE["SCREEN"][1]
            self.status["move_y"] = -1 * abs(self.status["move_y"])
        if self.rect.top <= 0:
            self.rect.top = 0
            self.status["move_y"] = abs(self.status["move_y"])

### Speed Up ###
class SpeedUp(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)

        ### Property ###
        self.property = {
            "move_speed": POWER_UP_PROPERTY["move_speed"]
        }

        ### Image ###
        self.IMAGE = {
            "ORIGIN": pygame.transform.scale(
                    myglobal.IMAGE["POWER_UP"]["SPEED_UP"].convert(),
                    myglobal.SIZE["POWER_UP"])
        }

        ### Music ###
        self.MUSIC = {
            "SOUND": pygame.mixer.Sound(myglobal.MUSIC["POWER_UP"])
        }

        ### Status ###
        self.status = {
            "move_x": 0,
            "move_y": 0,
            "angle": random.uniform(-1, 1)
        }

        ##### Initial #####
        direction = (self.status["angle"]**2 + 1) ** 0.5
        self.status["move_x"] = self.property["move_speed"] * self.status["angle"] / direction
        self.status["move_y"] = self.property["move_speed"] / direction
        self.image = self.IMAGE["ORIGIN"]
        self.image.set_colorkey(myglobal.COLOR["BLACK"])
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.MUSIC["SOUND"].set_volume(2)

    ##### Power Up #####
    def power_up(self, player):
        if player.property["move_speed"] <= 20:
            player.property["move_speed"] += 5
        self.MUSIC["SOUND"].play()

    ##### Update #####
    def update(self):
        ### Move ###
        self.rect.x += self.status["move_x"]
        self.rect.y += self.status["move_y"]
        if self.rect.right >= myglobal.SIZE["SCREEN"][0]:
            self.rect.right = myglobal.SIZE["SCREEN"][0]
            self.status["move_x"] = -1 * abs(self.status["move_x"])
        if self.rect.left <= 0:
            self.rect.left = 0
            self.status["move_x"] = abs(self.status["move_x"])
        if self.rect.bottom >= myglobal.SIZE["SCREEN"][1]:
            self.rect.bottom = myglobal.SIZE["SCREEN"][1]
            self.status["move_y"] = -1 * abs(self.status["move_y"])
        if self.rect.top <= 0:
            self.rect.top = 0
            self.status["move_y"] = abs(self.status["move_y"])

### Bomb Number Up ###
class BombUp(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)

        ### Property ###
        self.property = {
            "move_speed": POWER_UP_PROPERTY["move_speed"]
        }

        ### Image ###
        self.IMAGE = {
            "ORIGIN": pygame.transform.scale(
                    myglobal.IMAGE["POWER_UP"]["BOMB_UP"].convert(),
                    myglobal.SIZE["POWER_UP"])
        }

        ### Music ###
        self.MUSIC = {
            "SOUND": pygame.mixer.Sound(myglobal.MUSIC["POWER_UP"])
        }

        ### Status ###
        self.status = {
            "move_x": 0,
            "move_y": 0,
            "angle": random.uniform(-1, 1)
        }

        ##### Initial #####
        direction = (self.status["angle"]**2 + 1) ** 0.5
        self.status["move_x"] = self.property["move_speed"] * self.status["angle"] / direction
        self.status["move_y"] = self.property["move_speed"] / direction
        self.image = self.IMAGE["ORIGIN"]
        self.image.set_colorkey(myglobal.COLOR["BLACK"])
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.MUSIC["SOUND"].set_volume(2)

    ##### Power Up #####
    def power_up(self, player):
        if player.property["bomb_number"] <= 4:
            player.property["bomb_number"] += 1
        self.MUSIC["SOUND"].play()

    ##### Update #####
    def update(self):
        ### Move ###
        self.rect.x += self.status["move_x"]
        self.rect.y += self.status["move_y"]
        if self.rect.right >= myglobal.SIZE["SCREEN"][0]:
            self.rect.right = myglobal.SIZE["SCREEN"][0]
            self.status["move_x"] = -1 * abs(self.status["move_x"])
        if self.rect.left <= 0:
            self.rect.left = 0
            self.status["move_x"] = abs(self.status["move_x"])
        if self.rect.bottom >= myglobal.SIZE["SCREEN"][1]:
            self.rect.bottom = myglobal.SIZE["SCREEN"][1]
            self.status["move_y"] = -1 * abs(self.status["move_y"])
        if self.rect.top <= 0:
            self.rect.top = 0
            self.status["move_y"] = abs(self.status["move_y"])

### Life Number Up ###
class LifeUp(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)

        ### Property ###
        self.property = {
            "move_speed": POWER_UP_PROPERTY["move_speed"]
        }

        ### Image ###
        self.IMAGE = {
            "ORIGIN": pygame.transform.scale(
                    myglobal.IMAGE["POWER_UP"]["LIFE_UP"].convert(),
                    myglobal.SIZE["POWER_UP"])
        }

        ### Music ###
        self.MUSIC = {
            "SOUND": pygame.mixer.Sound(myglobal.MUSIC["POWER_UP"])
        }

        ### Status ###
        self.status = {
            "move_x": 0,
            "move_y": 0,
            "angle": random.uniform(-1, 1)
        }

        ##### Initial #####
        direction = (self.status["angle"]**2 + 1) ** 0.5
        self.status["move_x"] = self.property["move_speed"] * self.status["angle"] / direction
        self.status["move_y"] = self.property["move_speed"] / direction
        self.image = self.IMAGE["ORIGIN"]
        self.image.set_colorkey(myglobal.COLOR["BLACK"])
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.MUSIC["SOUND"].set_volume(2)

    ##### Power Up #####
    def power_up(self, player):
        if player.property["life_number"] <= 4:
            player.property["life_number"] += 1
        self.MUSIC["SOUND"].play()

    ##### Update #####
    def update(self):
        ### Move ###
        self.rect.x += self.status["move_x"]
        self.rect.y += self.status["move_y"]
        if self.rect.right >= myglobal.SIZE["SCREEN"][0]:
            self.rect.right = myglobal.SIZE["SCREEN"][0]
            self.status["move_x"] = -1 * abs(self.status["move_x"])
        if self.rect.left <= 0:
            self.rect.left = 0
            self.status["move_x"] = abs(self.status["move_x"])
        if self.rect.bottom >= myglobal.SIZE["SCREEN"][1]:
            self.rect.bottom = myglobal.SIZE["SCREEN"][1]
            self.status["move_y"] = -1 * abs(self.status["move_y"])
        if self.rect.top <= 0:
            self.rect.top = 0
            self.status["move_y"] = abs(self.status["move_y"])
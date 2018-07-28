# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-07-22 22:12:24
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-07-28 22:02:59

import pygame
import random

import my_source._myglobal as myglobal
import my_source._bullet as bullet
import my_source._explosion as explosion
import my_source._powerup as powerup

##### Property Define #####
### Plane One ###
PLANE_ONE_PROPERTY = {
    "HEALTH_POINT": 200,
    "MOVE_SPEED": 1,
    "ATTACK_SPEED": 200,
    "SCORE": 100
}
### Plane Two ###
PLANE_TWO_PROPERTY = {
    "HEALTH_POINT": 100,
    "MOVE_SPEED": 2,
    "ATTACK_SPEED": 400,
    "SCORE": 100
}
### Plane Three ###
PLANE_THREE_PROPERTY = {
    "HEALTH_POINT": 50,
    "MOVE_SPEED": 4,
    "ATTACK_SPEED": 600,
    "SCORE": 100
}

##### Enemy Classes #####
### Block ###
class Block(pygame.sprite.Sprite):
    def __init__(self, kind=random.randint(1,4)):
        pygame.sprite.Sprite.__init__(self)

        ##### Choose Kind #####
        if kind == 1:
            ### Property ###
            self.property = {
                "health_point": random.randint(30, 80),
                "move_speed": random.randint(15, 25),
                "rotate_speed": random.randint(-15, 15),
                "damage_point": 0,
                "score": 0
            }
            ### Image ###
            self.IMAGE = {
                "ORIGIN": myglobal.IMAGE["BLOCK_ONE"].convert()
            }
        elif kind == 2:
            ### Property ###
            self.property = {
                "health_point": random.randint(70, 120),
                "move_speed": random.randint(10, 20),
                "rotate_speed": random.randint(-10, 10),
                "damage_point": 0,
                "score": 0
            }
            ### Image ###
            self.IMAGE = {
                "ORIGIN": myglobal.IMAGE["BLOCK_TWO"].convert()
            }
        elif kind == 3:
            ### Property ###
            self.property = {
                "health_point": random.randint(110, 160),
                "move_speed": random.randint(5, 15),
                "rotate_speed": random.randint(-5, 5),
                "damage_point": 0,
                "score": 0
            }
            ### Image ###
            self.IMAGE = {
                "ORIGIN": myglobal.IMAGE["BLOCK_THREE"].convert()
            }
        else:
            ### Property ###
            self.property = {
                "health_point": random.randint(150, 200),
                "move_speed": random.randint(2, 10),
                "rotate_speed": random.randint(-2, 2),
                "damage_point": 0,
                "score": 0
            }
            ### Image ###
            self.IMAGE = {
                "ORIGIN": myglobal.IMAGE["BLOCK_FOUR"].convert()
            }

        ##### Status #####
        self.status = {
            "move_x": 0,
            "move_y": 0,
            "last_time": 0,
            "angle": random.uniform(-1, 1),
            "rotate_angle": 0,
            "image_copy": 0,
            "power_up_flag": random.randint(1, 8)
        }

        ##### Initial #####
        self.property["damage_point"] = self.property["health_point"] / 2
        self.property["score"] = self.property["damage_point"]
        direction = (self.status["angle"]**2 + 1) ** 0.5
        self.status["move_x"] = self.property["move_speed"] * self.status["angle"] / direction
        self.status["move_y"] = self.property["move_speed"] / direction
        self.image = pygame.transform.scale(self.IMAGE["ORIGIN"], (self.property["health_point"],self.property["health_point"]))
        self.image.set_colorkey(myglobal.COLOR["BLACK"])
        self.status["image_copy"] = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, (myglobal.SIZE["SCREEN"][0] - self.rect.w))
        self.rect.bottom = 0

    ##### Collision Response #####
    def collide_animation(self, center, explosions, powerups):
        enemy_explosion = explosion.Explosion(center, myglobal.IMAGE["ENEMY_EXPLOSION"])
        explosions.add(enemy_explosion)
        if self.status["power_up_flag"] == 1:
            my_powerup = powerup.random_powerup(center)
            powerups.add(my_powerup)
        self.kill()

    ##### Update #####
    def update(self):
        ### Move ###
        self.rect.x += self.status["move_x"]
        self.rect.y += self.status["move_y"]
        if (self.rect.left >= myglobal.SIZE["SCREEN"][0] or
            self.rect.right <= 0 or self.rect.top >= myglobal.SIZE["SCREEN"][1]):
            self.rect.x = random.randint(0, (myglobal.SIZE["SCREEN"][0] - self.rect.w))
            self.rect.bottom = 0

        ### Rotate ###
        now = pygame.time.get_ticks()
        if (now - self.status["last_time"]) > 16:
            self.status["rotate_angle"] += self.property["rotate_speed"]
            self.status["rotate_angle"] %= 360
            self.image = pygame.transform.rotate(self.status["image_copy"], self.status["rotate_angle"])
            old_center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = old_center
            self.status["last_time"] = now

### Plane ###
class Plane(pygame.sprite.Sprite):
    def __init__(self, kind=random.randint(1,3), body=random.randint(1,3)):
        pygame.sprite.Sprite.__init__(self)

        ##### Choose Kind #####
        if kind == 1:
            ### Property ###
            self.property = {
                "health_point": PLANE_ONE_PROPERTY["HEALTH_POINT"],
                "move_speed": PLANE_ONE_PROPERTY["MOVE_SPEED"],
                "attack_speed": PLANE_ONE_PROPERTY["ATTACK_SPEED"],
                "damage_point": 0,
                "score": PLANE_ONE_PROPERTY["SCORE"]
            }
            ### Image ###
            self.IMAGE = {
                "ORIGIN": myglobal.IMAGE["PLANE_ONE"].convert()
            }
        elif kind == 2:
            ### Property ###
            self.property = {
                "health_point": PLANE_TWO_PROPERTY["HEALTH_POINT"],
                "move_speed": PLANE_TWO_PROPERTY["MOVE_SPEED"],
                "attack_speed": PLANE_TWO_PROPERTY["ATTACK_SPEED"],
                "damage_point": 0,
                "score": PLANE_TWO_PROPERTY["SCORE"]
            }
            ### Image ###
            self.IMAGE = {
                "ORIGIN": myglobal.IMAGE["PLANE_TWO"].convert()
            }
        else:
            ### Property ###
            self.property = {
                "health_point": PLANE_THREE_PROPERTY["HEALTH_POINT"],
                "move_speed": PLANE_THREE_PROPERTY["MOVE_SPEED"],
                "attack_speed": PLANE_THREE_PROPERTY["ATTACK_SPEED"],
                "damage_point": 0,
                "score": PLANE_THREE_PROPERTY["SCORE"]
            }
            ### Image ###
            self.IMAGE = {
                "ORIGIN": myglobal.IMAGE["PLANE_THREE"].convert()
            }

        ##### Set Kind #####
        if body == 1:
            ### Property Change ###
            self.property["health_point"] *= 4
            self.property["score"] *= 4
            ### Image Decide ###
            self.image = pygame.transform.scale(self.IMAGE["ORIGIN"], myglobal.SIZE["PLANE_LARGE"])
        elif body == 2:
            ### Property Change ###
            self.property["health_point"] *= 2
            self.property["move_speed"] *= 2
            self.property["attack_speed"] *= 2
            self.property["score"] *= 2
            ### Image Decide ###
            self.image = pygame.transform.scale(self.IMAGE["ORIGIN"], myglobal.SIZE["PLANE_MIDDLE"])
        else:
            ### Property Change ###
            self.property["move_speed"] *= 4
            self.property["attack_speed"] *= 4
            ### Image Decide ###
            self.image = pygame.transform.scale(self.IMAGE["ORIGIN"], myglobal.SIZE["PLANE_SMALL"])

        ##### Status #####
        self.status = {
            "move_x": 0,
            "move_y": 0,
            "angle": random.uniform(-1, 1),
            "last_time": 0,
            "power_up_flag": random.randint(1, 4)
        }

        ##### Initial #####
        self.property["damage_point"] = self.property["health_point"] / 2
        direction = (self.status["angle"]**2 + 1) ** 0.5
        self.status["move_x"] = self.property["move_speed"] * self.status["angle"] / direction
        self.status["move_y"] = self.property["move_speed"] / direction
        self.image.set_colorkey(myglobal.COLOR["BLACK"])
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, (myglobal.SIZE["SCREEN"][0] - self.rect.w))
        self.rect.bottom = 0

    ##### Shot Bullet #####
    def shot(self, bullets):
        enemy_bullet = bullet.EnemyBullet((self.rect.centerx, self.rect.bottom))
        bullets.add(enemy_bullet)

    ##### Collision Response #####
    def collide_animation(self, center, explosions, powerups):
        enemy_explosion = explosion.Explosion(center, myglobal.IMAGE["ENEMY_EXPLOSION"])
        explosions.add(enemy_explosion)
        if self.status["power_up_flag"] == 1:
            my_powerup = powerup.random_powerup(center)
            powerups.add(my_powerup)
        self.kill()

    ##### Update #####
    def update(self, bullets):
        ### Move ###
        self.rect.x += self.status["move_x"]
        self.rect.y += self.status["move_y"]
        if (self.rect.left >= myglobal.SIZE["SCREEN"][0] or
            self.rect.right <= 0 or self.rect.top >= myglobal.SIZE["SCREEN"][1]):
            self.rect.x = random.randint(0, (myglobal.SIZE["SCREEN"][0] - self.rect.w))
            self.rect.bottom = 0

        ### Shot ###
        now = pygame.time.get_ticks()
        if (now - self.status["last_time"]) > self.property["attack_speed"]:
            self.shot(bullets)
            self.status["last_time"] = now
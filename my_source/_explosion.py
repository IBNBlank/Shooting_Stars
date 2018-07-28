# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-07-22 22:15:53
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-07-28 22:02:32

import pygame

import my_source._myglobal as myglobal

##### Explosion Class ######
class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, explosion_animation):
        pygame.sprite.Sprite.__init__(self)

        ### Image ###
        self.IMAGE = {
            "ORIGIN": explosion_animation
        }

        ### Music ###
        self.MUSIC = {
            "SOUND": pygame.mixer.Sound(myglobal.MUSIC["EXPLOSION"])
        }

        ### Status ###
        self.status = {
            "frame_all": 0,
            "frame": 0,
            "last_time": 0
        }

        ##### Initial #####
        self.status["frame_all"] = len(self.IMAGE["ORIGIN"])
        self.image = self.IMAGE["ORIGIN"][0]
        self.image.set_colorkey(myglobal.COLOR["BLACK"])
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.status["last_time"] = pygame.time.get_ticks()
        self.MUSIC["SOUND"].set_volume(0.1)
        self.MUSIC["SOUND"].play()

    ##### Update #####
    def update(self):
        ### Update Image ###
        now = pygame.time.get_ticks()
        if (now - self.status["last_time"]) > 20:
            if self.status["frame"] < self.status["frame_all"]:
                self.image = self.IMAGE["ORIGIN"][self.status["frame"]]
                self.image.set_colorkey(myglobal.COLOR["BLACK"])
                self.status["frame"] += 1
                self.status["last_time"] = now
            else:
                self.kill()
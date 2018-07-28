# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-07-26 23:55:32
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-07-28 22:18:25

import pygame

import my_source._myglobal as myglobal

##### UI Classes #####
### Start ###
class UiStart(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        ### Image ###
        self.IMAGE = {
            "BACKGROUND": myglobal.IMAGE["BACKGROUND"]["BACKGROUND_ONE"].convert()
        }

        ### Music ###
        self.MUSIC = {
            "BACKGROUND": myglobal.MUSIC["BACKGROUND"]["BACKGROUND_ONE"]
        }

        ### Status ###
        self.status = {
            "title": "Shooting Star",
            "inform": "Press shoot to start",
            "last_time": 0,
            "blink_time": 600
        }

        ##### Initial #####
        self.image = self.IMAGE["BACKGROUND"]
        self.rect = self.image.get_rect()
        pygame.mixer.music.load(self.MUSIC["BACKGROUND"])
        pygame.mixer.music.play(loops=-1)
        self.status["last_time"] = pygame.time.get_ticks()

    ##### Render #####
    def render(self, screen):
        ### Render Background ###
        screen.blit(self.image, self.rect)

        ### Draw Title ###
        myglobal.draw_text(
            self.status["title"], screen,
            myglobal.COLOR["WHITE"], 110,
            myglobal.SIZE["SCREEN"][0]/2, 250)

        ### Draw Inform ###
        now = pygame.time.get_ticks()
        if (now - self.status["last_time"]) < self.status["blink_time"]:
            myglobal.draw_text(
                self.status["inform"], screen,
                myglobal.COLOR["WHITE"], 50,
                myglobal.SIZE["SCREEN"][0]/2, 450)
            pygame.draw.rect(
            screen, myglobal.COLOR["LIGHT_BLUE"],
            (0,0,600,800), 20)
            pygame.draw.rect(
            screen, myglobal.COLOR["LIGHT_BLUE"],
            (125,430,350,70), 6)
        elif (now - self.status["last_time"]) > 2*self.status["blink_time"]:
                self.status["last_time"] = now

### Over ###
class UiOver(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        ### Image ###
        self.IMAGE = {
            "BACKGROUND": myglobal.IMAGE["BACKGROUND"]["BACKGROUND_THREE"].convert()
        }

        ### Music ###
        self.MUSIC = {
            "BACKGROUND": myglobal.MUSIC["BACKGROUND"]["BACKGROUND_THREE"]
        }

        ### Status ###
        self.status = {
            "over": "Game Over",
            "last_time": 0,
            "blink_time": 700
        }

        ##### Initial #####
        self.image = self.IMAGE["BACKGROUND"]
        self.rect = self.image.get_rect()
        pygame.mixer.music.load(self.MUSIC["BACKGROUND"])
        pygame.mixer.music.play()
        self.status["last_time"] = pygame.time.get_ticks()

    ##### Render #####
    def render(self, screen):
        ### Render Background ###
        screen.blit(self.image, self.rect)

        ### Draw Over ###
        now = pygame.time.get_ticks()
        if (now - self.status["last_time"]) < self.status["blink_time"]:
            myglobal.draw_text(
                self.status["over"], screen,
                myglobal.COLOR["WHITE"], 140,
                myglobal.SIZE["SCREEN"][0]/2, 280)
            pygame.draw.rect(
            screen, myglobal.COLOR["LIGHT_BLUE"],
            (0,0,600,800), 20)
        elif (now - self.status["last_time"]) > 2*self.status["blink_time"]:
                self.status["last_time"] = now

### Game ###
class UiGame(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        ### Image ###
        self.IMAGE = {
            "LIFE_ICON": player.IMAGE["LIFE"],
            "BOMB_ICON": pygame.transform.scale(
                myglobal.IMAGE["UI"]["BOMB_ICON"].convert(),
                myglobal.SIZE["BOMB_ICON"]),
            "BACKGROUND": myglobal.IMAGE["BACKGROUND"]["BACKGROUND_TWO"].convert()
        }

        ### Music ###
        self.MUSIC = {
            "BACKGROUND": myglobal.MUSIC["BACKGROUND"]["BACKGROUND_TWO"]
        }

        ### Status ###
        self.status = {
            "health_point": 0,
            "hp_color": 0,
            "bomb_number": 0,
            "life_number": 0,
            "score": 0
        }

        ##### Initial #####
        self.IMAGE["LIFE_ICON"].set_colorkey(myglobal.COLOR["BLACK"])
        self.IMAGE["BOMB_ICON"].set_colorkey(myglobal.COLOR["BLACK"])
        self.image = self.IMAGE["BACKGROUND"]
        self.rect = self.image.get_rect()
        pygame.mixer.music.load(self.MUSIC["BACKGROUND"])
        pygame.mixer.music.play(loops=-1)

    ##### Update #####
    def update(self, player):
        ### Update Score ###
        self.status["score"] = int(myglobal.score)

        ### Update Player ###
        self.status["health_point"] = player.property["health_point"]
        self.status["bomb_number"] = player.property["bomb_number"]
        self.status["life_number"] = player.property["life_number"]

        ### Update HP Color ###
        if self.status["health_point"] < 100:
            self.status["hp_color"] = myglobal.COLOR["RED"]
        elif self.status["health_point"] < 200:
            self.status["hp_color"] = myglobal.COLOR["YELLOW"]
        else :
            self.status["hp_color"] = myglobal.COLOR["GREEN"]

    ##### Render #####
    def render(self, screen):
        ### Draw HP ###
        pygame.draw.rect(
            screen, self.status["hp_color"],
            (14,14,self.status["health_point"]/2,22))
        pygame.draw.rect(
            screen, myglobal.COLOR["WHITE"],
            (14,14,150,22), 3)

        ### Draw Score ###
        pygame.draw.rect(
            screen, myglobal.COLOR["BLACK"],
            (250,10,100,30))
        pygame.draw.rect(
            screen, myglobal.COLOR["WHITE"],
            (250,10,100,30), 3)
        myglobal.draw_text(
            str(self.status["score"]), screen,
            myglobal.COLOR["WHITE"], 25,
            myglobal.SIZE["SCREEN"][0]/2, 18)

        ### Draw Life Icon ###
        life_rect = self.IMAGE["LIFE_ICON"].get_rect()
        life_rect.right = myglobal.SIZE["SCREEN"][0] - 10
        life_rect.y = 10
        for i in range(self.status["life_number"]):
            screen.blit(self.IMAGE["LIFE_ICON"], life_rect)
            life_rect.right = life_rect.x - 10

        ### Draw Bomb Icon ###
        bomb_rect = self.IMAGE["BOMB_ICON"].get_rect()
        bomb_rect.right = myglobal.SIZE["SCREEN"][0] - 10
        bomb_rect.y = 10 + life_rect.bottom
        for i in range(self.status["bomb_number"]):
            screen.blit(self.IMAGE["BOMB_ICON"], bomb_rect)
            bomb_rect.right = bomb_rect.x - 10

    ##### Render Background #####
    def render_background(self, screen):
        screen.blit(self.image, self.rect)
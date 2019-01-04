# -*- coding: utf-8 -*-
# @Author: IBNBlank
# @Date:   2018-07-22 19:56:30
# @Last Modified by:   IBNBlank
# @Last Modified time: 2018-07-28 22:19:12

import pygame
from os import path

##### Color Define #####
COLOR = {
    "BLACK": (0,0,0),
    "WHITE": (255,255,255),
    "RED": (255,0,0),
    "YELLOW": (255,255,0),
    "GREEN": (0,255,0),
    "LIGHT_BLUE": (100,255,255)
}

##### Path Define #####
### image ###
image_dir = path.join(path.join(path.dirname(__file__), path.pardir), 'image')
player_img = path.join(image_dir, 'player')
block_img = path.join(image_dir, 'block')
plane_img = path.join(image_dir, 'plane')
bullet_img = path.join(image_dir, 'bullet')
powerup_img = path.join(image_dir, 'powerup')
ui_img = path.join(image_dir, 'ui')
explosion_img = path.join(image_dir, 'explosion')
player_one_img = path.join(player_img, 'player_one')
player_two_img = path.join(player_img, 'player_two')
player_three_img = path.join(player_img, 'player_three')
player_four_img = path.join(player_img, 'player_four')
block_one_img = path.join(block_img, 'block_one')
block_two_img = path.join(block_img, 'block_two')
block_three_img = path.join(block_img, 'block_three')
block_four_img = path.join(block_img, 'block_four')
plane_one_img = path.join(plane_img, 'plane_one')
plane_two_img = path.join(plane_img, 'plane_two')
plane_three_img = path.join(plane_img, 'plane_three')
bullet_my_img = path.join(bullet_img, 'my_bullet')
bullet_enemy_img = path.join(bullet_img, 'enemy_bullet')
bomb_my_img = path.join(bullet_img, 'my_bomb')
explosion_my_img = path.join(explosion_img, 'my_explosion')
explosion_enemy_img = path.join(explosion_img, 'enemy_explosion')
explosion_bullet_img = path.join(explosion_img, 'bullet_explosion')
atk_img = path.join(powerup_img, 'atk_up')
hp_img = path.join(powerup_img, 'hp_up')
speed_img = path.join(powerup_img, 'speed_up')
bomb_img = path.join(powerup_img, 'bomb_up')
life_img = path.join(powerup_img, 'life_up')
### music ###
music_dir = path.join(path.join(path.dirname(__file__), path.pardir), 'music')

##### Image Define #####
### Explosion ###
EXPLOSION_PLAYER_ANIMATION = []
for i in range(24):
    if i < 10:
        explosion_temp_img = pygame.image.load(
            path.join(explosion_my_img, 'expl_11_000{0}.png'.format(i)))
    else:
        explosion_temp_img = pygame.image.load(
            path.join(explosion_my_img, 'expl_11_00{0}.png'.format(i)))
    explosion_temp_img = pygame.transform.rotozoom(explosion_temp_img, 0, 1.5)
    EXPLOSION_PLAYER_ANIMATION.append(explosion_temp_img)
EXPLOSION_ENEMY_ANIMATION = []
for i in range(24):
    if i < 10:
        explosion_temp_img = pygame.image.load(
            path.join(explosion_enemy_img, 'expl_02_000{0}.png'.format(i)))
    else:
        explosion_temp_img = pygame.image.load(
            path.join(explosion_enemy_img, 'expl_02_00{0}.png'.format(i)))
    explosion_temp_img = pygame.transform.rotozoom(explosion_temp_img, 0, 5.2)
    EXPLOSION_ENEMY_ANIMATION.append(explosion_temp_img)
EXPLOSION_BULLET_ANIMATION = []
for i in range(9):
    explosion_temp_img = pygame.image.load(
        path.join(explosion_bullet_img, 'regularExplosion0{0}.png'.format(i)))
    explosion_temp_img = pygame.transform.rotozoom(explosion_temp_img, 0, 0.5)
    EXPLOSION_BULLET_ANIMATION.append(explosion_temp_img)

### Image ###
IMAGE = {
    "BACKGROUND": {
        "BACKGROUND_ONE": pygame.image.load(path.join(image_dir, 'background_one.png')),
        "BACKGROUND_TWO": pygame.image.load(path.join(image_dir, 'background_two.jpg')),
        "BACKGROUND_THREE": pygame.image.load(path.join(image_dir, 'background_three.jpg'))
    },
    "PLAYER_ONE": {
        "ORIGIN": pygame.image.load(path.join(player_one_img, 'origin.png')),
        "BLANK": pygame.image.load(path.join(player_one_img, 'blank.png'))
    },
    "PLAYER_TWO": {
        "ORIGIN": pygame.image.load(path.join(player_two_img, 'origin.png')),
        "BLANK": pygame.image.load(path.join(player_two_img, 'blank.png'))
    },
    "PLAYER_THREE": {
        "ORIGIN": pygame.image.load(path.join(player_three_img, 'origin.png')),
        "BLANK": pygame.image.load(path.join(player_three_img, 'blank.png'))
    },
    "PLAYER_FOUR": {
        "ORIGIN": pygame.image.load(path.join(player_four_img, 'origin.png')),
        "BLANK": pygame.image.load(path.join(player_four_img, 'blank.png'))
    },
    "BLOCK_ONE": pygame.image.load(path.join(block_one_img, 'origin.png')),
    "BLOCK_TWO": pygame.image.load(path.join(block_two_img, 'origin.png')),
    "BLOCK_THREE": pygame.image.load(path.join(block_three_img, 'origin.png')),
    "BLOCK_FOUR": pygame.image.load(path.join(block_four_img, 'origin.png')),
    "PLANE_ONE": pygame.image.load(path.join(plane_one_img, 'origin.png')),
    "PLANE_TWO": pygame.image.load(path.join(plane_two_img, 'origin.png')),
    "PLANE_THREE": pygame.image.load(path.join(plane_three_img, 'origin.png')),
    "BULLET": {
        "MY_BULLET": {
            "BULLET": pygame.image.load(path.join(bullet_my_img, 'origin.png')),
            "SHOT_LIGHT": pygame.image.load(path.join(bullet_my_img, 'shot_light.png'))
        },
        "ENEMY_BULLET": {
            "BULLET": pygame.image.load(path.join(bullet_enemy_img, 'origin.png')),
            "SHOT_LIGHT":  pygame.image.load(path.join(bullet_enemy_img, 'shot_light.png'))
        },
        "MY_BOMB": pygame.image.load(path.join(bomb_my_img, 'origin.png'))
    },
    "MY_EXPLOSION": EXPLOSION_PLAYER_ANIMATION,
    "ENEMY_EXPLOSION": EXPLOSION_ENEMY_ANIMATION,
    "BULLET_EXPLOSION": EXPLOSION_BULLET_ANIMATION,
    "POWER_UP": {
        "ATK_UP": pygame.image.load(path.join(atk_img, 'origin.png')),
        "HP_UP": pygame.image.load(path.join(hp_img, 'origin.png')),
        "SPEED_UP": pygame.image.load(path.join(speed_img, 'origin.png')),
        "BOMB_UP": pygame.image.load(path.join(bomb_img, 'origin.png')),
        "LIFE_UP": pygame.image.load(path.join(life_img, 'origin.png'))
    },
    "UI":{
        "BOMB_ICON": pygame.image.load(path.join(ui_img, 'bomb_icon.png'))
    }
}

### Size Define ###
SIZE = {
    "SCREEN": (600,800),
    "PLAYER_ONE": (53,40),
    "PLAYER_ONE_LIFE": (26,26),
    "PLAYER_TWO": (53,40),
    "PLAYER_TWO_LIFE": (26,26),
    "PLAYER_THREE": (53,40),
    "PLAYER_THREE_LIFE": (26,26),
    "PLAYER_FOUR": (53,53),
    "PLAYER_FOUR_LIFE": (26,26),
    "PLANE_SMALL": (52,42),
    "PLANE_MIDDLE": (104,84),
    "PLANE_LARGE": (156,126),
    "MY_BULLET": (10,60),
    "ENEMY_BULLET": (9,50),
    "MY_BOMB": (208,576),
    "MY_SHOT_LIGHT": (50,50),
    "ENEMY_SHOT_LIGHT": (40,40),
    "POWER_UP": (30,30),
    "BOMB_ICON": (26,26)
}

##### Music Define #####
MUSIC = {
    "BACKGROUND": {
        "BACKGROUND_ONE": path.join(music_dir, 'background_one.ogg'),
        "BACKGROUND_TWO": path.join(music_dir, 'background_two.mp3'),
        "BACKGROUND_THREE": path.join(music_dir, 'background_three.wav'),
    },
    "MY_SHOT": path.join(music_dir, 'my_shot.wav'),
    "ENEMY_SHOT": path.join(music_dir, 'enemy_shot.wav'),
    "EXPLOSION": path.join(music_dir, 'explosion.wav'),
    "POWER_UP":path.join(music_dir, 'power_up.ogg')
}

##### Variable Define #####
FPS = 60
score = 0
enemy_time = 2000
last_time = 0
joystick_flag = True
scene_flag = 1
last_scene_flag = 1

##### Draw Text Define #####
def draw_text(text, surface, color, size, x, y):
    font_name = pygame.font.match_font('my_font.ttf')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x ,y)
    surface.blit(text_surface, text_rect)
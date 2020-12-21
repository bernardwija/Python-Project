import pygame
import os

pygame.font.init()
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

#MATERIALS ~~~~~~~~~~~~~
font = pygame.font.SysFont("comicsans",50)
fps = 60
music = 10
sfx = 10

yellow = pygame.image.load(os.path.join('my_assets','enemy_yellow.png'))
pink = pygame.image.load(os.path.join('my_assets','enemy_pink.png'))
brown = pygame.image.load(os.path.join('my_assets','enemy_brown.png'))
player = pygame.image.load(os.path.join('my_assets','player.png'))

heart = pygame.image.load(os.path.join('my_assets','heart_shot.png'))
senpie = pygame.image.load(os.path.join('my_assets','senpie_shot.png'))

background = pygame.image.load(os.path.join('my_assets','background.png'))
menu = pygame.image.load(os.path.join('my_assets','menu.png'))
winback = pygame.image.load(os.path.join('my_assets','win_screen.png'))
looseback = pygame.image.load(os.path.join('my_assets','loose_screen.png'))
setting = pygame.image.load(os.path.join('my_assets','settings.png'))
howtoplay = pygame.image.load(os.path.join('my_assets','howtoplay.png'))
creds = pygame.image.load(os.path.join('my_assets','menusettings.png'))

pop = pygame.mixer.Sound(os.path.join('my_assets','bubble.wav'))
ahh = pygame.mixer.Sound(os.path.join('my_assets','Ahh1.wav'))
ugh = pygame.mixer.Sound(os.path.join('my_assets','steve.wav'))

#WINDOW ~~~~~~~~~~~~~~
width, height = 750, 750
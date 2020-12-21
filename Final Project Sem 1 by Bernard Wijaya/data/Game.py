import pygame
import sys
import random
import os

import Materials as mtrls
from Elements import collide,Boy,Girls

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

#MATERIALS ~~~~~~~~~~~~~
font = mtrls.font
fps = mtrls.fps
music = mtrls.music
sfx = mtrls.sfx

background = mtrls.background
menu = mtrls.menu
winback = mtrls.winback
looseback = mtrls.looseback
setting = mtrls.setting
howtoplay = mtrls.howtoplay
creds = mtrls.creds

ahh = mtrls.ahh
ugh = mtrls.ugh

#WINDOW ~~~~~~~~~~~~~~
width, height = mtrls.width, mtrls.height
disp = pygame.display.set_mode((width, height))
pygame.display.set_caption('PlayBoy')
mainclock = pygame.time.Clock()

#WRITINGS ~~~~~~~~~
def drawtext(text, font, color, screen, x, y):
    rendered = font.render(text, 1, color)
    coordinates = (x, y)
    screen.blit(rendered, coordinates)

#MAIN MENU ~~~~~~~~~~
def main_menu(music,sfx):
    #background music
    pygame.mixer.music.load(os.path.join('my_assets', 'undertale_shop.mp3'))
    pygame.mixer.music.set_volume(music/10)
    pygame.mixer.music.play(-1)

    click = False
    while True:
        disp.blit(menu, (0, 0))

        #mouse control with interface
        mx, my = pygame.mouse.get_pos()
        playbutton = pygame.Rect(260, 310, 220, 65)
        optbutton = pygame.Rect(260, 400, 220, 65)
        if playbutton.collidepoint((mx,my)):
            if click:
                howto(music,sfx)
        if optbutton.collidepoint((mx,my)):
            if click:
                option(music,sfx)
        pygame.draw.rect(disp, (0,0,0), playbutton)
        pygame.draw.rect(disp, (0,0,0), optbutton)
        drawtext('Play',font,(255,255,255),disp,335,325)
        drawtext('Option', font, (255, 255, 255), disp, 310, 417)

        #screen physics
        click = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        mainclock.tick(fps)

#MUSIC SETTINGS ~~~~~~~~~~~~~~
def option(music,sfx):

        click = False
        while True:

            disp.blit(setting, (0, 0))
            drawtext(f"{music}", font, (0, 0, 0), disp, 180, 330)
            drawtext(f"{sfx}", font, (0, 0, 0), disp, 440, 328)

            # mouse control with interface
            mx, my = pygame.mouse.get_pos()
            music_up_button = pygame.Rect(262, 232, 78, 100)
            music_down_button = pygame.Rect(262, 364, 78, 100)
            sfx_up_button = pygame.Rect(523, 228, 78, 100)
            sfx_down_button = pygame.Rect(523, 362, 78, 100)
            mainbutton = pygame.Rect(130, 530, 180, 60)
            creditsbutton = pygame.Rect(450, 530, 180, 60)
            if music_up_button.collidepoint((mx, my)):
                if click:
                    if music < 10:
                        music += 1
            if music_down_button.collidepoint((mx, my)):
                if click:
                    if music > 0:
                        music -= 1
            if sfx_up_button.collidepoint((mx, my)):
                if click:
                    if sfx < 10:
                        sfx += 1
            if sfx_down_button.collidepoint((mx, my)):
                if click:
                    if sfx > 0:
                        sfx -= 1
            if mainbutton.collidepoint((mx, my)):
                if click:
                    pygame.mixer.music.stop()
                    main_menu(music,sfx)
            if creditsbutton.collidepoint((mx, my)):
                if click:
                    credits(music,sfx)
            pygame.draw.rect(disp, (0, 0, 0), music_up_button)
            pygame.draw.rect(disp, (0, 0, 0), music_down_button)
            pygame.draw.rect(disp, (0, 0, 0), sfx_up_button)
            pygame.draw.rect(disp, (0, 0, 0), sfx_down_button)
            pygame.draw.rect(disp, (0, 0, 0), mainbutton)
            pygame.draw.rect(disp, (0, 0, 0), creditsbutton)
            drawtext('Save', font, (255, 255, 255), disp, 175, 545)
            drawtext('Credits', font, (255, 255, 255), disp, 475, 545)

            # screen physics
            click = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        main_menu(music,sfx)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            mainclock.tick(fps)

#CREDITS ~~~~~~~~~~~~~~~~
def credits(music,sfx):
    click = False
    while True:
        disp.blit(creds, (0, 0))

        # mouse control with interface
        mx, my = pygame.mouse.get_pos()
        mainbutton = pygame.Rect(265, 540, 220,60)
        if mainbutton.collidepoint((mx, my)):
            if click:
                main_menu(music, sfx)
        pygame.draw.rect(disp, (0, 0, 0), mainbutton)
        drawtext('Main Menu', font, (255, 255, 255), disp, 283, 555)

        # screen physics
        click = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    option(music, sfx)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        mainclock.tick(fps)

#HOW TO PLAY ~~~~~~~~~~~~~~
def howto(music,sfx):
    click = False
    while True:
        disp.blit(howtoplay, (0, 0))

        # mouse control with interface
        mx, my = pygame.mouse.get_pos()
        menubutton = pygame.Rect(50, 600, 220, 65)
        playbutton = pygame.Rect(480, 600, 220, 65)
        if menubutton.collidepoint((mx, my)):
            if click:
                main_menu(music, sfx)
        if playbutton.collidepoint((mx, my)):
            if click:
                pygame.mixer.music.stop()
                main(music, sfx)
        pygame.draw.rect(disp, (0, 0, 0), menubutton)
        pygame.draw.rect(disp, (0, 0, 0), playbutton)
        drawtext('Play >>', font, (255, 255, 255), disp, 530, 615)
        drawtext('Main Menu', font, (255, 255, 255), disp, 65, 615)

        # screen physics
        click = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu(music,sfx)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        mainclock.tick(fps)

#WIN GAME ~~~~~~~~~~~~~~~~~
def win(music,sfx):
    # background music
    pygame.mixer.music.load(os.path.join('my_assets', 'undertale_sans.mp3'))
    pygame.mixer.music.set_volume(music/10)
    pygame.mixer.music.play(-1)

    click = False
    while True:
        disp.blit(winback, (0, 0))

        # mouse control with interface
        mx, my = pygame.mouse.get_pos()
        playbutton = pygame.Rect(60, 650, 220, 65)
        mainbutton = pygame.Rect(470, 650, 220, 65)
        if playbutton.collidepoint((mx, my)):
            if click:
                pygame.mixer.music.stop()
                main(music,sfx)
        if mainbutton.collidepoint((mx, my)):
            if click:
                pygame.mixer.music.stop()
                main_menu(music,sfx)
        pygame.draw.rect(disp, (0, 0, 0), playbutton)
        pygame.draw.rect(disp, (0, 0, 0), mainbutton)
        drawtext('Play Again', font, (255, 255, 255), disp, 75, 665)
        drawtext('Main Menu', font, (255, 255, 255), disp, 485, 665)

        # screen physics
        click = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    main_menu(music,sfx)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        mainclock.tick(fps)

#LOOSE GAME ~~~~~~~~~~~~~~~~
def loose(music,sfx):
    # background music
    pygame.mixer.music.load(os.path.join('my_assets', 'undertale_determination.mp3'))
    pygame.mixer.music.set_volume(music/10)
    pygame.mixer.music.play(-1)

    click = False
    while True:
        disp.blit(looseback, (0, 0))

        # mouse control with interface
        mx, my = pygame.mouse.get_pos()
        trybutton = pygame.Rect(60, 635, 220, 65)
        mainbutton = pygame.Rect(470, 635, 220, 65)
        if trybutton.collidepoint((mx, my)):
            if click:
                pygame.mixer.music.stop()
                main(music,sfx)
        if mainbutton.collidepoint((mx, my)):
            if click:
                pygame.mixer.music.stop()
                main_menu(music,sfx)
        pygame.draw.rect(disp, (255, 192, 203), trybutton)
        pygame.draw.rect(disp, (255, 192, 203), mainbutton)
        drawtext('Try Again?', font, (255, 255, 255), disp, 75, 650)
        drawtext('Main Menu', font, (255, 255, 255), disp, 485, 650)

        # screen physics
        click = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    main_menu(music,sfx)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        mainclock.tick(fps)

#GAME PHYSICS ~~~~~~~~~~~~~~
def main(music,sfx):
    #background music
    pygame.mixer.music.load(os.path.join('my_assets', 'background.mp3'))
    pygame.mixer.music.set_volume(music/10)
    pygame.mixer.music.play(-1)

    #variables
    run = True
    lvl = 0
    live = 5

    player_speed = 6
    boy = Boy(330, 630)

    girls = []
    lvl_len = 5
    girl_speed = 1

    shoot_speed = 4

    lost = False

    #mechanics
    while run:
        mainclock.tick(fps)

        #round mechanism
        if len(girls) == 0:
            lvl += 1
            lvl_len += 4
            for i in range(lvl_len):
                girl = Girls(random.randrange(50,width-100),random.randrange(-1500,-100),random.choice(['y','p','b']))
                girls.append(girl)

        if live <= 0 or boy.sanity <= 0:
            lost = True
        if lost:
            pygame.mixer.music.stop()
            loose(music,sfx)
        if lvl == 6:
            pygame.mixer.music.stop()
            win(music,sfx)

        #taking a hit
        for girl in girls:
            girl.position(girl_speed)
            girl.shoot_position(shoot_speed,boy,sfx)

            if random.randrange(0,2*60)== 1:
                girl.girlshot()

            if collide(girl, boy):
                boy.sanity -= 10
                ugh.play()
                ugh.set_volume(sfx/10)
                ahh.play()
                ahh.set_volume(sfx/10)
                girls.remove(girl)

            elif girl.y + girl.get_height() > height:
                live -= 1
                girls.remove(girl)

        boy.shoot_position(-shoot_speed, girls,sfx)

        #game controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and boy.x - player_speed > 0: #left
            boy.x -= player_speed
        if keys[pygame.K_d] and boy.x + player_speed + boy.get_width() < width: #right
            boy.x += player_speed
        if keys[pygame.K_w] and boy.y - player_speed > 0: #up
            boy.y -= player_speed
        if keys[pygame.K_s] and boy.y + player_speed + boy.get_height() + 15 < height: #down
            boy.y += player_speed
        if keys[pygame.K_SPACE]:
            boy.boyshot(sfx)

        #display
        def redraw_disp():
            disp.blit(background, (0, 0))
            drawtext(f"Level: {lvl}", font, (0, 0, 0), disp, 600, 60)
            drawtext(f"Chance: {live}", font, (0, 0, 0), disp, 25, 60)

            for girl in girls:
                girl.draw(disp)
            boy.draw(disp)

            pygame.display.update()

        redraw_disp()

        #screen physics
        for event in pygame.event.get():
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_ESCAPE:
                 pygame.mixer.music.stop()
                 main_menu(music,sfx)
         if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

main_menu(music,sfx)

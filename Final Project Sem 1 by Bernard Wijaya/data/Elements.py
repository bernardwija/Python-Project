import pygame

import Materials as mtrls

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

#WINDOW ~~~~~~~~~~~~~~
width, height = mtrls.width, mtrls.height

#MATERIALS ~~~~~~~~~~~~~
yellow = mtrls.yellow
pink = mtrls.pink
brown = mtrls.brown
player = mtrls.player

heart = mtrls.heart
senpie = mtrls.senpie

pop = mtrls.pop
ahh = mtrls.ahh
ugh = mtrls.ugh

#GAME ELEMENTS ~~~~~~~~~~~~~~
#shoot collide
def collide(obj1,obj2):
    offsetx = obj2.x - obj1.x
    offsety = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask,(offsetx,offsety))

#Game Elements
#character main
class Characters:

    cd = 30

    def __init__(self, x, y, sanity=100):
        self.x = x
        self.y = y
        self.sanity = sanity
        self.chara_img = None
        self.shoot_img = None
        self.shooters = []
        self.cd_counter = 0

    def draw(self,page):
        page.blit(self.chara_img, (self.x,self.y))
        for bullet in self.shooters:
            bullet.draw(page)

    def get_width(self):
        return self.chara_img.get_width()
    def get_height(self):
        return self.chara_img.get_height()

    #shoot
    def boyshot(self,sfx):
        if self.cd_counter == 0:
            bullet = Shoot(self.x,self.y,self.shoot_img)
            self.shooters.append(bullet)
            self.cd_counter = 1
            pop.play()
            pop.set_volume(sfx/10)
    def cooldown(self):
        if self.cd_counter >= self.cd:
            self.cd_counter = 0
        elif self.cd_counter > 0:
            self.cd_counter +=1
    def shoot_position(self,speed,obj,sfx):
        self.cooldown()
        for bullet in self.shooters:
            bullet.position(speed)
            if bullet.offscreen(height):
                self.shooters.remove(bullet)
            elif bullet.collision(obj):
                obj.sanity -= 10
                ugh.play()
                ugh.set_volume(sfx/10)
                self.shooters.remove(bullet)

#player
class Boy(Characters):
    def __init__(self,x,y,sanity=100):
        super().__init__(x,y,sanity)
        self.chara_img = player
        self.shoot_img = heart
        self.mask = pygame.mask.from_surface(self.chara_img)
        self.max_sanity = sanity

    def shoot_position(self,speed,objs,sfx):
        self.cooldown()
        for bullet in self.shooters:
            bullet.position(speed)
            if bullet.offscreen(height):
                self.shooters.remove(bullet)
            else:
                for obj in objs:
                    if bullet.collision(obj):
                        ahh.play()
                        ahh.set_volume(sfx/10)
                        objs.remove(obj)
                        if bullet in self.shooters:
                            self.shooters.remove(bullet)

    def draw(self,window):
        super().draw(window)
        self.sanitybar(window)

    def sanitybar(self,window):
        pygame.draw.rect(window, (255,0,0), (self.x,self.y + self.chara_img.get_height() + 1, self.chara_img.get_width(), 15))
        pygame.draw.rect(window, (0,255,0), (self.x,self.y + self.chara_img.get_height() + 1, self.chara_img.get_width() * (self.sanity/self.max_sanity), 15))

#enemy
class Girls(Characters):
    girl_clr = {
                'y':(yellow,senpie),
                'p':(pink,senpie),
                'b':(brown,senpie)
                }
    def __init__(self,x,y,clr,sanity=100):
        super().__init__(x,y,sanity)
        self.chara_img,self.shoot_img = self.girl_clr[clr]
        self.mask = pygame.mask.from_surface(self.chara_img)

    def position(self, speed):
        self.y += speed

    def girlshot(self):
        if self.cd_counter == 0:
            bullet = Shoot(self.x-10,self.y+30,self.shoot_img)
            self.shooters.append(bullet)
            self.cd_counter = 1

#shoot
class Shoot:
    def __init__(self,x,y,img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self,page):
        page.blit(self.img,(self.x, self.y))
    def position(self,speed):
        self.y += speed
    def offscreen(self,height):
        return not (self.y <= height and self.y >=0)
    def collision(self,obj):
        return collide(self,obj)



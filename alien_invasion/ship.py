import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        self.screen=screen
        self.ai_settings = ai_settings

        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        # self.bottom = float(self.rect.bottom)


        self.moving_right = False
        self.moving_left = False
        # self.moving_up = False
        # self.moving_dowm = False


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # if self.moving_up and self.rect.right < self.screen_rect.right:
         #    self.bottom -= self.ai_settings.ship_speed_factor
        # if self.moving_dowm and self.rect.bottom > 0:
         #    self.bottom += self.ai_settings.ship_speed_factor


        self.rect.centerx=self.center
        # self.rect.bottom=self.bottom


    def blitme(self):
        self.screen.blit(self.image,self.rect)

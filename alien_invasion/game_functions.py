import sys
import pygame
from bullet import Bullet



# 按键按下
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    #elif event.key == pygame.K_UP:
     #   ship.moving_up = True
    #elif event.key == pygame.K_DOWN:
     #   ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


# 事件检测
def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event, ship)


# 按键松开事件
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    #elif event.key == pygame.K_UP:
     #   ship.moving_up = False
    #elif event.key == pygame.K_DOWN:
     #   ship.moving_down = False


# 重绘屏幕
def update_screen(ai_settings, screen, ship, bullets):
    # 重绘
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


# 刷新子弹
def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

# 开火效果
def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullet_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

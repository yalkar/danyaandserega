import pygame
import random


def x_ch():
    """""
    Prevents egg and brick from spawning together. Returns x coordinate of the brick.
    
    :param x_egg: X coordinate of the egg spawn. Taken from the main part of the code.
    :type x_egg: int.
    :param x_brik: x coordinate of brick spawn. X coordinate of brick respawn. First taken from the main part of the code, and then calculated in this function.
    :type x_brik: int.
    :returns: x_brik.
    :rtype: int.
    """""
    global x_egg, x_brik
    while abs(x_egg - x_brik) < 250:
        x_brik = random.choice(x1)
    else:
        return x_brik


def player_draw():
    """""
    Responsible for character animation.  It displays a picture of the character, depending on the counter value.
    
    :param player_counter: Is a counter. When it reaches the specified value, it is reset.
    :type player_counter: int.
    """""
    ct = 1
    global player_counter
    if player_counter == 2:
        player_counter = 0
    screen.blit(player[player_counter], (x_pl, y_pl))
    if len(player) == 1:
        ct = 0
    else:
        ct = 1
    player_counter += ct


def popadanie(x, y, x_pl, w_pl, y_pl, h_pl):
    """""
    Checks if the character caught a falling object. Returns True if caught, and False if not caught.
    
    :param x: X coordinate of the falling object.
    :type x: int.
    :param y: Y coordinate of the falling object.
    :type y: int.
    :param x_pl: X coordinate of the player.
    :type x_pl: int.
    :param y_pl: Y coordinate of the player.
    :type y_pl: int.
    :param w_pl: Character width.
    :type w_pl: int.
    :param h_pl: Charater Height.
    :type h_pl: int.
    :returns: True or False.
    :rtype: bool.
    """""
    if x in range(x_pl - w_pl, x_pl + w_pl) and y in range(y_pl - h_pl // 2, y_pl + h_pl // 2):
        return True
    else:
        return False


if __name__ == '__main__':
    player_counter = 0
    pygame.init()
    player_walk = [pygame.image.load("Player.png"), pygame.image.load("Player2.png")]
    player_no_walk = pygame.image.load('Player.png')
    player = player_no_walk
    w_pl = player.get_width()
    h_pl = player.get_height()
    screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    w, h = pygame.display.get_surface().get_size()
    pygame.display.set_caption("Kortal Mombat")
    icon = pygame.image.load("Icon.png")
    egg = pygame.image.load('egg.png')
    w_egg = egg.get_width()
    h_egg = egg.get_height()
    brik = pygame.image.load('brik.png')
    w_brik = brik.get_width()
    h_brik = brik.get_height()
    pygame.display.set_icon(icon)
    grass1 = pygame.Surface((1980, 10))
    grass1.fill((0, 102, 0))
    dirt1 = pygame.Surface((1980, 35))
    dirt1.fill((102, 51, 0))
    stone1 = pygame.Surface((1980, 40))
    stone1.fill((96, 96, 96))
    player_anim_count = 0
    myfont = pygame.font.Font("Shrift.otf", 35)
    text_score = myfont.render('SCORE', False, 'Black')
    text_max_score = myfont.render('MAX SCORE', False, 'Black')
    text_health = myfont.render('HEALTH', False, 'Black')
    game = True
    x_pl = w // 2
    y_pl = h - 80 - h_pl
    start_sp_pl = 30
    sp_pl = start_sp_pl
    x1 = list(range(200, (w - 200)))
    y_egg = 55
    start_entity_speed = 10
    speed_entity = start_entity_speed
    x_egg = random.choice(x1)
    x_brik = 0
    y_brik = 55
    start_health = 3
    health = start_health
    max_score = 0
    score = 0
    score1 = myfont.render(str(score), True, 'Black')
    max_score1 = myfont.render(str(max_score), True, 'Black')
    health1 = myfont.render(str(health), True, 'Black')
    loose = myfont.render('LOOSE', False, 'Red')
    score2 = 0
    health_add = 0
    starting = False
    sp_en_test = False
    while game:
        keys = pygame.key.get_pressed()
        pygame.time.delay(100)
        screen.fill((127, 213, 255))
        if not starting:
            speed_entity = 0
            sp_pl = 0
            if keys[pygame.K_r]:
                score2 = 0
                y_egg = 55
                y_brik = 55
                starting = True
                health = start_health
                health1 = myfont.render(str(health), True, 'Black')
                pygame.display.update()

        elif starting:
            if player == player_no_walk:
                screen.blit(player, (x_pl, y_pl))
            elif player == player_walk:
                player_draw()
            if sp_en_test == False:
                speed_entity = start_entity_speed
                sp_en_test = True
            sp_pl = start_sp_pl
            screen.blit(egg, (x_egg, y_egg))
            screen.blit(brik, (x_brik, y_brik))
        if health == 0:
            sp_en_test = False
            speed_entity = 0
            max_score = max(max_score, score)
            max_score1 = myfont.render(str(max_score), True, 'Black')
            score = 0
            score1 = myfont.render(str(score), True, 'Black')
            screen.blit(loose, (w // 2, h // 2))
            starting = False
            if keys[pygame.K_r]:
                score2 = 0
                starting = True
                health = start_health
                health1 = myfont.render(str(health), True, 'Black')
            pygame.display.update()
        screen.blit(grass1, (0, h - 85))
        screen.blit(dirt1, (0, h - 75))
        screen.blit(stone1, (0, h - 40))
        screen.blit(text_score, (20, 5))
        screen.blit(score1, (230, 5))
        screen.blit(text_max_score, (450, 5))
        screen.blit(max_score1, (820, 5))
        screen.blit(text_health, (20, 55))
        screen.blit(health1, (250, 55))
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    game = False
                    pygame.QUIT
        if keys[pygame.K_a]:
            if x_pl > sp_pl:
                player = player_walk
                sp_pl_l = sp_pl
                x_pl -= sp_pl_l
            else:
                sp_pl_l = 0
        if keys[pygame.K_d]:
            if x_pl < w - sp_pl - w_pl:
                player = player_walk
                sp_pl_r = sp_pl
                x_pl += sp_pl_r
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            player = player_no_walk
        if y_egg < h - 85 - h_egg:
            y_brik += speed_entity
            y_egg += speed_entity
            if y_brik >= h - 85 - h_brik:
                y_brik = 55
            if popadanie(x_brik, y_brik, x_pl, w_pl, y_pl, h_pl):
                health -= 1
                health1 = myfont.render(str(health), True, 'Black')
                screen.blit(health1, (250, 55))
                y_brik = 55
                x_brik = random.choice(x1)
                x_ch()
            if popadanie(x_egg, y_egg, x_pl, w_pl, y_pl, h_pl):
                if score % 100 == 0 and score != 0:
                    score += 20
                elif score % 100 != 0 or score == 0:
                    score += 10
                score2 += 10
                if score2 >= 70:
                    speed_entity += 1
                if score2 >= 140:
                    health_add += 1
                    score2 = 0
                    if health_add == 1:
                        health += 1
                        health_add = 0
                        health1 = myfont.render(str(health), True, 'Black')
                        pygame.display.update()
                y_egg = 55
                y_brik = 55
                score1 = myfont.render(str(score), True, 'Black')
                screen.blit(score1, (230, 5))
                x_egg = random.choice(x1)
                x_brik = random.choice(x1)
                x_ch()
        else:
            health -= 1
            health1 = myfont.render(str(health), True, 'Black')
            screen.blit(health1, (250, 55))
            y_egg = 55
            x_egg = random.choice(x1)
            x_brik = random.choice(x1)
            x_ch()
        pygame.display.update()

import pygame
import sys
import pygame.mixer_music
from Scripts.Menu.buttons_class import Button
from configs.screen_config import SIZE, HEIGHT, WIDTH
from configs.btns_config import MENU_WEAPON_BUTTON_DEFINITIONS
from configs.music import MUSIC

def weapon_scene(index):
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Weapon_scene")
    background = pygame.image.load("Assets\_UIMenu\Background.png").convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    buttons = pygame.sprite.Group()
    button_instances = {}
    for btn_def in MENU_WEAPON_BUTTON_DEFINITIONS:
        btn = Button(screen, btn_def["x_pos"], btn_def["y_pos"], btn_def["width"], btn_def["height"], "",btn_def["image"], btn_def["hover_image"])
        buttons.add(btn)
        button_instances[btn_def["name"]] = btn
    running = True
    while running:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:
                if event.button == button_instances["mashinegun"]:
                    index = 0
                elif event.button == button_instances["rocketlauncher"]:
                    index = 1
                elif event.button == button_instances["blaster"]:
                    index = 2
                elif event.button == button_instances["firethrower"]:
                    index = 3
                elif event.button == button_instances["lasergun"]:
                    index = 4
                elif event.button == button_instances["exit"]:
                    print("Exiting weapon scene")
                    running = False
            for btn in button_instances.values():
                btn.handle_event(event)
        mouse_pos = pygame.mouse.get_pos()
        for btn in button_instances.values():
            btn.check_hover(mouse_pos)
        buttons.draw(screen)
        pygame.display.flip()
    return index

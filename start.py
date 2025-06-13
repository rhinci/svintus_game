from scene.Menu import main_menu
from Scripts.Menu.canvas_class import Interface
import pygame as pg
from configs.screen_config import LOGO_DATA,SIZE,WIDTH,HEIGHT
#инициализация основных систем
pg.init()
pg.mixer.init()
screen = pg.display.set_mode(SIZE)
pg.mixer.music.load(LOGO_DATA['music'])
pg.mixer.music.play(-1)
pg.mixer.music.set_volume(1)
#проигрывание анимации логотипа команды
font_size = int(HEIGHT * 0.1)
pixel_font = pg.font.Font("Assets\Alagard-12px-unicode.otf", font_size)
index = 0
ANIMATION_COOLDOWN = 250
update_time = 0
while index < len(LOGO_DATA['anim']):
    text_surface = pixel_font.render("SVINTUS GAME PRODUCTION", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 6))
    screen.blit(text_surface, text_rect)
    screen.blit(pg.transform.scale(pg.image.load(LOGO_DATA['anim'][index]).convert(),LOGO_DATA['size']),(WIDTH/4,HEIGHT/4))
    if pg.time.get_ticks()- update_time > ANIMATION_COOLDOWN:
          update_time = pg.time.get_ticks()
          index+=1
    pg.display.flip()
pg.mixer.music.unload()
#запуск игры
main_menu()

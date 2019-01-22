import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    #Initialize game, settings and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make a ship, bullets and aliens
    ship = Ship(ai_settings,screen)
    alien = Alien(ai_settings,screen)
    bullets = Group()
    aliens = Group()

    #Create the fleet of aliens
    gf.create_fleet(ai_settings,screen,aliens)

    #Start the main loop for the game.
    while True:

        #Watch for events
        gf.check_events(ai_settings,screen,ship,bullets)

        #Update ship and bullets status.
        ship.update()
        gf.update_bullets(bullets)

        #Redraw the screen during each pass through the loop make the most recent drawn screen visible.
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()

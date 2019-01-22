import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #Initialize game, settings and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make a ship.
    ship = Ship(ai_settings,screen)

    #Make a group to store bullets in.
    bullets = Group()

    #Start the main loop for the game.
    while True:

        #Watch for events
        gf.check_events(ai_settings,screen,ship,bullets)

        #Update ship and bullets status.
        ship.update()
        bullets.update()

        #Get rid of bullets that have dissapeared from the screen.
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        

        
        #Redraw the screen during each pass through the loop make the most recent drawn screen visible.
        gf.update_screen(ai_settings,screen,ship, bullets)

run_game()

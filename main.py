from logger import log_state
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Containers
    updatable = pygame.sprite.Group() # Objects that can be updated
    drawable = pygame.sprite.Group()  # Objects that can be drawn
    Player.containers = (updatable, drawable)
    
    # Initialize game
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    delta_time = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # Begin game loop
    while (True):
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        delta_time = clock.tick(60) / 1_000
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        updatable.update(delta_time)
        pygame.display.flip()

if __name__ == "__main__":
    main()

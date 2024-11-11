import pygame
from constants import (SCREEN_HEIGHT, SCREEN_WIDTH)
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys


def main():
    passes, fails = pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteriods = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteriods, updatables, drawables)
    AsteroidField.containers = updatables
    Shot.containers = (shots, updatables, drawables)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0

    while True:
        screen.fill((0, 0, 0))

        for u in updatables:
            u.update(dt)

        for a in asteriods:
            if a.isColliding(player):
                sys.exit("Game over!")

        for d in drawables:
            d.draw(screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

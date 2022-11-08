import pygame
import config
from game import Game


def main():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    clock = pygame.time.Clock()

    Game.init(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        delta_time = calculate_tick()
        Game.main_loop(delta_time)

        screen.fill((0, 0, 0))
        clock.tick(config.FRAME_RATE)


ticks_last_frame = 0
ticks = 0


def calculate_tick() -> float:
    global ticks, ticks_last_frame
    ticks = pygame.time.get_ticks()
    delta_time = (ticks - ticks_last_frame) / 1000.0
    ticks_last_frame = ticks

    return delta_time


if __name__ == '__main__':
    main()

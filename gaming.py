import sys
import pygame
import random


def generate_random_shape():
    shape_type = random.choice(['rect', 'circle'])
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    x = random.randint(50, 950)
    y = random.randint(-20000, 750)

    if shape_type == 'rect':
        width = random.randint(50, 150)
        height = random.randint(50, 150)
        return {'type': 'rect', 'rect': (x, y, width, height), 'color': color}
    elif shape_type == 'circle':
        radius = random.randint(25, 75)
        return {'type': 'circle', 'circle': (x, y, max(radius, 1)), 'color': color}


def main():
    pygame.init()

    WIDTH = 1000
    HEIGHT = 800
    DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

    x = 100
    y = 100
    yv = 0
    ya = 0.1
    xv = 3

    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)

    background_shapes = [generate_random_shape() for _ in range(500)]

    while True:
        DISPLAY.fill(WHITE)

        scroll_offset = max(0, HEIGHT // 2 - y)

        for shape_data in background_shapes:
            shape_type = shape_data['type']
            color = shape_data['color']
            if shape_type == 'rect':
                rect = shape_data['rect']
                adjusted_rect = (rect[0], rect[1] + scroll_offset, rect[2], rect[3])
                pygame.draw.rect(DISPLAY, color, adjusted_rect)
            elif shape_type == 'circle':
                pygame.draw.circle(DISPLAY, color, (shape_data['circle'][0], shape_data['circle'][1] + scroll_offset),
                                   shape_data['circle'][2])

        pygame.draw.rect(DISPLAY, GREEN, (x, y + scroll_offset, 50, 50))

        yv += ya
        y = min(y+yv,HEIGHT)
        x += xv

        if y + 50 >= DISPLAY.get_height():
            yv = 0.65 * -abs(yv)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            yv = -10
        elif keys[pygame.K_s]:
            yv = 40

        if x < 0 or x + 50 > DISPLAY.get_width():
            xv = -xv

        pygame.display.update()
        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()

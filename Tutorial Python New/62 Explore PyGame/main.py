import pygame


"""
- langkah langkah
- init
- user input / database input
- update asset
- render display
"""

# initial pygame
pygame.init()
isRun = True

# membuat window / display surface object
window_lebar = 500
window_panjang = 500
window = pygame.display.set_mode((window_lebar, window_panjang))  # 500 px x 500 px

# posisi
x = 150
y = 150

# size
WIDTH = 20
HEIGHT = 20

speed = 5

# Object game

while isRun:
    pygame.time.delay(10)
    # user input / database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

    # ambil semua keyboard press
    keys = pygame.key.get_pressed()

    # ambil ke kiri
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed

    if keys[pygame.K_RIGHT] and x < window_lebar - WIDTH:
        x += speed

    if keys[pygame.K_UP] and y > 0:
        y -= speed

    if keys[pygame.K_DOWN] and y < window_panjang - HEIGHT:
        y += speed

    # update asset
    window.fill((255, 255, 255))
    pygame.draw.rect(window, (255, 0, 0), (x, y, WIDTH, HEIGHT))

    # render ke display
    pygame.display.update()


pygame.quit()

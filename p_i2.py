import pygame

pygame.init()

win = pygame.display.set_mode((1540, 840))
pygame.display.set_caption("Gra")

x = 200
y = 200
width = 20
heigth = 25
vel = 10

isJump = False
jumpCount = 10

run = True
while run:
	pygame.time.delay(100)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and x > vel:
		x -= vel

	if keys[pygame.K_RIGHT] and x < 1540 - width - vel:
		x += vel

	if not(isJump):

		if keys[pygame.K_UP] and y > vel:
			y -= vel

		if keys[pygame.K_DOWN] and y < 840 - heigth - vel:
			y += vel

		if keys[pygame.K_SPACE]:
			isJump = True
	else:

		if jumpCount >= -10:
			neg = 1
			if jumpCount < 0:
				neg = -1
			y -= (jumpCount ** 2) * 0.5 * neg
			jumpCount -= 1
		else:
			isJump = False
			jumpCount = 10

	win.fill((245, 230, 255))
	pygame.draw.rect(win, (30, 20, 0), (x, y, width, heigth))
	pygame.display.update()

pygame.quit()
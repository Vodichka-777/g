import pygame
mw = pygame.display.set_mode(
    (500, 500)
)
LIGHT_BLUE = (200, 200, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
clock = pygame.time.Clock()
mw.fill(LIGHT_BLUE)

class Area():
    def __init__(self, x, y, widht, height, color):
        self.rect = pygame.Rect(x, y, widht, height)
        self.color = color
    def set_color(self, new_color):
        self.color = new_color
    def fill(self):
        pygame.draw.rect(mw, self.color, self.rect,)
    def outline(self, frame_color, thickness):
        pygame.draw.rect(mw, frame_color, self.rect, thickness)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
    def colliderect(self, rect):
        return self.rect.colliderect(rect.rect)

class Picture(Area):
    def __init__(self, filename, x, y, widht, height, color):
        Area.__init__(self, x, y, widht, height, color)
        self.image  = pygame.transform.scale(pygame.image.load(filename), (widht-10, height-10))

    def draw(self):
        self.fill()
        mw.blit(self.image, (self.rect.x+5, self.rect.y+5))

ball = Picture('png-klev-club-ztnb-p-metallicheskii-shar-png-7.png', 200, 350, 50, 50, LIGHT_BLUE)
platform = Picture('png-klev-club-p-platforma-png-1.png', 200, 450, 100, 30, LIGHT_BLUE)
x, y = 10, 10
x_shift = 25
count = 8
lines = 3
blocks = list()

for j in range(lines):
    for i in range(count):
        block = Picture('Cacodemon.webp', x, y, 55, 55, LIGHT_BLUE)
        x += 60
        blocks.append(block)
    x = 10 
    x+= x_shift
    x_shift+= 25
    y += 60
    count -= 1

dy, dx = 5, 5
move_right = False
move_left = False
while True:
    ball.draw()
    platform.draw()
    for block in blocks:
        block.draw()
        if ball.colliderect(block):
            dy*=-1
            blocks.remove(block)
            block.fill()
        

    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
                move_right = True
        if event.key == pygame.K_LEFT:
            move_left = True
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            move_right = False
        if event.key == pygame.K_LEFT:
                move_left = False



        
    if move_right:
        platform.rect.x += 5
        print(1)
    if move_left:
        platform.rect.x -= 5
        print(2)
    ball.rect.x += dx
    ball.rect.y += dy
    if ball.colliderect(platform):
        dy *= -1
    if ball.rect.x < 0 or ball.rect.x > 450:
        dx *= -1
    if ball.rect.y < 0:
        dy *= -1
        
    pygame.display.update()
    clock.tick(40)
import pygame

screen_width = 800
screen_height = 800

bg = pygame.image.load('asteroids_sprites/game_bg.png')
player_sprite = pygame.image.load('asteroids_sprites/player.png')

asteroid_small = pygame.image.load('asteroids_sprites/asteroid_small.png')
asteroid_med = pygame.image.load('asteroids_sprites/asteroid_med.png')
asteroid_lrg = pygame.image.load('asteroids_sprites/asteroid_lrg.png')

pygame.display.set_caption('Asteroids')
window = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

game_over = False

class Player(object):
    def __init__(self):
        self.img = player_sprite
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.x = screen_width // 2
        self.y = screen_height // 2

    def draw(self, window):
        window.blit(self.img, [self.x, self.y, self.width, self.height])

def redrawGameWindow():
    window.blit(bg, (0,0))
    player.draw(window)
    pygame.display.update()

player = Player()
running = True
while running:
    clock.tick(60)
    if not game_over:
        pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    redrawGameWindow()
pygame.quit()
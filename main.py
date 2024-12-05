import pygame
import math

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

        self.angle = 0
        self.rotated_surf = pygame.transform.rotate(self.img, self.angle)
        self.rotated_rect = self.rotated_surf.get_rect()
        self.rotated_rect.center = (self.x, self.y)

        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cos * self.width // 2, self.y - self.sin * self.height // 2)

    def draw(self, window):
        #window.blit(self.img, [self.x, self.y, self.width, self.height])
        window.blit(self.rotated_surf, self.rotated_rect)

    def turn_left(self):
        self.angle += 5
        self.rotated_surf = pygame.transform.rotate(self.img, self.angle)
        self.rotated_rect = self.rotated_surf.get_rect()
        self.rotated_rect.center = (self.x, self.y)
        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cos * self.width // 2, self.y - self.sin * self.height // 2)

    def turn_right(self):
        self.angle -= 5
        self.rotated_surf = pygame.transform.rotate(self.img, self.angle)
        self.rotated_rect = self.rotated_surf.get_rect()
        self.rotated_rect.center = (self.x, self.y)
        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cos * self.width // 2, self.y - self.sin * self.height // 2)

    def move_forward(self):
        self.x += self.cos * 6
        self.y -= self.sin * 6
        self.rotated_surf = pygame.transform.rotate(self.img, self.angle)
        self.rotated_rect = self.rotated_surf.get_rect()
        self.rotated_rect.center = (self.x, self.y)
        self.cos = math.cos(math.radians(self.angle + 90))
        self.sin = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cos * self.width // 2, self.y - self.sin * self.height // 2)        

class Bullet(object):
    def __init__(self):
        self.point = player.head
        self.x, self.y = self.point
        self.width = 4
        self.height = 4

        self.cos = player.cos
        self.sin = player.sin

        self.x_velocity = self.cos * 10
        self.y_velocity = self.sin * 10

    def move(self):
        self.x += self.x_velocity
        self.y -= self.y_velocity

    def check_offscreen(self):
        if self.x < -50 or self.x > screen_width or self.y > self.height or self.y < -50:
            return True

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), [self.x, self.y, self.width, self.height])
    
def redrawGameWindow():
    window.blit(bg, (0,0))
    player.draw(window)
    
    for bullet in player_bullets:
        bullet.draw(window)

    pygame.display.update()

player = Player()
player_bullets = []

running = True
while running:
    clock.tick(60)
    if not game_over:
        for bullet in player_bullets:
            bullet.move()
            if bullet.check_offscreen():
                player_bullets.pop(player_bullets.index(bullet))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.turn_left()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.turn_right()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player.move_forward()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_over:
                    player_bullets.append(Bullet())

    redrawGameWindow()
pygame.quit()
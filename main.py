import pygame
from pygame import color


class Player:
    def __init__(self, speed, width, height, x, y, skin):
        self.texure = pygame.image.load(skin)
        self.texure = pygame.transform.scale(self.texure, [width, height])
        self.hitbox = self.texure.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed
        self.walk_sound = pygame.mixer.Sound("walking-soundscape-200112.ogg")
        self.walk_sound.play(-1)
        self.walk_sound.set_volume(0)

    def draw(self, window):
        window.blit(self.texure, self.hitbox)

    def move(self):
        keys = pygame.key.get_pressed()
        self.walk_sound.set_volume(0)
        if keys[pygame.K_d]:
            self.hitbox.x += self.speed
            self.walk_sound.set_volume(1)
        if keys[pygame.K_a]:
            self.hitbox.x -= self.speed
            self.walk_sound.set_volume(1)
        if keys[pygame.K_s]:
            self.hitbox.y += self.speed
            self.walk_sound.set_volume(1)
        if keys[pygame.K_w]:
            self.hitbox.y -= self.speed
            self.walk_sound.set_volume(1)

class Wall:
    def __init__(self, width, height, x, y, color):
        self.hitbox = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.hitbox)

class Gold:
    def __init__(self, width, height, x, y, skin):
        self.texure = pygame.image.load(skin)
        self.texure = pygame.transform.scale(self.texure, [width, height])
        self.hitbox = self.texure.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y

    def draw(self, window):
        window.blit(self.texure, self.hitbox)

def win_window(window):
    fps = pygame.time.Clock()
    win_lbl = pygame.font.Font(None, 48).render("Ти переміг!")
    while True:
        window.fill([255, 255, 255])
        window.blit(win_lbl, [200, 200])
        pygame.display.flip()

        fps.tick(60)



pygame.init()
window = pygame.display.set_mode([700, 500])
fps = pygame.time.Clock()
player = Player(5, 50, 50,20, 250, "hero.png")
gold = Gold(50, 50,500, 410, "treasure.png")
background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, [700, 500])
game = True

walls = [
    Wall(100, 20,80, 70, [123,123, 123]),
    Wall(20, 150, 80, 70, [123, 123, 123]),
    Wall(100, 20, 180, 70, [123, 123, 123]),
    Wall(100, 20, 280, 70, [123, 123, 123]),
    Wall(100, 20, 380, 70,[123, 123, 123]),
    Wall(100, 20, 480, 70, [123, 123, 123]),
    Wall(20, 150, 80, 330, [123, 123, 123]),
    Wall(500, 20,80, 470, [123,123, 123]),
    Wall(20, 380, 560, 90, [123, 123, 123]),
    Wall(20, 100, 470, 370, [123, 123, 123]),
    Wall(90, 20, 470, 280, [123, 123, 123]),
    Wall(90, 20, 100, 330, [123, 123, 123]),

]
pygame.mixer.init()
pygame.mixer.music.load("jungles.ogg")
pygame.mixer.music.play(-1)

kick_sound = pygame.mixer.Sound("kick.ogg")
gold_sound = pygame.mixer.Sound("money.ogg")
walk_sound = pygame.mixer.Sound("walking-soundscape-200112.ogg")
while game:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            print(x, y)

    player.move()

    for wall in walls:
        if player.hitbox.colliderect(wall.hitbox):
            kick_sound.play()
            player.hitbox.x = 20
            player.hitbox.y = 250

    if player.hitbox.colliderect(gold.hitbox):
        gold_sound.play()
        player.hitbox.x = 20
        player.hitbox.y = 250





    window.blit(background, [0, 0])
    player.draw(window)
    gold.draw(window)

    for wall in walls:
        wall.draw(window)
    pygame.display.flip()

    fps.tick(60)
import pygame


pygame.init()

WIDTH, HEIGHT = 1200, 700
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ONESHOT")
bg_music = pygame.mixer.Sound("Files/sounds/bg_music.ogg")
bg_music.play(-1)
icon = pygame.image.load("Files/Sprites and pictures/pictures/icon.png")
pygame.display.set_icon(icon)
def load_sprite_images(direction, count):
    images = []
    for i in range(1, count + 1):
        image = pygame.image.load(f'Files/Sprites and pictures/sprites/player_sprite/Niko_looking_{direction}({i}).jpg')
        images.append(image)
    return images



class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 5
        self.direction = "down"

        
        self.moving = False

        self.sprites = {
            "down": load_sprite_images("down", 4),
            "left": load_sprite_images("left", 3),
            "right": load_sprite_images("right", 4),
            "up": load_sprite_images("up", 3)
        }
        self.current_frame = 0
        self.image = self.sprites[self.direction][self.current_frame]
        self.clock = pygame.time.Clock()

    def update(self):
        keys = pygame.key.get_pressed()
        self.moving = False

        if keys[pygame.K_DOWN] and self.y < HEIGHT - 64:
            self.direction = "down"
            self.y += self.velocity
            self.moving = True
        elif keys[pygame.K_UP] and self.y > 0:
            self.direction = "up"
            self.y -= self.velocity
            self.moving = True
        elif keys[pygame.K_LEFT] and self.x > 0:
            self.direction = "left"
            self.x -= self.velocity
            self.moving = True
        elif keys[pygame.K_RIGHT] and self.x < WIDTH - 64:
            self.direction = "right"
            self.x += self.velocity
            self.moving = True

        if self.moving:
            self.current_frame += 0.1
            if self.current_frame >= len(self.sprites[self.direction]):
                self.current_frame = 0
        else:
            self.current_frame = 0

        self.image = self.sprites[self.direction][int(self.current_frame)]

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))




class Lamp:
    def __init__(self) -> None:
        pass

player = Player(WIDTH // 2, HEIGHT // 2)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    window.fill('black')
    player.draw(window)
    player.update()
    pygame.display.update()
    player.clock.tick(60)
pygame.quit()



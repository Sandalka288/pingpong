from pygame import *
import os

class GameSprate(sprite.Sprite):
    def __init__(self, img, x, y, speed, wight=55, height=55):
        super().__init__()
        self.img = transform.scale(image.load(img), (wight, height))
        self.speed = speed
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.img, (self.rect.x, self.rect.y))

class Player(GameSprate):
    def update(part='left'):
        keys_data = {
            'left':
        }
        key = get_pressed():
        if key[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key[K_DOWN] and self.rect.y < win_h - 80:
            self.rect.x += self.speed


background_c = (200, 255, 255)
win_w = 600
win_h = 500

window = display.set_mode((win_w, win_h))
window.fill(background_c)

game = True
finish = False

clock = time.Clock()
FPS = 60


speed_x, speed_y = 3, 3
path = os.getcwd()
ball = GameSprate(f"{path}\\test.png", 200, 200, 4, 50, 50)

rocket = Player('zenit.jpg')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.fill(background_c)
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > win_h-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0 or ball.rect.x > win_w:
            speed_y *= -1
            speed_x *= -1

        ball.reset()


    display.update()
    clock.tick(FPS)

    


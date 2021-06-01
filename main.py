import sys
import pygame

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Script typeface', 35)


screen = pygame.display.set_mode((751, 500))
backround = pygame.image.load("C:/Users/kyria/Desktop/control_servo_via_air_condition/155.jpg")
#  i have to convert from jpg to bmp
ball = pygame.image.load('C:/Users/kyria/Desktop/control_servo_via_air_condition/ball3.png')
x, y = 304, 436

pygame.display.set_caption("Kiriakos game")

velocity_for_y = 0
velocity_x = 0
gravity_for_x = 0
gravity_for_y = -0.5
score = 0
a= 0
direction = 'None'


def touch_the_ground_or_the_sky(y_position):
    if y_position > 436:
        y_position = 436
    elif y_position < 0:
        y_position = 0

    return y_position


while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_y_position = pygame.mouse.get_pos()[1]
            mouse_x_position = pygame.mouse.get_pos()[0]
            if mouse_y_position < (y + 64) and mouse_y_position > y and  mouse_x_position > x and mouse_x_position < (x + 64):
                velocity_for_y = 16
                score += 1
                if mouse_x_position > (x - 32) and mouse_x_position < (x + 32):
                    gravity_for_x = 1
                    a = 0.2
                    direction = 'Right'
                elif mouse_x_position < (x + 64) and mouse_x_position > (x + 32):
                    gravity_for_x = -1
                    a = -0.2

    score_font = my_font.render(f"Your Score:{str(score)}", False, (245, 245, 245))
    screen.blit(score_font, (580, 25))

    y -= velocity_for_y  # changing the position of y
    velocity_for_y = velocity_for_y + gravity_for_y
    y = touch_the_ground_or_the_sky(y)
    if y == 436:
        score = 0

    x += velocity_x
    velocity_x = velocity_x + gravity_for_x
    gravity_for_x = gravity_for_x - a
    if gravity_for_x == -1:
        velocity_x = 0
        gravity_for_x = 0
        a = 0
    elif gravity_for_x == 1:
        velocity_x = 0
        gravity_for_x = 0
        a = 0

    if x < 0:
        gravity_for_x = 1
        a = 0.2
        print('hey')
    elif x > 687:
        gravity_for_x = -1
        a = -0.2
        print('hey')

    screen.blit(ball, (int(x), int(y)))
    pygame.display.update()
    screen.blit(backround, (0, 0))











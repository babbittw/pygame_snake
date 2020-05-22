# import the pygame module, so you can use it
import pygame

from data.Snake import *
from data.Tile import *
from data.GLOBALS import *



import random

def replace_apple(snake, apple):

    while True:
        x = random.randint(0, SCREEN_SIZE_TILES - 1)
        y = random.randint(0, SCREEN_SIZE_TILES - 1)

        valid = True
        n = snake.snake.start_node
        while n is not None:
            if n.data.location[0] == x and n.data.location[1] == y:
                valid = False
                break
            n = n.next
        if valid:
            break

    x *= TILE_SIZE
    y *= TILE_SIZE

    new_location = (x, y)
    apple.move(new_location)


# define a main function
def main():
    # initialize the pygame module
    pygame.mixer.pre_init(44100, -16, 1, 512)
    #pygame.mixer.pre_init(frequency=44100)
    pygame.init()
    #pygame.mixer.init(frequency=44100)
    #pygame.mixer.init(44100, -16, 1, 512)
    # load and set the logo
    #logo = pygame.image.load("C:/Users/wbabbitt/PycharmProjects/Pycharm_HelloWorld/data/snake_logo.png")
    logo = pygame.image.load("data/snake_logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Snake")

    #apple_crunch = pygame.mixer.Sound('C:/Users/wbabbitt/PycharmProjects/Pycharm_HelloWorld/data/sounds/apple_crunch.wav')
    #game_over = pygame.mixer.Sound('C:/Users/wbabbitt/PycharmProjects/Pycharm_HelloWorld/data/sounds/game_over.wav')

    apple_crunch = pygame.mixer.Sound('data/sounds/apple_crunch.wav')
    game_over = pygame.mixer.Sound('data/sounds/game_over.wav')

    # boop = pygame.mixer.Sound('data/sounds/boop.wav')

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((SCREEN_SIZE_PIXELS, SCREEN_SIZE_PIXELS))
    random.seed(1)
    # define a variable to control the main loop
    running = True

    direction = ''

    apple = Tile(screen, (255, 0, 0), (60,60))
    snake = Snake(screen)
    # main loop
    while running:
        pygame.time.delay(DELAY)
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        keys = pygame.key.get_pressed()

        #movement
        if keys[pygame.K_LEFT] and direction != 'r':
            #boop.play()
            direction = 'l'
        if keys[pygame.K_RIGHT] and direction != 'l':
            #boop.play()
            direction = 'r'
        if keys[pygame.K_UP] and direction != 'd':
            #boop.play()
            direction = 'u'
        if keys[pygame.K_DOWN] and direction != 'u':
            #boop.play()
            direction = 'd'

        if direction != '':
            snake.move(direction, TILE_SIZE)

        # Edge Check
        if snake.out_of_bounds() or snake.collision():
            if direction != '':
                game_over.play()
            direction = ''
            snake.reset()


        if  snake.get_head_tile().get_tile_cords() == apple.get_tile_cords():
            apple_crunch.play()
            snake.grow(direction)
            replace_apple(snake, apple)

        screen.fill((0, 0, 0))
        apple.draw()
        snake.draw()
        pygame.display.update()





        #Edge check
        # if snake.head_x < 0 or snake.head_y < 0 or snake.head_x > 580 or snake.head_y > 580:
        #     snake.head_x = 300
        #     snake.head_y = 300
        #     direction = ''








        #draw snake


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()



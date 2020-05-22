import pygame
from data.Tile import *
from data.GLOBALS import *

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class List:

    def __init__(self):
        self.start_node = None
        self.size = 0

    def push_front(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            new_node = Node(data)
            new_node.next = self.start_node
            self.start_node.prev = new_node
            self.start_node = new_node

        self.size += 1

    def push_back(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            n = self.start_node
            while n.next is not None:
                n = n.next

            new_node = Node(data)
            n.next = new_node
            new_node.prev = n

        self.size += 1

    def pop_front(self):
        if self.start_node is None:
           return
        if self.start_node.next is None:
            self.start_node = None
            self.size -= 1
            return
        self.start_node = self.start_node.next
        self.start_node.prev = None
        self.size -= 1

class Snake:

    def __init__(self, screen):
        self.screen = screen
        self.width = 20
        self.height = 20
        self.snake = List()

        if STARTING_LENGTH % 2:
            self.c_to_add = False
            head_tile = Tile(self.screen, SNAKE_COLOR1, (START_X, START_Y))
            self.snake.push_front(head_tile)
        else:
            self.c_to_add = True
            head_tile = Tile(self.screen, SNAKE_COLOR2, (START_X, START_Y))
            self.snake.push_front(head_tile)



        for i in range(STARTING_LENGTH - 1):
            self.grow('r')

    def out_of_bounds(self):
        n = self.snake.start_node
        while n is not None:
            if n.data.location[0] >= SCREEN_SIZE_PIXELS or n.data.location[1] >= SCREEN_SIZE_PIXELS \
                    or n.data.location[0] < 0 or n.data.location[1] < 0:
                return True
            n = n.next
        return False

    def collision(self):
        head = self.snake.start_node
        n = head.next
        while n is not None:
            if head.data.location[0] == n.data.location[0] and head.data.location[1] == n.data.location[1]:
                return True
            n = n.next
        return False


    def move(self, direction, vel):

        n = self.snake.start_node

        new_location = n.data.location
        old_location = new_location  # old n value, where 2nd will go

        if direction == 'l':
            new_location = (new_location[0] - vel, new_location[1])
        elif direction == 'r':
            new_location = (new_location[0] + vel, new_location[1])
        elif direction == 'u':
            new_location = (new_location[0], new_location[1] - vel)
        elif direction == 'd':
            new_location = (new_location[0], new_location[1] + vel)


        n.data.move(new_location)

        while n.next is not None:
            n = n.next
            new_location = old_location
            old_location = n.data.location
            n.data.move(new_location)


    def reset(self):
        while self.snake.size != 0:
            self.snake.pop_front()

        #Once we remove all the elements we need to add some back and reset the location of it

        if STARTING_LENGTH % 2:
            self.c_to_add = False
            head_tile = Tile(self.screen, SNAKE_COLOR1, (START_X, START_Y))
            self.snake.push_front(head_tile)
        else:
            self.c_to_add = True
            head_tile = Tile(self.screen, SNAKE_COLOR2, (START_X, START_Y))
            self.snake.push_front(head_tile)



        for i in range(STARTING_LENGTH - 1):
            self.grow('r')


    def draw(self):
        #pygame.draw.rect(self.screen, self.color, (self.head_x, self.head_y, self.width, self.height))
        #Traverse list and for every node data.draw()

        n = self.snake.start_node
        while n is not None:
            n.data.draw()
            n = n.next

    def get_head_tile(self):
        return self.snake.start_node.data

    def grow(self, direction):
        # for i in range(APPLE_GROWTH):
        #     if self.c_to_add:
        #         self.snake.push_back(Tile(self.screen, SNAKE_COLOR1, (self.snake.start_node.data.location[0], self.snake.start_node.data.location[1])))
        #         self.c_to_add = False
        #     else:
        #         self.snake.push_back(Tile(self.screen, SNAKE_COLOR2, (self.snake.start_node.data.location[0], self.snake.start_node.data.location[1])))
        #         self.c_to_add = True

        new_location = self.snake.start_node.data.location

        if direction == 'l':
            new_location = new_location[0] + TILE_SIZE, new_location[1]
        elif direction == 'r':
            new_location = new_location[0] - TILE_SIZE, new_location[1]
        elif direction == 'u':
            new_location = new_location[0], new_location[1] + TILE_SIZE
        elif direction == 'd':
            new_location = new_location[0], new_location[1] - TILE_SIZE

        new_location = self.snake.start_node.data.location

        for i in range(APPLE_GROWTH):
            if self.c_to_add:
                self.snake.push_back(Tile(self.screen, SNAKE_COLOR1, new_location))
                self.c_to_add = False
            else:
                self.snake.push_back(Tile(self.screen, SNAKE_COLOR2, new_location))
                self.c_to_add = True

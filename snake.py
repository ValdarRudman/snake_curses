# SNAKE
import random
import curses
from curses import wrapper

def main(screen):
    curses.curs_set(0)

    screen_height, screen_width = screen.getmaxyx()

    window = curses.newwin(screen_height, screen_width, 0, 0)
    window.timeout(100)
    window.keypad(1)

    snake_x = screen_width / 2
    snake_y = screen_height / 2
    snake = [
        [snake_x, snake_y],
        [snake_x, snake_y - 1],
        [snake_x, snake_y - 2],
    ]
    window.addch(int(snake[0][1]), int(snake[0][0]), curses.ACS_CKBOARD)

    food = [screen_width / 4, screen_height / 2]
    window.addch(int(food[1]), int(food[0]), curses.ACS_PI)

    key = curses.KEY_RIGHT
    past_key = curses.KEY_LEFT
    while True:
        next_key = window.getch()
        key = key if next_key == -1 else next_key

        if key == past_key and past_key == curses.KEY_LEFT:
            key = curses.KEY_RIGHT
        if key == past_key and past_key == curses.KEY_RIGHT:
            key = curses.KEY_LEFT
        if key == past_key and past_key == curses.KEY_UP:
            key = curses.KEY_DOWN
        if key == past_key and past_key == curses.KEY_DOWN:
            key = curses.KEY_UP
        
        if snake[0][0] in [0, screen_width] or snake[0][1] in [0, screen_height] or snake[0] in snake[1:]:
            curses.endwin()
            quit()

        head = [snake[0][0], snake[0][1]]

        # TODO: check does not change to direction it is moving from
        if key == curses.KEY_LEFT:
            head[0] -= 1
            past_key = curses.KEY_RIGHT
        if key == curses.KEY_RIGHT:
            head[0] += 1
            past_key = curses.KEY_LEFT
        if key == curses.KEY_UP:
            head[1] -= 1
            past_key = curses.KEY_DOWN
        if key == curses.KEY_DOWN:
            head[1] += 1
            past_key = curses.KEY_UP
        
        snake.insert(0, head)

        if snake[0] == food:
            food = None

            while food is None:
                new_food = [
                    random.randint(1, screen_width - 1), 
                    random.randint(1, screen_height - 1)
                ]

                food = new_food if new_food not in snake else None

            window.addch(food[1], food[0], curses.ACS_PI)

        else:
            tail = snake.pop()
            window.addch(int(tail[1]), int(tail[0]), ' ')

        window.addch(int(snake[0][1]), int(snake[0][0]), curses.ACS_CKBOARD)

wrapper(main)
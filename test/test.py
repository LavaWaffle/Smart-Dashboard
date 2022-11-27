
import os, sys
sys.path.insert(0, os.path.abspath(""))
from src.dashboard import SmartDashboard
from concurrent.futures import ThreadPoolExecutor
import pygame
pygame.init()

dashboard = SmartDashboard()

def main():
    WIN_WIDTH = 500
    WIN_HEIGHT = 500

    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption('Test Environment')
    x = 50
    y = 50
    width = 50
    height = 50
    vel = 5
    isTopHalf = True
    fourCourners = 'topLeft'
    run = True
    # pygame clock 30 fps
    clock = pygame.time.Clock()


    while run:
        SmartDashboard.putNumber("x",x)
        SmartDashboard.putNumber("y",y)
        SmartDashboard.putBoolean("isTopHalf",isTopHalf)
        SmartDashboard.putString("fourCourners",fourCourners)
        # SmartDashboard.test()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x > vel:
            x -= vel
        if keys[pygame.K_RIGHT] and x < WIN_WIDTH - width - vel:
            x += vel
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < WIN_HEIGHT - height - vel:
            y += vel

        # check if player is in top half of screen
        if y < WIN_HEIGHT / 2:
            isTopHalf = True
        else:
            isTopHalf = False

        # check if player is in top left corner
        if x < WIN_WIDTH / 2 and y < WIN_HEIGHT / 2:
            fourCourners = 'topLeft'
        # check if player is in top right corner
        elif x > WIN_WIDTH / 2 and y < WIN_HEIGHT / 2:
            fourCourners = 'topRight'
        # check if player is in bottom left corner
        elif x < WIN_WIDTH / 2 and y > WIN_HEIGHT / 2:
            fourCourners = 'bottomLeft'
        # check if player is in bottom right corner
        elif x > WIN_WIDTH / 2 and y > WIN_HEIGHT / 2:
            fourCourners = 'bottomRight'

        win.fill((102, 102, 102))
        pygame.draw.rect(win, (90, 200, 255), (x, y, width, height))
        pygame.display.update()


    SmartDashboard.kill()

def run_io_tasks_in_parallel(tasks):
    with ThreadPoolExecutor() as executor:
        running_tasks = [executor.submit(task) for task in tasks]
        for running_task in running_tasks:
            running_task.result()

if __name__ == "__main__":
    run_io_tasks_in_parallel([main, dashboard.run, dashboard.update])
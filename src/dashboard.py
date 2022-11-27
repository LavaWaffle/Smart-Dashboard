from typing import List, Union, Type
import time
import os, sys
# from SmarthDashboard.src.dTypes.Number import Number
from src.dTypes.Number import Number
from src.dTypes.Boolean import Boolean
from src.dTypes.String import String

def toString(x):
    return x.get()

class SmartDashboard:
    dashboardItems: List[Union[Type[Boolean], Type[Number]]] = []

    @staticmethod
    def putNumber(key: str, value: int):
        """
        Add a number to the dashboard
        :param key: The key to use
        :param value: The value to use
        """
        SmartDashboard.__putNumber(key,value)

    @staticmethod
    def putNumber(key: str, value: float):
        """
        Add a number to the dashboard
        :param key: The key to use
        :param value: The value to use
        """
        SmartDashboard.__putNumber(key,value)

    @staticmethod
    def __putNumber(key:str,value):
        # check if the key already exists
        if (x:=SmartDashboard.__findItem(key)) is not False:
            x.set(value)
            return
        # if it doesn't, add it
        SmartDashboard.dashboardItems.append(
            Number(key,value)
        )

    @staticmethod
    def putBoolean(key: str, value: bool):
        """
        Add a boolean to the dashboard
        :param key: The key to use
        :param value: The value to use
        """
        # check if the key already exists
        if (x:=SmartDashboard.__findItem(key)) is not False:
            x.set(value)
            return
        # if it doesn't, add it
        SmartDashboard.dashboardItems.append(
            Boolean(key,value)
        )

    @staticmethod
    def putString(key: str, value: str):
        """
        Add a string to the dashboard
        :param key: The key to use
        :param value: The value to use
        """
        # check if the key already exists
        if (x:=SmartDashboard.__findItem(key)) is not False:
            x.set(value)
            return
        # if it doesn't, add it
        SmartDashboard.dashboardItems.append(
            String(key,value)
        )

    @staticmethod
    def __findItem(key: str):
        """
        Check if a key exists
        :param key: The key to check
        :return: True if it exists, False if it doesn't
        """
        for item in SmartDashboard.dashboardItems:
            if item.key == key:
                # if it does, return it
                return item
        return False

    @staticmethod
    def run():
        while True:
            time.sleep(1)
            SmartDashboard.test()

    @staticmethod
    def test():
        print(list(map(toString,SmartDashboard.dashboardItems)))

    @staticmethod
    def kill():
        os.exit(0)
        os.exit(1)
        exit()
        sys.exit()


    



# import pygame
# pygame.init()

# WIN_WIDTH = 500
# WIN_HEIGHT = 500

# screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.RESIZABLE)
# pygame.display.set_caption('Smart Dashboard')

# def draw_window():
#     screen.fill((102, 102, 102))
#     pygame.display.update()

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.VIDEORESIZE:
#             screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
#     draw_window()

# pygame.quit()

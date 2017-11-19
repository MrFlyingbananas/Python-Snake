import threading
import pygame

class Game(object):
    def __init__(self, update_loop, draw_loop, width=600, height=800):
        pygame.init()
        self._screen = pygame.display.set_mode((width, height))
        self._surfaces = []
        self._draw_thread = threading.Thread(target=draw_loop, name='Draw')
        self._update_thread = threading.Thread(target=update_loop, name='Update')
    def load_image(self, path):
        return pygame.image.load(path)
    def draw_rect(self, loc):
        pass
    def loop(self):
        while 1:
            for event in pygame.event.get():
                pass

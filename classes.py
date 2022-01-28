import pygame

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Label:
    def __init__(self, position, text='', centered=True):
        self.position = position
        self.text = text
        self.centered = centered
    
    def draw(self, surface, text=''): 
        if text != '':
            font = pygame.font.SysFont('SegoeUI', 20)
            text = font.render(text, 1, (0,0,0))
            if self.centered:
                surface.blit(text, (self.position.x-text.get_width()/2, self.position.y-text.get_height()/2))
            else:
                surface.blit(text, (self.position.x, self.position.y))
                surface.blit(text, (self.position.x, self.position.y))
class Level:
    def __init__(self, width, height, tile_size):
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.grid = []
        self.playing = False

level = Level(25,25,30)
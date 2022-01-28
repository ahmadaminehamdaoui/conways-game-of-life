from tkinter import Grid
import pygame, sys, ctypes
from classes import *
user32 = ctypes.windll.user32
width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# setup
pygame.init()
pygame.display.init()
pygame.display.set_caption('Level Editor')
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

# level
future_grid = []

line = []
for y in range(level.height):
    for x in range(level.width):
        line.append(0)
    level.grid.append(line)
    line = []

# ui
clicking = {'left':0,'right':0}
labels = []
display = {'fps':False}

# functions
def update_cell(x, y):
    global future_grid
    counter = 0
    try:
        if level.grid[y+1][x]==1: counter+=1 
    except:pass
    try:
        if level.grid[y-1][x]==1: counter+=1
    except:pass
    try:
        if level.grid[y][x+1]==1: counter+=1
    except:pass
    try:
        if level.grid[y][x-1]==1: counter+=1
    except:pass
    try:
        if level.grid[y+1][x+1]==1: counter+=1
    except:pass
    try:
        if level.grid[y+1][x-1]==1: counter+=1
    except:pass
    try: 
        if level.grid[y+1][x-1]==1: counter+=1
    except:pass
    try:
        if level.grid[y+1][x+1]==1: counter+=1
    except:pass

    if counter==2 or counter == 3:
        future_grid[y][x] = 1

while True:
    # --- frame refresh
    screen.fill((0,0,0))
    current_fps = round(clock.get_fps())
    mouse = pygame.mouse.get_pos()

    labels = []

    future_grid = []
    line = []
    for y in range(level.height):
        for x in range(level.width):
            line.append(0)
    future_grid.append(line)
    line = []

    # --- game
    origin = [int(width/2-(level.tile_size*level.width)/2), int(height/2-(level.tile_size*level.height)/2)]
    if clicking['left'] or clicking['right']:
        print(int((mouse[1]-origin[1])*level.tile_size))
        level.grid[int((mouse[1]-origin[1])//level.tile_size)][int((mouse[0]-origin[0])//level.tile_size)] = 1 if clicking['left'] else 0
    
    for y in range(level.height):
        for x in range(level.width):
            update_cell(x,y)

    # --- events handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: clicking['left'] = True
            elif event.button == 3: clicking['right'] = True

        elif event.type == pygame.MOUSEBUTTONUP:
            clicking = {'left':0,'right':0}

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                display['fps'] = not display['fps']
            elif event.key == pygame.K_RETURN:
                level.playing = not level.playing
    
    # --- ui
    if display['fps']:
        labels.append(Label(Vec2(origin[0]+10, origin[1]+10), 'FPS: '+str(current_fps), centered = False))

    # --- drawing
    # map
    for y in range(level.height):
        for x in range(level.width):
            color = (255,255,255) if level.grid[y][x]==0 else (0,0,0)
            pygame.draw.rect(screen, color, pygame.Rect(origin[0]+x*level.tile_size, origin[1]+y*level.tile_size, level.tile_size, level.tile_size))
    # mouse overlay
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(origin[0]+int((mouse[0]-origin[0])//level.tile_size*level.tile_size), origin[1]+int((mouse[1]-origin[1])//level.tile_size*level.tile_size), level.tile_size, level.tile_size),1)
    # ui
    for label in labels:
        label.draw(screen, label.text)
  
    # --- update
    pygame.display.update()
    clock.tick(60)
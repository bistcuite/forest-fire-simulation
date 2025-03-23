import pygame
import numpy as np

N = 50  
CELL_SIZE = 10  
p = 0.8
FPS = 10  

EMPTY = (0, 0, 0)
TREE = (34, 139, 34)
FIRE = (255, 69, 0) 

def initialize_forest(N, tree_density=0.6):
    forest = np.random.choice([0, 1], size=(N, N), p=[1-tree_density, tree_density])
    return forest

def spread_fire(forest):
    new_forest = forest.copy()
    for i in range(N):
        for j in range(N):
            if forest[i, j] == 2:  
                new_forest[i, j] = 0  
            elif forest[i, j] == 1:  
                neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                for ni, nj in neighbors:
                    if 0 <= ni < N and 0 <= nj < N and forest[ni, nj] == 2:
                        if np.random.rand() < p:
                            new_forest[i, j] = 2
                            break
    return new_forest

pygame.init()
screen = pygame.display.set_mode((N * CELL_SIZE, N * CELL_SIZE))
clock = pygame.time.Clock()
forest = initialize_forest(N)
running = True

while running:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  
            x, y = pygame.mouse.get_pos()
            i, j = y // CELL_SIZE, x // CELL_SIZE
            if forest[i, j] == 1:
                forest[i, j] = 2
    
    forest = spread_fire(forest)    
    for i in range(N):
        for j in range(N):
            color = EMPTY if forest[i, j] == 0 else TREE if forest[i, j] == 1 else FIRE
            pygame.draw.rect(screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()

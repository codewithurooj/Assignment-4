import pygame
import time

# Constants for the canvas and cell sizes
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(grid, eraser_rect, screen):
    """Erase objects that the eraser comes in contact with."""
    for rect in grid[:]:
        if eraser_rect.colliderect(rect):
            pygame.draw.rect(screen, (255, 255, 255), rect)  # Change to white
            grid.remove(rect)

def main():
    # Initialize pygame
    pygame.init()

    # Create the canvas
    screen = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
    pygame.display.set_caption("Eraser Simulation")
    screen.fill((255, 255, 255))  # Fill the background with white

    # Create a grid of blue cells
    grid = []
    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
        for col in range(0, CANVAS_WIDTH, CELL_SIZE):
            rect = pygame.Rect(col, row, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (0, 0, 255), rect)  # Draw blue rectangle
            grid.append(rect)

    # Create the eraser rectangle
    eraser_rect = pygame.Rect(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, ERASER_SIZE, ERASER_SIZE)
    
    running = True
    clock = pygame.time.Clock()

    # Game loop
    while running:
        screen.fill((255, 255, 255))  # Clear screen
        for rect in grid:
            pygame.draw.rect(screen, (0, 0, 255), rect)  # Re-draw remaining cells

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Get mouse position and update eraser position
        mouse_x, mouse_y = pygame.mouse.get_pos()
        eraser_rect.topleft = (mouse_x, mouse_y)

        # Erase overlapping objects
        erase_objects(grid, eraser_rect, screen)

        # Draw the eraser
        pygame.draw.rect(screen, (255, 182, 193), eraser_rect)  # Pink eraser

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()

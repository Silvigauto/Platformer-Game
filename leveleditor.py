import pygame
import json

# ---------------- CONFIG ----------------
TILE_SIZE = 50
ROWS = 15
COLS = 30
SCREEN_WIDTH = COLS * TILE_SIZE
SCREEN_HEIGHT = ROWS * TILE_SIZE + 60
FPS = 60

# IDs de tiles
# 0 = vacío
# 1 = piedra violeta
# 2 = piedra gris
# 3 = lava
# 4 = enemigo
# 5 = salida
# 6 = moneda
TILE_COLORS = {
    0: (30, 30, 30),      # vacío
    1: (160, 100, 200),  # piedra violeta
    2: (130, 130, 130),  # piedra gris
    3: (200, 60, 60),    # lava
    4: (180, 50, 50),    # enemigo
    5: (60, 200, 60),    # salida
    6: (240, 200, 0),    # moneda
}

TILE_KEYS = {
    pygame.K_0: 0,
    pygame.K_1: 1,
    pygame.K_2: 2,
    pygame.K_3: 3,
    pygame.K_4: 4,
    pygame.K_5: 5,
    pygame.K_6: 6,
}

# ---------------- INIT ----------------
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Editor de Niveles")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 22)

# Matriz del nivel
level = [[0 for _ in range(COLS)] for _ in range(ROWS)]
current_tile = 1

# ---------------- HELPERS ----------------
def draw_grid():
    for r in range(ROWS):
        for c in range(COLS):
            tile_id = level[r][c]
            color = TILE_COLORS.get(tile_id, (255, 0, 255))
            rect = pygame.Rect(c*TILE_SIZE, r*TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (80, 80, 80), rect, 1)


def draw_ui():
    ui_rect = pygame.Rect(0, ROWS*TILE_SIZE, SCREEN_WIDTH, 60)
    pygame.draw.rect(screen, (20, 20, 20), ui_rect)
    txt = f"Tile actual: {current_tile} | Click izq: pintar | Click der: borrar | Teclas 0-6 | S: guardar JSON"
    screen.blit(font.render(txt, True, (220, 220, 220)), (10, ROWS*TILE_SIZE + 20))


def save_level(path="level1.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(level, f, indent=4)
    print(f"Nivel guardado en {path}")

# ---------------- LOOP ----------------
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key in TILE_KEYS:
                current_tile = TILE_KEYS[event.key]
            if event.key == pygame.K_s:
                save_level()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if my < ROWS * TILE_SIZE:
                r = my // TILE_SIZE
                c = mx // TILE_SIZE
                if event.button == 1:  # pintar
                    level[r][c] = current_tile
                if event.button == 3:  # borrar
                    level[r][c] = 0

    screen.fill((0, 0, 0))
    draw_grid()
    draw_ui()
    pygame.display.flip()

pygame.quit()

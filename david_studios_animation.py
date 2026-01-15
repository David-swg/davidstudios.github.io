# david_studios_animation.py
import pygame
import random
import sys

# --------------------------
# CONFIGURATION
# --------------------------
WIDTH, HEIGHT = 800, 600
FONT_SIZE = 32
TEXT = "DAVID STUDIOS"
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
FPS = 60

# --------------------------
# INITIALISATION PYGAME
# --------------------------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("David Studios Animation")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Courier", FONT_SIZE, bold=True)

# Couleurs
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 150, 0)

# --------------------------
# CLASSES
# --------------------------
class Symbol:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(5, 15)
        self.char = random.choice(SYMBOLS)
    
    def fall(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = random.randint(-50, 0)
            self.char = random.choice(SYMBOLS)
    
    def draw(self):
        symbol_surface = font.render(self.char, True, GREEN)
        screen.blit(symbol_surface, (self.x, self.y))

# Générer des symboles aléatoires
symbols = [Symbol(random.randint(0, WIDTH), random.randint(-HEIGHT, 0)) for _ in range(200)]

# --------------------------
# BOUCLE PRINCIPALE
# --------------------------
def main():
    glitch_timer = 0
    glitch_text = TEXT
    while True:
        screen.fill(BLACK)
        
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Dessiner les symboles
        for symbol in symbols:
            symbol.fall()
            symbol.draw()
        
        # Texte principal avec effet glitch
        glitch_timer += 1
        display_text = glitch_text
        if glitch_timer % 20 == 0:
            # Change aléatoirement une lettre pour l'effet glitch
            display_text = "".join(random.choice(SYMBOLS) if random.random() > 0.7 else c for c in TEXT)
        text_surface = font.render(display_text, True, GREEN)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text_surface, text_rect)
        
        pygame.display.flip()
        clock.tick(FPS)

# --------------------------
# LANCER L'ANIMATION
# --------------------------
if __name__ == "__main__":
    main()



import pygame

# Initialize Pygame
pygame.init()

# Define screen size
screen = pygame.display.set_mode((800, 600))

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define fonts
font = pygame.font.Font(None, 36)

# Load ectoplasm image
ectoplasm_image = pygame.image.load('ectoplasm.png') # do i need .convert()
ectoplasm_image = pygame.transform.scale(ectoplasm_image, (50, 50))

# Player class to hold player stats
class Player:
    def __init__(self, health, coins):
        self.health = health
        self.coins = coins

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)  # The health can't drop below 0

    def add_coin(self, amount):
        self.coins = min(10, self.coins + amount)  # The max coins is 10

# UI class to handle drawing the elements on the screen
class GameUI:
    def __init__(self, player):
        self.player = player

    def draw_health_bar(self, surface, x, y):
        max_health = 100
        bar_width = 200
        bar_height = 20

        # Health bar background
        pygame.draw.rect(surface, RED, (x, y, bar_width, bar_height))

        # Health bar foreground (based on current health)
        current_health_width = (self.player.health / max_health) * bar_width
        pygame.draw.rect(surface, GREEN, (x, y, current_health_width, bar_height))

    def draw_coin_counter(self, surface, x, y):
        text = font.render(f"Coins: {self.player.coins}/10", True, WHITE)
        surface.blit(text, (x, y))

    def draw_ectoplasm(self, surface, x, y):
        surface.blit(ectoplasm_image, (x, y))

# Create a Player object
player = Player(health=100, coins=5)

# Create a GameUI object, passing the player to it
game_ui = GameUI(player)

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))  # Fill background with black

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the UI elements in a horizontal line
    y_position = 50  # Keep the same Y position for all elements

    # Starting X positions for the elements
    x_health_bar = 50
    x_coin_counter = x_health_bar + 300  # Adjust spacing after health bar
    x_ectoplasm = x_coin_counter + 300  # Adjust spacing after coin counter

    # Draw the health bar
    game_ui.draw_health_bar(screen, x_health_bar, y_position)

    # Draw the coin counter
    game_ui.draw_coin_counter(screen, x_coin_counter, y_position)

    # Draw the ectoplasm image
    game_ui.draw_ectoplasm(screen, x_ectoplasm, y_position)

    # Update player stats (simulate health dropping and coins increasing)
    player.take_damage(0.1)
    player.add_coin(0.01)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()


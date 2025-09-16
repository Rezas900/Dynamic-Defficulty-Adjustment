from .config import *

# Auxiliary functions for the game

def display_score(screen, font, score):
    """A fuction for show score on the screen"""
    score_text = font.render(f"Score: {int(score)}", True, BLACK)
    screen.blit(score_text, (10, 10))


# def game_over_screen(screen, font):
#     """game over screen display function"""
#     game_over_text = self.title_font.render("Game Over", True, BLACK)
#     restart_text = self.button_font.render("Press SPACE to Restart", True, BLACK)
#     final_score_text = self.score_font.render(f"Your Score: {int(self.score)}", True, BLACK) 
#     game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50))
#     restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50))
#     final_score_rect = final_score_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100))
#     self.screen.blit(game_over_text, game_over_rect)
#     self.screen.blit(restart_text, restart_rect)
#     self.screen.blit(final_score_text, final_score_rect)

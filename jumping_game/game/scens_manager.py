import sys
import pygame
from .config import * 
from .utils import display_score
from .sprites import Player, Obstacle
from .data_logger import get_next_obstacles_features, save_game_data_to_csv


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Jumping Game")
        self.clock = pygame.time.Clock()
        
        self.title_font = pygame.font.Font(None, 80)
        self.button_font = pygame.font.Font(None, 60)
        self.score_font = pygame.font.Font(None, 50)

        self.player = Player()
        self.obstacles = [
            Obstacle(SCREEN_WIDTH, 450, 30, 50),
            Obstacle(SCREEN_WIDTH + 400, 450, 30, 50),
            Obstacle(SCREEN_WIDTH + 800, 420, 40, 80) # کمی تنوع
        ]
        
        self.ground_rect = pygame.Rect(0, 500, SCREEN_WIDTH, 100)
        self.start_button_rect = pygame.Rect(SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 + 50, 200, 80)
        
        self.current_obstacle_speed = STARTING_OBSTACLE_SPEED
        self.score = 0
        self.game_state = "MENU"

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self._handle_input(event)
            
            self._update_game()
            
            pygame.display.flip()
            self.clock.tick(FPS)
            
        pygame.quit()
        sys.exit()

    def _handle_input(self, event):
        if self.game_state == "MENU":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.start_button_rect.collidepoint(event.pos):
                    self.game_state = "PLAYING"

        elif self.game_state == "PLAYING":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()
                elif event.key == pygame.K_s:
                    self.player.dive()

        elif self.game_state in ["GAME_OVER", "WIN"]:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self._reset_game() 

    def _update_game(self):
        self.screen.fill(WHITE)

        if self.game_state == "MENU":
            welcome_text = self.title_font.render("Jumping Game", True, BLACK)
            welcome_rect = welcome_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50))
            self.screen.blit(welcome_text, welcome_rect)
            pygame.draw.rect(self.screen, GREEN, self.start_button_rect, border_radius=15)
            start_text = self.button_font.render("Start", True, BLACK)
            start_text_rect = start_text.get_rect(center=self.start_button_rect.center)
            self.screen.blit(start_text, start_text_rect)

        elif self.game_state == "PLAYING":
            self.current_obstacle_speed += SPEED_INCREASE_RATE
            self.score += 0.1

            self.player.update()
            for obstacle in self.obstacles:
                obstacle.update(self.current_obstacle_speed)

            pygame.draw.rect(self.screen, BLACK, self.ground_rect)
            self.player.draw(self.screen)
            for obstacle in self.obstacles:
                obstacle.draw(self.screen)
            display_score(self.screen, self.score_font, self.score)

            for obstacle in self.obstacles:
                if self.player.rect.colliderect(obstacle.rect):
                    collided_obstacle_height = obstacle.rect.height
                    collided_obstacle_width = obstacle.rect.width

                    game_data = [
                        int(self.score), 
                        self.player.rect.y,
                        self.current_obstacle_speed,
                        collided_obstacle_height,
                        collided_obstacle_width
                    ]
                    
                    next_features = get_next_obstacles_features(obstacle, self.obstacles)
                    game_data.extend(next_features)
                    
                    save_game_data_to_csv(game_data)
                    
                    self.game_state = "GAME_OVER" 
                    break 

            if self.score >= WIN_SCORE: 
                self.game_state = "WIN" 

        elif self.game_state == "GAME_OVER":
            game_over_text = self.title_font.render("Game Over", True, BLACK)
            restart_text = self.button_font.render("Press SPACE to Restart", True, BLACK)
            final_score_text = self.score_font.render(f"Your Score: {int(self.score)}", True, BLACK) 
            game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50))
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50))
            final_score_rect = final_score_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100))
            self.screen.blit(game_over_text, game_over_rect)
            self.screen.blit(restart_text, restart_rect)
            self.screen.blit(final_score_text, final_score_rect)

        elif self.game_state == "WIN":
            win_text = self.title_font.render("You Win!", True, GREEN)
            restart_text = self.button_font.render("Press SPACE to Play Again", True, BLACK)
            win_rect = win_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50))
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50))
            self.screen.blit(win_text, win_rect)
            self.screen.blit(restart_text, restart_rect)

    def _reset_game(self):
        self.score = 0
        self.current_obstacle_speed = STARTING_OBSTACLE_SPEED
        self.player.reset()
        for obstacle in self.obstacles:
            obstacle.reset()
        self.game_state = "PLAYING" 
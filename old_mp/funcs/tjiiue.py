NAME = "贪吃蛇"

from funcs.addons.commands import *
from funcs.addons.tjiiue.Snake import *
from funcs.addons.tjiiue.Food import *
import pygame

def draw_game(snake, food, score):
    window.fill(BLACK)

    # 绘制蛇
    for segment in snake.body:
        pygame.draw.rect(window, GREEN,(segment[0], segment[1], CELL_SIZE, CELL_SIZE))

    # 绘制食物
    pygame.draw.rect(window, RED,(food.position[0], food.position[1], CELL_SIZE, CELL_SIZE))

    # 显示分数
    font = pygame.font.SysFont(None, FONT_SIZE_NORMAL)
    text = font.render(f"Score: {score}", True, WHITE)
    window.blit(text, (10, 10))

    pygame.display.update()

def game_over(score):
    window.fill(BLACK)
    font = pygame.font.SysFont(None, FONT_SIZE_LARGE)
    text = font.render("Game Over!", True, RED)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
    window.blit(text, text_rect)

    font = pygame.font.SysFont(None, FONT_SIZE_NORMAL)
    text = font.render(f"Final Score: {score}. Press Space to restart", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))
    window.blit(text, text_rect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run()


def run():
    # 初始化 Pygame
    pygame.init()

    # 游戏窗口设置
    global window
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(GAME_TITLE)
    print_title(NAME)
    print("请在新打开的窗口中操作。")
    snake = Snake()
    food = Food(snake)
    score = 0
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(FPS)

        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(RIGHT)
                elif event.key == pygame.K_ESCAPE:
                    running = False
                    clear_screen()

        # 更新游戏状态
        if not snake.move():
            game_over(score)
            return

        # 检查是否吃到食物
        if snake.body[0] == food.position:
            snake.grow = True
            score += 1
            food = Food(snake)

        # 绘制游戏
        draw_game(snake, food, score)

    pygame.quit()
    return


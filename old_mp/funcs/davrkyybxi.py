NAME = "打砖块游戏"

import random, pygame
from funcs.addons.commands import *
from funcs.addons.davrkyybxi.consts import *

def run():
    clear_screen()
    print_title(NAME)
    print("请在新打开的窗口中操作。")
    # 初始化pygame
    pygame.init()

    # 设置窗口大小
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("打砖块游戏")

    # 设置时钟
    clock = pygame.time.Clock()

    # 球的属性
    ball_pos = [WIDTH // 2 + random.randint(-10, 10), HEIGHT - 100]
    ball_radius = 8  # 将球的大小调整为8
    ball_speed = [5, -5]

    # 平台的属性
    platform_width = 100
    platform_height = 10
    platform_pos = [WIDTH // 2 - platform_width // 2, HEIGHT - 2 * platform_height]
    platform_speed = 10

    # 砖块的属性
    bricks = []
    for i in range(8):
        for j in range(13):
            x = j * (BRICK_WIDTH + 5) + 15
            y = i * (BRICK_HEIGHT + 5) + 40
            bricks.append([x, y])

    paused = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.ACTIVEEVENT:
                if event.gain == 0: paused = True
                else: paused = False
        if paused:
            clock.tick(60)
            continue

        # 获取按键状态
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and platform_pos[0] > 0:
            platform_pos[0] -= platform_speed
        if keys[pygame.K_RIGHT] and platform_pos[0] < WIDTH - platform_width:
            platform_pos[0] += platform_speed

        # 更新球的位置
        ball_pos[0] += ball_speed[0]
        ball_pos[1] += ball_speed[1]

        # 碰撞检测
        if ball_pos[0] <= 0 or ball_pos[0] >= WIDTH - ball_radius:
            ball_speed[0] = -ball_speed[0]
        if ball_pos[1] <= 0:
            ball_speed[1] = -ball_speed[1]
        if ball_pos[1] >= HEIGHT:
            pygame.quit()
            print("球碰到了下边缘。")
            print("你失败了。")
            return

        # 检测与平台碰撞
        if (platform_pos[0] <= ball_pos[0] <= platform_pos[0] + platform_width or
            platform_pos[0] <= ball_pos[0] + ball_radius <= platform_pos[0] + platform_width) and \
                platform_pos[1] <= ball_pos[1] + ball_radius <= platform_pos[1] + platform_height:
            # 简单反弹，可以根据需要调整反弹的角度
            ball_speed[1] = -ball_speed[1]
            # 根据碰撞点调整水平速度
            collision_point_x = ball_pos[0] + ball_radius - platform_pos[0]
            relative_collision_point_x = collision_point_x / platform_width
            # 调整水平速度
            ball_speed[0] = (relative_collision_point_x - 0.5) * 10  # 这里的数值可以根据需要调整

        # 检测与砖块碰撞
        for brick in bricks[:]:
            brick_x, brick_y = brick  # 假设 brick 是一个 [x, y] 的列表
            if (brick_x <= ball_pos[0] <= brick_x + BRICK_WIDTH or
                brick_x <= ball_pos[0] + ball_radius * 2 <= brick_x + BRICK_WIDTH) and \
                    brick_y <= ball_pos[1] <= brick_y + BRICK_HEIGHT:
                ball_speed[1] = -ball_speed[1]
                bricks.remove(brick)
                break

        # 绘制背景
        screen.fill(BLACK)

        # 绘制砖块
        for brick in bricks:
            pygame.draw.rect(screen, ORANGE, (brick[0], brick[1], BRICK_WIDTH, BRICK_HEIGHT))

        # 绘制平台
        pygame.draw.rect(screen, WHITE, (platform_pos[0], platform_pos[1], platform_width, platform_height))

        # 绘制球
        pygame.draw.circle(screen, RED, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

        # 刷新屏幕
        pygame.display.flip()

        # 控制帧率
        clock.tick(FPS)

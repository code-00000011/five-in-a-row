import time
import pygame


class GameMain_1:
    def __init__(self):
        print("---------棋盘初始化----------")
        self.game_map = [[0 for x in range(1, 20, 1)] for y in range(1, 20, 1)]  # 二维列表棋盘
        self.sum = 1  # 得分
        self.before_sum = 0
        self.step_number = 0
        self.final = 0
        self.result = 0
        self.x = 0
        self.y = 0
        self.step = 0
        # 下了多少步

    def ending(self):
        """
        判断是否胜利
        0游戏进行
        1玩家胜利
        2电脑胜利
        :return: 人胜利 或 电脑胜利 或 游戏进行
        """

        for x in range(1, 15):  # 防止超出范围并且节约计算资源
            for y in range(1, 15):
                # ------------------------------------------------------------------------------------------------------
                if (self.game_map[x][y] == 1 and self.game_map[x + 1][y + 1] == 1 and self.game_map[x + 2][y + 2] == 1
                        and self.game_map[x + 3][y + 3] == 1 and self.game_map[x + 4][y + 4] == 1):
                    self.final = 1
                if self.game_map[x][y] == 2 and self.game_map[x + 1][y + 1] == 2 and self.game_map[x + 2][
                    y + 2] == 2 and self.game_map[x + 3][y + 3] == 2 and self.game_map[x + 4][y + 4] == 2:
                    self.final = 2  # 斜着判定1 /
                # -------------------------------------------------------------------------------------------------------
                if self.game_map[x + 4][y] == 1 and self.game_map[x + 3][y + 1] == 1 and self.game_map[x + 2][
                    y + 2] == 1 and self.game_map[x + 1][y + 3] == 1 and self.game_map[x][y + 4] == 1:
                    self.final = 1
                if self.game_map[x + 4][y] == 2 and self.game_map[x + 3][y + 1] == 2 and self.game_map[x + 2][
                    y + 2] == 2 and self.game_map[x + 1][y + 3] == 2 and self.game_map[x][y + 4] == 2:
                    self.final = 2  # 斜着判定2 \
                # ------------------------------------------------------------------------------------------------------
                if self.game_map[x][y] == 1 and self.game_map[x][y + 1] == 1 and self.game_map[x][y + 2] == 1 and \
                        self.game_map[x][y + 3] == 1 and self.game_map[x][y + 4] == 1:
                    self.final = 1
                if self.game_map[y][x] == 2 and self.game_map[x][y + 1] == 2 and self.game_map[x][y + 2] == 2 and \
                        self.game_map[x][y + 3] == 2 and self.game_map[x][y + 4] == 2:
                    self.final = 2  # Y轴判定
                # ------------------------------------------------------------------------------------------------------
                if self.game_map[x][y] == 1 and self.game_map[x + 1][y] == 1 and self.game_map[x + 2][y] == 1 and \
                        self.game_map[x + 3][y] == 1 and self.game_map[x + 4][y] == 1:
                    self.final = 1
                if self.game_map[x][y] == 2 and self.game_map[x + 1][y] == 2 and self.game_map[x + 2][y] == 2 and \
                        self.game_map[x + 3][y] == 2 and self.game_map[x + 4][y] == 2:
                    self.final = 2  # X轴判定
                # ------------------------------------------------------------------------------------------------------s

    def play(self):
        pygame.init()
        pygame.mixer.music.load('E:/wuziqi/.venv/music/back.WAV')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(start=-1, fade_ms=3000)
        sound_1 = pygame.mixer.Sound('E:/wuziqi/.venv/music/audio_down.wav')
        jocker = pygame.mixer.Sound('E:/wuziqi/.venv/music/jocker.wav')
        screen = pygame.display.set_mode((1200, 900))
        screen = pygame.display.set_mode((900, 900))
        pygame.display.set_caption("宇宙无敌暴龙五子棋")
        qiu_qi_lin = (218, 165, 32)  # 秋麒麟色，棋盘底色
        black = (0, 0, 0)
        screen.fill(qiu_qi_lin)  # 设置棋盘底色
        for i in range(0, 15, 1):  # 画横线
            if i == 0 or i == 14:
                thick = 5
            else:
                thick = 1
            pygame.draw.line(surface=screen, color=black, start_pos=(30, 30 + i * 60), end_pos=(870, 30 + i * 60),
                             width=thick)
        for i in range(0, 15, 1):  # 画竖线
            if i == 0 or i == 14:
                thick = 5
            else:
                thick = 1
            pygame.draw.line(surface=screen, color=black, start_pos=(i * 60 + 30, 30), end_pos=(i * 60 + 30, 870),
                             width=thick)
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    site_x, site_y = event.pos
                    x = (site_x - 30) // 60
                    y = (site_y - 30) // 60
                    if self.step % 2 == 0 and self.game_map[x][y] == 0:
                        sound_1.play()
                        pygame.draw.circle(surface=screen, color=(255, 255, 255), width=0,
                                           center=(x * 60 + 30, y * 60 + 30), radius=20)  # 下白子
                        self.game_map[x][y] = 1
                        self.step = self.step+1
                        pygame.display.flip()
                        self.ending()
                        if self.final == 1:
                            color_font = (251, 192, 45)
                            color2_back = (139, 195, 74)
                            text = pygame.font.SysFont(name="SimHei", size=60)  # 设置显示文字的类型和大小
                            text_font = text.render("恭喜你白棋，你赢了", True, color_font, color2_back)
                            screen.blit(text_font, (180, 300))
                            pygame.display.flip()
                            time.sleep(3)
                            pygame.quit()
                            return
                        continue

                    # ---------------黑子走下一步---------------
                    if self.step % 2 == 1 and self.game_map[x][y] == 0:
                        sound_1.play()
                        pygame.draw.circle(surface=screen, color=black, width=0,
                                           center=(x * 60 + 30, y * 60 + 30), radius=20)  # 下黑子
                        self.game_map[x][y] = 2
                        self.step = self.step+1
                        pygame.display.flip()
                        self.ending()
                        if self.final == 2:
                            color_font = (251, 192, 45)
                            color2_back = (139, 195, 74)
                            text = pygame.font.SysFont("SimHei", 60,)  # 设置显示文字的类型和大小
                            text_font = text.render("恭喜你黑棋，你赢了", True, color_font, color2_back )
                            screen.blit(text_font, (180, 300))
                            pygame.display.flip()
                            time.sleep(3)
                            pygame.quit()
                            return
                        continue
                    elif self.ending() == 0:
                        continue
                    # ----------------判断结局222-----------------

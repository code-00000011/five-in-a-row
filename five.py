# 后门版
import time
import json
import pygame
import ollama
import random


class GameMain:
    def __init__(self):
        self.data = [None for x in range(15)]  # 大语言模型切片存储
        self.game_map = [[0 for x in range(0, 19, 1)] for y in range(0, 19, 1)]  # 二维列表棋盘
        self.sum = 1  # AI得分
        self.before_sum = 0  # 中间变量分数
        self.final = 0  # 结果
        self.x = 0  # 获取AI的X坐标
        self.y = 0  # 获取AI的Y坐标
        self.step = 0  # 步数
        self.regret = [None for x in range(0, 112, 1)]  # 悔棋

    def time_data_in(self):  # 读取棋盘
        while True:
            f = open("txt.json", "r")
            f_1 = json.loads(f.readline())  # json格式文件，用于存储列表
            time.sleep(1)  # 每过一秒读取一次
            if self.game_map != f_1:  # 判断棋盘是否被修改
                self.game_map = f_1  # 被修改则覆盖当前棋盘
                f.close()
                break
            else:
                continue  # 没被修改就重新判断

    def time_data_out(self):  # 写入（对外输出棋盘）
        doc = open("txt.json", "r")
        doc_1 = doc.readline()
        if self.game_map != doc_1:
            doc.close()
            doc = open("txt.json", "w")
            doc.write(json.dumps(self.game_map))  # 以JSON格式写入
            doc.close()

    def ending(self):
        """
        判断是否胜利
        0游戏进行
        1玩家胜利
        2电脑胜利
        :return: 人胜利 或 电脑胜利 或 游戏进行
        """

        for x in range(1, 14):  # 防止超出范围并且节约计算资源
            for y in range(1, 14):
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
                # ------------------------------------------------------------------------------------------------------

    def ai_green_hands(self):
        for i in range(2):  # 第一次循环找到最高分，第二次循环返回最高分的坐标
            for x in range(0, 15):
                for y in range(0, 15):
                    if self.game_map[x][y] == 0:
                        self.game_map[x][y] = 2
                        self.sum = 0
                        # --------------------------------------------------------------------------------------------------------------
                        # 五子判定
                        mark = 99999  # 斜着五子判定\
                        if (self.game_map[x][y] == 2 and
                                self.game_map[x + 1][y + 1] == 2 and
                                self.game_map[x + 2][y + 2] == 2 and
                                self.game_map[x + 3][y + 3] == 2 and
                                self.game_map[x + 4][y + 4] == 2):
                            self.sum = self.sum + mark
                        if x >= 4 and y >= 4:
                            if (self.game_map[x][y] == 2 and
                                    self.game_map[x - 1][y - 1] == 2 and
                                    self.game_map[x - 2][y - 2] == 2 and
                                    self.game_map[x - 3][y - 3] == 2 and
                                    self.game_map[x - 4][y - 4] == 2):
                                self.sum = self.sum + mark

                        if (self.game_map[y][x] == 2 and
                                self.game_map[y + 1][x] == 2 and
                                self.game_map[y + 2][x] == 2 and
                                self.game_map[y + 3][x] == 2 and
                                self.game_map[y + 4][x] == 2):
                            self.sum = self.sum + mark

                        if (self.game_map[x][y] == 2 and
                                self.game_map[x + 1][y] == 2 and
                                self.game_map[x + 2][y] == 2 and
                                self.game_map[x + 3][y] == 2 and
                                self.game_map[x + 4][y] == 2):
                            self.sum = self.sum + mark

                        # --------------------------------------------------------------------------------------------------------------
                        # 4子判定
                        mark = 300
                        if (self.game_map[x][y] == 2 and
                                self.game_map[x + 1][y + 1] == 2 and
                                self.game_map[x + 2][y + 2] == 2 and
                                self.game_map[x + 3][y + 3] == 2):
                            self.sum = self.sum + mark

                        if x >= 4 and y >= 4:
                            if (self.game_map[x][y] == 2 and
                                    self.game_map[x - 1][y - 1] == 2 and
                                    self.game_map[x - 2][y - 2] == 2 and
                                    self.game_map[x - 3][y - 3] == 2):
                                self.sum = self.sum + mark

                        if (self.game_map[y][x] == 2 and
                                self.game_map[y + 1][x] == 2 and
                                self.game_map[y + 2][x] == 2 and
                                self.game_map[y + 3][x] == 2):
                            self.sum = self.sum + mark

                        if (self.game_map[x][y] == 2 and
                                self.game_map[x + 1][y] == 2 and
                                self.game_map[x + 2][y] == 2 and
                                self.game_map[x + 3][y] == 2):
                            self.sum = self.sum + mark
                        # --------------------------------------------------------------------------------------------------------------
                        # 三子判定
                        mark = 200
                        if (self.game_map[x][y] == 2 and
                                self.game_map[x + 1][y + 1] == 2 and
                                self.game_map[x + 2][y + 2] == 2):
                            self.sum = self.sum + mark

                        if x >= 4 and y >= 4:
                            if (self.game_map[x][y] == 2 and
                                    self.game_map[x - 1][y - 1] == 2 and
                                    self.game_map[x - 2][y - 2] == 2):
                                self.sum = self.sum + mark

                        if (self.game_map[y][x] == 2 and
                                self.game_map[y + 1][x] == 2 and
                                self.game_map[y + 2][x] == 2):
                            self.sum = self.sum + mark

                        if (self.game_map[x][y] == 2 and
                                self.game_map[x + 1][y] == 2 and
                                self.game_map[x + 2][y] == 2):
                            self.sum = self.sum + mark
                        # --------------------------------------------------------------------------------------------------------------
                        # 活三判定
                        mark = 210
                        if (self.game_map[x][y] == 2 and
                                self.game_map[x + 1][y] == 2 and
                                self.game_map[x + 1][y + 1] == 2):
                            self.sum = self.sum + mark  # -/

                        if (self.game_map[x][y] == 2 and
                                self.game_map[x][y + 1] == 2 and
                                self.game_map[x + 1][y + 1]):
                            self.sum = self.sum + mark  # \-

                        if (self.game_map[y][x] == 2 and
                                self.game_map[y + 1][x + 1] == 2 and
                                self.game_map[y][x + 2] == 2):
                            self.sum = self.sum + mark  # \/
                        if y - 1 > 0:
                            if (self.game_map[x][y] == 0 and
                                    self.game_map[x + 1][y - 1] == 2 and
                                    self.game_map[x + 2][y] == 2):
                                self.sum = self.sum + mark  # /\
                            # --------------------------------------------------------------------------------------------------------------
                            # 在玩家下的子旁边落子
                        if x - 1 > 0:
                            if self.game_map[x][y] == 2 and self.game_map[x - 1][y] == 1:
                                self.sum = self.sum + 24
                            if self.game_map[x][y] == 2 and self.game_map[x - 1][y + 1] == 1:
                                self.sum = self.sum + 24
                        if y - 1 > 0:
                            if self.game_map[x][y] == 2 and self.game_map[x + 1][y - 1] == 1:
                                self.sum = self.sum + 24
                            if self.game_map[x][y] == 2 and self.game_map[x][y - 1] == 1:
                                self.sum = self.sum + 24
                        if x - 1 > 0 and y - 1 > 0:
                            if self.game_map[x][y] == 2 and self.game_map[x - 1][y - 1] == 1:
                                self.sum = self.sum + 24
                        # 右下角三个判定
                        if self.game_map[x][y] == 2 and self.game_map[x + 1][y] == 1:
                            self.sum = self.sum + 24

                        if self.game_map[x][y] == 2 and self.game_map[x][y + 1] == 1:
                            self.sum = self.sum + 24

                        if self.game_map[x][y] == 2 and self.game_map[x + 1][y + 1] == 1:
                            self.sum = self.sum + 24
                        # ---------------防御加分----------------
                        # ---------------防御三子（任意）/(必须）-----------
                        mark = 999
                        if self.game_map[x][y] == 2 and self.game_map[x + 1][y + 1] == 1 and self.game_map[x + 2][
                            y + 2] == 1 and self.game_map[x + 3][y + 3] == 1:
                            self.sum = self.sum + 24
                            if self.game_map[x + 4][y + 4] != 2:
                                self.sum = self.sum + mark

                        if self.game_map[x][y] == 2 and self.game_map[x + 1][y] == 1 and self.game_map[x + 2][
                            y] == 1 and self.game_map[x + 3][y] == 1:
                            self.sum = self.sum + 24
                            if self.game_map[x + 4][y] != 2:
                                self.sum = self.sum + mark

                        if self.game_map[x][y] == 2 and self.game_map[x][y + 1] == 1 and self.game_map[x][
                            y + 2] == 1 and self.game_map[x][y + 3] == 1:
                            self.sum = self.sum + 24
                            if self.game_map[x][y + 4] != 2:
                                self.sum = self.sum + mark

                        if self.game_map[x + 4][y] == 2 and self.game_map[x + 3][y + 1] == 1 and self.game_map[x + 2][
                            y + 2] == 1 and self.game_map[x + 1][y + 3] == 1:
                            self.sum = self.sum + 24
                            if self.game_map[x][y + 4] != 2:
                                self.sum = self.sum + mark
                        # ---------------防御四子----------------
                        mark = 9999
                        if (self.game_map[x][y] == 2
                                and self.game_map[x + 1][y + 1] == 1
                                and self.game_map[x + 2][y + 2] == 1
                                and self.game_map[x + 3][y + 3]
                                and self.game_map[x + 4][y + 4] == 1):
                            self.sum = self.sum + mark

                        if (self.game_map[x][y] == 2
                                and self.game_map[x][y + 1] == 1
                                and self.game_map[x][y + 2] == 1
                                and self.game_map[x][y + 3]
                                and self.game_map[x][y + 4] == 1):
                            self.sum = self.sum + mark

                        if (self.game_map[x][y] == 2
                                and self.game_map[x + 1][y] == 1
                                and self.game_map[x + 2][y] == 1
                                and self.game_map[x + 3][y]
                                and self.game_map[x + 4][y] == 1):
                            self.sum = self.sum + mark

                        if (self.game_map[x + 4][y] == 2
                                and self.game_map[x + 3][y + 1] == 1
                                and self.game_map[x + 2][y + 2] == 1
                                and self.game_map[x + 1][y + 3]
                                and self.game_map[x][y + 4] == 1):
                            self.sum = self.sum + mark
                        # ----------------------------------------------------------------------------------------------
                        if i == 0 and self.before_sum <= self.sum:
                            self.before_sum = self.sum
                            self.game_map[x][y] = 0
                        if i == 0 and self.before_sum > self.sum:
                            self.game_map[x][y] = 0  # 找到最高分并且不改变当前位置
                        if i == 1 and self.before_sum == self.sum:
                            self.x = x
                            self.y = y
                            self.before_sum = 0
                            self.sum = 0
                            return
                        if i == 1 and self.before_sum != self.sum:
                            self.game_map[x][y] = 0

    def ai_master(self):
        question = f"""
        你是一个顶级五子棋解说猫娘。在这个五棋棋游戏中，我们使用了一个二维列表来表示棋盘，其中：
        二维列表中的一维列表的顺序（从0到15）代表行的坐标
        二维列表中的一维列表中的数字的顺序（从0到15）代表列的坐标
        - 0 表示空位
        - 1 表示白棋
        - 2 表示黑棋
        当前棋局如下：
        {str(self.game_map)}
        （注意：这里为了展示方便，我将二维列表转换为了字符串格式。实际传递时，请确保你的模型能够处理二维列表或相应的数据结构。）       
        例如"[[0,0],[0,1]]"，表示在第二行第二列下了白子
        请根据当前棋局(一定要确定所有白棋的位置和所有黑棋的位置），分析棋局并且为白子提出建议（不要告诉我棋子的位置，仅使用中部，上方，下方等词）。

        回答时不要换行
        请记住，你是一只猫娘(名为香子兰）！注意猫娘的用语！ 多使用一些语气词哦~

        建议少于150字                
        """
        response_1 = ollama.chat(model='qwen2.5:7b', messages=[
            {
                'role': 'user',
                'content': question,
            },
        ])
        return response_1['message']['content']

    def play(self):
        def line():
            """
            划线，横线竖线覆盖棋盘
            :return:
            """
            for q in range(0, 15, 1):  # 画横线
                if q == 0 or q == 14:
                    thick = 5
                else:
                    thick = 1
                pygame.draw.line(surface=screen, color=(0, 0, 0), start_pos=(30, 30 + q * 60),
                                 end_pos=(870, 30 + q * 60),
                                 width=thick)
            for q in range(0, 15, 1):  # 画竖线
                if q == 0 or q == 14:
                    thick = 5
                else:
                    thick = 1
                pygame.draw.line(surface=screen, color=(0, 0, 0), start_pos=(q * 60 + 30, 30),
                                 end_pos=(q * 60 + 30, 870),
                                 width=thick)


        def restart():
            pygame.draw.rect(screen, (249, 168, 37), (30, 30, 840, 870), 0)  # 画长方形覆盖
            self.game_map = [[0 for x in range(0, 19, 1)] for y in range(0, 19, 1)]
            self.final = 0
            self.step = 0

        def ai_advice():
            talk_ai = self.ai_master()
            pygame.draw.rect(screen, (255, 214, 0), (887, 102, 300, 480), 0)  # 画长方形覆盖
            pygame.display.flip()
            for i in range(15):
                self.data[i] = talk_ai[14 * i:14 * (i + 1):1]  # 输出AI的建议
                text_ai_1 = pygame.font.SysFont(name="华文中宋", size=20)
                text_font_ai_1 = text_ai_1.render(self.data[i], True, (0, 0, 0), )
                screen.blit(text_font_ai_1, (900, 115 + i * 30))
                pygame.display.flip()

        def score_step():
            text_s = pygame.font.SysFont(name="华文楷体", size=40)  # 设置显示文字的类型和大小
            word_s = "步数：" + str(self.step) + "    "
            text_font_s = text_s.render(word_s, True, (255, 255, 255), (184, 134, 11))
            screen.blit(text_font_s, (895, 630))
            pygame.display.flip()

        def regret():
            self.step -= 1
            be_x_1 = self.regret[self.step][0]
            be_y_1 = self.regret[self.step][1]
            self.step -= 1
            be_x_2 = self.regret[self.step][0]
            be_y_2 = self.regret[self.step][1]
            self.game_map[be_x_1][be_y_1] = 0
            self.game_map[be_x_2][be_y_2] = 0
            pygame.draw.circle(surface=screen, color=(249, 168, 37), width=0,
                               center=(be_x_1 * 60 + 30, be_y_1 * 60 + 30), radius=20)  # 清除下子
            if be_x_1 == 0 or be_x_1 == 14:
                thick = 5
            else:
                thick = 1
            pygame.draw.line(surface=screen, color=(0, 0, 0), start_pos=(be_x_1 * 60 + 10, be_y_1 * 60 + 30),
                             end_pos=(be_x_1 * 60 + 50, be_y_1 * 60 + 30),
                             width=thick)
            if be_y_1 == 0 or be_y_1 == 14:
                thick = 5
            else:
                thick = 1
            pygame.draw.line(surface=screen, color=(0, 0, 0), start_pos=(be_x_1 * 60 + 30, be_y_1 * 60 + 10),
                             end_pos=(be_x_1 * 60 + 30, be_y_1 * 60 + 50),
                             width=thick)
            pygame.display.flip()
            time.sleep(0.6)
            pygame.draw.circle(surface=screen, color=(249, 168, 37), width=0,
                               center=(be_x_2 * 60 + 30, be_y_2 * 60 + 30), radius=20)
            pygame.display.flip()
            if be_x_2 == 0 or be_x_2 == 14:
                thick = 5
            else:
                thick = 1
            pygame.draw.line(surface=screen, color=(0, 0, 0), start_pos=(be_x_2 * 60 + 10, be_y_2 * 60 + 30),
                             end_pos=(be_x_2 * 60 + 50, be_y_2 * 60 + 30),
                             width=thick)
            if be_y_2 == 0 or be_y_2 == 14:
                thick = 5
            else:
                thick = 1
            pygame.draw.line(surface=screen, color=(0, 0, 0), start_pos=(be_x_2 * 60 + 30, be_y_2 * 60 + 10),
                             end_pos=(be_x_2 * 60 + 30, be_y_2 * 60 + 50),
                             width=thick)
            score_step()
            pygame.display.flip()

        pygame.init()
        back = pygame.mixer.Sound('E:/wuziqi/.venv/music/back_final.WAV')
        back.play()
        pygame.mixer.Sound.set_volume(back,0.25)

        sound_1 = pygame.mixer.Sound('E:/wuziqi/.venv/music/down_loudly.WAV')
        sound_button = pygame.mixer.Sound('E:/wuziqi/.venv/music/button.WAV')
        sound_open = pygame.mixer.Sound('E:/wuziqi/.venv/music/open.WAV')
        sound_close = pygame.mixer.Sound('E:/wuziqi/.venv/music/close.WAV')
        fail = pygame.mixer.Sound('E:/wuziqi/.venv/music/DDD.wav')
        win = pygame.mixer.Sound('E:/wuziqi/.venv/music/VVV.wav')
        screen = pygame.display.set_mode((1200, 900))
        pygame.display.set_caption("智慧棋盘")
        qiu_qi_lin = (249, 168, 37)  # 秋麒麟色，棋盘底色
        screen.fill(qiu_qi_lin)  # 设置棋盘底色
        line()
        pygame.draw.rect(screen, (255, 214, 0), (887, 30, 300, 840), 0)
        text = pygame.font.SysFont(name="华文仿宋", size=40)  # 设置显示文字的类型和大小
        text_font = text.render("  AI建议", True, (0, 0, 0), )
        screen.blit(text_font, (895, 45))
        pygame.draw.line(surface=screen, color=(0, 0, 0), start_pos=(889, 100), end_pos=(1184, 100),
                         width=3)
        pygame.draw.line(surface=screen, color=(0, 0, 0), start_pos=(889, 600), end_pos=(1184, 600),
                         width=3)
        pygame.display.flip()

        # --------步数显示----------
        score_step()
        # --------重新开始----------
        text = pygame.font.SysFont(name="华文楷体", size=40)  # 设置显示文字的类型和大小
        text_font = text.render("重新开始", True, (0, 0, 0), (184, 134, 11))
        screen.blit(text_font, (895, 720))
        # --------悔棋显示----------
        text = pygame.font.SysFont(name="华文楷体", size=40)  # 设置显示文字的类型和大小
        text_font = text.render("悔棋", True, (0, 0, 0), (184, 134, 11))
        screen.blit(text_font, (1090, 720))
        pygame.display.flip()
        # --------建议显示----------
        text_1 = pygame.font.SysFont(name="华文楷体", size=40)  # 设置显示文字的类型和大小
        word = "更多建议"
        text_font_1 = text_1.render(word, True, (0, 0, 0), (184, 134, 11))
        screen.blit(text_font_1, (895, 810))
        pygame.display.flip()
        # --------退出显示----------
        text_1 = pygame.font.SysFont(name="华文楷体", size=40)  # 设置显示文字的类型和大小
        word = "退出"
        text_font_1 = text_1.render(word, True, (0, 0, 0), (184, 134, 11))
        screen.blit(text_font_1, (1090, 810))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEMOTION:
                    site_x, site_y = event.pos

                    # --------重新开始闪烁----------
                    if 895 < site_x < 1055 and 720 < site_y < 772:
                        color = (255, 255, 255)
                    else:
                        color = (0, 0, 0)
                    text = pygame.font.SysFont(name="华文楷体", size=40)  # 设置显示文字的类型和大小
                    text_font = text.render("重新开始", True, color, (184, 134, 11))
                    screen.blit(text_font, (895, 720))

                    # --------悔棋显示闪烁----------
                    if 1090 < site_x < 1171 and 720 < site_y < 771:
                        color = (255, 255, 255)
                    else:
                        color = (0, 0, 0)
                    text = pygame.font.SysFont(name="华文楷体", size=40)  # 设置显示文字的类型和大小
                    text_font = text.render("悔棋", True, color, (184, 134, 11))
                    screen.blit(text_font, (1090, 720))

                    # --------建议显示闪烁----------
                    if 895 < site_x < 1056 and 810 < site_y < 862:
                        color = (255, 255, 255)
                    else:
                        color = (0, 0, 0)
                    text_1 = pygame.font.SysFont(name="华文楷体", size=40)  # 设置显示文字的类型和大小
                    word = "更多建议"
                    text_font_1 = text_1.render(word, True, color, (184, 134, 11))
                    screen.blit(text_font_1, (895, 810))

                    # --------退出显示----------
                    if 1090 < site_x < 1170 and 810 < site_y < 862:
                        color = (255, 255, 255)
                    else:
                        color = (0, 0, 0)
                    text_1 = pygame.font.SysFont(name="华文楷体", size=40)  # 设置显示文字的类型和大小
                    word = "退出"
                    text_font_1 = text_1.render(word, True, color, (184, 134, 11))
                    screen.blit(text_font_1, (1090, 810))
                    pygame.display.flip()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    site_x, site_y = event.pos
                    x = (site_x - 15) // 60  # 获取X和Y（下棋子的横坐标）
                    y = (site_y - 15) // 60
                    # --------重新开始=按钮----------
                    if 895 < site_x < 1055 and 720 < site_y < 772:
                        sound_open.play()
                        pygame.mixer.Sound.set_volume(sound_open,0.3)
                        restart()
                        line()
                        score_step()
                        pygame.draw.rect(screen, (255, 214, 0), (887, 102, 300, 480), 0)  # 画长方形覆盖
                        pygame.display.flip()

                    # ---------退出=按钮--------
                    if 1090 < site_x < 1170 and 810 < site_y < 860:
                        pygame.mixer.Sound.stop(back)
                        sound_close.play()
                        pygame.mixer.Sound.set_volume(sound_close, 0.3)
                        time.sleep(1.3)
                        pygame.quit()
                    # ---------建议=按钮--------
                    if 895 < site_x < 1056 and 810 < site_y < 862:
                        sound_button.play()
                        pygame.mixer.music.set_volume(0)
                        pygame.draw.rect(screen, (255, 214, 0), (887, 102, 300, 480), 0)  # 画长方形覆盖
                        text_ai = pygame.font.SysFont(name="华文楷体", size=20)
                        text_font_ai = text_ai.render("正在生成建议请稍后......", True, (0, 0, 0), )
                        screen.blit(text_font_ai, (900, 115))
                        pygame.display.flip()
                        ai_advice()

                    # -----------悔棋---------------
                    if 1090 < site_x < 1170 and 720 < site_y < 771 :
                        sound_button.play()
                        if self.step > 1:
                            regret()
                    if self.step % 2 == 0 and x < 15 and y < 15 and self.game_map[x][y] == 0:
                        sound_1.play()
                        pygame.draw.circle(surface=screen, color=(255, 255, 255), width=0,
                                           center=(x * 60 + 30, y * 60 + 30), radius=20)  # 下白子
                        self.game_map[x][y] = 1
                        self.regret[self.step] = [x, y]
                        self.step = self.step + 1
                        score_step()
                        self.ending()
                        if self.final == 1:
                            text = pygame.font.SysFont(name="华文楷体", size=60)  # 设置显示文字的类型和大小
                            text_font = text.render("恭喜你""白棋，你赢了", True, (251, 192, 45), (139, 195, 74))
                            screen.blit(text_font, (160, 300))
                            pygame.display.flip()
                            win.play()

                    # ---------------机器走下一步---------------
                    if self.step % 2 == 1:
                        self.ai_green_hands()
                        time.sleep(random.uniform(0, 1.2))
                        sound_1.play()
                        pygame.draw.circle(surface=screen, color=(0, 0, 0), width=0,
                                           center=(self.x * 60 + 30, self.y * 60 + 30), radius=20)  # 下黑子
                        pygame.display.flip()
                        self.regret[self.step] = [self.x, self.y]
                        self.step = self.step + 1
                        # ----------步数显示--------------
                        score_step()
                        self.ending()
                        ai_advice()
                        if self.final == 2:
                            color_font = (251, 192, 45)
                            color2_back = (139, 195, 74)
                            text = pygame.font.SysFont(name="华文楷体", size=60)  # 设置显示文字的类型和大小
                            text_font = text.render("嘻嘻，人类，你输了", True, color_font, color2_back)
                            screen.blit(text_font, (160, 300))
                            pygame.display.flip()
                            pygame.mixer.music.fadeout(1500)
                            fail.play()

                    elif self.ending() == 0:
                        continue

# 开发日志
## 时间：**2024.11.6**
### 预计完成功能（A）
1. 完善五子模AI 左下到右下判定 右下判定 下判定 右判定 有时四子连珠不下五子
2. ```def ai_green_hands(self):
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

                    if self.game_map[x][y] == 2 and self.game_map[x + 1][y] == 1 and self.game_map[x + 2][y] == 1 and \
                            self.game_map[x + 3][y] == 1:
                        self.sum = self.sum + 24
                        if self.game_map[x + 4][y] != 2:
                            self.sum = self.sum + mark

                    if self.game_map[x][y] == 2 and self.game_map[x][y + 1] == 1 and self.game_map[x][y + 2] == 1 and \
                            self.game_map[x][y + 3] == 1:
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
                        self.game_map[x][y] = 0```
3. 完着人人对战:
界面改成和A工断一样
4. 增加语音:
AI阅读建议
探索性增加AI对话
5. 完善qwen提示词:
让AI工清楚场上棋子的个数和位置 *(传步数)*
6. 更换背景音乐:
让张新吹一首
增加右下角按钮声音
增加右下角动效
胜利动画和音效



def ai_green_hands(self):
    five = 0
    four = 0
    three = 0
    flexible_three = 0
    flexible_four = 0
    beside = 0
    defend_three = 0
    defend_four = 0
    for i in range(2):  # 第一次循环找到最高分，第二次循环返回最高分的坐标
        for x in range(0, 15):
            for y in range(0, 15):
                if self.game_map[x][y] == 0:
                    self.game_map[x][y] = 2
                    self.sum = 0
                    # --------------------------------------------------------------------------------------------------------------
                    # 五子判定
                    for x1 in range(0, 15):
                        for y1 in range(0, 15):
                              # 斜着五子判定\
                            if (self.game_map[x][y] == 2 and
                                    self.game_map[x + 1][y + 1] == 2 and
                                    self.game_map[x + 2][y + 2] == 2 and
                                    self.game_map[x + 3][y + 3] == 2 and
                                    self.game_map[x + 4][y + 4] == 2):
                                five += 1

                            if x >= 4 and y >= 4:
                                if (self.game_map[x][y] == 2 and
                                        self.game_map[x - 1][y - 1] == 2 and
                                        self.game_map[x - 2][y - 2] == 2 and
                                        self.game_map[x - 3][y - 3] == 2 and
                                        self.game_map[x - 4][y - 4] == 2):
                                    five += 1

                            if (self.game_map[y][x] == 2 and
                                    self.game_map[x][y + 1] == 2 and
                                    self.game_map[x][y + 2] == 2 and
                                    self.game_map[x][y + 3] == 2 and
                                    self.game_map[x][y + 4] == 2):
                                five += 1

                            if (self.game_map[x][y] == 2 and
                                    self.game_map[x + 1][y] == 2 and
                                    self.game_map[x + 2][y] == 2 and
                                    self.game_map[x + 3][y] == 2 and
                                    self.game_map[x + 4][y] == 2):
                                five += 1

                            # --------------------------------------------------------------------------------------------------------------
                            # 4子判定
                            if (self.game_map[x][y] == 2 and
                                    self.game_map[x + 1][y + 1] == 2 and
                                    self.game_map[x + 2][y + 2] == 2 and
                                    self.game_map[x + 3][y + 3] == 2):
                                four += 1

                            if x >= 4 and y >= 4:
                                if (self.game_map[x][y] == 2 and
                                        self.game_map[x - 1][y - 1] == 2 and
                                        self.game_map[x - 2][y - 2] == 2 and
                                        self.game_map[x - 3][y - 3] == 2):
                                    four += 1

                            if (self.game_map[y][x] == 2 and
                                    self.game_map[x][y + 1] == 2 and
                                    self.game_map[x][y + 2] == 2 and
                                    self.game_map[x][y + 3] == 2):
                                four += 1
                            if (self.game_map[x][y] == 2 and
                                    self.game_map[x + 1][y] == 2 and
                                    self.game_map[x + 2][y] == 2 and
                                    self.game_map[x + 3][y] == 2):
                                four += 1
                            # --------------------------------------------------------------------------------------------------------------
                            # 三子判定
                            if (self.game_map[x][y] == 2 and
                                    self.game_map[x + 1][y + 1] == 2 and
                                    self.game_map[x + 2][y + 2] == 2):
                                three += 1

                            if x >= 4 and y >= 4:
                                if (self.game_map[x][y] == 2 and
                                        self.game_map[x - 1][y - 1] == 2 and
                                        self.game_map[x - 2][y - 2] == 2):
                                    three += 1

                            if (self.game_map[y][x] == 2 and
                                    self.game_map[x][y + 1] == 2 and
                                    self.game_map[x][y + 2] == 2):
                                three += 1

                            if (self.game_map[x][y] == 2 and
                                    self.game_map[x + 1][y] == 2 and
                                    self.game_map[x + 2][y] == 2):
                                three += 1
                            # --------------------------------------------------------------------------------------------------------------
                            # 活三判定
                            mark = 210
                            if (self.game_map[x][y] == 2 and
                                    self.game_map[x + 1][y] == 2 and
                                    self.game_map[x + 1][y + 1] == 2):
                                flexible_three += 1  # -/

                            if (self.game_map[x][y] == 2 and
                                    self.game_map[x][y + 1] == 2 and
                                    self.game_map[x + 1][y + 1]):
                                flexible_three += 1  # \-

                            if (self.game_map[y][x] == 2 and
                                    self.game_map[x + 1][y + 1] == 2 and
                                    self.game_map[x + 2][y] == 2):
                                flexible_three += 1  # \/
                            if y - 1 > 0:
                                if (self.game_map[x][y] == 0 and
                                        self.game_map[x + 1][y - 1] == 2 and
                                        self.game_map[x + 2][y] == 2):
                                    flexible_three += 1  # /\
                                # --------------------------------------------------------------------------------------------------------------
                                # 在玩家下的子旁边落子
                            if x - 1 > 0:
                                if self.game_map[x][y] == 2 and self.game_map[x - 1][y] == 1:
                                    beside += 1
                                if self.game_map[x][y] == 2 and self.game_map[x - 1][y + 1] == 1:
                                    beside += 1
                            if y - 1 > 0:
                                if self.game_map[x][y] == 2 and self.game_map[x + 1][y - 1] == 1:
                                    beside += 1
                                if self.game_map[x][y] == 2 and self.game_map[x][y - 1] == 1:
                                    beside += 1
                            if x - 1 > 0 and y - 1 > 0:
                                if self.game_map[x][y] == 2 and self.game_map[x - 1][y - 1] == 1:
                                    beside += 1
                            # 右下角三个判定
                            if self.game_map[x][y] == 2 and self.game_map[x + 1][y] == 1:
                                beside += 1

                            if self.game_map[x][y] == 2 and self.game_map[x][y + 1] == 1:
                                beside += 1

                            if self.game_map[x][y] == 2 and self.game_map[x + 1][y + 1] == 1:
                                beside += 1
                            # ---------------防御加分----------------
                            # ---------------防御三子（任意）/(必须）-----------
                            # ----------------------------------------------左上到右下
                            if x-1 > 0 and y-1 > 0 and \
                                    self.game_map[x][y] == 1 and\
                                    self.game_map[x + 1][y + 1] == 1 and \
                                    self.game_map[x + 2][y + 2] == 1 and \
                                    self.game_map[x - 1][y - 1] != 2:
                                    defend_three += 1
                            if self.game_map[x][y] == 1 and \
                                    self.game_map[x + 1][y + 1] == 1 and \
                            self.game_map[x + 2][y + 2] == 1 and \
                                    self.game_map[x + 3][y + 3] != 2:
                                defend_three += 1
                            # ---------------------------------------------横着
                            if self.game_map[x + 1][y] == 1 and \
                                    self.game_map[x + 2][y] == 1 and \
                                    self.game_map[x + 3][y] == 1 and \
                                    self.game_map[x + 4][y] != 2:
                                defend_three += 1
                            if x-1>0 and self.game_map[x + 1][y] == 1 and \
                                    self.game_map[x + 2][y] == 1 and\
                                    self.game_map[x + 3][y] == 1 and \
                                    self.game_map[x - 1][y] != 2:
                                defend_three += 1
                            # ------------------------------------------------竖着
                            if self.game_map[x][y + 1] == 1 and \
                                    self.game_map[x][y + 2] == 1 and \
                                    self.game_map[x][y + 3] == 1 and \
                                    self.game_map[x][y + 4] != 2 :
                                defend_three += 1

                            if y - 1 > 0 and self.game_map[x][y + 1] == 1 and \
                                      self.game_map[x][y + 2] == 1 and \
                                      self.game_map[x][y + 3] == 1 and \
                                      self.game_map[x][y - 1] != 2:
                                  defend_three += 1
                            # -------------------------------------------------左下到右上
                            if x-3 > 0 and y - 3 > 0 and \
                                    self.game_map[x][y] == 1 and \
                                    self.game_map[x-1][y-1] == 1 and \
                                    self.game_map[x-2][y-2] == 1 and \
                                    self.game_map[x-3][y-3] != 2:
                                defend_three += 1
                            if x - 2 > 0 and y - 2 > 0 and \
                                      self.game_map[x][y] == 1 and \
                                      self.game_map[x - 1][y - 1] == 1 and \
                                      self.game_map[x - 2][y - 2] == 1 and \
                                      self.game_map[x + 1][y + 1] != 2:
                                  defend_three += 1
                            # ---------------防御四子----------------
                            if (     self.game_map[x ][y] == 1
                                    and self.game_map[x + 1][y + 1] == 1
                                    and self.game_map[x + 2][y + 2] == 1
                                    and self.game_map[x + 3][y + 3] == 1
                                    and (self.game_map[x + 4][y + 4] != 2
                                    or self.game_map[x-1][y-1] != 2)):
                                self.sum = self.sum + mark

                            if (self.game_map[x][y] == 2
                                    and self.game_map[y + 1][x] == 1
                                    and self.game_map[y + 2][x] == 1
                                    and self.game_map[y + 3][x]
                                    and self.game_map[y + 4][x] == 1):
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

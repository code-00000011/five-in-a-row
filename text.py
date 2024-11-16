from five import GameMain
from human_1 import GameMain_1
import pygame


def main():
    print(pygame.font.get_fonts())
    pygame.init()
    screen = pygame.display.set_mode((900, 900))
    back = pygame.image.load("back.jpg")
    screen.blit(back, (-130, -130))
    pygame.display.flip()
    text = pygame.font.SysFont(name="隶书", size=60)
    text_1 = pygame.font.SysFont(name="华文新魏", size=120, )
    text_2 = pygame.font.SysFont(name="华文新魏", size=20, )
    pygame.display.set_caption("智慧棋盘")
    text_font_1 = text.render("人机对战", True, (255, 255, 255), )
    text_font_2 = text.render("人人对战", True, (255, 255, 255), )
    text_font_3 = text_1.render("智慧棋盘", True, (255, 255, 255), )
    text_font_4 = text_2.render("抵制不良游戏，拒绝盗版游戏。 注意自我保护，谨防受骗上当。", True, (255, 255, 255), )
    text_font_5 = text_2.render("适度游戏益脑，沉迷游戏伤身。 合理安排时间，享受健康生活。", True, (255, 255, 255), )
    screen.blit(text_font_1, (320, 400))
    screen.blit(text_font_2, (320, 600))
    screen.blit(text_font_3, (220, 120))
    screen.blit(text_font_4, (170, 850))
    screen.blit(text_font_5, (170, 870))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:

                site_x, site_y = event.pos
                if 400 < site_y < 599 and 400 < site_x < 700:  # 人机对战
                    pygame.quit()
                    g = GameMain()
                    g.play()
                elif 600 < site_y < 899 and 400 < site_x < 700:  # 人人对战
                    pygame.quit()
                    g = GameMain_1()
                    g.play()
                else:
                    continue


if __name__ == "__main__":
    main()

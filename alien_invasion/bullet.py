import pygame
from pygame.sprite import Sprite
class Bullet(Sprite) :
    """管理飞船并发射所有的子弹"""

    def __init__(self , ai_game) :
        """在飞船当前位置创建一个子弹的对象"""
        super().__init__() 
        #父类定义的继承
        self.screen =  ai_game.screen 
        self.settings = ai_game.settings 
        self.color = self.settings.bullet_color

        #在（ 0，0 ）处设置一个表示子弹的矩形 ， 在设置正确的位置
        self.rect = pygame.Rect( 0 ,0 , self.settings.bullet_width , self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        #储存用浮点数表示的子弹位置
        self.y = float(self.rect.y)

    def update (self) :
        """向上移动子弹"""
        #更新子弹的位置
        self.y -= self.settings.bullet_speed
        #更新表示子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self) :
        """在屏幕上重新绘制子弹"""
        pygame.draw.rect(self.screen , self.color , self.rect )

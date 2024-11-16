import random
import assets
import pyxel

SCREEN_HEIGHT = 38
SCREEN_WIDTH = 78

COLORS_WHEEL = [7,7,7,7,7,7,0,0,0,0,0,0,0,0,0,0,7]

class App:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="Profile Picture Maker")
        self.cursor_pos = 0
        self.avatar = random.randint(0, len(assets.avatars)-1)
        self.avatar_col = random.randint(0, 15)

        self.border = random.randint(0, len(assets.borders)-1)
        self.border_col = random.randint(0, 15)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_RIGHT):
            match self.cursor_pos:
                case 0:
                    self.border += 1
                case 1:
                    self.border_col += 1
                case 2:
                    self.avatar += 1
                case 3:
                    self.avatar_col += 1
        elif pyxel.btnp(pyxel.KEY_LEFT):
            match self.cursor_pos:
                case 0:
                    self.border -= 1
                case 1:
                    self.border_col -= 1
                case 2:
                    self.avatar -= 1
                case 3:
                    self.avatar_col -= 1
        
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            mx = pyxel.mouse_x
            my = pyxel.mouse_y
            
            if mx >= 2 and my >= 2 and mx <= 17 and my <= 17:
                self.cursor_pos = 0
            elif mx >= 20 and my >= 2 and mx <= 35 and my <= 17:
                self.cursor_pos = 1
            elif mx >= 2 and my >= 20 and mx <= 17 and my <= 34:
                self.cursor_pos = 2
            elif mx >= 20 and my >= 20 and mx <= 35 and my <= 35:
                self.cursor_pos = 3

        self.border %= len(assets.borders)
        self.border_col %= 16

        self.avatar %= len(assets.avatars)
        self.avatar_col %= 16

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(SCREEN_WIDTH/2-1, 0, 2, SCREEN_HEIGHT, 7)

        assets.borders[self.border].display(2, 2, 7)
        assets.avatars[self.avatar].display(2, 20, 7)

        assets.borders[self.border].display(43, 3, self.border_col, size=2)
        assets.avatars[self.avatar].display(43, 3, self.avatar_col, size=2)

        pyxel.rect(20, 2, 16, 16, self.border_col)
        pyxel.rect(20, 20, 16, 16, self.avatar_col)
        pyxel.text(23, 7, "col", COLORS_WHEEL[self.border_col])
        pyxel.text(23, 25, "col", COLORS_WHEEL[self.avatar_col])

        pyxel.rectb(1 + 18 * (self.cursor_pos % 2), 1 + 18 * (self.cursor_pos // 2), 18, 18, 9)

        mx = pyxel.mouse_x
        my = pyxel.mouse_y

        pyxel.rect(mx-1, my, 3, 1, 2)
        pyxel.rect(mx, my-1, 1, 3, 2)

App()
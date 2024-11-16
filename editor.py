import pyperclip
import pyxel

class App:
    def __init__(self):
        pyxel.init(17, 17, title="Asset Editor")
        self.x = 0
        self.y = 0
        self.color = 6
        self.shiftlock = False

        self.matrix = ["0" * 16 for _ in range(16)]

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_UP):
            self.y -= 1
            if self.y < 0: self.y = 0 
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.y += 1
            if self.y > 15: self.y = 15
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.x += 1
            if self.x > 15: self.x = 15
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.x -= 1
            if self.x < 0: self.x = 0
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.flip()
        if pyxel.btnp(pyxel.KEY_O):
            self.color += 1
        if pyxel.btnp(pyxel.KEY_I):
            self.color -= 1
        if pyxel.btnp(pyxel.KEY_BACKSPACE):
            self.matrix = ["0" * 16 for _ in range(16)]
        if pyxel.btnp(pyxel.KEY_ALT):
            pyperclip.copy(str(self.matrix))
        if pyxel.btnp(pyxel.KEY_CTRL):
            self.shiftlock = not self.shiftlock

        self.color %= 15 
        
    def flip(self):
        line = list(self.matrix[self.y])
        line[self.x] = str(1-int(line[self.x]))
        self.matrix[self.y] = "".join(line)

    def draw(self):
        pyxel.cls(0)
        if pyxel.btn(pyxel.KEY_SHIFT) or self.shiftlock:
            pyxel.rect(1, self.y+1, 16, 1, 5)
            pyxel.rect(self.x+1, 1, 1, 16, 5)

        pyxel.rect(0, self.y+1, 1, 1, 1)
        pyxel.rect(self.x+1, 0, 1, 1, 1)
        pyxel.rect(self.x+1, self.y+1, 1, 1, 12)

        i = 0
        for line in self.matrix:
            i+=1
            j = 0
            for pixel in list(line):
                j+=1
                if pixel == "1":
                    pyxel.rect(j, i, 1, 1, self.color+1)


App()
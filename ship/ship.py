from kivy.graphics import Color, Triangle

ship=None


def ship(self):
    with self.canvas:
        Color(0, 0, 1)
        self.ship = Triangle()


def updateship(self):
    self.ship.points = [3 / 7 * self.width + self.currentoffsetx, 1 / 7 * self.height + self.currentoffsety1,
                        self.width / 2 + self.currentoffsetx, 2 / 7 * self.height + self.currentoffsety1,
                        4 / 7 * self.width + self.currentoffsetx, 1 / 7 * self.height + self.currentoffsety1]
def _keyboard_closed(self):
    self._keyboard.unbind(on_key_down=self._on_keyboard_down)
    self._keyboard = None





def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
    if keycode[1] == 'left':
        self.currentoffsetx = self.currentoffsetx - self.movementfactor*15*self.height/1000


    elif keycode[1] == 'right':
        self.currentoffsetx = self.currentoffsetx + self.movementfactor*15*self.height/1000

    elif keycode[1]=='down':
        self.currentoffsety1=self.currentoffsety1-self.movementfactor*15*self.height/1000

    elif keycode[1]=='up':
        self.currentoffsety1=self.currentoffsety1+self.movementfactor*15*self.height/1000


    return True

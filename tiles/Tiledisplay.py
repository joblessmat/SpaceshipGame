from kivy.graphics import Color, Quad
import random


def tile(self):
    with self.canvas:
        Color(1, 1, 1)

        for i in range(0, 3):
            self.tiles.append(Quad())


def gameover(self):
    self.currentoffsety=0
    self.currentoffsetz=0
    print("GAME OVER ")




def updatetile(self):
    self.scorestring = str(self.score)

    x1=1/7*self.width
    y1=self.height
    dx=1/7*self.width
    dy=1/7*self.height



    for i in range(0,3):




        self.tiles[i].points=[self.z*x1,y1+i*dy-self.currentoffsetz,self.z*x1,y1+(i+1)*dy-self.currentoffsetz,self.z*x1+dx,y1+(i+1)*dy-self.currentoffsetz,self.z*x1+dx,y1+i*dy-self.currentoffsetz]
        x111 = 3 / 7 * self.width + self.currentoffsetx  ##SHIP COORDINATE
        x222 = 4 / 7 * self.width + self.currentoffsetx
        y111 = 2/7*self.height + self.currentoffsety1
        y000 = 1/7 *self.height + self.currentoffsety1


        x11 = self.z * x1
        x22 = self.z * x1 + dx
        y11 = y1 + i * dy - self.currentoffsetz
        y22 = y11 + self.height/7


        if(((x111 >= x11 and x111<= x22 and y111 >=y11 and y000<=y22) or (x222 >= x11 and x222<= x22 and y111 >=y11 and y000<=y22) and (self.checkcountonce==0))):
            self.checkcount=self.checkcount+1
            if(self.checkcount/10000>0 and self.checkcount/10000 <1):
                self.checkcount=10000


            self.score=self.score+int(self.checkcount/10000)













        if (y1 + (2 + 1) * dy - self.currentoffsetz <0):


            if(self.checkcount!=0):

                if (self.score >= self.targetscore):
                    self.factor = self.factor * 1.25
                    self.targetscore = self.targetscore + 500
                    self.movementfactor=self.movementfactor*1.5


                self.checkcount = 0
                self.currentoffsetz = 0
                i = 0
                self.z = random.randrange(0, 7)

            else:
                self.stategamestarted = False
                self.menutitle="G  A  M  E    O  V  E  R"
                self.menubuttontitle="RESTART"
                self.soundgameoverimpact.play()
                self.soundmusic1.stop()



                self.checkcountonce+=1


                if(self.checkcountonce==1):
                    print("GAME OVER")
                    self.scorestring = str(self.score)


                self.currentoffsety=0





















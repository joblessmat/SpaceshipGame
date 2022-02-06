from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.graphics import Line, Color, Quad, Triangle
from kivy.lang import Builder
from kivy.properties import Clock, ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
import random




Builder.load_file("menu.kv")






class MainWidget(RelativeLayout):
    from updates import update1,update2
    from keyboard import _keyboard_closed,_on_keyboard_down


    from Tiledisplay import tile,updatetile
    from ship import ship,updateship

    stategamestarted = False
    menu_widget=ObjectProperty()


    def __init__(self,**kwargs):


        super(MainWidget,self).__init__(**kwargs) #WE USE THIS INIT FUNCTION TO TELL THE CLASS TO IMMEDIATELY RUN THIS FUNCTION

        self.sounds()

        self.tile()
        self.ship()


        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

        Clock.schedule_interval(self.update, 1 / 60)

    currentoffsety = 0
    currentoffsetx = 0
    currentoffsetz = 0
    currentoffsety1= 0
    numberofgames=0
    targetscore=500
    movementfactor=1





    linenum = 8
    linewidth = 0.1  # % of screen width

    z=random.randrange(0,7)

    vertiline = []
    horiline=[]
    tiles=[]
    checkcount = 0
    checkcountonce=0
    score=0
    speed_y=None

    menutitle=StringProperty("W 0 R K 1 N G    T 1 T l 3")
    scorestring = StringProperty(" 0")
    menubuttontitle=StringProperty("START")










    inc = 1

    def transform(self,x,y):
        return self.transformperspective(x,y)

    def transformperspective(self,x,y):
        tr_y= self.height
        return int(x),int(y)

    soundbegin=None
    soundgalaxy=None
    soundgameoverimpact=None
    soundgameovervoice=None
    soundmusic1=None
    soundrestart=None






    def startbutton(self):
        self.stategamestarted=True
        self.menu_widget.opacity = 0
        self.currentoffsetz=0
        self.currentoffsety=0
        self.checkcount=0
        self.checkcountonce=0
        self.score=0
        self.soundmusic1.play()
        self.movementfactor=1
        self.factor=1
        self.targetscore=0
        self.currentoffsetx=0
        self.currentoffsety1=0

    def sounds(self):

        self.soundgameoverimpact = SoundLoader.load("audio/gameover.wav")

        self.soundmusic1 = SoundLoader.load("audio/music1.wav")





    factor=1



    def update(self,dt):   #FIXTHEHORIZONTALPARTVALUES


        self.updatetile()
        self.updateship()

        if(self.stategamestarted==False):
            self.menu_widget.opacity=1

        if(self.stategamestarted==True):
            time_factor = dt * 60

            self.speed_y=8*self.height

            self.currentoffsety = self.currentoffsety + self.factor*self.speed_y * time_factor / 1000
            self.currentoffsetz = self.currentoffsetz + self.factor*self.speed_y * time_factor / 1000



            if (self.currentoffsety >= self.height / 7):
                self.currentoffsety = 0


class GalaxyApp(App):
    pass

GalaxyApp().run()














import pygame as pg
from .. import setup,tools

class Survive(tools._State):
    """This State is updated while our game shows the Survive screen."""
    def __init__(self):
        tools._State.__init__(self)

        self.title = self.render_font("Fixedsys500c",20,"Survive",(255,255,0))
        self.title_rect = self.title.get_rect(center=(setup.SCREEN_RECT.centerx,200))

        self.ne_key = self.render_font("Fixedsys500c",20,"[Press Any Key]",(255,255,0))
        self.ne_key_rect = self.ne_key.get_rect(center=(setup.SCREEN_RECT.centerx,500))
        self.blink = False
        self.timer = 0.0

    def render_font(self,font,size,msg,color=(255,255,255)):
        """Takes the name of a loaded font, the size, and the color and returns
       a rendered surface of the msg given."""
        selected_font = pg.font.Font(setup.FONTS[font],size)
        return selected_font.render(msg,1,color)

    def update(self,surface,keys,mouse):
        """Updates the title screen."""
        surface.fill((0,0,0))

        surface.blit(self.title, self.title_rect)
        if pg.time.get_ticks() - self.timer > 1000/5.0:
            self.blink = not self.blink
            self.timer = pg.time.get_ticks()
        if self.blink:
            surface.blit(self.ne_key,self.ne_key_rect)


    def get_event(self,event):
        """Get events from Control.  Currently changes to next state on any key
       press."""
        if event.type == pg.KEYDOWN:
            self.next = "MENU"
            self.done = True

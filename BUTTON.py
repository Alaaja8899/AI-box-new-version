import pygame as pyg,random,sys
#button class
class Button:
	def __init__(self,x,y,image,scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pyg.transform.scale(image,[width*scale,height*scale])
		self.rect = self.image.get_rect()
		self.rect.topleft = (x,y)
	def draw(self,surface):
		pos = pyg.mouse.get_pos()
		click = pyg.mouse.get_pressed()
		if self.rect.collidepoint(pos):
			if click[0] == 1:
				return True
		surface.blit(self.image,[self.rect.x,self.rect.y])

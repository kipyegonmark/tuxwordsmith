"""
/***************************************************************************

	Author			:Charles B. Cosse 
	
	Email			:ccosse@gmail.com
					
	Website			:www.asymptopia.org
	
	Copyright		:(C) 2002-2007 Asymptopia Software.
	
 ***************************************************************************/
"""

import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
	def __init__(self,name,tray,actor,solver):
		pygame.sprite.Sprite.__init__(self)

		self.name=name
		self.tray=tray
		self.actor=actor
		self.solver=solver
		self.score=0
		self.recording=0
		self.wait_counter=0
		self.mode=0
		
	def set_mode(self,mode):
		self.mode=mode

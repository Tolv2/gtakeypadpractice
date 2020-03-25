import os
from time import sleep,time
from random import shuffle
try:
	import pygame
except:
	os.system("pip install pygame")
	import pygame

Resolution=(1162,515)
PrintPos=(125,20)
ComponentPositions=[
None,
(570,20),
(718,20),
(866,20),
(1014,20),
(570,258),
(718,258),
(866,258),
(1014,258),
]
MenuPositions=[
(867,125),
(1063,125),
(971,173),
]
BoxPos=(971,208)
file=open("results.txt", "a")
CheckPos=(622, 450)
SuccPos=(550+266,465)
FailPos=(550+272,465)
Backdrop=(0,0,0)
class KeypadPractice():
	def __init__(self):
		pygame.init()
		self.display=pygame.display.set_mode(Resolution)
		pygame.display.set_caption("GTA Online - The Diamond Casino Heist | Fingerprint Hack Practice")
		self.display.fill(Backdrop)
		os.chdir(os.path.dirname(os.path.abspath(__file__))+"\\assets\\")
		self.mainMenu()
	def mainMenu(self):
		self.display.fill(Backdrop)
		menu=pygame.image.load("MainMenu.png")
		noBox=pygame.image.load("noBox.png")
		yesBox=pygame.image.load("yesBox.png")
		unselectMenu=pygame.image.load("unselectMenu.png")
		unBox=pygame.image.load("unBox.png")
		selectMenu=pygame.image.load("selectMenu.png")
		self.display.blit(menu, (0,0))
		delay=True
		self.display.blit(yesBox,BoxPos)
		menuPos=0
		self.display.blit(selectMenu, MenuPositions[0])
		pygame.display.update()
		broken=False
		while not broken:
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					quit()
				if event.type==pygame.KEYDOWN:
					self.display.blit(unselectMenu, MenuPositions[menuPos])
					key=event.key
					if key in [pygame.K_UP, pygame.K_LEFT]:
						menuPos=0
					if key==pygame.K_RIGHT:
						menuPos=1
					if key==pygame.K_DOWN:
						menuPos=2
					if key==pygame.K_RETURN:
						if menuPos==0:
							broken=True
							break
						if menuPos==1:
							quit()
						if menuPos==2:
							self.display.blit(unBox, BoxPos)
							if delay:
								delay=False
								self.display.blit(noBox, BoxPos)
							elif not delay:
								delay=True
								self.display.blit(yesBox, BoxPos)
					self.display.blit(selectMenu, MenuPositions[menuPos])
			pygame.display.update()
		self.main(delay)
	def main(self, wait):
		select=pygame.image.load("select.png")
		unselect=pygame.image.load("unselect.png")
		check=pygame.image.load("check.png")
		uncheck=pygame.image.load("uncheck.png")
		success=pygame.image.load("success.png")
		unresult=pygame.image.load("unsuccessfail.png")
		fail=pygame.image.load("fail.png")
		self.display.fill(Backdrop)
		theOrder=list(range(1,5))
		shuffle(theOrder)
		while True:
			for i in theOrder:
				self.display.fill(Backdrop)
				solved=False
				os.chdir(str(i))
				pattern=pygame.image.load("print.png")
				self.display.blit(pattern, PrintPos)
				order=list(range(1,9))
				shuffle(order)
				on=list()
				off=list()
				for x in range(1,9):
					curr="component"+str(order[x-1])+".png"
					off.append(pygame.image.load(curr))
					curr="component"+str(order[x-1])+"s.png"
					on.append(pygame.image.load(curr))
					self.display.blit(off[x-1], ComponentPositions[x])
				pygame.display.update()
				solution=[0,0,0,0,0,0,0,0]
				for x in range(len(order)):
					if order[x] in [5,6,7,8]:
						solution[x]=1
				currentPos=1
				selections=[0,0,0,0,0,0,0,0]
				self.display.blit(select, self.alter(ComponentPositions[1], -5, -5))
				pygame.display.update()
				start=time()
				while not solved:
					for event in pygame.event.get():
						if event.type==pygame.QUIT:
							file.close()
							quit()
						if event.type==pygame.KEYDOWN:
							key=event.key
							if key==pygame.K_ESCAPE:
								os.chdir("..")
								self.mainMenu()
							if key==pygame.K_RETURN:
								if selections[currentPos-1]==1:
									self.display.blit(off[currentPos-1], ComponentPositions[currentPos])
									selections[currentPos-1]=0
								else:
									self.display.blit(on[currentPos-1], ComponentPositions[currentPos])
									selections[currentPos-1]=1
							pygame.display.update()
							if key in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN]:
								self.display.blit(unselect, self.alter(ComponentPositions[currentPos], -5, -5))
								if key==pygame.K_RIGHT and not(currentPos in [4,8]):
									currentPos+=1
								elif key==pygame.K_LEFT and not(currentPos in [1,5]):
									currentPos-=1
								elif key==pygame.K_UP and not(currentPos in [1,2,3,4]):
									currentPos-=4
								elif key==pygame.K_DOWN and not(currentPos in [5,6,7,8]):
									currentPos+=4
								self.display.blit(select, self.alter(ComponentPositions[currentPos], -5, -5))
							if key==pygame.K_TAB and selections.count(1)==4:
								if wait:
									self.display.blit(check, CheckPos)
									pygame.display.update()
									sleep(3)
								if selections==solution:
									score=time()-start
									score=list(str(score))
									newscore=str()
									for x in range(4):
										newscore+=score[x]
									file.write(str(newscore)+" s\n")
									self.display.blit(pygame.font.Font(None, 21).render((newscore+" s"), 1, (255,255,255)), self.alter(SuccPos, 65, -2))
									self.display.blit(success, SuccPos)
									pygame.display.update()
									sleep(1)
									solved=True
								else:
									self.display.blit(fail, FailPos)
									pygame.display.update()
									sleep(1)
								self.display.blit(uncheck, CheckPos)
								self.display.blit(unresult, SuccPos)
						pygame.display.update()
				os.chdir("..")
	def alter(self, inp, x,y):
		o1=inp[0]+x
		o2=inp[1]+y
		return (o1,o2)
if __name__ == '__main__':
	running = KeypadPractice() 
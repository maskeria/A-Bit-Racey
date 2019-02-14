import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (200, 0, 0)
purple = (128,0,128)
green = (0, 200, 0)
sentdex = (53, 115, 200)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_sentdex = (73, 135, 255)

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('A bit racey')

clock = pygame.time.Clock()

carImg = pygame.image.load('car.png')
car_width = 80
car_height = 110
carImg = pygame.transform.scale(carImg, (car_width, car_height))


def things_dodged(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render("Dodged: " + str(count), True, white)
	gameDisplay.blit(text, (0,0))

def things(thingx, thingy, thingw, thingh, color):
	pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
################ make things coming from all direction
	
	
def button(msg, x, y, w, h, ic, ac, action=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	#print(click + mouse)
	
	
	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		
		pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
		if click[0] == 1 and action != None:
			action()
	else:
		pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
	
	smallText = pygame.font.Font("freesansbold.ttf",20)
	textSurf, textRect = text_objects(msg, smallText)
	textRect.center = ( (x+(w/2)), (y+(h/2)) )
	gameDisplay.blit(textSurf, textRect)
		
		
#############make a start screen function 
def game_intro():
	
	intro = True
	
	while intro:
		for event in pygame.event.get():
			#print(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
		gameDisplay.fill(black)
		largeText =  pygame.font.Font('freesansbold.ttf', 115)
		textSurf, textRect = text_objects("A Bit Racey", largeText) #still need to make text object function
		textRect.center = ((display_width/2), (display_height/2))
		gameDisplay.blit(textSurf, textRect)
		
		button("Go!", 150, 500, 100, 50, green, bright_green, game_loop)
		button("Quit :(", 550, 500, 100, 50, red, bright_red, quitGame)
		button("Instructions", 325, 500, 140, 50, sentdex, bright_sentdex, instructions)
		
		
			
		pygame.display.update()
		clock.tick(15)

def instructions():
	instruct = True
	while instruct:
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				
		gameDisplay.fill(black)
		message_display("USE ARROW KEYS TO MOVE", 50)
		
		button("Go!", 150, 500, 100, 50, green, bright_green, game_loop)
		button("Quit :(", 550, 500, 100, 50, red, bright_red, quitGame)
			
		pygame.display.update()
		clock.tick(15)



def quitGame():
	pygame.quit()
	quit()
		
def car(x,y):
	gameDisplay.blit(carImg, (x,y))
	

def text_objects(text, font):
	textSurface = font.render(text, True, white) #included with pygame
	return textSurface, textSurface.get_rect()
	
def message_display(text, size):
	largeText =  pygame.font.Font('freesansbold.ttf', size)
	textSurf, textRect = text_objects(text, largeText) #still need to make text object function
	textRect.center = ((display_width/2), (display_height/2))
	gameDisplay.blit(textSurf, textRect)
	
	pygame.display.update()
	
	#time.sleep(1)
	
	#game_loop()
	

def crash():
	message_display('YOU CRASHED', 100)
	time.sleep(1)
	game_intro()
	
def game_loop(): #this is now the game loop

	x = (display_width * 0.45)
	y = (display_height * 0.8)
	
	x1 = 0
	x2 = 0
	y1 = 0
	y2 = 0
	
	thing_startx = random.randrange(0, display_width)
	thing_starty = -600
	thing_speed = 4
	thing_width = 100
	thing_height = 100
	
	dodged = 0
	

	gameExit = False

	while not gameExit:#game loop, not anymore
		
		for event in pygame.event.get(): #logic loop
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
			###########  Event Handler
			
			if event.type == pygame.KEYUP: #For when keys not pressed
				if event.key == pygame.K_LEFT:
					x1 = 0
				if event.key == pygame.K_RIGHT:
					x2 = 0
				if event.key == pygame.K_UP:
					y1 = 0
				if event.key == pygame.K_DOWN:
					y2 = 0
			if event.type == pygame.KEYDOWN: #for when keys pressed
				if event.key == pygame.K_LEFT:
					x1 = -5
				if event.key == pygame.K_RIGHT:
					x2 = 5
				if event.key == pygame.K_UP:
					y1 = -5
				if event.key == pygame.K_DOWN:
					y2 = 5
			############			

		x += x1 + x2
		y += y1 + y2
			
		gameDisplay.fill(black)
		
		
		#things(thingx, thingy, thingw, thingh, color)
		things(thing_startx, thing_starty, thing_width, thing_height, sentdex)
		thing_starty += thing_speed
		car(x,y)
		things_dodged(dodged)
		
		#Questionnaire / logic
		
		if x > display_width - car_width or x < 0 or y > display_height-car_height or y < 0:
			
			crash()
			
		if thing_starty > display_height:
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0, display_width)
			dodged += 1
			thing_speed += 0.7
			thing_width += (dodged * 1.1)
			#########we can also change the width randomly
			
		
		if y < thing_starty + thing_height - 15 and y > thing_starty :
			#print('y crossover')
			
			if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x+car_width < thing_startx + thing_width:
				crash()
		
		
		pygame.display.update()
		clock.tick(60)

	
game_intro()
game_loop()	
pygame.quit()
quit()


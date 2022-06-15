#Tic Tac Toe with Images
import pygame
from pygame.locals import *


pygame.init()

HEIGHT = 700
WIDTH = 700
line_width = 10
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')


colors={"lightyellow":(252, 243, 207),"black":(51,0,102),"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51), "cream":(255, 255, 210),"cyan":(5, 156, 150)}
#colors
#print(pygame.font.get_fonts())
# white=(255,255,51)
# blue= (204, 255, 229)
# green= (74, 189, 41)
# yellow= (0, 102, 204)
# red= (255, 51, 153)
# purple= (158, 98, 170)
# npurple= (102,102,255)1
# lightpink=(250, 219, 216)

#define fonts
SCORE_FONT = pygame.font.SysFont('comicsans', 60)
INFO_FONT = pygame.font.SysFont('comicsansms', 19)
WIN_FONT = pygame.font.SysFont('comicsansms', 45)
STAR_FONT = pygame.font.SysFont('comicsansms', 18)
MENU_FONT = pygame.font.SysFont('comicsans', 35)
CHOICE_FONT = pygame.font.SysFont('comicsans', 45)
TITLE_FONT = pygame.font.SysFont('comicsans', 50)

pygame


#define variables
clicked = False
player = 1
pos = (0,0)
markers = []
game_over = False
winner = 0
xClr=colors.get("pink")
Oclr=colors.get("blue")
#setup a rectangle for "Play Again" Option
again_rect = Rect(WIDTH // 2 - 80, HEIGHT // 2, 160, 50)
X_Img=pygame.image.load("pygameFiles\Images\mark-XBlack.png")
X_Img=pygame.transform.scale(X_Img,(WIDTH//3-10,WIDTH//3-10))
O_Img=pygame.image.load("pygameFiles\Images\mark-O.png")
O_Img=pygame.transform.scale(O_Img,(WIDTH//3-10,WIDTH//3-10))

#create empty 3 x 3 list to represent the grid
def zeroGrid():
	for x in range (3):
		row = [0] * 3
		markers.append(row)

def instr():
    print("in instr")
    screen.fill(colors.get("white"))
    myFile=open('pygameFiles\inst.txt', 'r')
    yi=50
    stuff= myFile.readlines()
    bg=colors.get("black")
    
    for line in stuff:
        line=line[0:len(line)-1]
        text=STAR_FONT.render(line, True,bg )
        screen.blit(text, (40,yi))
        pygame.display.update()
        pygame.time.delay(50)
        yi+=50
    myFile.close()
    
    pygame.time.delay(5000)
def draw_board():
	bg = colors.get("cream")
	gridClr = colors.get("cyan")
	screen.fill(bg)
	for x in range(1,3):
		pygame.draw.line(screen, gridClr, (0, WIDTH//3 * x), (WIDTH,WIDTH//3 * x), line_width)
		pygame.draw.line(screen, gridClr, (HEIGHT//3 * x, 0), (HEIGHT//3 * x, HEIGHT), line_width)

def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:

                #screen.blit(X_Img,(x_pos * WIDTH//3+5 , y_pos * WIDTH//3+5 ))
				pygame.draw.line(screen, xClr, (x_pos * WIDTH//3 + 15, y_pos * WIDTH//3 + 15), (x_pos * WIDTH//3 + WIDTH//3-15, y_pos * WIDTH//3 + WIDTH//3-15), line_width)
				pygame.draw.line(screen, xClr, (x_pos * WIDTH//3 + WIDTH//3-15, y_pos * WIDTH//3 + 15), (x_pos * WIDTH//3 + 15, y_pos * WIDTH//3 + WIDTH//3-15), line_width)
            if y == -1:
                screen.blit(O_Img,(x_pos * WIDTH//3+5 , y_pos * WIDTH//3+5))
            	pygame.draw.circle(screen, Oclr, (x_pos * WIDTH//3 + WIDTH//6, y_pos * WIDTH//3 + WIDTH//6), WIDTH//6-25, line_width)
            y_pos += 1
        x_pos += 1	


def check_game_over():
	global game_over
	global winner

	x_pos = 0
	for x in markers:
		#check columns
		if sum(x) == 3:
			winner = 1
			game_over = True
		if sum(x) == -3:
			winner = 2
			game_over = True
		#check rows
		if markers[0][x_pos] + markers [1][x_pos] + markers [2][x_pos] == 3:
			winner = 1
			game_over = True
		if markers[0][x_pos] + markers [1][x_pos] + markers [2][x_pos] == -3:
			winner = 2
			game_over = True
		x_pos += 1

	#check cross
	if markers[0][0] + markers[1][1] + markers [2][2] == 3 or markers[2][0] + markers[1][1] + markers [0][2] == 3:
		winner = 1
		game_over = True
	if markers[0][0] + markers[1][1] + markers [2][2] == -3 or markers[2][0] + markers[1][1] + markers [0][2] == -3:
		winner = 2
		game_over = True

	#check for tie
	if game_over == False:
		tie = True
		for row in markers:
			for i in row:
				if i == 0:
					tie = False
		#if it is a tie, then call game over and set winner to 0 (no one)
		if tie == True:
			game_over = True
			winner = 0


def draw_game_over(winner):def
    end_text=" "
    if winner != 0:
        end_text = "   Player " + str(winner) + " wins!"
    elif winner == 0:
        end_text = "   You have tied!"
    green=colors.get("limeGreen")
    end_img = INFO_FONT.render(end_text, True, colors.get("blue"))
    pygame.draw.rect(screen, green, (WIDTH // 2 - 100, HEIGHT // 2 - 60, 200, 50))
    screen.blit(end_img, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
    
    again_text = '   Play Again?'
    again_img = INFO_FONT.render(again_text, True, colors.get("blue"))
    pygame.draw.rect(screen, green, again_rect)
    screen.blit(again_img, (WIDTH // 2 - 80, HEIGHT // 2 + 10))
instr()

#main loop
run = True
while run:
	#draw board and markers first
	draw_board()
	draw_markers()
	#handle events
	for event in pygame.event.get():
		#handle game exit
		if event.type == pygame.QUIT:
			run = False
		#run new game
		if game_over == False:
			#check for mouseclick
			if event.type == pygame.MOUSEBUTTONDOWN: 
				pos = pygame.mouse.get_pos()
				cell_x = pos[0] // (WIDTH//3)
				cell_y = pos[1] // (WIDTH//3)
				if markers[cell_x][cell_y] == 0:
					markers[cell_x][cell_y] = player
					player *= -1
					check_game_over()

	#check if game has been won
	if game_over == True:
		draw_game_over(winner)
		#check for mouseclick to see if we clicked on Play Again
		if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
			clicked = True
		if event.type == pygame.MOUSEBUTTONUP and clicked == True:
			clicked = False
			pos = pygame.mouse.get_pos()
			if again_rect.collidepoint(pos):
				#reset variables
				game_over = False
				player = 1
				pos = (0,0)
				markers = []
				winner = 0
				#create empty 3 x 3 list to represent the grid
				zeroGrid()

	#update display
	pygame.display.update()

pygame.quit()
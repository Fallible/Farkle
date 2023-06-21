import pygame, sys, time, random
from pygame.locals import *

# Set up pygame
pygame.init()
mainClock = pygame.time.Clock()
FPS = 60
TEXTCOLOR = (0, 0, 0)
BACKGROUNDCOLOR = (0, 128, 0)

# Global variables
scoring_rule = []

# Set up the window
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Farkle')
pygame.mouse.set_visible(True)

# Set up font
font = pygame.font.SysFont(None, 48)

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: 
                    terminate()
                return
            
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# players are going to be an object
class player():
    player_id = 0
    player_name = ""
    banked_points = 0
    turn_points_pre_banked = 0
    on_table_points = 0
    current_hand = []

# Set up the Die object definition
class d6_die():
    current_value = 0
    die_value_range = 6
    die_image = None
    die_image_transformed = None
    die_rect = None
    keep_die = False

# Set image to die roll
def set_image_to_roll(die, current_value):
    if current_value == 1:
        die.die_image = pygame.image.load('Farkle\\assets\one_die.bmp')
    if current_value == 2:
        die.die_image = pygame.image.load('Farkle\\assets\\two_die.bmp')
    if current_value == 3:
        die.die_image = pygame.image.load('Farkle\\assets\\three_die.bmp')
    if current_value == 4:
        die.die_image = pygame.image.load('Farkle\\assets\\four_die.bmp')
    if current_value == 5:
        die.die_image = pygame.image.load('Farkle\\assets\\five_die.bmp')
    if current_value == 6:
        die.die_image = pygame.image.load('Farkle\\assets\six_die.bmp')
    die.die_img_transformed = pygame.transform.scale(die.die_image, (WINDOWHEIGHT / 5, WINDOWHEIGHT / 5))        

# Change image on die selection
def change_image_selected(die, current_value):
    if current_value == 1:
        die.die_image = pygame.image.load('Farkle\\assets\one_die_selected.bmp')
    if current_value == 2:
        die.die_image = pygame.image.load('Farkle\\assets\\two_die_selected.bmp')
    if current_value == 3:
        die.die_image = pygame.image.load('Farkle\\assets\\three_die_selected.bmp')
    if current_value == 4:
        die.die_image = pygame.image.load('Farkle\\assets\\four_die_selected.bmp')
    if current_value == 5:
        die.die_image = pygame.image.load('Farkle\\assets\\five_die_selected.bmp')
    if current_value == 6:
        die.die_image = pygame.image.load('Farkle\\assets\six_die_selected.bmp')
    die.die_img_transformed = pygame.transform.scale(die.die_image, (WINDOWHEIGHT / 5, WINDOWHEIGHT / 5))     

# Die positions top left
d1_saved = (WINDOWWIDTH / 20, WINDOWHEIGHT / 5)
d2_saved = ((WINDOWWIDTH / 20) + (3 * WINDOWWIDTH / 20), WINDOWHEIGHT / 5)
d3_saved = ((WINDOWWIDTH / 20) + (6 * WINDOWWIDTH / 20), WINDOWHEIGHT / 5)
d4_saved = ((WINDOWWIDTH / 20) + (9 * WINDOWWIDTH / 20), WINDOWHEIGHT / 5)
d5_saved = ((WINDOWWIDTH / 20) + (12 * WINDOWWIDTH / 20), WINDOWHEIGHT / 5)
d6_saved = ((WINDOWWIDTH / 20) + (15 * WINDOWWIDTH / 20), WINDOWHEIGHT / 5)
d1_current_hand = (WINDOWWIDTH / 20, (WINDOWHEIGHT / 5) + 2 * (WINDOWHEIGHT / 5))
d2_current_hand = ((WINDOWWIDTH / 20) + (3 * WINDOWWIDTH / 20), (WINDOWHEIGHT / 5) + 2 * (WINDOWHEIGHT / 5))
d3_current_hand = ((WINDOWWIDTH / 20) + (6 * WINDOWWIDTH / 20), (WINDOWHEIGHT / 5) + 2 * (WINDOWHEIGHT / 5))
d4_current_hand = ((WINDOWWIDTH / 20) + (9 * WINDOWWIDTH / 20), (WINDOWHEIGHT / 5) + 2 * (WINDOWHEIGHT / 5))
d5_current_hand = ((WINDOWWIDTH / 20) + (12 * WINDOWWIDTH / 20), (WINDOWHEIGHT / 5) + 2 * (WINDOWHEIGHT / 5))
d6_current_hand = ((WINDOWWIDTH / 20) + (15 * WINDOWWIDTH / 20), (WINDOWHEIGHT / 5) + 2 * (WINDOWHEIGHT / 5))

# Create new player function
def create_new_player():
    new_player = player()
    new_player.player_id = len(players) + 1
    players.append(new_player)

# Define end of turn (fail)
def fail_turn_end(player_id):
    players[player_id].on_table_points = 0

# Define rolling a die
def roll_die(die):
    roll_value = random.randint(1, die.die_value_range)
    die.current_value = roll_value
    set_image_to_roll(die, roll_value)

# roll up new hand
def roll_new_hand(player_id):
    players[player_id].current_hand.clear()
    for die in range(6):
        new_die = d6_die()
        roll_die(new_die)
        new_die.die_image_transformed = pygame.transform.scale(new_die.die_image, (WINDOWHEIGHT / 5, WINDOWHEIGHT / 5))
        new_die.die_rect = new_die.die_image_transformed.get_rect()
        if die == 0:
            new_die.die_rect.topleft = d1_current_hand
        if die == 1:
            new_die.die_rect.topleft = d2_current_hand
        if die == 2:
            new_die.die_rect.topleft = d3_current_hand
        if die == 3:
            new_die.die_rect.topleft = d4_current_hand
        if die == 4:
            new_die.die_rect.topleft = d5_current_hand
        if die == 5:
            new_die.die_rect.topleft = d6_current_hand                                                            
        players[player_id].current_hand.append(new_die)

# Show the splash screen
windowSurface.fill(BACKGROUNDCOLOR)
drawText('Farkle', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('Press a key to roll first hand.', font, windowSurface, (WINDOWWIDTH /3) -30, (WINDOWHEIGHT /3) + 50)
pygame.display.update()
waitForPlayerToPressKey()


# Define scoring options.  Return name of scoring rule and list of active dice.
# def evaluate_scoring_options(current_hand, scoring_rule):
    

# Set state for initial launch of the game
keep_die_1 = keep_die_2 = keep_die_3 = keep_die_4 = keep_die_5 = keep_die_6 = False
IS_LAST_TURN = False
players = []
players.append(create_new_player())
roll_new_hand(0)

# Draw a blank board upon which elements will be added
windowSurface.fill(BACKGROUNDCOLOR)

# Draw the banked points score
drawText('Points in bank: %s' % (players[0].banked_points), font, windowSurface, 10, 10)
drawText('Current turn points: %s' % (players[0].turn_points_pre_banked), font, windowSurface, 10, 50)

# Hacky section of one-off code to format placement of dice on game board
#test_die_img_transformed = pygame.transform.scale(players[0].current_hand[0].die_image, (WINDOWHEIGHT / 5, WINDOWHEIGHT / 5))
#test_die_img_transformed1 = pygame.transform.scale(players[0].current_hand[1].die_image, (WINDOWHEIGHT / 5, WINDOWHEIGHT / 5))
#test_die_img_transformed2 = pygame.transform.scale(players[0].current_hand[2].die_image, (WINDOWHEIGHT / 5, WINDOWHEIGHT / 5))
#test_die_img_transformed3 = pygame.transform.scale(players[0].current_hand[3].die_image, (WINDOWHEIGHT / 5, WINDOWHEIGHT / 5))
#test_die_img_transformed4 = pygame.transform.scale(players[0].current_hand[4].die_image, (WINDOWHEIGHT / 5, WINDOWHEIGHT / 5))
#test_die_img_transformed5 = pygame.transform.scale(players[0].current_hand[5].die_image, (WINDOWHEIGHT / 5, WINDOWHEIGHT / 5))
#windowSurface.blit(test_die_img_transformed, players[0].current_hand[0].die_rect)
#windowSurface.blit(test_die_img_transformed1, players[0].current_hand[1].die_rect)
#windowSurface.blit(test_die_img_transformed2, players[0].current_hand[2].die_rect)
#windowSurface.blit(test_die_img_transformed3, players[0].current_hand[3].die_rect)
#windowSurface.blit(test_die_img_transformed4, players[0].current_hand[4].die_rect)
#windowSurface.blit(test_die_img_transformed5, players[0].current_hand[5].die_rect)
#players[0].current_hand[0].die_rect.topleft = (WINDOWWIDTH / 14, WINDOWHEIGHT / 5)
#players[0].current_hand[1].die_rect.topleft = ((WINDOWWIDTH / 14) + (2 * WINDOWWIDTH / 14), WINDOWHEIGHT / 5)
#players[0].current_hand[2].die_rect.topleft = ((WINDOWWIDTH / 14) + (4 * WINDOWWIDTH / 14), WINDOWHEIGHT / 5)
#players[0].current_hand[3].die_rect.topleft = ((WINDOWWIDTH / 14) + (6 * WINDOWWIDTH / 14), WINDOWHEIGHT / 5)
#players[0].current_hand[4].die_rect.topleft = ((WINDOWWIDTH / 14) + (8 * WINDOWWIDTH / 14), WINDOWHEIGHT / 5)
#players[0].current_hand[5].die_rect.topleft = ((WINDOWWIDTH / 14) + (10 * WINDOWWIDTH / 14), WINDOWHEIGHT / 5)
#windowSurface.blit(test_die_img_transformed, players[0].current_hand[0].die_rect)
#windowSurface.blit(test_die_img_transformed1, players[0].current_hand[1].die_rect)
#windowSurface.blit(test_die_img_transformed2, players[0].current_hand[2].die_rect)
#windowSurface.blit(test_die_img_transformed3, players[0].current_hand[3].die_rect)
#windowSurface.blit(test_die_img_transformed4, players[0].current_hand[4].die_rect)
#windowSurface.blit(test_die_img_transformed5, players[0].current_hand[5].die_rect)

# windowSurface.blit(test_die_img_transformed, )

pygame.display.update()
waitForPlayerToPressKey()

while True:
    # Game is running loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
        
            if event.type == KEYDOWN:
                if event.type == K_1 and not players[0].current_hand[0].keep_die:
                    players[0].current_hand[0].keep_die = True
                    windowSurface.blit(players[0].current_hand[0].die_img_transformed, players[0].current_hand[0].die_rect)
                if event.type == K_2 and not players[0].current_hand[1].keep_die:
                    players[0].current_hand[1].keep_die = True
                    windowSurface.blit(players[0].current_hand[1].die_img_transformed, players[0].current_hand[1].die_rect)
                if event.type == K_3 and not players[0].current_hand[2].keep_die:
                    players[0].current_hand[2].keep_die = True 
                    windowSurface.blit(players[0].current_hand[2].die_img_transformed, players[0].current_hand[2].die_rect)
                if event.type == K_4 and not players[0].current_hand[3].keep_die:
                    players[0].current_hand[3].keep_die = True
                    windowSurface.blit(players[0].current_hand[3].die_img_transformed, players[0].current_hand[3].die_rect)
                if event.type == K_5 and not players[0].current_hand[4].keep_die:
                    players[0].current_hand[4].keep_die = True
                    windowSurface.blit(players[0].current_hand[4].die_img_transformed, players[0].current_hand[4].die_rect)
                if event.type == K_6 and not players[0].current_hand[5].keep_die:
                    players[0].current_hand[5].keep_die = True
                    windowSurface.blit(players[0].current_hand[5].die_img_transformed, players[0].current_hand[5].die_rect)
                
        # Draw a clear window
        windowSurface.fill(BACKGROUNDCOLOR)

        # Draw the banked points score
        drawText('Points in bank: %s' % (players[0].banked_points), font, windowSurface, 10, 10)
        drawText('Current turn points: %s' % (players[0].turn_points_pre_banked), font, windowSurface, 10, 50)
        
        # Draw dice
        for die in players[0].current_hand:
            windowSurface.blit(die.die_img_transformed, die.die_rect)

        pygame.display.update()

        mainClock.tick(FPS)

        # Stop the game and show "Game Over" screen
        drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
        drawText('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
        pygame.display.update()
        waitForPlayerToPressKey()
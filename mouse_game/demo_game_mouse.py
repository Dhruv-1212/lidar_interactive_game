import pygame
from pygame import mixer
import time
import pygame.font

from pygame.locals import *

start_time = pygame.time.get_ticks()

#Initialization
pygame.init()

#Screen creation
screen = pygame.display.set_mode((1200,700))

#landing page image
land_image = pygame.image.load("img/land_image.jpg")

'''Background sound'''
mixer.music.load("img/smilee.mp3")
mixer.music.play(-1)

#page_2
char_s_image = pygame.image.load("img/Premium-Vector-Happy-cute-little-kid-study-alphabet-character.png")
char_s_image_status = 0

#page_3
char_s_scene = pygame.image.load("img/first_image.jpg")
char_s_scene_status = 0
s_command = mixer.sound("sound/s_command.mp3")
a_command = mixer.sound("sound/a_command.mp3")
t_command = mixer.sound("sound/t_command.mp3")

apple_intro= pygame.image.load("img/apple_intro.jpg")
apple_intro_colour= pygame.image.load("img/apple_intro_colour.jpg")
soap_intro=pygame.image.load("img/soap_intro.jpg")
soap_intro_colour=pygame.image.load("img/soap_intro_colour.jpg")
spoon_intro=pygame.image.load("img/spoon_intro.jpg")
spoon_intro_colour=pygame.image.load("img/spoon_intro_colour.jpg")
socks_intro=pygame.image.load("img/socks_intro.jpg")
socks_intro_colour=pygame.image.load("img/socks_intro_colour.jpg")
#page5
night_scene_image = pygame.image.load("img/night_scene.jpg")
night_scene_image_status = 0 #currently inactive

#page_7
forest_scene_image = pygame.image.load("img/forest_scene_image.jpg")
forest_scene_status = 0 #currently inactive

#page 9
branch_scene_image = pygame.image.load("img/branch_scene.jpg")

#page 11
stars_scene = pygame.image.load("img/stars_scene.jpg")

# -----------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
# char a image
char_a_image = pygame.image.load("img/char_a_image.png")
a1_scene = pygame.image.load("img/a1_scene.png")
a1_apples = pygame.image.load("img/a1_apples.png")
a1_axe = pygame.image.load("img/a1_axe.png")
a1_ant = pygame.image.load("img/a1_ant.png")

a2_scene = pygame.image.load("img/a2_scene.png")
a2_apples = pygame.image.load("img/a2_apples.png")
a2_axe = pygame.image.load("img/a2_axe.png")
a2_alligator = pygame.image.load("img/a2_alligator.png")
a2_ant = pygame.image.load("img/a2_ant.png")

a3_scene = pygame.image.load("img/a3_scene.png")
a3_arrow = pygame.image.load("img/a3_arrow.png")

a4_scene = pygame.image.load("img/a4_scene.png")
a4_ambulance = pygame.image.load("img/a4_ambulance.png")

summary_apples=pygame.image.load("img/apple_summary.png")

t1_scene = pygame.image.load("img/t1_scene.jpg")
t1_table = pygame.image.load("img/t1_table.png")
t1_tent = pygame.image.load("img/t1_tent.png")
t1_tiger = pygame.image.load("img/t1_tiger.png")
scaling_factor = 0.85
original_size = t1_tiger.get_size()
new_size = (int(original_size[0] * scaling_factor), int(original_size[1] * scaling_factor))

t1_tiger = pygame.transform.scale(t1_tiger, new_size)
t1_tomato = pygame.image.load("img/t1_tomato.png")

t2_scene = pygame.image.load("img/t2_scene.png")
t2_table = pygame.image.load("img/t2_table.png")
t2_tent = pygame.image.load("img/t2_tent.png")
t2_tree = pygame.image.load("img/t2_tree.png")


t3_scene = pygame.image.load("img/t3_scene.png")
t3_table = pygame.image.load("img/t3_table.png")
t3_tap = pygame.image.load("img/t3_tap.png")
t3_tie = pygame.image.load("img/t3_tie.png")
t3_toad = pygame.image.load("img/t3_toad.png")

#Setting the Title
pygame.display.set_caption("Game")

#Setting the icon
icon_image = pygame.image.load("img/languages.png")
pygame.display.set_icon(icon_image)

#Sun Image Load
sun_image = pygame.image.load("img/final_sun_image.jpg")

#Snake Image Load
snake_image = pygame.image.load("img/snake.jpg")
forest_snake_image = pygame.image.load("img/forest_snake.jpg")

#Swing Image Load
swing_image = pygame.image.load("img/swing.jpg")

#Stone Image Load
stone_image = pygame.image.load("img/stone_image.jpg")
forest_stone_image = pygame.image.load("img/forest_stone.jpg")

#spider image load
spider_image = pygame.image.load("img/spider.jpg")
forest_spider_image = pygame.image.load("img/forest_spider.jpg")

#stars image load
stars_image = pygame.image.load("img/stars.jpg")
six_image = pygame.image.load("img/six.png")
superstar_sound = mixer.sound("sound/superstar.mp3")
try_sound = mixer.sound("sound/try.mp3")

#empty screen image for branches number
white_band = pygame.image.load("img/empty_screen.png")

#font for the text of the buttons
font = pygame.font.Font("freesansbold.ttf",28)

font_num = pygame.font.Font("freesansbold.ttf",56)

font2 = pygame.font.Font("freesansbold.ttf",32)
font3 = pygame.font.Font("freesansbold.ttf",48)
font4 = pygame.font.Font("freesansbold.ttf",84)

# winner image load
winner_image_new=pygame.image.load("img/animal_img.jpg")
# winner_image = pygame.image.load("img/46141 (1).jpg")
# winner_image_new = pygame.image.load("img/win2.png")
# winner_image_new = pygame.image.load("img/win3.png")
# winner_image_new = pygame.image.load("img/win4.png")
# winner_image_new = pygame.image.load("img/win5.png")
# winner_image_new = pygame.image.load("img/win6.png")
# winner_image_new = pygame.image.load("img/win7.png")
# winner_image_new = pygame.image.load("img/win8.png")
# winner_image_new = pygame.image.load("img/win9.png")
# winner_image_new = pygame.image.load("img/win10.png")
# winner_image_new = pygame.image.load("img/win11.png")
# winner_image_new = pygame.image.load("img/win9.png")

#sakshar image
sakshar_image = pygame.image.load("img/SAKSHAR.jpg")
# hint_light=pygame.image.load("img/hint_light.png")
#text names of the images
font_new = pygame.font.Font("freesansbold.ttf", 42)
sun_text = font_new.render("sun", True, (255,128, 0))
stone_text = font_new.render("stones", True, (102,0,204))
swing_text = font_new.render("swing", True, (210,0,0))
snake_text = font_new.render("snake", True, (0,160,0))
spider_text = font_new.render("spider",True,(0,0,200))
forest_spider_text = font_new.render("spider",True,(240,30,30))
stars_text = font_new.render("stars",True,(240,230,30))
six_text = font_new.render("six",True,(0,0,200))


#a1_scene
ant_sound = mixer.sound("sound/ant_sound.mp3")
apples_sound = mixer.sound("sound/apples_sound.mp3")
axe_sound = mixer.sound("sound/axe_sound.mp3")
apples_text = font_new.render("apples", True, (205,10,10))
axe_text = font_new.render("axe", True, (70,70,70))
ant_text = font_new.render("ant", True, (153,0,76))


#a2_scene
ant_sound = mixer.sound("sound/ant_sound.mp3")
apples_sound = mixer.sound("sound/apples_sound.mp3")
axe_sound = mixer.sound("sound/axe_sound.mp3")
alligator_sound = mixer.sound("sound/alligator_sound.mp3")
alligator_text = font_new.render("alligator", True, (0,155,0))
apples_text = font_new.render("apples", True, (205,10,10))
axe_text = font_new.render("axe", True, (70,70,70))
ant_text = font_new.render("ant", True, (153,0,76))

#a3scene
arrow_sound = mixer.sound("sound/arrow_sound.mp3")
arrow_text = font_new.render("arrow", True, (255,128,0))

#a4scene
ambulance_sound = mixer.sound("sound/ambulance_sound.mp3")
ambulance_text = font_new.render("ambulance", True, (0,100,210))

#tmodule
t_char_image = pygame.image.load("img/t_char.png")
table_sound = mixer.sound("sound/table_sound.mp3")
tap_sound = mixer.sound("sound/tap_sound.mp3")
tent_sound = mixer.sound("sound/tent_sound.mp3")
tie_sound = mixer.sound("sound/tie_sound.mp3")
tiger_sound = mixer.sound("sound/tiger_sound.mp3")
toad_sound = mixer.sound("sound/toad_sound.mp3")
tomatoes_sound = mixer.sound("sound/tomatoes_sound.mp3")
tree_sound = mixer.sound("sound/tree_sound.mp3")
table_text = font_new.render("table", True, (0,155,0))
tap_text = font_new.render("tap", True, (205,10,10))
tent_text = font_new.render("tent", True, (70,70,70))
tie_text = font_new.render("tie", True, (153,0,76))
tiger_text = font_new.render("tiger", True, (153,0,76))
toad_text = font_new.render("toad", True, (153,0,76))
tomatoes_text = font_new.render("tomatoes", True, (153,0,76))
tree_text = font_new.render("tree", True, (153,0,76))


#sun,stones,snake and swing sound
sun_sound = mixer.sound("sound/Sun.mp3")
stones_sound = mixer.sound("sound/Stones.mp3")
snake_sound = mixer.sound("sound/Snake.mp3")
swing_sound = mixer.sound("sound/Swing.mp3")

#for the night scene
night_stones_sound = mixer.sound("sound/Stones.mp3")
night_swing_sound = mixer.sound("sound/Swing.mp3")
spider_sound = mixer.sound("sound/spider.mp3")
stars_sound = mixer.sound("sound/stars.mp3")

#for the branches scene and stars scene
branches_sound = mixer.sound("sound/branches_sound.mp3")
stars_scene_sound = mixer.sound("sound/stars_sound_1.mp3")
empty = pygame.image.load("img/empty.png")
point1 = pygame.image.load("img/1 point.png")
point2 = pygame.image.load("img/2 points.png")
point3 = pygame.image.load("img/3points.png")
point4 = pygame.image.load("img/4points.png")

empty_3 = pygame.image.load("img/empty_3.png")
point1_3 = pygame.image.load("img/1 points_3.png")
point2_3 = pygame.image.load("img/2points_3.png")
point3_3 = pygame.image.load("img/3points_3.png")

def sound_play():
    level_complete_sound = mixer.sound("sound/success-1-6297.mp3")
    level_complete_sound.play()

def night_scene_sound_play():
    level_complete_sound = mixer.sound("sound/success-1-6297.mp3")
    level_complete_sound.play()

def a1_scene_sound_play():
    level_complete_sound = mixer.sound("sound/success-1-6297.mp3")
    level_complete_sound.play()

def a2_scene_sound_play():
    level_complete_sound = mixer.sound("sound/success-1-6297.mp3")
    level_complete_sound.play()

def a3_scene_sound_play():
    level_complete_sound = mixer.sound("sound/success-1-6297.mp3")
    level_complete_sound.play()

def a4_scene_sound_play():
    level_complete_sound = mixer.sound("sound/success-1-6297.mp3")
    level_complete_sound.play()

def t1_scene_sound_play():
    level_complete_sound = mixer.sound("sound/success-1-6297.mp3")
    level_complete_sound.play()

def t2_scene_sound_play():
    level_complete_sound = mixer.sound("sound/success-1-6297.mp3")
    level_complete_sound.play()

def t3_scene_sound_play():
    level_complete_sound = mixer.sound("sound/success-1-6297.mp3")
    level_complete_sound.play()

def forest_scene_sound_play():
    level_complete_sound = mixer.sound("sound/success-1-6297.mp3")
    level_complete_sound.play()

def wrong_answer_sound_play():
    wrong_answer_sound = mixer.sound("sound/wrong_ans.wav")
    wrong_answer_sound.play()

def branch_scene_sound_play():
    level_complete_sound = mixer.sound("sound/success-1-6297.mp3")
    level_complete_sound.play()

def post_audio_scene_sound_play():
    level_complete_sound = mixer.sound("sound/success-1-6297.mp3")
    level_complete_sound.play()

def show_score(x,y,points):
    score = font_new.render("Score : "+str(points),True,(255,130,0))
    screen.blit(score,(x,y))

# def get_speech_input():
#         recognizer = sr.Recognizer()

#         with sr.Microphone() as source:
#             print("Say something:")
#             audio = recognizer.listen(source, timeout=3)

#         try:
#             text = recognizer.recognize_google(audio)
#             print("You said:", text)
#             return text
#         except sr.UnknownValueError:
#             print("Sorry, I could not understand what you said.")
#             return None
#         except sr.RequestError as e:
#             print("Sorry, I encountered an error while requesting the API; {0}".format(e))
#             return None





#the button class with init method having parameters as text, x-y coordinates, button enabling, height and width
class Button:
    def __init__(self,text,x_pos,y_pos,enabled,height,width):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.height = height
        self.width = width
        # self.draw()

    #function to draw the button
    def draw(self):

        button_text = font.render(self.text, True, "white")
        button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(self.width,self.height))
        pygame.draw.rect(screen,"#f07e0c",button_rect,0,5)
        screen.blit(button_text,(self.x_pos + 5,self.y_pos + 10))

    #function to check the button click
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(self.width,self.height))

        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False

class Button4:
    def __init__(self,text,x_pos,y_pos,enabled,height,width):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.height = height
        self.width = width
        # self.draw()

    #function to draw the button
    def draw(self):

        button_text = font3.render(self.text, True, "white")
        button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(self.width,self.height))
        pygame.draw.rect(screen,"#f07e0c",button_rect,0,5)
        screen.blit(button_text,(self.x_pos + 5,self.y_pos + 10))

    #function to check the button click
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(self.width,self.height))

        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False

class Button2:
    def __init__(self, text, x_pos, y_pos, enabled, height, width,hovered):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.height = height
        self.width = width
        self.hovered = hovered  # Track whether the mouse pointer is over the button

    def draw(self):
        if self.hovered:
            button_color = (49, 20, 50)  # Red when hovered
        else:
            button_color = (122, 73, 136)  # Default color

        button_text = font2.render(self.text, True, "white")
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.width, self.height))
        pygame.draw.rect(screen, button_color, button_rect, 0, 5)
        screen.blit(button_text, (self.x_pos + 5, self.y_pos + 5))

    def check_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.width, self.height))
        self.hovered = button_rect.collidepoint(mouse_pos)

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(self.width,self.height))

        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False

class Button3:
    def __init__(self, text, x_pos, y_pos, enabled, height, width,hovered):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.height = height
        self.width = width
        self.hovered = hovered  # Track whether the mouse pointer is over the button

    def draw(self):
        if self.hovered:
            button_color = (49, 20, 50)  # Red when hovered
        else:
            button_color = (122, 73, 136)  # Default color

        button_text = font4.render(self.text, True, "white")
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.width, self.height))
        pygame.draw.rect(screen, button_color, button_rect, 0, 5)
        screen.blit(button_text, (self.x_pos + 10, self.y_pos + 10))

    def check_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (self.width, self.height))
        self.hovered = button_rect.collidepoint(mouse_pos)

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(self.width,self.height))

        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False


class New_Button:
    def __init__(self,text,x_pos,y_pos,enabled,height,width):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.height = height
        self.width = width
        # self.draw()

    #function to draw the button
    def draw(self):
        button_text = font_num.render(self.text, True, "white")
        button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(self.width,self.height))
        pygame.draw.rect(screen,"#12e3d9",button_rect,0,5)
        screen.blit(button_text,(self.x_pos + 20,self.y_pos + 17))

    #function to check the button click
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos,self.y_pos),(self.width,self.height))
        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False



#Beginning status of several elements which will be modified as per the transitions of the game
input_1 = True
input_2 = False
char_s_scene_status = 0
sun_image_status = 0
snake_image_status = 0
swing_image_status = 0
stone_image_status = 0
sound_play_status = 1
night_scene_sound_play_status = 1
music_play_status = 0
delay_status = 1
sun_sound_status = 1 # 1 means active now.....From now onwards, I will use this notation
snake_sound_status = 1
stones_sound_status = 1
swing_sound_status = 1
night_stones_sound_status = 1 #active
night_swing_sound_status = 1 #active
spider_image_status = 1 #currently inactive
stars_image_status = 1 #currently inactive
spider_sound_status = 1 #active
stars_sound_status = 1
night_delay_status = 1 #for delay
forest_spider_sound_status = 1 #active
forest_sun_sound_status = 1 #active
forest_stones_sound_status = 1 #active
forest_snake_sound_status = 1 #active
forest_delay_status = 1
forest_scene_sound_play_status = 1
branch_scene_status = 0 #inactive
branch_scene_sound_status = 1 #active
post_branch_scene_status = 0 #inactive
branch_sound_status = 1 #active
stars_scene_status = 0 #inactive
stars_scene_sound_status = 1 #active
speech_detection_status = 0 #inactive---------------------------
superstar_sound_status = 1 #active
six_image_status = 0 #inactive
post_stars_scene_status = 0 #inactive
post_audio_scene_sound_status = 1
char_a_image_status = 0
a1scene_status = 0
a1_apples_image_status = 0 #inactive
a1_axe_image_status = 0 #inactive
a1_ant_image_status = 0
a1_apples_sound_status = 1
a1_axe_sound_status = 1
a1_ant_sound_status = 1
a1_delay_status = 1
a1_scene_sound_play_status = 1

a2_scene_status = 0

a2_apples_status = 0
a2_alligator_status = 0
a2_axe_status = 0
a2_ant_status = 0
a2_delay_status = 1
a2_scene_sound_play_status = 1
a2_apples_sound_status = 1
a2_axe_sound_status = 1
a2_alligator_sound_status = 1
a2_ant_sound_status = 1

a3_scene_status = 0

a3_apples_status = 0
a3_axe_status = 0
a3_arrow_status = 0
a3_scene_sound_play_status = 1
a3_delay_status = 1
a3_apples_sound_status = 1
a3_axe_sound_status = 1
a3_arrow_sound_status = 1

a4_scene_status = 0
a4_apples_status = 0
a4_ambulance_status = 0
a4_alligator_status = 0
a4_ant_status = 0
a4_delay_status = 1
a4_scene_sound_play_status = 1
a4_apples_sound_status = 1
a4_alligator_sound_status = 1
a4_ambulance_sound_status = 1
a4_ant_sound_status = 1

t_char_status = 0

t1_scene_status = 0

t1_table_image_status = 0 #inactive
t1_tent_image_status = 0 #inactive
t1_tiger_image_status = 0
t1_tomato_image_status = 0
t1_tomato_sound_status = 1
t1_table_sound_status = 1
t1_tent_sound_status = 1
t1_tiger_sound_status = 1
t1_delay_status = 1
t1_scene_sound_play_status = 1

t2_scene_status = 0

t2_table_image_status = 0 #inactive
t2_tent_image_status = 0 #inactive
t2_tree_image_status = 0
t2_tomato_image_status = 0
t2_tomato_sound_status = 1
t2_table_sound_status = 1
t2_tent_sound_status = 1
t2_tree_sound_status = 1
t2_delay_status = 1
t2_scene_sound_play_status = 1

t3_scene_status = 0

t3_tie_image_status = 0 #inactive
t3_tap_image_status = 0 #inactive
t3_toad_image_status = 0
t3_table_image_status = 0
t3_toad_sound_status = 1
t3_table_sound_status = 1
t3_tap_sound_status = 1
t3_tie_sound_status = 1
t3_delay_status = 1
t3_scene_sound_play_status = 1
last_scene_status=0



s_command_status = 1
a_command_status = 1
t_command_status = 1

#analytics
time_0_0_status = 1
time_1_1_status = 1
time_1_2_1_status = 1
time_1_2_status = 1
time_1_3_1_status = 1
time_1_3_status = 1
time_1_4_1_status = 1
time_1_4_status = 1
time_1_5_1_status = 1
time_1_5_status = 1
time_2_1_1_status = 1
time_2_1_status = 1
time_2_2_1_status = 1
time_2_2_status = 1
time_2_3_1_status = 1
time_2_3_status = 1
time_2_4_1_status = 1
time_2_4_status = 1
time_3_1_1_status = 1
time_3_1_status = 1
time_3_2_1_status = 1
time_3_2_status = 1
time_3_3_1_status = 1
time_3_3_status = 1


time_0_0 = 0
time_1_1 = 0
time_1_2_1 = 0
time_1_2 = 0
time_1_3_1 = 0
time_1_3 = 0
time_1_4_1 = 0
time_1_4 = 0
time_1_5_1 = 0
time_1_5 = 0
time_2_1_1 = 0
time_2_1 = 0
time_2_2_1 = 0
time_2_2 = 0
time_2_3_1 = 0
time_2_3 = 0
time_2_4_1 = 0
time_2_4 = 0
time_3_1_1 = 0
time_3_1 = 0
time_3_2_1 = 0
time_3_2 = 0
time_3_3_1 = 0
time_3_3 = 0

n_s1=4
n_s2=4
n_s3=4
n_s4=4
n_a1=4
n_a2=4
n_a3=4
n_a4=4
n_t1=4
n_t2=4
n_t3=4
n_t4=4

active_s1_1=4
active_s1_2=4
active_s1_3=4
active_s1_4=4

active_s2_1=4
active_s2_2=4
active_s2_3=4
active_s2_4=4

active_s3_1=4
active_s3_2=4
active_s3_3=4
active_s3_4=4

active_s4_1=4
active_s4_2=4
active_s4_3=4
active_s4_4=4


active_a1_1=4
active_a1_2=4
active_a1_3=4
active_a1_4=4


active_a2_1=4
active_a2_2=4
active_a2_3=4
active_a2_4=4

active_a3_1=4
active_a3_2=4
active_a3_3=4
active_a3_4=4

active_a4_1=4
active_a4_2=4
active_a4_3=4
active_a4_4=4

active_t1_1=4
active_t1_2=4
active_t1_3=4
active_t1_4=4

active_t2_1=4
active_t2_2=4
active_t2_3=4
active_t2_4=4

active_t3_1=4
active_t3_2=4
active_t3_3=4
active_t3_4=4

active_t4_1=4
active_t4_2=4
active_t4_3=4
active_t4_4=4

hint_s1=4
hint_s2=4
hint_s3=4
hint_s4=4#not used
hint_a1=3
hint_a2=3
hint_a3=4
hint_a4=4
hint_t1=4
hint_t2=4
hint_t3=4

summary_status_s1=0
summary_status_s2=0
summary_status_s3=0
summary_status_s4=0
summary_status_a1=0
summary_status_a2=0
summary_status_a3=0
summary_status_a4=0
summary_status_t1=0
summary_status_t2=0
summary_status_t3=0

summary_status=0

t_a1_1=0
t_a1_2=0
t_a1_3=0
t_a2_1=0
t_a2_2=0
t_a2_3=0
t_a3_1=0
t_a3_2=0
t_a3_3=0
t_a4_1=0
t_a4_2=0
t_a4_3=0
t_a4_4=0

t_s1_1=0
t_s1_2=0
t_s1_3=0
t_s1_4=0
t_s2_1=0
t_s2_2=0
t_s2_3=0
t_s2_4=0
t_s3_1=0
t_s3_2=0
t_s3_3=0
t_s3_4=0



t_t1_1=0
t_t1_2=0
t_t1_3=0
t_t1_4=0
t_t2_1=0
t_t2_2=0
t_t2_3=0
t_t2_4=0
t_t3_1=0
t_t3_2=0
t_t3_3=0
t_t3_4=0
t_t4_1=0
t_t4_2=0
t_t4_3=0
t_t4_4=0

my_button_3 = Button("SUN",240,15,True,150,130)
my_button_3.draw()

my_button_4 = Button("SNAKE",800,550,True,200,150)
my_button_4.draw()

my_button_5 = Button("SWING",500,200,True,240,150)
my_button_5.draw()

my_button_apple = Button("apple",30,10,True,340,400)
my_button_apple.draw()

my_button_spoon = Button("spoon",150,360,True,150,330)
my_button_spoon.draw()

my_button_soap = Button("saop",530,380,True,430,280)
my_button_soap.draw()

my_button_socks = Button("socks",560,10,True,450,320)
my_button_socks.draw()

global_click_check = 0
total_click_count = 0
wrong_clicks=0
correct_clicks=0
initial_button=1
control = True #status of the main while loop

soap=0
apple=0
socks=0
spoon=0
bg_image = pygame.image.load("img/demo_screen.png")


apple_active=0
spoon_active=0
socks_active=0
soap_active=0


hint=3
active1=1
active2=1
active3=1
active4=1

while control: #main running loop of the game screen
    pygame.draw.rect(screen, (129, 33, 191), (1000, 0, 200, 700))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            control = False
        # ensuring that the screen ends only when the quit event is pressed
    screen.blit(land_image,(0,0))

    if (initial_button):
        my_button_1 = Button4("LET US PLAY", 360, 590, True, 60, 320)
        my_button_1.draw()
        input_1 = my_button_1.check_click()
        if input_1:
            char_s_image_status = 1
            input_1 = 0
            global_click_check = 1

    # my_button_2 = Button("NEXT",470,90,True,50,90)

    if char_s_image_status == 1:
        if s_command_status == 1:
            s_command.play()
            s_command_status = 0
        screen.fill((255,255,255))
        screen.blit(char_s_image,(180,170))
        my_button_2 = Button("NEXT",480,550,True,50,90)
        my_button_2.draw()
        input_2 = my_button_2.check_click()
        if input_2:
            char_s_scene_status = 1
            global_click_check = 1
            time.sleep(1.0)



    if char_s_scene_status == 1:
        if time_0_0_status == 1:
            time_0_0 = pygame.time.get_ticks()
            time_0_0_status = 0
        char_s_image_status = 0
        screen.fill((255,255,255))
        screen.blit(bg_image,(0,0))
        pygame.draw.rect(screen, (129, 33, 191), (1000, 0, 200, 700))

        # if(spoon==0):
        #     screen.blit(spoon_intro, (20, 20))
        # if(spoon==1):
        #     screen.blit(spoon_intro_colour, (20, 20))
        # if(socks==0):
        #     screen.blit(socks_intro, (300, 20))
        # if(socks==1):
        #     screen.blit(socks_intro_colour, (300, 20))
        # if(soap==0):
        #     screen.blit(soap_intro, (450, 320))
        # if(soap==1):
        #     screen.blit(soap_intro_colour, (450, 320))
        # if(apple==0):
        #     screen.blit(apple_intro, (600, 20))
        # if(apple==1):
        #     screen.blit(apple_intro_colour, (600, 20))

        input_3 = my_button_spoon.check_click()
        if (input_3):
            spoon_active = 1
            if (active1):
                hint -= 1
                active1 = 0
        input_4 = my_button_soap.check_click()
        if (input_4):
            soap_active = 1
            if(active2):
                hint -= 1
                active2 = 0
        input_5 = my_button_apple.check_click()
        if (input_5):
            apple_active = 1
            if(active3):
                hint -= 1
                active3 = 0
        input_6 = my_button_socks.check_click()
        if (input_6):
            socks_active = 1
            if(active4):
                hint -= 1
                active4 = 0

        if (hint == 3):
            screen.blit(empty_3, (1015, 65))
        if (hint == 2):
            screen.blit(point1_3, (1015, 65))
        if (hint == 1):
            screen.blit(point2_3, (1015, 65))
        if (hint == 0):
            screen.blit(point3_3, (1015, 65))

        if(apple_active):
            screen.blit(apple_intro_colour,(30,10))
        if(soap_active):
            screen.blit(soap_intro_colour,(530,384))
        if(socks_active):
            screen.blit(socks_intro_colour,(520,10))
        if(spoon_active):
            screen.blit(spoon_intro_colour,(150,360))


    my_button_61 = Button2("END GAME", 1007, 180, True, 47, 183, False)
    # my_button_61.check_hover()
    my_button_61.draw()
    input_break = my_button_61.check_click()
    if (input_break):

        control = False
        break

    my_button_62 = Button3("S", 1057, 280, True, 93, 77, False)
    my_button_62.check_hover()
    my_button_62.draw()

    my_button_63 = Button3("A", 1057, 430, True, 92, 77, False)
    my_button_63.check_hover()
    my_button_63.draw()

    my_button_64 = Button3("T", 1057, 570, True, 92, 77, False)
    my_button_64.check_hover()
    my_button_64.draw()

    input_62 = my_button_62.check_click()
    if input_62:
        char_s_image_status = 1
        input_62 = 0
        global_click_check = 1

    input_63 = my_button_63.check_click()
    if input_63:
        char_a_image_status = 1
        char_s_image_status = 0
        char_s_scene_status = 0
        initial_button = 0
        input_63 = 0

        night_scene_image_status = 0
        branch_scene_status = 0
        forest_scene_status = 0
        global_click_check = 1

    input_64 = my_button_64.check_click()
    if input_64:
        t_char_status = 1
        char_s_image_status = 0
        char_s_scene_status = 0
        initial_button = 0
        input_64 = 0
        char_a_image_status = 0
        a3_scene_status = 0
        a1scene_status = 0
        a4_scene_status = 0
        a2_scene_status = 0
        global_click_check = 1

        night_scene_image_status = 0
        branch_scene_status = 0
        forest_scene_status = 0
    pygame.display.update()

end_time = pygame.time.get_ticks()
total_game_time = end_time - start_time

# with open('analytics.txt', 'a') as file:
#     file.write(str(time_1_1) + " " + str(time_1_2) + " " + str(time_1_3) + " " + str(time_1_4) +
#                " " + str(time_1_5) + " " + str(time_2_1) + " " + str(time_2_2) + " " + str(time_2_3)
#                + " " + str(time_2_4) + " " + str(time_3_1) + " " + str(time_3_2) + " " +
#                str(time_3_3) + " " + str(total_game_time) + " " + str(t_a1_1) + " " + str(t_a1_2) + " " + str(
#         t_a1_3) + " " + str(t_a2_1) + " " + str(t_a2_2) + " " + str(t_a2_3) + " " + str(t_a3_1) + " " + str(
#         t_a3_2) + " " + str(t_a3_3) + " " + str(t_a4_1) + " " + str(t_a4_2) + " " + str(t_a4_3) + " " + str(
#         t_a4_4) + " " + str(t_s1_1) + " " + str(t_s1_2) + " " + str(t_s1_3) + " " + str(t_s1_4) + " " + str(
#         t_s2_1) + " " + str(t_s2_2) + " " + str(t_s2_3) + " " + str(t_s2_4) + " " + str(t_s3_1) + " " + str(
#         t_s3_2) + " " + str(t_s3_3) + " " + str(t_s3_4) + " " + str(t_t1_1) + " " + str(t_t1_2) + " " + str(
#         t_t1_3) + " " + str(t_t1_4) + " " + str(t_t2_1) + " " + str(t_t2_2) + " " + str(t_t2_3) + " " + str(
#         t_t2_4) + " " + str(t_t3_1) + " " + str(t_t3_2) + " " + str(t_t3_3) + " " + str(t_t3_4) + " " + str(
#         wrong_clicks) + str(correct_clicks) + "\n")
pygame.quit()
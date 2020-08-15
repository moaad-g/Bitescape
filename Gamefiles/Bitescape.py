from tkinter import *
from tkinter import messagebox as ms
import sqlite3
import os
import random
import pygame
import time
import ctypes
#-----------------------------------------------------------------------------#
#Level Templates.
levels = { 1: [[
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "  S                             ",
    "============= = ==  == = =======",],
    #level 1 stage 1
    [
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "            --  --              ",
    "S      - -           --         ",
    "======                    ======",]],
    #level 1 stage 2     
    2 : [[
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                    -           ",
    "                  -             ",
    "S      ---      -               ",
    "=======     ---       ==========",],
    #level 2 stage 1
    [
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                              - ",
    "                          -     ",
    "                       --       ",
    "S            E     ---          ",
    "======  ==========             =",],
    #level 2 stage 2
    [
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "S                               ",
    "===                             ",
    "===                 --          ",
    "===               -             ",
    "===   =     E    =     -  --    ", 
    "===   ============             =",]],
    #level 2 stage 3
    3 : [[       
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                    --          ",
    " S                 -            ",
    "==================      -  --   ", 
    "==================             =",],                
    [
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                       ---   ---",
    "S --      3   3    ---          ",
    "=      ===========              ",],
    [
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                             e  ",
    "                            ----",
    "                          -     ",
    "S                       -       ",
    "=====     =    =      -         ",
    "=====  =  =  - =   -            ",
    "=====  =  =    =                ",]],
    4 :[[
    "                               =",
    "                               =",
    "S                              =",
    "--------                       =",
    "         -      e              =",
    "             ----    3  E  3   =",
    "                  ------------ =",
    "                               =",
    "                           =====",
    "                       ----    =",
    "                                ",
    "                     ----  --   ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                             -  ", 
    "                       ==      =",],
    [
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                               =",
    "                        ---     ",
    "                     --         ",
    "                       --      -",
    "                   --          =",
    "    =                  ---     =",
    "S  ==   e     E    ---         =",
    "=====  ===========             =",],
    [
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "        -   ---   -             ",
    "      -             ---     ====",
    "                        -       ",
    "-----                           ",
    "      --                    =   ",
    "          ---               ====",
    "                                ",
    "S    -  -                       ",
    "----                            ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",]],
    5 :[[       
    "                           =====",
    "                              = ",
    "S                           ==  ",
    "--------    -  - - - -     ==   ",
    "         -                =     ",
    "                        = =     ",
    "                        = =     ",
    "                        = =     ",
    "                        = =     ",
    "                        = =     ",
    "                        = =     ",
    "                        = =     ",
    "                        = =     ",
    "                                ",
    "                         mmm    ",
    "                                ",
    "                                ", 
    "                                ",],
    [
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "S                               ",
    "=====                           ",
    "====mm           3 3    --      ",
    "===             ------      mm  ",
    "=                               ",],
    [
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                                ",
    "                             e  ",
    "S                        e -----",
    "=== --- mm              ---     ",
    "===                   =         ",]],
    6 :[[
    "                                ",
    "                                ",
    "                                ",
    "                 3 3 3 3 3   e =",
    "               --------------- =",
    "            -                  =",
    "     --  -                      ",
    "   -                           =",
    " -                             =",
    "    --     E       -  ---  -   =",
    "       ---------              ==",
    "                          -----=",
    "                      ---      =",
    "                   --          =",
    "                --             =",
    "             --                =",
    "S                               ",
    "================================",],
    [
    "                               =",
    "                               =",
    "S                              =",
    "===                            =",
    "==                             =",
    "                               =",
    "               =               =",
    "    mm                         =",
    "             E                 =",
    "            =====              =",
    "                   =  E        =",
    "           ======= =======     =",
    "                           e   =",
    "                   =============",
    "                                ",
    "                 3 3    --     =",
    "                ------       - =",
    "================================"],
    [
    "                                ",
    "                  3 3 3 3 3     ",
    "              ==================",
    "          --                   =",
    "        -                      =",
    "          -                    =",
    "            -    e  e    E     =",
    "               ------   ----   =",
    "                              -=",
    "                           -   =",
    "               E      =        =",
    "            ------  - ==========",
    "          -                    =",
    "        -                      =",
    "S    ==                        =",
    "===  ==                        =",
    "===  ==                         ",
    "===  ===========================",]],
    
         }

#--------------------------------------------------------------------------------------------#w
#dictionary contains all images
level_images = { 1 : ["level_1 bg.png","level_1 plat.png","level_1 wall.png",], 2: ["level_2 bg.png","level_2 plat.png","level_2 wall.png",], 3: ["level_3 bg.png","level_3 plat.png","level_3 wall.png",], 4:["level_4 bg.png","level_4 plat.png","level_4 wall.png"],5:["lvl_5 bg.png","level_5 plat.png","level_5 wall.png"],6:["lvl_6 bg.png","level_6 plat.png","level_6 wall.png"]}
#set up the groups and lists for the sprites
character_sprites = pygame.sprite.Group() #player sprite, enemysprite
wall_sprites = pygame.sprite.Group() #walls and platforms
background_sprites = pygame.sprite.Group()
walls = []
moving_platforms = []
enemies = []
enemies_zero = []
#set up display
pygame.display.set_caption("Bit Escape")
width = 1280
height = 720
ctypes.windll.user32.SetProcessDPIAware()
block_width = int(width/32)
block_height = int(height/18)
#set screen variables
screen = pygame.display.set_mode((width, height))#sets the screen in pygame
clock = pygame.time.Clock()

Lives = 3
inc = 0
wallmove = 0
speed = (width/256)
gravity  = 8#(width/256)
collision = False
bp = False
right= False
left = False

red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
#classes
class PlayerSprite(pygame.sprite.Sprite):#player class
    def __init__(self, spawnpointx, spawnpointy):
        super().__init__()
        self.right_img = pygame.image.load("CPU NEW.png").convert_alpha()
        self.left_img =  pygame.image.load("CPU NEW.png").convert_alpha()
        self.image = pygame.image.load("CPU NEW.png").convert_alpha()#sets sprite image
        self.image.set_colorkey([255,255,255])
        self.image = pygame.transform.scale(self.image, (block_width,block_height))
        self.rect = self.image.get_rect(center=(spawnpointx,spawnpointy))

    #makes the player sprite move
    def move(self,dx,dy,collision, right, left,Lives):
        if right == True:
                self.image = self.right_img
                self.image.set_colorkey([255,255,255])
                self.image = pygame.transform.scale(self.image, (block_width,block_height)) 
        if left == True:
                self.image = self.left_img
                self.image.set_colorkey([255,255,255])
                self.image = pygame.transform.scale(self.image, (block_width,block_height))             
        if dx!=0:
            collision,Lives = self.move_single_axis(dx,0,collision,Lives)
        if dy!=0:
            collision,Lives = self.move_single_axis(0,dy,collision,Lives)

        left = False
        right = False
        return collision, Lives
    
    def jump(self,jump_in,jump,collision):
        if jump_in == 1:
            self.rect.y -= 10
            dy = -20
        if jump_in == 2:
            self.rect.y -= 20
            dy = -30
        if jump_in ==  3 :
            self.rect.y -= 50
            dy = -50
        if jump_in ==  4 :
            self.rect.y -= 30
            dy = -30
        if jump_in ==  5 :
            self.rect.y -= 20
            dy = -15
        if jump_in ==  6 :
           self.rect.y -= 15
           dy = -7.5
        for wall in walls:
            if self.rect.colliderect(wall.rect):                   
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                    
                if dy < 0:
                    self.rect.top = wall.rect.bottom

    #system for moving includes wall collisions
    def move_single_axis(self, dx, dy,collision,Lives):
        self.rect.x += dx 
        self.rect.y += dy
        collision = False
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left
                    collision = True
                if dx < 0:
                    self.rect.left = wall.rect.right
                    collision = True
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                    collision = True
                if dy < 0:
                    self.rect.top = wall.rect.bottom
                    collision = True
                    
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                if dx > 0:
                    self.rect.right = enemy.rect.left
                    Lives = Lives-1
                if dx < 0:
                    self.rect.left = enemy.rect.right
                    Lives = Lives-1
                if dy > 0:
                    self.rect.bottom = enemy.rect.top
                    if enemy in enemies_zero:
                        enemy.death()
                    else:
                        Lives = Lives-1
                if dy < 0:
                    self.rect.top = enemy.rect.bottom
                    Lives = Lives-1
                    
        return collision,Lives
    
class EnemySprite(pygame.sprite.Sprite):
    def __init__(self, spawnpointx, spawnpointy):
        super().__init__()
        enemies.append(self)
        self.image = pygame.image.load("1.png")
        self.image.set_colorkey([255,255,255])
        self.image = pygame.transform.scale(self.image, ((20,block_height)))
        self.rect = self.image.get_rect(center=(spawnpointx, spawnpointy))
    def move(self,Increment):
        #gravity
        if self.rect.y < (height-block_height):
            self.rect.y += 5
        #length of oscillation   
        if 0<Increment<51.:
            self.rect.x += 2
        else:
            self.rect.x -= 2
        #collision
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if 5 > 0:
                    self.rect.bottom = wall.rect.top
                if 5 < 0:
                    self.rect.top = wall.rect.bottom
#subclass of enemy (killable)               
class EnemySprite0(EnemySprite):
    def __init__(self,spawnpointx, spawnpointy):
        enemies_zero.append(self)
        EnemySprite.__init__(self,spawnpointx, spawnpointy)
        self.image = pygame.image.load("0.png")
        self.image.set_colorkey([255,255,255])
        self.image = pygame.transform.scale(self.image, (20,block_height))
        self.rect = self.image.get_rect(center=(spawnpointx, spawnpointy))

    def death(self):
        #deletes object
        enemies.remove(self)
        character_sprites.remove(self)
#subclass of enemy (moves up and down)        
class EnemySprite1(EnemySprite):
    def __init__(self,spawnpointx, spawnpointy):
        EnemySprite.__init__(self,spawnpointx, spawnpointy)
        self.image = pygame.image.load("2.png")
        self.image.set_colorkey([255,255,255])
        self.image = pygame.transform.scale(self.image, (block_width,20))
        self.rect = self.image.get_rect(center=(spawnpointx, spawnpointy))
    def move(self,Increment):
        if 0<Increment<51:
            self.rect.y += 2
        else:
            self.rect.y -= 2
        if Increment >= 100:
                Increment = 0
        
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if 5 > 0:
                    self.rect.bottom = wall.rect.top
                if 5 < 0:
                    self.rect.top = wall.rect.bottom
       
        

        
class Wall(pygame.sprite.Sprite):
    def __init__(self, name, wx, wy):
        super().__init__()
        #makes a list of all the walls in a level
        walls.append(self)
        self.image = pygame.image.load(name).convert_alpha()
        self.image.set_colorkey([255,255,255])

class Floor(Wall):
      def __init__(self, name, wx, wy):
        Wall.__init__(self, name, wx, wy)  
        self.image = pygame.transform.scale(self.image, (block_width,block_height))
        self.rect = self.image.get_rect(center=(wx+(block_width/2),wy+(block_height/2)))
#subclass of Wall (skinny)        
class Platform(Wall):
      def __init__(self, name, wx, wy):
        Wall.__init__(self, name, wx, wy)  
        self.image = pygame.transform.scale(self.image, (block_width,20))
        self.rect = self.image.get_rect(center=(wx+(block_width/2),wy+(10)))
#subclass of Platform (moving)       
class Moving(Platform):
    def __init__(self, name, wx, wy):
        moving_platforms.append(self)
        Platform.__init__(self, name, wx, wy)  

    def move(self,wallmove):
        if 0 < wallmove<=200:
            self.rect.x += 2
        elif 200 < wallmove <= 400:
            self.rect.x -= 2


            
class Player_Profile():
    def __init__(self):
        #sets attributes and loads the usernme from text file
        self.username = ""
        self.progress_list = []
        self.points_list = []
        with open("Player_Profile.txt", "r") as username_file:
            username = username_file.readlines()
            self.username = username[0]
                        
    #creates list of points etc etc        
    def database_connect(self):
        Database= sqlite3.connect("GameData2.db")
        c = Database.cursor()
        #gets list of the player's points
        c.execute('''SELECT * FROM Points WHERE Username= ? ''',(self.username,))
        self.points_list = c.fetchall()
        #gets list of the player's points
        c.execute('''SELECT * FROM Progress WHERE Username= ? ''',(self.username,))
        self.progress_list = c.fetchall()
        Database.close()
    #only updates score if its higher than their personal best    
    def update_progress_points(self,points,num):
        Database= sqlite3.connect("GameData2.db")
        c = Database.cursor()
        if num == 1:
            if points > self.points_list[0][1]:
                c.execute('''UPDATE Points SET Level1points =? WHERE Username =?''',(points,self.username))
                c.execute('''UPDATE Progress SET Level =? WHERE Username =?''',(1,self.username))
        elif num == 2:
            if points > self.points_list[0][2]:
                c.execute('''UPDATE Points SET Level2points =? WHERE Username =?''',(points,self.username))
                c.execute('''UPDATE Progress SET Level2 =? WHERE Username =?''',(1,self.username))
        elif num == 3:
            if points > self.points_list[0][3]:
                c.execute('''UPDATE Points SET Level3points =? WHERE Username =?''',(points,self.username))
                c.execute('''UPDATE Progress SET Level3=? WHERE Username =?''',(1,self.username))
        elif num == 4:
            if points > self.points_list[0][4]:
                c.execute('''UPDATE Points SET Level4points =? WHERE Username =?''',(points,self.username))
                c.execute('''UPDATE Progress SET Level4 =? WHERE Username =?''',(1,self.username))
        elif num == 5:
            if points > self.points_list[0][5]:
                c.execute('''UPDATE Points SET Level5points =? WHERE Username =?''',(points,self.username))
                c.execute('''UPDATE Progress SET Level5 =? WHERE Username =?''',(1,self.username))
        elif num == 6:
            if points > self.points_list[0][6]:
                c.execute('''UPDATE Points SET Level6points =? WHERE Username =?''',(points,self.username))
                c.execute('''UPDATE Progress SET Level6 =? WHERE Username =?''',(1,self.username))
            
        Database.commit()
        Database.close()
        #updates the lists
        self.database_connect()
        
    def reports(self,num):
        #loads list of scores from database in descending order
        Database= sqlite3.connect("GameData2.db")
        c = Database.cursor()
        if num == 1:
            c.execute('''SELECT Username, Level1points FROM Points ORDER BY Level1points DESC''')
            highscore_list = c.fetchall()
        elif num == 2:
            c.execute('''SELECT Username, Level2points FROM Points ORDER BY Level1points DESC''')
            highscore_list = c.fetchall()
        elif num == 3:
            c.execute('''SELECT Username, Level3points FROM Points ORDER BY Level1points DESC''')
            highscore_list = c.fetchall()
        elif num == 4:
            c.execute('''SELECT Username, Level4points FROM Points ORDER BY Level1points DESC''')
            highscore_list = c.fetchall()
        elif num == 5:
            c.execute('''SELECT Username, Level5points FROM Points ORDER BY Level1points DESC''')
            highscore_list = c.fetchall()    
        elif num == 6:
            c.execute('''SELECT Username, Level6points FROM Points ORDER BY Level1points DESC''')
            highscore_list = c.fetchall()
            
        Database.close()
        #shortens list to top 3 scores
        while len(highscore_list) > 3:
            highscore_list.pop()
        #displays top 3 scores in order in ascending order
        screen.fill((50,205,50))
        size=50
        h = (height/7)*6
        n=3
        for x in range (0,3):
            score = highscore_list.pop()
            name = str(score[0])
            point = str(score[1])
            message_display(("Top Scores:") , width/2, 50,80)
            message_display((str(n)+") "+name+":"), width/2-size,h,size)
            message_display(point, width/2+(5*size),h,size)
            h -= 2*(720/7)
            size+=10
            n-=1
            pygame.display.flip()
            time.sleep(1.5)
        
            

class Quizload():
    def __init__(self):
        self.quizdict = {}
        
    def Load_Questions(self):
        self.quizdict = {}
        x=0
        with open("Quiz.txt", "r") as quiz_file:
            lines_read = quiz_file.readlines()
            
            #lines_read is  a list of everything
            temp_list = []            
            for item in range (0,len(lines_read)):
                if item>0 and item%4 == 0:  
                  self.quizdict[x] = (temp_list)  
                  x+=1
                  temp_list = []
                current_line = lines_read[item]
                new_line = str(current_line)
                temp_list.append(new_line)
                item +=1
                if item == (len(lines_read)):
                    self.quizdict[x] = (temp_list)  
                    x+=1
                    temp_list = []
    def Add_Question(self):
        #loads python file
        import question_add
        play_button = False
        mouse = [0,0]
        button_width = 500
        button_height = 200
        click = False
        background = (pygame.image.load("Background 1.jpg").convert_alpha())
        #loop till player writes
        while play_button != True:
            clock.tick(60)
            screen.fill
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    mouse = pygame.mouse.get_pos()
                else:
                    mouse = mouse
            click = pygame.mouse.get_pressed()
            screen.blit(background,(0,0))
            play_button, mouse = button(click,mouse,"write",((width/2)-(button_width/2)),((height/2)-(button_height/2)),button_width,button_height, green, play_button)
            pygame.display.flip()
         #loads function from file and closes the game   
        question_add.run()
        pygame.quit()
class QuizGenerator(Quizload):
    def __init__(self):
        Quizload.__init__(self)
    
    def select_question(self, points,correct):
        def display_question(question,option_1,option_2,option_3,points,correct):
        #sets variables necessary for the buttons
            click = False
            mouse = [0,0]
            opt_1 = False
            opt_2 = False
            opt_3 = False
            button_width = ((2/10)*width)
            button_height = 200
            timer_length = 650
            timer_colour = green
            #finds correct answer and removes ! from the front
            if option_1[0] == "!":
                option_1 = option_1[1:(len(option_1))]
                correct_answer = "opt_1"
            if option_2[0] == "!":
                option_2 = option_2[1:(len(option_2))]
                correct_answer = "opt_2"
            if option_3[0] == "!":
                option_3 = option_3[1:(len(option_3))]
                correct_answer = "opt_3"

            #timer for quiz start
            screen.fill((red))
            message_display("Question Time", width/2, ((1/9)*height),50)
            message_display("3", width/2, (height/2),200)
            pygame.display.flip()
            time.sleep(1)
            screen.fill((255,140,0))
            message_display("Question Time", width/2, ((1/9)*height),50)
            message_display("2", width/2, (height/2),200)
            pygame.display.flip()
            time.sleep(1)
            screen.fill((green))
            message_display("Question Time", width/2, ((1/9)*height),50)
            message_display("1", width/2, (height/2),200)
            pygame.display.flip()
            time.sleep(1)
            #starts a loop where the question is shown and the answers are displayed as buttons
            while opt_1 == False and opt_2 == False and opt_3 == False and timer_length>0 :
                clock.tick(60)
                screen.fill((50,205,50))
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEMOTION:
                        mouse = pygame.mouse.get_pos()
                    else:
                        mouse = mouse
                click = pygame.mouse.get_pressed()
                message_display(question, width/2, (height/2)-50,50)
                opt_1,mouse = button(click,mouse,option_1,((1/10)*width),((5/9)*height),button_width,button_height,red,opt_1)
                opt_2,mouse = button(click,mouse,option_2,((4/10)*width),((5/9)*height),button_width,button_height,red,opt_2)
                opt_3,mouse = button(click,mouse,option_3,((7/10)*width),((5/9)*height),button_width,button_height,red,opt_3)
                pygame.draw.rect(screen, timer_colour,(((width/2) - (timer_length/2)),((1/9)*height),timer_length,30))
                timer_length = timer_length-3
                if timer_length < 150:
                    timer_colour = red
                pygame.display.flip()
            #selects options
            if opt_1 == True:
                answer_chosen = "opt_1"

            elif opt_2 == True:
                answer_chosen = "opt_2"
            elif opt_3 == True:
                answer_chosen = "opt_3"
            else:
                answer_chosen = "timeout"
            result_screen = False
            if answer_chosen == correct_answer:
                    correct = True
                    screen.fill((0,255,0))
                    message_display("CORRECT", width/2, (height/2),50)
                    pygame.display.flip()
                    time.sleep(2)

                    
            elif answer_chosen == "timeout":
                        correct = False
                        screen.fill((255,0,0))
                        click = pygame.mouse.get_pressed()
                        message_display("OUT OF TIME", width/2, (height/2),50)
                        pygame.display.flip()
                        time.sleep(2)

            else:
                        correct = False
                        screen.fill((255,0,0))
                        click = pygame.mouse.get_pressed()
                        message_display("INCORRECT", width/2, (height/2),50)
                        pygame.display.flip()
                        time.sleep(2)

            return points,correct
        ###############################################################################################
        def create_text(question_list,points,correct):
            new_question_list = []
            #creating and formatting questions as strings
            for x in range (0,(len(question_list))):  
                word = (question_list[x][0:(len(question_list[x])-1)])
                new_question_list.append(word)
            #seperates question and options
            question = (new_question_list[0])
            option_1 = (new_question_list[1])
            option_2 = (new_question_list[2])
            option_3 = (new_question_list[3])
            #
            points,correct = display_question(question,option_1,option_2,option_3,points,correct)
            return points,correct
        #selecting a random quiz from the quiz dictionary
        correct = False
        question_num = random.randint(0,(len(self.quizdict))-1)
        question_list = self.quizdict[question_num]
        points,correct = create_text(question_list,points,correct)
        return points, correct
    
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
profile = Player_Profile()
#-#-#-#-#-#--#-#-#-#-#-#-#--#-#-#-#-#-#-#-#
def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

def button(click,mouse,msg,x,y,w,h, colour, bp):
    colour = (0, 204, 0)
    if (x+w > mouse[0] > x) and ( y < mouse[1] < y+h):
        colour = (0,100,0)
        if click[0] == 1:
            bp = True
    pygame.draw.rect(screen, (0,0,0),(x-(h//20),y-(h//20),(w+(h//10)),(h+(h//10))))
    pygame.draw.rect(screen, colour,(x,y,w,h))
    #my_text = pygame.font.Font("freesansbold.ttf",(int(h//2)))
    message_display(msg,(x+w/2),(y+h/2), int(w//5))
    return bp,mouse
            
def message_display(text, top, left, size):
    my_text = pygame.font.Font("freesansbold.ttf",size)
    text_surface, text_rect = text_objects(text,my_text)
    text_rect.center = ((top),(left))
    screen.blit(text_surface, text_rect)

#-------------------------------------------------------------------------------------------#
#initialise pygame
Quiz_Question = QuizGenerator()
Quiz_Question.Load_Questions()
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
#-------------------------------------------------------------------------------------------#
def drawwalls(level_pics,level,character_sprites):
    #Draws walls an platforms
    x = y = 0
    for row in level:
        for col in row:
            #each sprite is called by a class and added to a group
            if col == "-":
                wall = Platform(level_pics[1], x, y)
                wall_sprites.add(wall)
            if col == "=":
                wall = Floor(level_pics[2], x, y)
                wall_sprites.add(wall)
            if col == "m":
                wall = Moving(level_pics[1], x,y)
                wall_sprites.add(wall)
            if col == "S":
                player_sprite = PlayerSprite(x, y)
                player_spawnpointx = x
                player_spawnpointy = y
                character_sprites.add(player_sprite)
            if col == "E":
                enemy_sprite =  EnemySprite(x, y)
                character_sprites.add(enemy_sprite)
            if col == "e":
                enemy_sprite =  EnemySprite1(x, y)
                character_sprites.add(enemy_sprite)
            if col == "3":
                enemy_sprite = EnemySprite0(x,y)
                character_sprites.add(enemy_sprite)
            x += block_width
        y += block_height
        x = 0
    return player_spawnpointx,player_spawnpointy, player_sprite,character_sprites
    
def emptywalls(character_sprites,enemies,walls,wall_sprites):
    wall_sprites.empty()
    character_sprites.empty()
    walls = []
    enemies = []
    return character_sprites,enemies,walls, wall_sprites

def life_lost(Lives):
        space = False
        mouse = [0,0]
        w = 450
        h = 150
        x = width/2 - w/2
        y = 103
        click = False
        pygame.draw.rect(screen, (0,0,0),(x-(h//20),y-(h//20),(w+(h//10)),(h+(h//10))))
        pygame.draw.rect(screen, (255,255,255),(x,y,w,h))
        message_display("YOU DIED!", width/2, 2*height/9,50)
        message_display("press space to respawn", width/2, (2*height/9)+45,30)
        while space == False:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    mouse = pygame.mouse.get_pos()
                else:
                    mouse = mouse
            click = pygame.mouse.get_pressed()
            pygame.display.flip()

            user_input = pygame.key.get_pressed()
            if user_input[pygame.K_SPACE]:
                space = True
            #space,mouse =  button(click,mouse,"respawn",((width/2)-(button_width/2)),((2/9)*height),button_width,button_height,green,space)
        
def time_points(points, final_time):
    add_points = 1000
    time_diff = add_points - final_time
    if time_diff > 0:
        points += time_diff
        
    return points
    
def EndScreen(points,level_num,correct):
    next_level = False
    menu_screen = False
    click = False
    mouse = [0,0]
    button_width = 300
    button_height = 100
    points = round(points,1)
    if correct == True:
        lvl_comp = "Level Complete"
        profile.update_progress_points(points,level_num)
        colour = green
    else:
        lvl_comp = "Level Failed"
        colour = red
    while next_level == False and menu_screen == False:
            clock.tick(60)
            screen.fill(colour)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                        mouse = pygame.mouse.get_pos()
                else:
                    mouse = mouse
            message_display(lvl_comp, width/2,((height/2)-50),50)
            message_display(("Points Scored: "+ str(points)) , width/2, (height/2),50)
            click = pygame.mouse.get_pressed()
            if correct == True:
                if level_num == 6:
                    menu_screen,mouse = button(click,mouse,"Menu",((width/2)-(button_width/2)),((6/9)*height),button_width,button_height,green,menu_screen)
                else:
                    menu_screen,mouse = button(click,mouse,"Menu",((3/16)*width),((6/9)*height),button_width,button_height,green,menu_screen)
                    next_level,mouse = button(click,mouse,("Level "+str(level_num+1)),((9/16)*width),((6/9)*height),button_width,button_height,green,next_level)
            else:
                menu_screen,mouse = button(click,mouse,"Menu",((3/16)*width),((6/9)*height),button_width,button_height,green,menu_screen)
                next_level,mouse = button(click,mouse,"retry",((width/2)-(button_width/2)),((6/9)*height),button_width,button_height,green,next_level)
            pygame.display.flip() 
    if menu_screen == True:
        level_num = Level_Select(0)
    else:
        if correct == True:
            level_num += 1
        else:
            pass        
    return level_num

def TutorialScreen():
    Back = False
    click = False
    mouse = [0,0]
    enemy1 = (pygame.image.load("1.png").convert_alpha())
    enemy1 = pygame.transform.scale(enemy1,(100,200))
    enemy2 = (pygame.image.load("0.png").convert_alpha())
    enemy2 = pygame.transform.scale(enemy2,(100,200))
    enemy3 =(pygame.image.load("2.png").convert_alpha())
    enemy3 = pygame.transform.scale(enemy3,(200,100))
    while Back == False:
        screen.fill((50,205,50))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mouse = pygame.mouse.get_pos()
            else:
                mouse = mouse
        click = pygame.mouse.get_pressed()
        message_display(("Controls:") , width/2, 50,80)
        message_display(("W : JUMP") , width/2 , 110,30)
        message_display(("A : LEFT") , width/2 , 150,30)
        message_display(("S :  RIGHT") , width/2 , 190,30)
        message_display(("Enemies:") , width/2, 260,80)
        screen.blit(enemy1,(width/8,310))
        screen.blit(enemy2,(width//2-50,310))
        screen.blit(enemy3,(7*width/8-100,370))
        Back, mouse = button(click,mouse,"<-",((width/2)-(200/2)),((height/2)+(200)),200,80, green, Back)
        pygame.display.flip()
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-##-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
def highscore_tester():
    mouse = [0,0]
    click = False
    stage_1 = False
    stage_2 = False
    stage_3 = False
    stage_4 = False
    stage_5 = False
    stage_6 = False
    button_width = ((4/16)*width)#256
    button_height = ((3/9)*height)-20#180
    while (stage_1 == False) and (stage_2 == False) and (stage_3 == False) and (stage_4 == False) and (stage_5 == False) and (stage_6 == False):
        clock.tick(60)
        screen.fill((50,205,50))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mouse = pygame.mouse.get_pos()
            else:
                mouse = mouse
        click = pygame.mouse.get_pressed()
        stage_1,mouse = button(click,mouse,"Level 1",((1/16)*width),((1/9)*height),button_width,button_height,red,stage_1)
        stage_2,mouse = button(click,mouse,"Level 2",((6/16)*width),((1/9)*height),button_width,button_height,red,stage_2)
        stage_3,mouse = button(click,mouse,"Level 3", ((11/16)*width),((1/9)*height),button_width,button_height,red,stage_3)
        stage_4,mouse = button(click,mouse,"Level 4", ((1/16)*width),((5/9)*height),button_width,button_height,red,stage_4)
        stage_5,mouse = button(click,mouse,"Level 5", ((6/16)*width),((5/9)*height),button_width,button_height,red,stage_5)
        stage_6,mouse = button(click,mouse,"Level 6", ((11/16)*width),((5/9)*height),button_width,button_height,red,stage_6)
        pygame.display.flip()
    if stage_1 == True:
        stage = 1
    elif stage_2 == True:
        stage = 2
    elif stage_3 == True:
        stage = 3
    elif stage_4 == True:
        stage = 4
    elif stage_5 == True:
        stage = 5
    elif stage_6 == True:
        stage = 6
    profile.reports(stage)
def TitleScreen():
    background = (pygame.image.load("Title 1.png").convert_alpha())
    break_loop = False
    while break_loop != True:
        clock.tick(60)
        screen.blit(background,(0,0))
        pygame.display.flip()
        background_sprites.empty()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_SPACE]:
            break_loop = True
    Menu()
    
def Menu():
    play_button = False
    Tutorial = False
    mouse = [0,0]
    button_width = 500
    button_height = 200
    click = False
    background = (pygame.image.load("Background 1.jpg").convert_alpha())
    while play_button != True and Tutorial != True:
        clock.tick(60)
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEMOTION:
                mouse = pygame.mouse.get_pos()
            else:
                mouse = mouse
        click = pygame.mouse.get_pressed()
        screen.blit(background,(0,0))
        play_button , mouse = button(click,mouse,"Menu",((width/2)-(button_width/2)),((height/2)-(button_height/2)),button_width,button_height, green, play_button)
        Tutorial , mouse = button(click,mouse,"Tutorial",((width/2)-(200/2)),((height/2)+(140)),200,80, green, Tutorial)
        pygame.display.flip()

    if play_button == True:
       pass
    else:
        TutorialScreen()
        Menu()


    
def Level_Select(stage):
    profile.database_connect()
    mouse = [0,0]
    click = False
    stage_1 = False
    stage_2 = False
    stage_3 = False
    stage_4 = False
    stage_5 = False
    stage_6 = False
    highscore_button = False
    add_button = False
    button_width = ((4/16)*width)#256
    button_height = ((3/9)*height)-20#180
    background = (pygame.image.load("Background 1.jpg").convert_alpha())
    while (stage_1 == False) and (stage_2 == False) and (stage_3 == False) and (stage_4 == False) and (stage_5 == False) and (stage_6 == False) and (highscore_button == False) and (add_button == False):
        clock.tick(60)
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEMOTION:
                mouse = pygame.mouse.get_pos()
            else:
                mouse = mouse
        click = pygame.mouse.get_pressed()
        screen.blit(background,(0,0))
        highscore_button,mouse = button(click,mouse,"HS",1200,20,50,20,red,highscore_button)
        stage_1,mouse = button(click,mouse,"Level 1",((1/16)*width),((1/9)*height),button_width,button_height,red,stage_1)
        if (profile.progress_list[0][1]) == 1:
            stage_2,mouse = button(click,mouse,"Level 2",((6/16)*width),((1/9)*height),button_width,button_height,red,stage_2)
        if (profile.progress_list[0][2]) == 1:
            stage_3,mouse = button(click,mouse,"Level 3", ((11/16)*width),((1/9)*height),button_width,button_height,red,stage_3)
        if (profile.progress_list[0][3]) == 1:
            stage_4,mouse = button(click,mouse,"Level 4", ((1/16)*width),((5/9)*height),button_width,button_height,red,stage_4)
        if (profile.progress_list[0][4]) == 1:
            stage_5,mouse = button(click,mouse,"Level 5", ((6/16)*width),((5/9)*height),button_width,button_height,red,stage_5)
        if (profile.progress_list[0][5]) == 1:
            stage_6,mouse = button(click,mouse,"Level 6", ((11/16)*width),((5/9)*height),button_width,button_height,red,stage_6)
        if  (profile.progress_list[0][6]) == 1:
            add_button,mouse = button(click,mouse,"AQ",80,20,50,20,red,add_button)
        pygame.display.flip()

    if stage_1 == True:
        stage = 1
    elif stage_2 == True:
        stage = 2
    elif stage_3 == True:
        stage = 3
    elif stage_4 == True:
        stage = 4
    elif stage_5 == True:
        stage = 5
    elif stage_6 == True:
        stage = 6  
    elif highscore_button == True:
        highscore_tester()
        stage = Level_Select(stage)
    elif add_button == True:
        QuizAdd = Quizload()
        QuizAdd.Add_Question()
    return stage

#-----------------------------------------#
#mainloop
running = True
stage = 0
level_num = 0
jump = False
jump_inc = 0
#------------------------------------------#
#level is the stage in the level number in the dictionary (basically everything)
#level_num is the level number (level 1, level 2, level 3)
#
#------------------------------------------#
TitleScreen()
pygame.mixer.music.load("fireflies new.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(20/100)
level_num = Level_Select(level_num)
level_pics = level_images[level_num]
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
level = levels[level_num][stage]
player_spawnpointx,player_spawnpointy,player_sprite, character_sprites = drawwalls(level_pics,level, character_sprites)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#-#-#-#-#-#
#-#-#-#-#-#
wall_colour = (255,255,255)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#
background = (pygame.image.load(level_pics[0]).convert_alpha())
background = pygame.transform.scale(background, (width,height))
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
timer_start = pygame.time.get_ticks()
points = 0
while running:
        clock.tick(60)
        screen.fill((0,255,0))
        if player_sprite.rect.x >= width - block_width:
            #moving onto the next stage
            if stage == (len(levels[level_num])-1):
                correct = False
                points += (level_num*5 + 20)
                final_time= (pygame.time.get_ticks() - timer_start)/1000
                points = time_points(points,final_time)
                points,correct = Quiz_Question.select_question(points,correct)
                level_num = EndScreen(points,level_num,correct)
                stage = -1
                points = 0
                level_pics = level_images[level_num]
                timer_start = pygame.time.get_ticks()
                Lives = 3
            character_sprites,enemies, walls, wall_sprites = emptywalls(character_sprites,enemies,walls, wall_sprites)
            screen.fill ((20,20,20))
            stage += 1
            level = levels[level_num][stage]
            background = (pygame.image.load(level_pics[0]).convert_alpha())
            background = pygame.transform.scale(background, (width,height))
            player_spawnpointx,player_spawnpointy ,player_sprite, character_sprites = drawwalls(level_pics,level, character_sprites)
            inc = 0
            wallmove = 0
            pygame.display.flip()  
        #adds the player sprite to the sprite group
        #draws all the sprites in their group
        screen.blit(background,(0,0))
        wall_sprites.draw(screen)
        character_sprites.draw(screen)
        message_display("Lives: " + str(Lives), width-block_width, block_height/2,15)
 
        lives_before = Lives
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_ESCAPE]:
            running = False
        #MOVEMENT
        #enemysprite movement
        for x in range(0,(len(enemies))):
                enemies[x].move(inc)
        inc += 1
        for x in range(0,(len(moving_platforms))):
            moving_platforms[x].move(wallmove)
        wallmove += 1
        #uses object 'player_sprite'
        
        #if the user is grounded    
        if collision == True:
            if user_input[pygame.K_w]:
                jump = True
        #if the user presses W the sprite will jump
        if jump == True:
            jump_inc +=1
            player_sprite.jump(jump_inc,jump,collision)
            if jump_inc == 7:
                jump_inc= 0
                jump = False
        if not player_sprite.rect.x <= 0:     
            if user_input[pygame.K_a]:
                right= False
                left = True
                collision, Lives = player_sprite.move(-speed, 0,collision,right,left,Lives)
                if player_sprite.rect.x < -59:
                    player_sprite.rect.x = width-1          
        if user_input[pygame.K_d]:
            right= True
            left = False
            collision, Lives = player_sprite.move(speed, 0,collision,right,left,Lives)
            if player_sprite.rect.x > width:
                player_sprite.rect.x= -59

        collision,Lives = player_sprite.move(0,gravity,collision,right,left,Lives)
        #reset values
        if player_sprite.rect.y >= (height - block_height):
            Lives -= 1
        if wallmove == 401:
                wallmove = 0   
        if inc == 100:
                inc = 0      
        if lives_before != Lives:
            if Lives == 0:
                #level over
                time.sleep(0.5)
                level_num = EndScreen(0,level_num,False)
                character_sprites,enemies, walls, wall_sprites = emptywalls(character_sprites,enemies,walls, wall_sprites)
                screen.fill ((20,20,20))
                stage = 0
                level = levels[level_num][stage]
                background = (pygame.image.load(level_pics[0]).convert_alpha())
                background = pygame.transform.scale(background, (width,height))
                player_spawnpointx,player_spawnpointy ,player_sprite, character_sprites = drawwalls(level_pics,level, character_sprites)
                inc = 0
                wallmove = 0
                Lives = 3
            else:
                life_lost(Lives)
                player_sprite.rect = player_sprite.image.get_rect(center=(player_spawnpointx,player_spawnpointy))
        pygame.display.flip()      
pygame.quit()

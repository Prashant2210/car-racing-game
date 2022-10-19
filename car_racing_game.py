from ast import If
from itertools import count
import pygame
from pygame import mixer
import random
import time
import os  
pygame.init()
#game_dispaly_surface

gd=pygame.display.set_mode((800,600))
pygame.display.update()
clock=pygame.time.Clock()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
light_green=(0,200,0)
blue=(0,0,255)
gray=(119,118,110)
#high score checking and calculations
if os.path.exists('high_score.txt'):
    with open('high_score.txt','r') as file:
        high_score=int(file.read())
else:
    high_score=0


car_img=pygame.image.load("car-clipart-sprite-sheet-14.jpg")
car_img=pygame.transform.scale(car_img,(100,100))
background=pygame.image.load("background1.jpg")
grass=pygame.image.load("download12.jpg")

def next_level():
    paused=True
    while paused:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    paused=False
                elif event.key==pygame.K_q:
                    pygame.quit()
                    quit()
        gd.blit(background,(0,0))
        pause_message(80,"Welcome to the next level",50,200)
        pause_message(50,"Press C to continue and Q to quit",200,300)
        pygame.display.update()
        clock.tick(5)


def back_button(x_button,y_button,mess_b):
    pygame.draw.rect(gd,red,[x_button,y_button,100,30])
    Message(50,mess_b,x_button,y_button)
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x_button<mouse[0]<x_button+100 and y_button<mouse[1]<y_button+30:
        pygame.draw.rect(gd,blue,[x_button,y_button,100,30])
        Message(50,mess_b,x_button,y_button)
        if click==(1,0,0) and mess_b=="BACK":
            mixer.music.load('button-click.wav')
            mixer.music.play()
            game_intro(high_score)
        if click==(1,0,0) and mess_b=="PAUSE":
            mixer.music.load('button-click.wav')
            mixer.music.play()
            pause()
        
def pause():
    paused=True
    while paused:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    paused=False
                elif event.key==pygame.K_q:
                    pygame.quit()
                    quit()
        gd.blit(background,(0,0))
        pause_message(100,"PAUSED!",200,200)
        pause_message(50,"Press C to continue and Q to quit",200,300)
        pygame.display.update()
        clock.tick(5)

def Message(size,mess,x_pos,y_pos):

    font=pygame.font.SysFont(None,size)
    render=font.render(mess,True,white)
    gd.blit(render, (x_pos,y_pos))
   

def pause_message(size,mess,x_pos,y_pos):
   
   font=pygame.font.SysFont(None,size)
   render=font.render(mess,True,black)
   gd.blit(render, (x_pos,y_pos))

Message(100,"START",150,100)
clock.tick(1)


def button(x_button,y_button,mess_b):
    pygame.draw.rect(gd,green,[x_button,y_button,100,30])
    Message(50,mess_b,x_button,y_button)
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x_button<mouse[0]<x_button+100 and y_button<mouse[1]<y_button+30:
        pygame.draw.rect(gd,light_green,[x_button,y_button,100,30])
        Message(50,mess_b,x_button,y_button)
        if click==(1,0,0) and mess_b=="PLAY":
            mixer.music.load('button-click.wav')
            mixer.music.play()
            Game_loop()
        elif click==(1,0,0) and mess_b=="QUIT":
            mixer.music.load('button-click.wav')
            mixer.music.play()
            pygame.quit()
            quit()

def car(x,y,count,high_score):
    gd.blit(car_img,(x,y))
    gd.blit(grass,(0,0))
    gd.blit(grass,(700,0))
    if 0<x<100 or 700<x+100:
        Message(100,"GAME OVER",200,200)
        font=pygame.font.SysFont(None,60)
        screen_text=font.render('Your Score: '+str(count),True,white)
        gd.blit(screen_text,(200,300))
        if count>high_score:
            high_score=count
            with open('high_score.txt','w') as file:
                file.write(str(high_score))
        hg_score=font.render('High Score: '+str(high_score),True,white)
        gd.blit(hg_score,(200,350))
        mixer.music.load('Game over.wav')
        mixer.music.play()
        pygame.display.update()
        clock.tick(0.3)
        game_intro(high_score)
    
def enmy_car(x_r,y_r):
    gd.blit(car_img,(x_r,y_r))

def car_crash(x,x_r,y,y_r,count,high_score):
    if x_r<x<x_r+80 and y_r<y<y_r+80 or x_r<x+80<x_r+80 and y_r<y<y_r+80:
        Message(50,"CRASHED!",200,200)
        font=pygame.font.SysFont(None,40)
        screen_text=font.render('Your Score: '+str(count),True,white)
        gd.blit(screen_text,(200,300))
        if count>high_score:
            high_score=count
            with open('high_score.txt','w') as file:
                file.write(str(high_score))
        hg_score=font.render('High Score: '+str(high_score),True,white)
        gd.blit(hg_score,(200,350))
        mixer.music.load('crashed.wav')
        mixer.music.play()
        pygame.display.update()
        time.sleep(2)
        game_intro(high_score)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()


def score(count):
    font=pygame.font.SysFont(None,30)
    screen_text=font.render('Score: '+str(count),True,white)
    pause_text=font.render('Press P to PAUSE ',True,white)
    gd.blit(screen_text,(710,0))
    gd.blit(pause_text,(620,30))
    


def game_intro(high_score):
    intro=False
    while intro==False:
       gd.blit(background,(0,0))
       font=pygame.font.SysFont(None,40)
       screen_text=font.render('High Score: '+str(high_score),True,black)
       gd.blit(screen_text,(600,10))
       
       button(100,300,"PLAY")
       button(600,300,"QUIT")
       for event in pygame.event.get():
           if event.type==pygame.QUIT:
               pygame.quit()
               quit()

       pygame.display.update()


def Game_loop():

   x=300
   y=490
   count=0
   x_r=random.randrange(100,600)
   y_r=0
   x_change=0
   
   



   game_over=False
   while game_over==False:
       for event in pygame.event.get():
           mixer.music.load('car speed-1.mp3')
           mixer.music.play(-1)
           if event.type==pygame.QUIT:
               game_over=True
           if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_LEFT:
                   x_change=+10
               elif event.key==pygame.K_RIGHT:
                   x_change=-10
               elif event.key==pygame.K_p:
                   pause()
           if event.type==pygame.KEYUP:
               if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                   x_change=0

    
    
       gd.fill(gray)
       car(x,y,count,high_score)
       score(count)
       back_button(0,0,"BACK")
       back_button(0,50,"PAUSE")
       enmy_car(x_r,y_r)
       y_r+=5
       if count>20:
        y_r+=10
       elif count>40:
        y_r+=15
       elif count>60:
        y_r+=20
       elif count>80:
        y_r+=25
       elif count>100:
        y_r+=30
       elif count>120:
        y_r+=35
       elif count>140:
        y_r+=40
    
       if y_r==600:
        x_r=random.randrange(100,600)
        count+=1
        y_r=0
       car_crash(x,x_r,y,y_r,count,high_score)
       x=x-x_change
       clock.tick(50)
      
       
       
       pygame.display.update()
    

game_intro(high_score)
pygame.display.update()
pygame.quit()
quit()
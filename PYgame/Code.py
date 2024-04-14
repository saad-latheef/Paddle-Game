import pygame
import random
from sys import exit



pygame.init()
screen=pygame.display.set_mode((700,450))
pygame.display.set_caption('Scene')
clock = pygame.time.Clock()
text_font= pygame.font.Font(None,50)



p1= pygame.image.load('paddle.png').convert()
p2=pygame.transform.scale(p1,(5,100))
paddle=p2.get_rect(topleft = (20,20))
paddle2=p2.get_rect(topleft=(670,20))

bound= pygame.image.load('paddle.png').convert()
bound2=pygame.transform.scale(p1,(700,10))
boundrect=bound2.get_rect(topleft = (0,0))
boundrect1=bound2.get_rect(bottomleft = (0,450))

ball=pygame.image.load('paddle.png').convert()
ball_=pygame.transform.scale(ball,(20,20))
ballrect=ball_.get_rect(topleft =(300,300))

dir=1
ydir=2
score11=0
score22=0


gamestate=True
while gamestate:

    
    score1= text_font.render(str(score11),1,(255,255,255))
    score2= text_font.render(str(score22),1,(255,255,255))
    scorerect=score1.get_rect(topleft=(300,40))
    scorerect2=score2.get_rect(topleft=(400,40))

    keys = pygame.key.get_pressed()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #boundary
    screen.blit(bound2,boundrect)
    screen.blit(bound2,boundrect1)

    #score
    screen.blit(score1,scorerect)
    if ballrect.x>710:
        ballrect.x=300
        score11+=1
    screen.blit(score2,scorerect2)
    if ballrect.x<-10:
        ballrect.x=300
        score22+=1


    #player1
    screen.blit(p2,paddle)
    if keys[pygame.K_s]:
        paddle.y+=7
    if keys[pygame.K_w]:
        paddle.y-=7
    if paddle.y<10:
        paddle.y=10
    if paddle.y>340:
        paddle.y=340

    #player2
    screen.blit(p2,paddle2)
    if keys[pygame.K_k]:
        paddle2.y+=7
    if keys[pygame.K_i]:
        paddle2.y-=7
    if paddle2.y<10:
        paddle2.y=10
    if paddle2.y>340:
        paddle2.y=340

    #ball
    screen.blit(ball_,ballrect)
    if dir==1:
        ballrect.x-=5
    if dir==0:
        ballrect.x+=5
    if ballrect.colliderect(paddle):
        dir=0
        ydir=random.randrange(0,2)
    if ballrect.colliderect(paddle2):
        dir=1
        ydir=random.randrange(0,2)
    if dir==0 or dir==1:
        if ydir==1:
            ballrect.y+=2
        else:
            ballrect.y-=2

    #collision with wall
    if ballrect.colliderect(boundrect):
        if ydir==1:
            ydir=0
        else:
            ydir=1
    if ballrect.colliderect(boundrect1):
        if ydir==1:
            ydir=0
        else:
            ydir=1
    
        
        
    pygame.display.update()
    screen.fill((0,0,0))
    clock.tick(60)

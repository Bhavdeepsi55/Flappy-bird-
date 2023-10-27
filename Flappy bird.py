import pygame 
import random 
sound_initiol = pygame.mixer.init()
font_initiol = pygame.font.init()
initiol = pygame.display.init()
screen = pygame.display.set_mode((400,600))
caption = pygame.display.set_caption("Flappy bird")
icon = pygame.display.set_icon(pygame.image.load("css/flappy_bird-removebg-preview.png"))
background = pygame.transform.scale(pygame.image.load("css/desktop-wallpaper-flappy-generator-plus-create-your-own-flappy-bird-game-background.jpg"),(800,600))
bird = pygame.transform.scale(pygame.image.load("css/flappy_bird-removebg-preview.png"),(150,100))
flappy_bird_start = pygame.transform.scale(pygame.image.load("css/flappy bird start.png"),(600,600))
flappy_bird_fall = pygame.mixer.Sound("css/01. Die.mp3")
flappy_bird_ponts = pygame.mixer.Sound("css/03. Point.mp3")
retry_button = pygame.transform.scale(pygame.image.load("css/flappyBirdPlayButton.png"),(150,100))
data = {"score":0,"bird_x":20,"bird_y":60,"pipe_x":400,"height_pipe1":500,"height_pipe2":700,"left_pipe":False,"bird_state": False,"flappy_bird_start_x":-90,'rect_height':700,'fall': True,"bord_score_True":False,"retry_button_x":-300,'blit_button': False}
run = True 
clock = pygame.time.Clock()
score_board = pygame.font.SysFont('Franklin Gothic',60)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:run = False,pygame.quit(),exit()
    screen.blit(background,(0,0))
    rect1 = pygame.draw.rect(screen,(255,0,0),(data['bird_x']+50,data['bird_y']+34,40,40))
    screen.blit(bird,(data['bird_x'],data['bird_y']))
    rect2 = pygame.draw.rect(screen,(255,0,0),(data['pipe_x']+10,-60,60,data['rect_height']-180))
    pipe= pygame.transform.rotate(pygame.transform.scale(pygame.image.load("css/38-388476_flappy-bird-pipes-png-bottle-removebg-preview.png"),(80,data['height_pipe1'])),180) 
    rect3 = pygame.draw.rect(screen,(255,0,0),(data['pipe_x']+10,data['height_pipe2']+20,60,data['height_pipe2']))
    pipe2 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("css/38-388476_flappy-bird-pipes-png-bottle-removebg-preview.png"),(80,500)),360)
    screen.blit(pipe,(data['pipe_x'],-20))
    screen.blit(pipe2,(data['pipe_x'],data['height_pipe2']))
    score_display = score_board.render(f"SCORE:{data['score']}",True,((252, 252, 250)))
    screen.blit(score_display,(20,20))
    screen.blit(retry_button,(data['retry_button_x'],300))
    # True is  data['bird_state']
    
    if data['bird_state']is True:data['bird_y']+=3
    screen.blit(flappy_bird_start,(data['flappy_bird_start_x'],0))
    if True is data['left_pipe']:data['pipe_x']-=2
    keys = pygame.key.get_pressed()
    if keys[pygame.K_KP_ENTER]:
        data['bird_state'] = True
        data['flappy_bird_start_x'] = -2000
        data['left_pipe'] = True
    if keys[pygame.K_SPACE]:data['bird_y']-=6
    if data['bird_y']>600:
        data['left_pipe'] = False
        if True is data['fall']:
            flappy_bird_fall.play()
            data['pipe_x'] = -2000
            data['bird_x'] = -2000
            data['fall'] = False
    if data['bird_x']>data['pipe_x']:flappy_bird_ponts.play()
    if keys[pygame.K_RSHIFT]:data['bird_y'] = 30
    if data['bird_y']<0:data['bird_y'] = 0
    if data['pipe_x']<-10:
        data_set = ['0','1','2','3','4','5','6']
        rand = random.choice(data_set)
        print(rand)

        if '0' in rand:data['height_pipe1'] = 0;data['height_pipe2'] = 100;data['rect_height'] = 100+110
        if '1' in rand:data['height_pipe1'] = 100;data['height_pipe2'] = 200;data['rect_height'] = 200+110
        if '2' in rand:data['height_pipe1'] = 200;data['height_pipe2'] = 300;data['rect_height'] = 300+110
        if '3' in rand:data['height_pipe1'] = 300;data['height_pipe2'] = 400;data['rect_height'] = 400+105
        if '4' in rand:data['height_pipe1'] = 400;data['height_pipe2'] = 500;data['rect_height'] = 500+105
        if '5' in rand:data['height_pipe1'] = 500;data['height_pipe2'] = 600;data['rect_height'] = 600+100
        if '6' in rand:data['height_pipe1'] = 300;data['height_pipe2'] = 400;data['rect_height'] = 400+105
        data['pipe_x']=500
        data['score']+=1

    if rect1.colliderect(rect2):
       
        data['bord_score_True'] = True
        data['bird_y'] = 1000
        data['pipe_x'] = -2000
        data['left_pipe'] = False
        data['bord_score_True']= True
        
   
    if rect1.colliderect(rect3):
        data['bord_score_True'] = True
        data['bird_y'] = 1000
        data['pipe_x'] = -2000
        data['left_pipe'] = False
    

    if data['pipe_x'] == -2000:
         data['blit_button'] = True
    if data['blit_button'] is True:
        screen.blit(retry_button,(125,300))
        #  125,300

    if  keys[pygame.K_KP_1]:
        data['bird_state'] = False
        data['bird_x'] = 20
        data['bird_y'] = 60
        data['bord_score_True'] = False
        data['fall'] = True
        data['flappy_bird_start_x'] = -90
        data['height_pipe1'] = 500
        data['height_pipe2'] = 700
        data['left_pipe'] = False
        data['pipe_x'] = 400
        data['rect_height'] = 700
        data['score'] = 0
        data['blit_button'] = False
        
    pygame.display.update()
    clock.tick(100)
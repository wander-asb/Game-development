import pygame

pygame.init()

window = pygame.display.set_mode([1280, 720])


title = pygame.display.set_caption('Meu primeiro game')
field = pygame.image.load(r'C:\Users\wande\Documents\game_development\assets\field.png')

player1 = pygame.image.load(r'C:\Users\wande\Documents\game_development\assets\player1.png')
player_1_y =310
player_1_moveup = False
player_1_movedown = False


player2 = pygame.image.load(r'C:\Users\wande\Documents\game_development\assets\player2.png')
player_2_y =310

ball = pygame.image.load(r'C:\Users\wande\Documents\game_development\assets\ball.png')
ball_x = 617
ball_y = 337
ball_dir = -8
ball_dir_y = 1


loop = True

def move_player():
    global player_1_y
    if (player_1_moveup):
        player_1_y -= 12
    else:
        player_1_y += 0

    if (player_1_movedown):
        player_1_y += 12
    else:
        player_1_y += 0

    if (player_1_y <= 0):
        player_1_y = 0
    elif player_1_y >= 575:
        player_1_y = 575

def move_player2():
    global player_2_y
    player_2_y = ball_y

def move_ball():
    global ball_x
    global ball_y
    global ball_dir
    global ball_dir_y

    ball_x += ball_dir
    ball_y += ball_dir_y

    if (ball_x < 120):
        if (player_1_y < ball_y + 23):
            if (player_1_y + 146 > ball_y):
                ball_dir *= -1

    if (ball_x > 1100):
        if (player_2_y < ball_y + 23):
            if (player_2_y + 146 > ball_y):
                ball_dir *= -1
    
    if (ball_y > 690):
        ball_dir_y *= -1
    elif (ball_y <= 0):
        ball_dir_y *= -1

    if (ball_x < -50):
        ball_x = 617
        ball_y = 337
        ball_dir_y *= -1
        ball_dir *= -1
        
    elif (ball_x > 1320):
        ball_x = 617
        ball_y = 337
        ball_dir_y *= -1
        ball_dir *= -1

def draw():
    window.blit(field, (0,0))
    window.blit(player1, (50, player_1_y))
    window.blit(player2, (1150, player_2_y))
    window.blit(ball, (ball_x, ball_y))


while loop:

    for events in pygame.event.get():
        if (events.type == pygame.QUIT):
            loop = False
        if (events.type == pygame.KEYDOWN):
            if (events.key == pygame.K_w):
                player_1_moveup = True
            elif events.key == pygame.K_s:
                player_1_movedown = True
        if (events.type == pygame.KEYUP):
            if (events.key == pygame.K_w):
                player_1_moveup = False
            elif events.key == pygame.K_s:
                player_1_movedown = False
                
    draw()
    move_ball()
    move_player()
    move_player2()
    pygame.display.update()




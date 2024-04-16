import pygame
# x = pygame.init()
pygame.init()
import random

# Game colors
white = (255,255, 255)
red =  (255, 0, 0)
black= (0,0,0)

screen_width = 600
screen_height = 400


# Creating Game window/Display
gameWindow = pygame.display.set_mode((screen_width,screen_height))

# Set the Game title from here
pygame.display.set_caption("My Game")
pygame.display.update()
pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color , x,y):
     screen_text = font.render(text, True, color)
     gameWindow.blit(screen_text, [x,y])
     
     
def plot_snake(gameWindo,color, snake_list, snake_size ):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x,y, snake_size, snake_size])




# Game loop
def gameloop():
    
    # Game Specific Valriables
    exit_game = False
    game_over = False
    snake_x = 50
    snake_y = 40
    velocity_y =0
    score = 0
    
    food_x = random.randint(20, screen_height/2)
    food_y = random.randint(20, screen_width/2)
    snake_size = 15
    fps = 22
    init_velocity = 0.1
    velocity_x =0
    snake_list = []
    snake_length = 1


    

    while not exit_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        # snake_x = snake_x+10
                        velocity_x = init_velocity
                        velocity_y = 0
                        
                    if event.key == pygame.K_LEFT:
                        # snake_x = snake_x -10
                        velocity_x = -init_velocity
                        velocity_y = 0
                        
                        
                        # snake_y = snake_y +10
                        velocity_y = init_velocity
                        velocity_x = 0
                        
                        
                    if event.key == pygame.K_UP:
                        
                        # snake_y = snake_y -10
                        if event.key == pygame.K_DOWN:
                            velocity_y = -init_velocity
                            velocity_x = 0
                        
                        
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            
            if abs(snake_x - food_x ) <6 and abs (snake_y - food_y ) <6 :
                score +=1
                food_x = random.randint(20, screen_height/2)
                food_y = random.randint(20, screen_width/2)
                snake_length +=15

                # pygame.Surface.fill(white, rect=None, special_flags=0)
            gameWindow.fill(white)
            text_screen ("Score :" + str(score*10), red, 5,5)
            pygame.draw.rect(gameWindow,red , [food_x, food_y, snake_size, snake_size])
                    
            
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            
            if len (snake_list)>snake_length:
                del snake_list[0]
                
            
            # Don't do it hardcore
            # pygame.draw.rect(gameWindow, black, [ snake_x, snake_y , snake_size , snake_size])
            plot_snake(gameWindow, black, snake_list, snake_size)
            pygame.display.update()
                
pygame.quit()

quit()
                
            
            
            
            
        
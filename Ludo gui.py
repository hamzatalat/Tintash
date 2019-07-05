#!/usr/bin/env python
# coding: utf-8

# In[68]:


import pygame
import random


out=0
random_no =0
curr1=0
curr2=0
mov1 = 0
mov2 = 0



out1=0
random_no1 =0
curr11=0
curr21=0
mov11 = 0
mov21 = 0





path1 = [[6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [5, 6], [4, 6], [3, 6], [2, 6], [1, 6], [0, 6], [0, 7], [0, 8],
         [1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 9], [6, 10], [6, 11], [6, 12], [6, 13], [6, 14], [7, 14],
         [8, 14], [8, 13], [8, 12], [8, 11], [8, 10], [8, 9], [9, 8], [10, 8], [11, 8], [12, 8], [13, 8], [14, 8],
         [14, 7], [14, 6], [13, 6], [12, 6], [11, 6], [10, 6], [9, 6], [8, 5], [8, 4], [8, 3], [8, 2], [8, 1],
         [8, 0], [7, 0], [6, 0]]
path2 = [[8, 13], [8, 12], [8, 11], [8, 10], [8, 9], [9, 8], [10, 8], [11, 8], [12, 8], [13, 8], [14, 8], [14, 7],
         [14, 6], [13, 6], [12, 6], [11, 6], [10, 6], [9, 6], [8, 5], [8, 4], [8, 3], [8, 2], [8, 1], [8, 0],
         [7, 0], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [5, 6], [4, 6], [3, 6], [2, 6], [1, 6], [0, 6],
         [0, 7], [0, 8], [1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 9], [6, 10], [6, 11], [6, 12], [6, 13],
         [6, 14], [7, 14], [8, 14]]


def player1(row,column,grid):
    global out
    global curr1
    global curr2
    global mov1
    global mov2
    global path1
    global path2
    a=path1[curr1%52][0]
    b=path1[curr1%52][1]
    aa=path1[curr2%52][0]
    bb=path1[curr2%52][1]


    mov1=0
    mov2=0
    if a==row and b==column:
        mov1=1
    if aa==row and bb==column:
        if mov1 != 1:
            mov2=1    

    if random_no==6 :
        #if out<2:
        out+=1
        if out==1:
            grid[2][2]=1
            a=path1[curr1%52][0]
            b=path1[curr1%52][1]
            grid[a][b]=8

        if out==2:
            grid[2][3]=1
            a=path1[curr2%52][0]
            b=path1[curr2%52][1]
            grid[a][b]=8
        
        
        if out > 2:
            if mov1 == 1:
                mov1 = 0
                a=path1[curr1%52][0]
                b=path1[curr1%52][1]
                if curr1!=0:
                    grid[a][b]=0
                else:
                    grid[a][b]=2
                curr1 = curr1 + random_no 
                a=path1[curr1%52][0]
                b=path1[curr1%52][1]
                grid[a][b]=8


            if mov2 ==1 :
                mov2 == 0
                a=path1[curr2%52][0]
                b=path1[curr2%52][1]
                if curr2!=0:
                    grid[a][b]=0
                else:
                    grid[a][b]=2
                curr2 = curr2 + random_no
                a=path1[curr2%52][0]
                b=path1[curr2%52][1]
                grid[a][b]=8
    if random_no < 6:

        if mov1 == 1:
            mov1 = 0
            a=path1[curr1%52][0]
            b=path1[curr1%52][1]
            if curr1!=0:
                grid[a][b]=0
            else:
                grid[a][b]=2
            curr1 = curr1 + random_no 
            a=path1[curr1%52][0]
            b=path1[curr1%52][1]
            grid[a][b]=8
            
        
        if mov2 ==1 :
            mov2 == 0
            a=path1[curr2%52][0]
            b=path1[curr2%52][1]
            if curr2!=0:
                grid[a][b]=0
            else:
                grid[a][b]=2
            curr2 = curr2 + random_no
            a=path1[curr2%52][0]
            b=path1[curr2%52][1]
            grid[a][b]=8
        global out1
        global curr11   
        t1=path1[curr1%52][0]
        t2=path1[curr1%52][1]
        t11=path1[curr1%52][0]
        t12=path1[curr1%52][1]
        if path1[curr1%52]==path2[curr11%52] or path1[curr1%52]==path2[curr21%52]:
            grid[t1][t2]=0
            out1-=1
            curr11=0
        if path1[curr2%52]==path2[curr11%52] or path1[curr2%52]==path2[curr21%52]:
            grid[t1][t2]=0
            out1-=1
            curr11=0
    return grid




def player2(row,column,grid):
    global out1
    global curr11
    global curr21
    global mov11
    global mov21
    global path2
    global random_no
    a=path2[curr11%52][0]
    b=path2[curr11%52][1]
    aa=path2[curr21%52][0]
    bb=path2[curr21%52][1]


    mov11=0
    mov21=0
    if a==row and b==column:
        mov11=1
    if aa==row and bb==column:
        if mov11 != 1:
            mov21=1    

    if random_no==6 :
        if out1<2:
            out1+=1
        if out1==1:
            grid[2][2]=1
            a=path2[curr11%52][0]
            b=path2[curr11%52][1]
            grid[a][b]=9
            
            grid[12][11]=1

        if out==2:
            grid[2][3]=1
            a=path2[curr21%52][0]
            b=path2[curr21%52][1]
            grid[a][b]=9
            grid[12][12]=1

    if random_no < 6:

        if mov11 == 1:
            mov11 = 0
            a=path2[curr11%52][0]
            b=path2[curr11%52][1]
            if curr11!=0:
                grid[a][b]=0
            else:
                grid[a][b]=2
            curr11 = curr11 + random_no 
            a=path2[curr11%52][0]
            b=path2[curr11%52][1]
            grid[a][b]=9
            
        
        if mov21 ==1 :
            mov21 == 0
            a=path2[curr21%52][0]
            b=path2[curr21%52][1]
            if curr21!=0:
                grid[a][b]=0
            else:
                grid[a][b]=2
            curr21 = curr21 + random_no
            a=path2[curr21%52][0]
            b=path2[curr21%52][1]
            grid[a][b]=9
            
                        
    return grid





def board():
    check=0
    global random_no
    global out
    global curr1
    global curr2
    global mov1
    global mov2
    global path1
    global path2
    no=0
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    YELLOW = (255,255,0)
    BLUE = ((0,0,255))

    # This sets the WIDTH and HEIGHT of each grid location
    WIDTH = 40
    HEIGHT = 40

    # This sets the margin between each cell
    MARGIN = 1
    

    # Create a 2 dimensional array. A two dimensional
    # array is simply a list of lists.
    grid = []
    for row in range(15):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(15):
            grid[row].append(0)  # Append a cell


    for i in range(0, 15):
        for j in range(0, 15):
            if (j < 6 or j > 8) and (i < 6 or i > 8):
                grid[i][j]=1

    #         else:
    #             self.lists[i][j] = '   '
            if (i > 5) and (i < 9) :
                grid[i][j]=0
            if (j > 5) and (j < 9):
                grid[i][j]=0


            if (j == 6 or j == 8) and (i == 6 or i == 8):
                grid[i][j]=1
            
            if (i == 7) and (j > 0) and (j < 7):
                grid[i][j]=2
            if (i == 7) and (j > 7) and (j < 14):
                grid[i][j]=3
            if (j == 7) and (i > 0) and (i < 7):
                grid[i][j]=4
            if (j == 7) and (i > 7) and (i < 14):
                grid[i][j]=5
            if (i==7 and j==7):
                grid[i][j]=0
            
            
            if i==6 and j==1:
                grid[i][j]=2
            if i==8 and j==2:
                grid[i][j]=2
                
                
            if i==2 and j==6:
                grid[i][j]=4
            if i==1 and j==8:
                grid[i][j]=4
                
            if i==6 and j==12:
                grid[i][j]=3
            if i==8 and j==13:
                grid[i][j]=3
            
            
            
            if i==12 and j==8:
                grid[i][j]=5
            if i==13 and j==6:
                grid[i][j]=5
                
            
            
            if i==2 and j==2:
                grid[i][j]=8
            if i==2 and j==3:
                grid[i][j]=8
            
            
            
            if i==12 and j==11:
                grid[i][j]=9
            if i==12 and j==12:
                grid[i][j]=9
                
    # Set row 1, cell 5 to one. (Remember rows and
    # column numbers start at zero.)
    grid[1][5] = 1

    # Initialize pygame
    pygame.init()

    # Set the HEIGHT and WIDTH of the screen
    WINDOW_SIZE = [615, 615]
    screen = pygame.display.set_mode(WINDOW_SIZE)

    # Set title of screen
    pygame.display.set_caption("Array Backed Grid")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one
                #grid[row][column] = 1
#                 mov1=0
#                 mov2=0
                
                
                
                
                
                random_no = random.randint(1, 6)
                if check==1:
                    grid=player2(row,column,grid)
                    check-=1
                if check==0:
                    check+=1
                    grid=player1(row,column,grid)
#                 a=path1[curr1%52][0]
#                 b=path1[curr1%52][1]
#                 aa=path1[curr2%52][0]
#                 bb=path1[curr2%52][1]
                
                
                
#                 if a==row and b==column:
#                     mov1=1
#                 if aa==row and bb==column:
#                     if mov1 != 1:
#                         mov2=1    
                
#                 if random_no==6 :
#                     if out<2:
#                         out+=1
#                     if out==1:
#                         grid[2][2]=1
#                         a=path1[curr1%52][0]
#                         b=path1[curr1%52][1]
#                         grid[a][b]=8
                        
#                     if out==2:
#                         grid[2][3]=1
#                         a=path1[curr2%52][0]
#                         b=path1[curr2%52][1]
#                         grid[a][b]=8
                        
#                 if random_no < 6:
                    
#                     if mov1 == 1:
#                         a=path1[curr1%52][0]
#                         b=path1[curr1%52][1]
#                         if curr1!=0:
#                             grid[a][b]=0
#                         else:
#                             grid[a][b]=2
#                         curr1 = curr1 + random_no 
#                         a=path1[curr1%52][0]
#                         b=path1[curr1%52][1]
#                         grid[a][b]=8
#                     if out==2:
#                         if mov2 ==1 :
#                             a=path1[curr2%52][0]
#                             b=path1[curr2%52][1]
#                             if curr2!=0:
#                                 grid[a][b]=0
#                             else:
#                                 grid[a][b]=2
#                             curr2 = curr2 + random_no
#                             a=path1[curr2%52][0]
#                             b=path1[curr2%52][1]
#                             grid[a][b]=8
                        

                
                print("Click ", pos, "Grid coordinates: ", row, column)

        # Set the screen background
        screen.fill(BLACK)

        # Draw the grid
        for row in range(15):
            for column in range(15):
                color = WHITE
                if grid[row][column] == 0:
                    color = WHITE
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
                if grid[row][column] == 1:
                    color = BLACK
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
                if grid[row][column] == 2:
                    color = GREEN
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
                if grid[row][column] == 3:
                    color = YELLOW
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
                if grid[row][column] == 4:
                    color = RED
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
                if grid[row][column] == 5:
                    color = BLUE
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
                if grid[row][column] == 8:
                    color = GREEN
                    pygame.draw.circle(screen, color, (((MARGIN + WIDTH) * column + MARGIN)+20 ,
                                      ((MARGIN + HEIGHT) * row + MARGIN)+20), 20, 20)

                if grid[row][column] == 9:
                    color = YELLOW
                    pygame.draw.circle(screen, color, (((MARGIN + WIDTH) * column + MARGIN)+20 ,
                                      ((MARGIN + HEIGHT) * row + MARGIN)+20), 20, 20)
        # Limit to 60 frames per second
        
        clock.tick(60)
        myfont = pygame.font.SysFont("monospace", 30)

        
        
        #image = pygame.image.load(r'C:\Users\tin\Desktop\1.jpg')
        #screen.blit(image, (0, 0))
        
        
        
        # render text
        label = myfont.render(str(random_no), 1, (0,0,0))
        screen.blit(label, (300, 300))
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
    
    
board()
#player1(0,0)


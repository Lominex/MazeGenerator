from PIL import Image
import time 
import random


image = Image.open('maze.png')
width = image.width
heigth = image.height
pixels = image.load()
image.save('mazeSolved.png')

cellSize = 3
cols = int(width / cellSize)
rows = int(heigth / cellSize)

w = int(width / cellSize)
h = int(heigth / cellSize)

grid = [[0 for x in range(w)] for y in range (h)]
visited = []
stack = []
solution = []
cell = 0

startTime = time.time()

def move_up(x, y):
    x, y = x ,y-2
    solution.append((x,y+2))
    solution.append((x,y+1))
    solution.append((x,y))
    stack.append((x,y))
    visited.append((x,y))
    return x, y

def move_right(x, y):
    x, y = x+2 ,y
    solution.append((x-2,y))
    solution.append((x-1,y))
    solution.append((x,y))
    stack.append((x,y))
    visited.append((x,y))
    return x, y

def move_down(x, y):
    x, y = x ,y+2
    solution.append((x,y-2))
    solution.append((x,y-1))
    solution.append((x,y))
    stack.append((x,y))
    visited.append((x,y))
    return x, y

def move_left(x, y):
    x, y = x-2 ,y
    solution.append((x+2,y))
    solution.append((x+1,y))
    solution.append((x,y))
    stack.append((x,y))
    visited.append((x,y))
    return x, y
            
def setup():


    print('########################')
    print('Widht : ' + str(width))
    print('Height: ' + str(heigth))
    print('Cols  : ' + str(cols))    
    print('Rows  : ' + str(rows))

    pixels[1, 1] = (0,255,0)
    stack.append((1,1))
    visited.append((1,1))
    solveMaze(1,1)
        

def solveMaze(x,y):
    cells = []
    Solved = False
    while not Solved:
        cells = []
        try:
            if(pixels[x,y] == (255,0,0)):
                Solved = True
                print('Solved')
        except IndexError:
            #print('NotFinisched')
            pass
        
        #pygame.time.wait(25)
        if(x+2 > 0 and y > 0 and pixels[x+1 ,y] == (255, 255, 255) and (x+2,y) not in visited and x < width-2):
            cells.append("right")
        if(x > 0 and y+2 > 0 and pixels[x ,y+1] == (255, 255, 255) and (x,y+2) not in visited and y < heigth-2):
            cells.append("down")
        if(x-2 > 0 and y > 0 and pixels[x-1 ,y] == (255, 255, 255) and (x-2,y) not in visited and x > 2):
            cells.append("left")
        if(x > 0 and y-2 > 0 and pixels[x ,y-1] == (255, 255, 255) and (x,y-2) not in visited and y > 2):
            cells.append("top")
        if(len(cells) > 0):
            #normal move
            choice = random.randint(0, len(cells)-1)
            if(cells[choice] == 'right'):
                x,y = move_right(x, y)
                #print('right')
            if(cells[choice] == 'down'):
                x,y = move_down(x, y)
                #print('down')
            if(cells[choice] == 'left'):
                x,y = move_left(x, y)
                #print('left')
            if(cells[choice] == 'top'):
                x,y = move_up(x, y)
                #print('top')
        else:
            #Backtrack
            x, y = stack[len(stack) - 1]
            solution.pop()
            solution.pop()
            #solution.pop()
            stack.pop()
            #print('back')
        #print(x, y)
    
    for pixel in solution:
        pixels[pixel] = (200,100,0)
    duration = round(time.time() - startTime, 3)
    print('Duration: ' + str(duration) + " seconds")
    print('########################')
    print('ENDE')
    pixels[width-2, heigth -2] = (255,0,0)  
    pixels[1, 1] = (0,255,0)        
    
setup()

image.save('mazeSolved.png')
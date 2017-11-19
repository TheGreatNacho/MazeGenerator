from random import randint
from math import sqrt
import png
import imageio
import os

def reverseDir(d):
    return (d<<2|d>>2)&15

def generateMaze(w,h,sp):
    print("Generating "+str(w)+" by "+str(h)+" maze at starting point ["+str(sp[0])+", "+str(sp[1])+"].")
    maze = [[0 for y in range(h)] for x in range(w)]
    spacesLeft = w*h
    stack = []
    stack.append([sp[0], sp[1]])
    i=0
    while len(stack)>0:
        cursor = stack[len(stack)-1]
        x = cursor[0]
        y = cursor[1]
        #input("Stack size: "+str(len(stack))+" ["+str(x)+","+str(y)+"]")
        d = [1,2,4,8]
        blocked = 1
        while blocked:
            move = d[randint(0, len(d)-1)]
            lx = x
            ly = y
            #Swap Move==N to Move&N
            if (move&1):
                lx=lx+1
            elif (move&2):
                ly=ly+1
            elif (move&4):
                lx=lx-1
            elif (move&8):
                ly=ly-1
            if (not (lx >=w or lx < 0 or ly >= h or ly < 0 or maze[lx][ly])):
                maze[x][y] += move
                x = lx
                y = ly
                maze[x][y] += reverseDir(move)
                stack.append([x,y])
                spacesLeft -= 1
                if (((((w*h)-spacesLeft)/(w*h))*100)%5==0):
                    print(str((((w*h)-spacesLeft)/(w*h))*100)+"% complete.")
                blocked = 0
            else:
                if (len(d)==1):
                    stack.remove(cursor)
                    blocked = 0
                else:
                    d.remove(move)
    print("Finished generating maze.")
    return maze

def generateMazeAnimated(w,h,sp):
    print("Generating "+str(w)+" by "+str(h)+" maze at starting point ["+str(sp[0])+", "+str(sp[1])+"].")
    maze = [[0 for y in range(h)] for x in range(w)]
    spacesLeft = w*h
    stack = []
    stack.append([sp[0], sp[1]])
    i=0
    while len(stack)>0:
        cursor = stack[len(stack)-1]
        x = cursor[0]
        y = cursor[1]
        #input("Stack size: "+str(len(stack))+" ["+str(x)+","+str(y)+"]")
        d = [1,2,4,8]
        blocked = 1
        while blocked:
            move = d[randint(0, len(d)-1)]
            lx = x
            ly = y
            if (move&1):
                lx=lx+1
            elif (move&2):
                ly=ly+1
            elif (move&4):
                lx=lx-1
            elif (move&8):
                ly=ly-1
            if (not (lx >=w or lx < 0 or ly >= h or ly < 0 or maze[lx][ly])):
                maze[x][y] += move
                x = lx
                y = ly
                maze[x][y] += reverseDir(move)
                stack.append([x,y])
                spacesLeft -= 1
                if (((((w*h)-spacesLeft)/(w*h))*100)%0.5==0):
                    print(str((((w*h)-spacesLeft)/(w*h))*100)+"% complete.")
                blocked = 0
                pngMaze(maze, "mazes/output/"+str(i)+".png")
                i=i+1
            else:
                if (len(d)==1):
                    stack.remove(cursor)
                    blocked = 0
                else:
                    d.remove(move)
    images = []
    for x in range(0, i-1):
        images.append(imageio.imread("mazes/output/"+str(x)+".png"))
        os.remove("mazes/output/"+str(x)+".png")
    imageio.mimsave("mazes/output/final.gif", images)
    print("Finished generating maze.")
    return maze

def generateMazeV2(w,h,sp,mS):
    print("Generating "+str(w)+" by "+str(h)+" maze at starting point ["+str(sp[0])+", "+str(sp[1])+"].")
    maze = [[0 for y in range(h)] for x in range(w)]
    stack = []
    stack.append([sp[0], sp[1]])
    bs=1
    while len(stack)>0:
        cursor = stack[len(stack)-1]
        x = cursor[0]
        y = cursor[1]
        #input("Stack size: "+str(len(stack))+" ["+str(x)+","+str(y)+"]")
        d = [1,2,4,8]
        blocked = 1
        while blocked:
            move = d[randint(0, len(d)-1)]
            lx = x
            ly = y
            if (move==1):
                lx=lx+1
            elif (move==2):
                ly=ly+1
            elif (move==4):
                lx=lx-1
            elif (move==8):
                ly=ly-1
            if (not (lx >=w or lx < 0 or ly >= h or ly < 0 or maze[lx][ly]&15 or (len(stack))>=mS*(w*h))):
                maze[x][y] += move
                x = lx
                y = ly
                maze[x][y] += reverseDir(move)
                stack.append([x,y])
                if (len(stack)>bs):
                    bs = len(stack)
                blocked = 0
            else:
                if (len(d)==1):
                    if (len(stack)>=mS*(w*h)):
                        maze[x][y] += 16
                    stack.remove(cursor)
                    blocked = 0
                else:
                    d.remove(move)
    print("Finished generating maze. Stack util: "+str((bs/(w*h))*100)+"%")
    return maze
def pngMaze(maze, name):
    h = len(maze[0])
    w = len(maze)
    p = [[0 for x in range(w*3)] for y in range(h*3)]
    for iy in range(0,h):
        for ix in range(0,w):
            cell = maze[ix][iy]
            if (cell):
                p[(iy*3)+1][(ix*3)+1] = 255
            else:
                p[(iy*3)+1][(ix*3)+1] = 0 
            if (16&cell):
                p[(iy*3)+1][(ix*3)+1] = 255
            if 1&cell:
                p[(iy*3)+1][(ix*3)+2] = 255
            if 2&cell:
                p[(iy*3)+2][(ix*3)+1] = 255
            if 4&cell:
                p[(iy*3)+1][(ix*3)] = 255
            if 8&cell:
                p[(iy*3)][(ix*3)+1] = 255
    
    f = open(name, 'wb')
    w = png.Writer(w*3, h*3, greyscale=True)
    w.write(f, p) ; f.close()
def saveMaze(maze, name):
    h = len(maze[0])
    w = len(maze)
    f = open(name+".nmf", "w+")
    f.write(chr(w)+chr(h))
    for iy in range(0,h):
        for ix in range(0,w):
            cell = maze[ix][iy]
            f.write(chr(cell))
        f.write(chr(32))
    f.close()
def openMaze(name):
    f = open(name+".nmf", "r")
    file = f.read()
    w = ord(file[0])
    h = ord(file[1])
    maze = [[0 for y in range(h)] for x in range(w)]
    file = file[2:]
    for iy in range(0,h):
        for ix in range(0, w):
            #print(ord(file[(iy*h)+ix]))
            maze[ix][iy] = ord(file[((iy*h)+ix)])
    f.close()
    return maze

m = generateMaze(100,100,[10,5])
pngMaze(m, "mazes/experiment.png")

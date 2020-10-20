import math

ballspd = 1.2

time = 0
angle = PI/2 * -1 #random(PI+0.5 , 2*PI-0.5)
ballspdX = 0.1 * ballspd
ballspdY = 0.1 * ballspd
ballposX = 250
ballposY = 250
block_numb = 10
block_list = []
brk = True
brickX = 0
brickY = 0
ballRadius = 5
anglemax = PI/ 1.9
ancienmouseX = 0
racHeight = 10
racLenght = 70

def setup ():
    size(500, 500)
    block_list_gen()
    frameRate(120)
    
    
def draw ():
    
    clear()
    angleAlea ()
    times()
    rec ()
    ballPos()
    wallhit ()
    #hit ()
    draw_brick ()
    hitingBrick ()
    aleaSpeed ()


def times (): 
    global time, time2
    time2 = millis() - time
    time = millis()

    
    
def rec () :
    global racLenght, racHeight
    if mouseX - racLenght/2 < 0.05*width :
        rect(0.05*width, 0.85*height , racLenght, racHeight, 4)
        
    elif mouseX - racLenght/2 > 0.85*width :
        rect(0.85*width, 0.85*height , racLenght, racHeight, 4)
        
    else :
        rect(mouseX - racLenght/2, 0.85*height , racLenght, racHeight, 4)
        
        
        
def ballPos () :
    global ballposX, ballposY, ballspdX, ballspdY, ballRadius, angle
    
    ballposX += cos(angle) * time2 * ballspdX * ballspd 
    ballposY -= sin(angle) * time2 * ballspdY * ballspd

    circle(ballposX, ballposY, 2*ballRadius)
    
def wallhit () :
    global ballposX, ballposY, ballspdX, ballspdY, ballRadius, angle
    
    if ballposX > width - ballRadius :
        angle = PI - angle
        ballspdX *= random(0.8,1.2)
        
    elif ballposX - ballRadius < 0 :
        angle = PI - angle
        ballspdX *= random(0.8,1.2)
        
    elif ballposY - 7 < 0 :
        angle = - angle
        ballspdY *= random(0.8,1.2)
    
        
def hit ():
    global ballposX, ballposY, ballspdX, ballspdY, block_list_gen, ballRadius, rectLenght, rectHeight, angle
    #mouseX - racLenght < ballposX < mouseX + racLenght   and   ballposY + ballRadius < 0.9*height + ballRadius  < ballposY + racHeight and ballspdY > 0 :
    if mouseX - racLenght/2 < ballposX < mouseX + racLenght/2  and     0.85*height < ballposY + ballRadius < 0.85*height + 0.2*racHeight :
        angle = - angle
        
def block_list_gen () :
    global block_numb, block_list, brickX, brickY
    for i in range (0, 4) :      
        for j in range (0,7):        
            block_list.append([brickX,brickY,int(random(1,3))])
            brickX += 1
            brickX = brickX%6
        brickY += 1
             

def draw_brick () :
    global block_list
    brickY_Draw = 20
    a = block_list[len(block_list)-1][1]
    for j in range (1, a) :
        for i in range (0, len(block_list)-1) :
            if block_list[i][2] != 0 :
                rect (block_list[i][0]*20, block_list[i][1]*20, 20, 10)
                
def hitingBrick () :
    global block_list, ballposX, ballposY, ballspdY, ballspdX
    for i in range (0, len(block_list)-1) :

        #                                                     horizontalHAUT                                                                                                 horizontalBAS
                                            
        #                         X                                                    Y                                                         X                                                     Y
        if block_list[i][0]*20 < ballposX < block_list[i][0]*20 + 20 and block_list[i][1]*20 + 10 > ballposY + ballRadius > block_list[i][1]*20 or block_list[i][0]*20 < ballposX < block_list[i][0]*20 + 20 and ballposY + ballRadius < block_list[i][1]*20 + 10 : 
            ballspdY *= -1
       
        
        #                                                       verticalDROITE                                                                                                       verticalGAUCHE
        
        #                            Y                                                          X                                                         Y                                                   X
        elif block_list[i][1]*20 < ballposY < block_list[i][1]*20 + 10 and ballposX - ballRadius < block_list[i][0]*20 + 20 or block_list[i][1]*20 < ballposY < block_list[i][1]*20 + 10 and ballposX + ballRadius < block_list[i][0]*20 : 
            ballspdX *= -1

def aleaSpeed () :
    global ancienmouseX, ballspd
    
    if mouseX - ancienmouseX > 5 :
        delta = abs(mouseX - ancienmouseX)
        ancienmouseX = mouseX
        delta /= 10

    else :
        delta = 1
    global delta
    
def angleAlea () :
    global racLenght, racHeight, angle, delta, ballspd
    if mouseX - racLenght/2 < ballposX < mouseX + racLenght / 2   and     0.85*height < ballposY + ballRadius < 0.85*height + 0.2*racHeight :
        ratio = (100*(ballposX-(mouseX - racLenght/2)) / racLenght)
        print ("ratio:", ratio)
        if ratio < 50 :
            angle =  (PI - ( (PI/2) * (ratio/50) ) ) 

        elif ratio > 50 :
            angle = ( (PI/2) - ((PI/2)/(ratio/100)) )*-1


    
    
            
     
        
                
    
            
        
        
        


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

        

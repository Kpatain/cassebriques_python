ballsdp = 10
ballspdX = random(0.2, 0.3) * ballsdp
ballspdY = random(0.2, 0.3) * ballsdp
ballposX = 250
ballposY = 250
block_numb = 10
block_list = []
brk = True
brickX = 0
brickY = 0
ballRadius = 5
rectLenght = 50
rectHeight = 50


def setup ():
    size(500, 500)
    block_list_gen()
    print(block_list)
    print  block_list[3][0]
    
    
def draw ():
    clear()
    rec ()
    ballPos()
    wallhit ()
    hit ()
    draw_brick ()
    hitingBrick () 
    
    
def rec () :
    if mouseX - 25 < 0.05*width :
        rect(0.05*width, height - 50, 50, 10, 4)
        
    elif mouseX - 25 > 0.85*width :
        rect(0.85*width, height - 50, 50, 10, 4)
        
    else :
        rect(mouseX - 25, height - 50, 50, 10, 4)
        
        
        
def ballPos () :
    global ballposX, ballposY, ballspdX, ballspdY, ballRadius
    ballposX += ballspdX
    ballposY += ballspdY
    circle(ballposX, ballposY, 2*ballRadius)
    
def wallhit () :
    global ballposX, ballposY, ballspdX, ballspdY, ballRadius
    if ballposX > width - ballRadius :
        ballspdX *= -1
        #ballposX -= ballRadius
        ballspdX *= random(0.8,1.2)
    elif ballposX - ballRadius < 0 :
        ballspdX *= -1
        #ballposX += ballRadius
        ballspdX *= random(0.8,1.2)
    elif ballposY - 7 < 0 :
        ballspdY *= -1
        #ballposY += ballRadius
        ballspdY *= random(0.8,1.2)
    
        
def hit ():
    global ballposX, ballposY, ballspdX, ballspdY, block_list_gen, ballRadius, rectLenght, rectHeight
    
    if mouseX - rectLenght < ballposX < mouseX + rectLenght   and   ballposY + ballRadius > height - 50 > ballposY + rectHeight and ballspdY > 0 :
        ballspdY *= -1
        
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
        if block_list[i][0]*20 < ballposX < block_list[i][0]*20 + 20 and ballposY + ballRadius > block_list[i][1]*20 or block_list[i][0]*20 < ballposX < block_list[i][0]*20 + 20 and ballposY + ballRadius < block_list[i][1]*20 + 10 : 
            ballspdY *= -1
       
        
        #                                                       verticalDROITE                                                                                                       verticalGAUCHE
        
        #                            Y                                                          X                                                         Y                                                   X
        elif block_list[i][1]*20 < ballposY < block_list[i][1]*20 + 10 and ballposX - ballRadius < block_list[i][0]*20 + 20 or block_list[i][1]*20 < ballposY < block_list[i][1]*20 + 10 and ballposX + ballRadius < block_list[i][0]*20 : 
            ballspdX *= -1
            
    
            
     
        
                
    
            
        
        
        


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

        

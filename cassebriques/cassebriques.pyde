

ballspd = 1.6

time = 0
angle = random(PI+0.5 , 2*PI-0.5) #PI/2 * -1 
ballspdX = 0.1 * ballspd
ballspdY = 0.1 * ballspd
ballposX = 250
ballposY = 50
block_numb = 10
block_list = []
brk = True
brickX = 0
brickY = 0
ballRadius = 5
anglemax = PI/ 1.9
ancienmouseX = 0
racHeight = 10
racLenght = 120
ballAngleMax = PI/1.99

def setup ():
    size(500, 500)
    #block_list_gen()
    frameRate(200)
    drawBricks (250 - bW/2, 100 - bH/2, 60, 20)
    drawBricks (20 - bW/2, 100 - bH/2, 60, 20)
    
    
def draw ():
    
    clear()
    drawBricks ()
    times()
    rec ()
    ballPos()
    col ()



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
    
def col () :

#wall
    global ballposX, ballposY, ballspdX, ballspdY, ballRadius, angle, racLenght, racHeight, angle, delta, ballspd, ballAngleMax
    
    #droite
    if ballposX + ballRadius > width  :
        angle = PI - angle
        ballspdX *= random(0.8,1.1)
    
    #gauche
    elif ballposX - ballRadius < 0 :
        angle = PI - angle
        ballspdX *= random(0.8,1.1)
    
    #haut
    elif ballposY - ballRadius < 0 :
        angle = - angle
        ballspdY *= random(0.8,1.1)
    
    #bas
    elif ballposY + ballRadius > height :
        angle = - angle
        ballspdY *= random(0.8,1.1)
        


#rack 
    elif mouseX - racLenght/2 < ballposX < mouseX + racLenght / 2   and     0.85*height < ballposY + ballRadius < 0.85*height + 0.2*racHeight :
        ratio = (ballposX - (mouseX - racLenght/2) - racLenght/2) / racLenght/2
        print ("ratio:", ratio)
        angle =  PI/2 - ratio * ballAngleMax
        print degrees (angle)


def drawBricks (bX, bY, bW, bH) :
    
s
    
    rect (bX, bY, bW, bH)
    
    #brick
    #droite
    '''
    elif bY <= ballposY < bY + bH and ballposX + ballRadius > bX and cos(angle) > 0 and ballposX < bX + bW/10 :
        #angle = PI - angle
        print ("1")
        angle = PI - angle
    
    #gauche
    elif bY <= ballposY < bY + bH and ballposX - ballRadius < bX + bW and cos(angle) < 0 and ballposX > bX + bW - bW/10 :
        #angle = PI - angle
        print ("2")
        angle = PI - angle
    
    #haut
    elif bX <= ballposX < bX + bW and ballposY - ballRadius < bY + bW and sin(angle) > 0 and ballposY > bY + bH - bH/10 :
        #angle = - angle
        print ("3")
        angle = - angle
        
    #bas
    elif bX <= ballposX < bX + bW and ballposY + ballRadius > bY and sin(angle) < 0 and ballposY < bY + bH/10 :
        #angle = - angle
        print ("4")
        angle = - angle
    '''
    
    if bX < ballposX < bX + bW :
        if bY < ballposY+ballRadius < bY+bH and ballspdY < 0  :
            angle = -angle
            ballposY = bY - ballRadius
        elif bY < ballposY < bY + bH and ballspdY > 0 :
            angle = - angle
            ballposY = bY + bH + ballRadius
            
    elif bY < ballposY < bY + bH :
        if bX < ballposX + ballRadius < bX + bW and ballspd > 0 :
            angle = PI - angle
            ballposX = bX - ballRadius
            
        elif bX < ballposX - ballRadius < bX + bW and ballspdX < 0 :
            angle = PI -angle
            ballposX = bX + bW + ballRadius

    '''
    
    if bY <= ballposY < bY + bH :
        print("en x")
        if ballposY > bY :
            print("en haut")
            if bX ballposX 
        elif ballposY < bY + bH :
            print ("en bas")
    elif bX <= ballposX < bX + bW :
        print("en y")
        if ballposX < bX :
            print("a gauche")
        elif ballposX > bX + bY :
            print ("a droite")
    '''
    

   

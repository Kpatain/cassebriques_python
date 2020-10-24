

ballspd = 1.2

time = 0
angle = PI/2 * -1 #random(PI+0.5 , 2*PI-0.5)
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
racLenght = 70
ballAngleMax = PI/1.99
bW = 100
bH = 90
bX = 250 - bW/2
bY = 250 - bH/2

def setup ():
    size(500, 500)
    #block_list_gen()
    frameRate(200)
    
    
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
    if ballposX > width - ballRadius :
        angle = PI - angle
        ballspdX *= random(0.8,1.2)
    
    #gauche
    elif ballposX - ballRadius < 0 :
        angle = PI - angle
        ballspdX *= random(0.8,1.2)
    
    #haut
    elif ballposY - 7 < 0 :
        angle = - angle
        ballspdY *= random(0.8,1.2)


#rack 
    elif mouseX - racLenght/2 < ballposX < mouseX + racLenght / 2   and     0.85*height < ballposY + ballRadius < 0.85*height + 0.2*racHeight :
        ratio = (ballposX - (mouseX - racLenght/2) - racLenght/2) / racLenght/2
        print ("ratio:", ratio)
        angle =  PI/2 - ratio * ballAngleMax
        print degrees (angle)

#brick
     #droite
    elif ballposX > bX - ballRadius and cos(angle) > 0 and ballposX < bX  :
        #angle = PI - angle
        print ("1")
        angle = PI - angle
    
    #gauche
    elif ballposX - ballRadius < bX + bW and cos(angle) < 0 and ballposX > bX + bW :
        #angle = PI - angle
        print ("2")
        angle = PI - angle
    
    #haut
    elif ballposY - ballRadius < bY + bH and sin(angle) > 0 and ballposY > bY + bH :
        #angle = - angle
        print ("3")
        angle = - angle
        
    #bas
    elif ballposY + ballRadius < bY  and sin(angle) < 0 and ballposY < bY :
        #angle = - angle
        print ("3")
        #angle = - angle
        
def drawBricks () :
    global ballposX, ballposY, ballRadius, ballspdX, ballspdY, bY, bX, bH, bW
    
    rect (bX, bY, bW, bH)
    

   

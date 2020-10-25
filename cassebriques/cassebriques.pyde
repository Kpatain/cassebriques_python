

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
bW = 60
bH = 20
bX = 250 - bW/2
bY = 100 - bH/2

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
        
        
def drawBricks () :
    global ballposX, ballposY, ballRadius, ballspdX, ballspdY, bY, bX, bH, bW
    
    rect (bX, bY, bW, bH)
    

   

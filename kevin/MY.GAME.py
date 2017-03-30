from gamelib import * 

game = Game(1550,1000,"DUCK HUNT")

bk = Image("images//donald-duck-trump-scandal-cnn.jpg",game)
bk.resizeTo(game.width, game.height)

game.setBackground(bk)

duck = Animation("images//f88b6d76578597b07204a240d51967cf.gif",3,game,200,300,10)

crosshair = Image("images//cross.png",game)
crosshair.resizeTo(100,100)          

bk.draw()
game.drawText("Press [SPACE] to play",320,400)
game.update(10)


game.wait(K_SPACE)


while not game.over:
    game.processInput()
    game.scrollBackground("left",2)
    duck.draw()
    

    if keys.Pressed[K_SPACE]:
        duck.y -= 4
                                               
    crosshair.moveTo(mouse.x, mouse.y)
        
    duck.y += 2
    game.displayScore(10)
    game.update(30)
    
    if duck.collidedWith(mouse) and mouse.LeftButton:
        game.score+=1#accumulator variable
        x = randint(150,650)
        y = randint(150,450)
        duck.moveTo(x,y)
        duck.speed+=5
        duck.resizeBy(-2)
       
        
        if duck.health<10:
         game.drawText("You lose!",300,0)
         game.over=True


gameover.draw()
game.drawText("Press [SPACE] to Exit  "+ str(game.score),320,400)
game.update(1)
game.wait(K_SPACE)
game.quit()

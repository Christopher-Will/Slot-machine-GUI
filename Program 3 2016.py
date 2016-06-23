#Name:Chris Will
#Email: c.will186@gmai.com
#section: 003
#Date: 4/1/15
#Preconitions: Receives bet from user and whether or not they wish to play again
#Postconidtions: Tells user how much money they won/lost and how much they now have.
# Will kick the user from the game if they don't have enough money, or allow them
# the chance to keep playing if there funds are still sufficient
#Purpose: Simulates a slot machine by having user input their wager and then 
# randomly selects three symbols which determine whether the user gets money or
# looses money.

from graphics import*
from random import*
from time import*

#1.def get_name(win):
'''Parameters: The graphics window
Purpose: Asks user for their name and greet them with some message
Postconiditons:Returns the vale for the users name'''
#.Design
def get_name(win):
    #. Ask the user for their name
    prompt=Text(Point(210,250),"What's your name?")
    prompt.draw(win)
    name=Entry(Point(330,250),10)
    name.draw(win)
    
    #. Get the users name and wait for a mouse click to clean up the graphics window
    #  and save their name in a variable
    win.getMouse()
    user_name=name.getText()
    prompt.undraw()
    name.undraw()
    
    #. Return their name
    return user_name

#2.def get_bet(pot,win):
'''Parameters: The current value of the pot and the graphics window
Purpose: Ask the user how much money they wish to bet and use a while loop
to determine if the amount entered is acceptable
Postconditions: Returns the value of the users bet'''
#.Design
def get_bet(pot,win):    
    #2. Ask the user how much they wish to bet
    bet_prompt=Text(Point(200,250),"How much to bet? (up to "+str(pot)+") ?")
    bet_prompt.draw(win)
    bet_entry=Entry(Point(350,250),4)
    bet_entry.draw(win)
    win.getMouse()
    user_bet = int(bet_entry.getText())
    
    #3. Use a while loop to tell the user that there bet was too high if the bet
    #   was > pot and ask for another bet
    while user_bet > pot:
        high_bet=Text(Point(300,400),"That bet is too high! Enter a lower bet ")
        high_bet.draw(win)
        win.getMouse()
        high_bet.undraw()
        user_bet = int(bet_entry.getText())
    
    #4. Use a while loop to tell user that there bet was too low if the bet was
    #   <= pot and ask for another bet
    while user_bet <= 0:
        low_bet=Text(Point(300,400),"That bet is too low! Enter a higher bet ")
        low_bet.draw(win)
        win.getMouse()
        low_bet.undraw()
        user_bet = int(bet_entry.getText())
    
    #5. Undraw the image that shows the current value of the pot, and the text
    #   and entry boxes which asked the user for their bet
    #pot_image.undraw()
    bet_prompt.undraw()
    bet_entry.undraw()
    
    #6. Return the value of the users bet
    return user_bet

#3. def translate(symbol):
'''Parameters: The int value associated with which of the nine randomized symbols
was selected. 
Purpose: Takes the int value with which the randomly selected symbol is associated
with and translates this into a string with the name of that symbol
Postconiditons: Returns the value of the string for which symbol was selected'''
def translate(symbol):
    #1. Use if/elif statements to determine what string the variable symbol should
    #   be associated with
    if symbol==1:
        result= "bell.gif"
    elif symbol==2:
        result= "apple.gif"
    elif symbol==3:
        result= "banana.gif"
    elif symbol==4:
        result= "orange.gif"
    elif symbol==5:
        result= "cherry.gif"
    elif symbol==6:
        result= "grapes.gif"
    elif symbol==7:
        result= "jackpot.gif"
    elif symbol==8:
        result= "lemon.gif"
    else:
        result= "melon.gif"
    
    #2. Return the value of the symbol that was randomly selected
    return result

#4. def find_winnings(result1,result2,result3,user_bet,win):
'''Parameters: The three symbols which the user got, the users bet, and the 
graphics window.
Purpose: Calculate how much money the user won or lost
Postconditions: Returns the value of how much the user won/lost.'''
#.Design
def find_winnings(result1,result2,result3,user_bet,win):
    #. Use if/elif statements to determine whether or not the user won and what
    #   the updated value of the pot should be    
    if result1==result2==result3 and result1==7:
        won_jackpot=Text(Point(250,450),"You won 3 JACKPOTS!")
        win_jackpot.draw(win)  
        result=(user_bet*20)
        jackpot_prompt=Text(Point(250,475),"You won $" + str(20*user_bet))
        jackpot_prompt.draw(win) 
        win.getMouse()
        jackpot_prompt.undraw()
        won_jackpot.undraw()
            
    elif result1==result2==result3 and result1==1:
        won_bells=Text(Point(250,450),"You won 3 BELLS!")
        won_bells.draw(win)
        result=(user_bet*10) 
        bells_prompt=Text(Point(250,475),"You won $"+str(10*user_bet))
        bells_prompt.draw(win)
        win.getMouse()
        bells_prompt.undraw()
        won_bells.undraw()
            
    elif result1==result2==result3:
        won_three=Text(Point(250,450),"You won 3 of a kind!")
        won_three.draw(win)
        result=(user_bet*3)
        three_prompt=Text(Point(250,475),"You won $"+str(3*user_bet))
        three_prompt.draw(win)
        win.getMouse()
        three_prompt.undraw()
        won_three.undraw()
    
    if (result1==result2) or (result1==result3) or (result2==result3):
        won_two=Text(Point(250,450),"You won 2 of a kind!")
        won_two.draw(win)
        result=(user_bet*2)
        two_prompt=Text(Point(250,475),"You won $"+str(2*user_bet))
        two_prompt.draw(win)
        win.getMouse()
        two_prompt.undraw()
        won_two.undraw()
            
    else:
        lost=Text(Point(250,450),"You lost your bet!")
        lost.draw(win)       
        result=user_bet
        lost_prompt=Text(Point(250,475),"$"+str(user_bet))
        lost_prompt.draw(win)
        win.getMouse()
        lost_prompt.undraw()
        lost.undraw()     
    #. Return the value associated with how much money the user won/lost
    return result

#5.def play_again(win)
'''Parameters:The graphics window
Purpose:Lets user choose whether or not they wish to keep playing
Postconditions: Returns the value that dictates whether the user chose to keep
playing or not.'''
def play_again(win):
    #. Ask the user if they wish to play again
    keep_playing=Text(Point(250,250),"Do you want to play again?")
    keep_playing.draw(win)    
    
    #. Draw a blue square with "YES" in it which will be the option to let the user
    #  keep playing
    yes=Rectangle(Point(50,60),Point(100,110))
    yes.setFill('blue')
    yes.draw(win)
    yes_text=Text(Point(75,85),"YES")
    yes_text.setSize(15)
    yes_text.setFill('white')
    yes_text.draw(win) 
    
    #. Draw a red square with "NO" in it which will the option to let the user 
    #  exit the game
    no=Rectangle(Point(300,60),Point(350,110))
    no.setFill('red')
    no.draw(win)
    no_text=Text(Point(325,85),"NO")
    no_text.setSize(15)
    no_text.setFill('black')
    no_text.draw(win)
    
    #. Wait for the user to click and get the coordinates of this click.
    click=win.getMouse()
    x_point=click.getX()
    y_point=click.getY()
    
    #. Use sentinel logic and while loops to have the user keep clicking in the 
    #  graphics window if their click was not in either of the 2 squares
    while not(x_point >=50 and x_point <= 100) and not(y_point >= 60 and y_point <= 110):
        win.getMouse()
        click=win.getMouse()
        x_point=click.getX()
        y_point=click.getY()       
 
    while not(x_point >= 300 and x_point <= 350) and not(y_point >=60 and y_point <= 110):
        win.getMouse()
        click=win.getMouse()
        x_point=click.getX()
        y_point=click.getY()  
    
    #. Use if statements to run the user through the game again or exit them from
    #  the game
    if (x_point >=50 and x_point <= 100) and (y_point >= 60 and y_point <= 110):
        done=False
    if (x_point >= 300 and x_point <= 350) and (y_point >= 60 and y_point <= 110):
        done=True 
    
    #. Clean up the graphics window    
    yes.undraw()
    no.undraw()
    yes_text.undraw()
    no_text.undraw()
    keep_playing.undraw()
    
    #. Return the value associated with whether the user wished to keep playing or not.
    return done
        
def main():
    #. Draw the graphics window
    win=GraphWin("Slot Machine!!!",500,600)
    
    #. Draw some welcoming prompt
    slot_machine=Text(Point(250,150),"Slot Machine")
    slot_machine.setSize(30)
    slot_machine.draw(win)
    
    #3. Run the get_name function to get the users name and save this in a variable
    name=get_name(win)
    
    #. Clean up the graphics window
    slot_machine.undraw() 
    
    #. Set the initial pot to 200 and display this
    pot=200
    pot_image=Text(Point(50,50),"Pot is $"+str(pot))
    pot_image.draw(win)
    
    #. Set the while loop flag to false
    done=False
    #. While the user has money and the user is not done playing
    while pot > 0 and not done:
        #. Call the get_bet function to get the users bet and save this in a variable
        final_bet=get_bet(pot,win)
        
        #. Get 3 random numbers in [1,10) 
        symbolA=randrange(1,10)
        symbolB=randrange(1,10)
        symbolC=randrange(1,10) 
   
        #.translate them into the names of 3 gif files
        result1=translate(symbolA)
        result2=translate(symbolB)
        result3=translate(symbolC) 
        
        #. display three gifs

        for i in range(20):
            symbolX=randrange(1,10)
            resultX=translate(symbolX)
            spinX=Image(Point(90,250), resultX)
            spinX.draw(win)
            sleep(0.03)
            spinX.undraw()
        spin1=Image(Point(90,250), result1)
        spin1.draw(win)  
        
        for i in range(20):
            symbolY=randrange(1,10)
            resultY=translate(symbolY)
            spinY=Image(Point(250,250), resultY)
            spinY.draw(win)
            sleep(0.03)
            spinY.undraw()
        spin2=Image(Point(250,250), result2)
        spin2.draw(win)
        
        for i in range(20):
            symbolZ=randrange(1,10)
            resultZ=translate(symbolZ)
            spinZ=Image(Point(410,250), resultZ)
            spinZ.draw(win)
            sleep(0.03)
            spinZ.undraw()        
        spin3=Image(Point(410,250), result3)
        spin3.draw(win)     
      #.Call the find_winnings function to find how much the user won/lost and
      # save this value in a variable
        result=find_winnings(result1,result2,result3,final_bet,win)
        
        #. Add the users winnings to the pot
        if result > final_bet:
            pot=pot+result
        else:
            pot=pot - result
            
        #. Display the updated value of the pot    
        pot_image.undraw()
        pot_image=Text(Point(50,50),"Pot is $"+str(pot))
        pot_image.draw(win)
        
        #. Undraw the 3 gifs
        spin1.undraw()
        spin2.undraw()
        spin3.undraw()
        
        #.if the pot is > 0
        if pot > 0:
        
       #. ask the user if they want to play again
            more_playing=play_again(win)
       #. if they say no, set play flag to True
        if more_playing:
            done=True
        #. Otherwise the user has no more money and change the value of the flag to 
        #  False
        else:
            done=False
    #. Tell the user how much money they left with or tell them that they are
    #  bankrupt and are kicked from the game
    if pot <= 0:
        bankrupt=Text(Point(250,250),"Goodbye! You are bankrupt!")
    
    else:
        game_over=Text(Point(250,250),name+", you left with $"+str(pot))
        game_over.draw(win)
        
   #. Wait for click
    win.getMouse()
    
   #.close window
    win.close()
main()

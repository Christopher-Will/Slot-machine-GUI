# Name: Christopher Will
# Email: c.will186@gmail.com 
# Section 003
# Purpose: To simulate a game of golf using the users angle, velocity, and desired
# number of swings to tell them if they hit a ball located in a random place.
# Date: 3/11/15
# Preconditions: User will input how many rounds they wish to play, desired difficulty,
# and the angle and velocity that the ball was hit with
# Postconditions: Will output the holes location, the trajectory of the users swings,
# whether they made it to the hole, and the percent of swings that made it to the
# hole.

from graphics import*
#. Need to import Graphwin, Entry, Text, Circle, Point, draw, undraw, setSize, 
#. setFill, getMouse, getText.
from math import pi, sin
#. Need to import pi and sin
from random import randrange
#. Need to import randrange
def main():
    
    #1. Draw graphics window and greet the user with "Golf!" in the center
    #  of this window. Win is is the graphics window and message is the "Golf!"
    #  message which will greet the user.
    
    win = GraphWin("Golf!",500,500)
    message = Text(Point(250,250), "Golf!")
    message.setSize(36)
    message.setFill('black')
    message.draw(win)
    
    #2. Create entry box where user can enter number of rounds they wish to play
    #  and ask them for this with a text next to the entry box. swings_entry is 
    #  where the user enters desired number of swings and swings_text asks the
    #  user for this number.
    
    swings_entry = Entry(Point(200,190),4)
    swings_entry.setFill('white')
    swings_entry.draw(win)
    swings_text = Text(Point(133,190), "# of Swings?")
    swings_text.draw(win)
     
    #3. Create an entry box where user can input the desired difficulty and use
    #  text to ask them for this. difficulty_entry is where the user can input
    #  their desired difficulty and difficulty_text asks the user for this number.
    
    difficulty_entry = Entry(Point(350,190),4)
    difficulty_entry.setFill('white')
    difficulty_entry.draw(win)    
    difficulty_text = Text(Point(295,190),"Difficulty?")
    difficulty_text.draw(win)
    
    #4. Get the users entry for difficulty and number of rounds to play and save 
    #  these in variables. swings typecasts the number of rounds which the user
    #  wished to play into an int. difficulty does the same, but for the difficulty
    #  that was entered.
    
    win.getMouse()
    swings = int(swings_entry.getText())    
    difficulty = int(difficulty_entry.getText())
    
    #5. Display the rounds and difficulty the user input in the top left corner
    #  of the window. swings is typecasted into an int so that it can be displayed
    #  to the user. swings_loop saves the number of swings the user wants to play
    #  as an int so it can be used in the for loop. difficulty and difficulty_loop
    #  do the same, but for the difficulty that was entered.
    
    swings = Text(Point(50,50),"Rounds "+ str(swings))
    swings.draw(win)
    swings_loop = int(swings_entry.getText())
    difficulty = Text(Point(50,75), "Difficulty "+str(difficulty))
    difficulty.draw(win)
    difficulty_loop = int(difficulty_entry.getText())
    
    #6. Undraw the "Golf!" message and the entry/text boxes which asked the
    #  user for rounds and difficulty
    
    difficulty_entry.undraw()
    difficulty_text.undraw()
    swings_entry.undraw()
    swings_text.undraw()
    message.undraw()      
    
    #7. Ask user for angle and velocity of their swing using text and entry boxes
    #  angle_entry and angle_text are used to get the angle from the user and
    #  velocity_entry and velocity_text are used to get the velocity.
    
    angle_entry = Entry(Point(200,190), 4)
    angle_entry.setFill('white')
    angle_entry.draw(win)
    angle_text = Text(Point(150,190), "Angle?")
    angle_text.draw(win)
    velocity_entry = Entry(Point(315,190), 4)
    velocity_entry.setFill('white')
    velocity_entry.draw(win)
    velocity_text = Text(Point(260,190), "Velocity?")
    velocity_text.draw(win)     
    
    #8. Display a message asking the user to enter their angle and velocity. 
    #  message_loop asks the user for their angle and velocity.
    
    message_loop = Text(Point(250,220), "Enter angle and velocity")
    message_loop.setSize(20)
    message_loop.setFill('black')
    message_loop.draw(win)      
    
    #9. Draw the golfer image in the lower left corner of the window. golfer
    #  is used to draw the gif of the golfer in the bottom of the window
    
    golfer = Image(Point(30,470), "golfer.gif")
    golfer.draw(win)

    #10. Initiliaze the number of holes made counter before the loop begins.
    #  holes_made is an accumulator which will be used in the loop to keep track
    #  of how many holes the user has made
    
    holes_made = 0

    #11. Use a for loop to let user play however many rounds of golf they entered
    for i in range(swings_loop):
        
        #12. Use a RNG to determine the holes location and display this location
        #  to the user. hole saves the random location of the hole and hole_window
        #  displays this location to the user
        
        hole = randrange(250,500)
        hole_window = Text(Point(260,250), "Hole location "+ str(hole))
        hole_window.draw(win)  
            
        #13. Draw the starting point for the golf ball in the graphics window and
        #  the location of the hole with the flag gif. ball_start is the initial
        #  location of the ball and flag is location of the hole, shown with the 
        #  flag gif.
        
        ball_start = Circle(Point(20,480), 10)
        ball_start.setFill('black')
        ball_start.draw(win)  
        flag = Image(Point(hole,470), "hole.gif")
        flag.draw(win)         
       
        #14. Get the angle and velocity from the user and convert the angle into
        #  radians. angle_degress gets the angle in degrees from the user and angle
        #  converts this into radians. velcoity saves the value of velocity as an int.
        
        win.getMouse()
        angle_degrees = int(angle_entry.getText())
        angle = angle_degrees * (pi/180)
        velocity = int(velocity_entry.getText())
        
        #15. Use kinematic equations to find distance and max height the ball 
        #  attains. Display this distance to the graphics window. distance is
        #  the max distance the ball travels and distance_text is used to display
        #  this value to the user. height saves the value for the max height 
        #  achieved by the ball.
        
        distance = round((((velocity**2) * sin(2 * angle))/9.8),1)
        distance_text = Text(Point(260,300), "Distance " +str(distance) +" meters")
        distance_text.draw(win)
        height = ((velocity**2) * (sin(angle)**2))/9.81
        
        #16. Draw the ball at max height and at max distance. ball_height draws the
        #  golf ball at max height and ball_distance draw the ball at max distance.
        
        ball_height = Circle(Point(distance/2,(480-height)), 10)
        ball_height.setFill('black')
        ball_height.draw(win)
        ball_distance = Circle(Point(distance,480), 10)
        ball_distance.setFill('black')
        ball_distance.draw(win)    
   
        #17. Use an if loop to display a unqiue message if the user just finished
        #  their last hole. end_game will prompt the user to end the loop if they
        #  finished their last round
        
        if i+1==swings_loop:
            end_game = Text(Point(270,270), "Click to end game ")
            end_game.setSize(15)
            end_game.setFill('green')
            end_game.draw(win)
            
        #18. Use an if/else loop to congratulate the user and increase the holes made 
        #  counter by 1 if they made the hole. Else tell them they missed and 
        #  fail to increase the holes made counter. made_hole displays a message
        #  if the user made it to the hole. missed_hole displays a message if the 
        #  user did not make it to the hole
        
        if (distance >=(hole-difficulty_loop)) and (distance<=(hole+difficulty_loop)):
            made_hole = Text(Point(260,340), "You made it! ")
            made_hole.setSize(20)
            made_hole.setFill('blue')
            made_hole.draw(win)
            holes_made = holes_made+1
            prompt=Text(Point(260,380), "Click for next round ")
            
            #19. Prompt the user to click for the next round if they are not on
            #  the final hole
            
            if i+1!=swings_loop:
                prompt.draw(win)             
            win.getMouse()
            made_hole.undraw()    
        else:
            missed_hole = Text(Point(260,340), "You missed it! ")
            missed_hole.setSize(20)
            missed_hole.setFill('red')
            missed_hole.draw(win)
            prompt=Text(Point(260,380), "Click for next round ")
            
            #20. Prompt the user to click for the next round if they are not on the
            #  final hole.
            
            if i+1!=swings_loop:
                prompt.draw(win)              
            win.getMouse()
            missed_hole.undraw()
                  
        #21. Undraw the graphics for the balls distance and height, the text which
        #  displays this distance, the holes location, and the "click for next
        #  round" messgae upon the users click
        
        flag.undraw()
        hole_window.undraw()
        distance_text.undraw()
        ball_height.undraw()
        ball_distance.undraw()
        prompt.undraw()
        
    #22. Display the % of holes that the user made to the graphics window and undraw
    #  the message prompting the user to click to end the game. Use anif/else
    #  statement to have a different message if the user didn't make any holes.
    #  percent_made shows how many holes the user made if and failure gives a
    #  unique message if they made no holes. total_holes is used to calculate how 
    #  many holes the user made
    
    ball_start.undraw()
    end_game.undraw()
    total_holes = round((holes_made/swings_loop) * 100,2)
    if total_holes > 0:
        percent_made = Text(Point(250,250), "You got "+ str(total_holes) +"%")
        percent_made.setSize(20)
        percent_made.setFill('blue')
        percent_made.draw(win)
    else:
        failure = Text(Point(250,250), "You got none! ")
        failure.setSize(20)
        failure.setFill('red')
        failure.draw(win)
        
    #23. Have user click to close the program and undraw the text asking the user
    #  for their angle and velocity. end_program prompts the user to end the program
    #  when the game is over.
    
    end_program = Text(Point(250,300), "Click to close program")
    end_program.setSize(25)
    end_program.setFill('black')
    end_program.draw(win)
    swings.undraw()
    difficulty.undraw()
    message_loop.undraw()
    win.getMouse()
    win.close()
main()
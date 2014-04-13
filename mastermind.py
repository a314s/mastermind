#import randint to use later
import random

colors = ['B','O','P','R','W','Y']

looping_needed = True #enable looping
while looping_needed:

    #ask user to pick secret code
    secret = raw_input("Are you ready to play?? Create a four color secret code with any combination of six colors. Your options are R, O, Y, P, W, or B. Please select your combination now: ")
    secret = secret.upper()
    
    #validate length    
    if len(secret) != 4:
        print "Oops! Try again."
        print
        
    #validate correct letters
    else:
        x = 0
        for letter in secret:
            if letter not in colors:
                x +=1
        if x > 0:
            print "Oops! Try again."
            print
        else:
            looping_needed = False

#create list with all of the possible combinations; leave empty for now
options_list = []

#add all possible combinations to options_list
for spotone in colors:
    for spottwo in colors:
        for spotthree in colors:
            for spotfour in colors:
                new_option = spotone + spottwo + spotthree + spotfour

                options_list.append(new_option)
                
guess = 'RYPO' #always start with this guess (could be other letters)
guess_number = 1 #counter keeps track of number of guesses made

looping_needed = True #enable looping
while looping_needed:

    #print the guess and the number of tries so far
    print
    print 'Computer Guess #' + str(guess_number) + ': ' + str(guess)

    black = 0 #number of black pegs (exact matches)
    white = 0 #number of white pegs (color matches)
    checksecret = [secret[0], secret[1], secret[2], secret[3]]
    checkguess = [guess[0], guess[1], guess[2], guess[3]]
    
    #if the first character in the secret code matches the first character in the guess
    #then give it one black peg. Then create temporary guess and secret words to check
    #whether the guess has the right amount of colors for white pegs.
    
    for i in [0,1,2,3]:
        if secret[i] == guess[i]:
            black += 1
            checkguess[i] = 'X'
            checksecret[i]= 'X'

    #Loop checks to see how many of each color are in temporary guess and secret codes.
    #If they have the right number of colors, add white peg   
    for color in colors:
        i = checksecret.count(color)
        j = checkguess.count(color)
        if i == 0 or j == 0:
            white = white
        elif i == j:
            white += i
        elif i > j:
            white += j
        else:
            white += i
            

    #print number of black and white pegs received
    print 'Computer receives ' + str(black) + ' black peg(s) and ' + str(white) + ' white peg(s).'
    
    #if 4 black pegs are received, game over! 
    if black == 4:
        print "Computer wins in " + str(guess_number) + " tries!"
        looping_needed = False
    else:
        options_list_index = 0 #counter for index in options_list

        #this loop changes items in options_list to 'invalid' if they don't equal
        #the same number of black pegs and white pegs. Uses the same logic as above.
        for item in options_list: 
           
            blackcounter = 0
            whitecounter = 0
            checkitem = [item[0], item[1], item[2], item[3]]
            checkguess = [guess[0], guess[1], guess[2], guess[3]]
            
            for i in [0,1,2,3]:
                if item[i] == guess[i]:
                    blackcounter += 1
                    checkitem[i] = 'X'
                    checkguess[i] = 'X'

            for color in colors:
                i = checkguess.count(color)
                j = checkitem.count(color)
                if i == 0 or j == 0:
                    whitecounter = whitecounter
                elif i == j:
                    whitecounter += i
                elif i > j:
                    whitecounter += j
                else:
                    whitecounter += i      
                
            if (blackcounter != black) or (whitecounter != white):
                options_list[options_list_index] = 'Invalid'
                
            options_list_index += 1 #loop through index
        
        length = len(options_list) #number of items in options_list
        options_list_index = 0 #set counter for index in options_list back to zero
        
        #loop through items in options_list and delete them if they're 'invalid'
        while options_list_index < length:
            if options_list[options_list_index] == 'Invalid':
                del options_list[options_list_index]
                options_list_index += -1
                length = len(options_list)
            options_list_index += 1
        
        number_of_options_left = len(options_list)
        nextguess = random.randint(0,number_of_options_left-1) #randomly select an index number
        guess = options_list[nextguess] #next guess equals the item in that index spot
        guess_number += 1 #increment guess number

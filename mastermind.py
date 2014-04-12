#import randint to use later
import random

looping_needed = True #enable looping
while looping_needed:

    #ask user to pick secret code
    secret = raw_input("Are you ready to play?? Create a four color secret code with any combination of six colors. Your options are R, O, Y, P, W, or B. Please select your combination now: ")
    secret = secret.upper()
    
    #validate length    
    if len(secret) != 4:
        print "Oops! Try again."
        
    #validate correct letters
    else:
        x = 0
        for letter in secret:
            if letter not in ['R','O','Y','W','P','B']:
                x +=1
        if x > 0:
            print "Oops! Try again."
            print
        else:
            looping_needed = False

#create list with all of the possible combinations; leave empty for now
options_list = []

#create list with color possibilities to use in the following loop
spot_one = {1:'B',2:'O',3:'P',4:'R',5:'W',6:'Y'}
spot_two = {1:'B',2:'O',3:'P',4:'R',5:'W',6:'Y'}
spot_three = {1:'B',2:'O',3:'P',4:'R',5:'W',6:'Y'}
spot_four = {1:'B',2:'O',3:'P',4:'R',5:'W',6:'Y'}

#add all possible combinations to options_list
for spot_one_color in spot_one:
    for spot_two_color in spot_two:
        for spot_three_color in spot_three:
            for spot_four_color in spot_four:
                new_option = spot_one.get(spot_one_color) + spot_two.get(spot_two_color) + spot_three.get(spot_three_color) + spot_four.get(spot_four_color)

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
    if secret[0] == guess[0]:
        black += 1
        checkguess[0] = 'X'
        checksecret[0]= 'X'
        
    if secret[1] == guess[1]:
        black += 1
        checkguess[1] = 'X'
        checksecret[1]= 'X'
        
    if secret[2] == guess[2]:
        black += 1
        checkguess[2] = 'X'
        checksecret[2]= 'X'
        
    if secret[3] == guess[3]:
        black += 1
        checkguess[3] = 'X'
        checksecret[3]= 'X'

    #Loop checks to see how many of each color are in temporary guess and secret codes.
    #If they have the right number of colors, add white peg   
    for letter in ['R','O','Y','W','P','B']:
        i = checksecret.count(letter)
        j = checkguess.count(letter)
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
    
    #print 4 black pegs are received, game over! 
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
            
            if item[0] == guess[0]:
                blackcounter += 1
                checkitem[0] = 'X'
                checkguess[0] = 'X'
                
            if item[1] == guess[1]:
                blackcounter += 1
                checkitem[1] = 'X'
                checkguess[1] = 'X'
                
            if item[2] == guess[2]:
                blackcounter += 1
                checkitem[2] = 'X'
                checkguess[2] = 'X'
                
            if item[3] == guess[3]:
                blackcounter += 1
                checkitem[3] = 'X'
                checkguess[3] = 'X'

            for letter in ['R','O','Y','W','P','B']:
                i = checkguess.count(letter)
                j = checkitem.count(letter)
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

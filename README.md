Mastermind.py
=========

## Table of Contents
 
* [Overview](#Overview)
* [Instructions](#Instructions)
* [Rules](#Rules)
* [About](#About)
 
## <a name="Overview"></a>Overview
Mastermind is a two-player code-breaking game where one player makes a secret code of four marbles from a set of six different colored marbles and another player tries to guess the code as quickly as possible. (Read more about the game [here][1].) 

I created this program to mimic the game. My program allows the user to create a secret Mastermind code and then the computer guesses the correct code within 10 turns. 

## <a name="Instructions"></a>Instructions

Fork this repository and clone your repo to your computer.

```$ git clone https://github.com/YOUR_GIT_USERNAME_GOES_HERE/mastermind.git```

You can only play this game in your python console. So now, go ahead and play! You should be prompted to select four colors from a set of six possibilities (R, Y, O, P, W, or B) after your enter this in your command line.

```$ c:\> python mastermind.py```

*Make sure you are in the correct folder before calling 'python mastermind.py'*
 
## <a name="Rules"></a>Rules

  - You select any combination of 4 of the 6 possible colors (e.g., 'RRRR', POOW', 'BWYB', or 'BWRP') to create a secret code
 
  - Player 2 (or the computer) will get one black peg for every correct color in a correct spot and one white peg for every correct color in an incorrect spot

  - Player 2 must guess the secret guess (or receive 4 black pegs) in less than 10 tries

## <a name="About"></a>About
Created by [@getLaura][2] as an exercise for [8th Light][3]'s Apprentice program. 


[1]:http://en.wikipedia.org/wiki/Mastermind_(board_game)
[2]:http://twitter.com/getlaura
[3]:http://8thlight.com

    
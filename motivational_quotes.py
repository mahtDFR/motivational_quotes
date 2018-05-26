#  Motivational Quotes
#  
#  Copyright 2018 Matt <Matt Jani>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

def mattQuote(): 
    from random import choice
    quotes = "From the ashes of disaster grow the roses of success.",\
    "Don't stop until you're proud.",\
    "Don't believe everything you think.",\
    "The less you give a fuck, the happier you'll be.",\
    "Don't let yesterday take up too much of today.",\
    "Do not feel lonely, the universe is inside you.",\
    "Be regular and orderly in your life, so that you may be violent and original in your work.",\
    "We do not see things the way they are. We see things the way we are.",\
    "You are an aperture through which the universe is looking at and exploring itself.",\
    "Be the energy you want to attract.",\
    "Great things never came from comfort zones.",\
    "Worry is a misue of your imagination.",\
    "Never stop being a good person because of bad people.",\
    "Comfort is the enemy of progress.",\
    "You don't get a refund on wasted time.",\
    "If you put your mind to it, you can accomplish anything.",\
    "If you have good thoughts, they will shine out of your face like sun beams and you will always be happy.",\
    "I must not fear. Fear is the mind-killer. Fear is the little-death that brings total obliteration. I will face my fear. I will permit it to pass over me and through me. And when it has gone past I will turn the inner eye to see its path. Where the fear has gone there will be nothing. Only I will remain.",\
    "Prove them wrong.",\
       
    print(choice(quotes))
    import time
    print(" ")
    userInput = input("Enter 'R' to restart or 'X' to exit").capitalize()
    print(" ")
    
    if userInput == "R":
        mattQuote()

    elif userInput == "X":
        print('Goodbye.')
        time.sleep(1)
        import sys
        sys.exit() # exits the program        
mattQuote()

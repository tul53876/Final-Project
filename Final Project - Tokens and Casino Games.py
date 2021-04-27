import sys
import random

tok = 50

#Roulette---------------------------------------------------------------------
"""
red_black_green = list(range(0, 37))
red = list(range(1, 36, 2))
black = list(range(2, 37, 2))
green = [0]

print("Betting on red earns triple the bet amount, and black doubles it. Betting on green earns seven times the bet amount.")

while True:
    select = input('If you would like to stop type 0, to bet red type 1, to bet black type 2, otherwise type 3 for green: ')

    if select == '1':
        amount = int(input("How much would you like to bet? "))

        if amount <= 0 or amount > tok:
            amount = int(input("How much would you like to bet? "))

        else:
            tok -= amount

            res = random.choice(red_black)

            print('The result is ', res)

            if res in red:
                print("W, You have won the game")
                tok += amount * 3
                print("Your new overall token total: " + str(tok))

            elif res in black:
                print("L, You have lost the game") 
                print("Your new overall token total: " + str(tok))
            
            elif res in green:
                print("L, You have lost the game")
                print("Your new overall token total: " + str(tok))
                
    if select == '2':
        amount = int(input("How much would you like to bet? "))

        while amount <= 0 or amount > tok:
            amount = int(input("How much would you like to bet? "))

        else:
            tok -= amount

            res = random.choice(red_black)

            print('The result is ', res)

            if res in black:
                print("W, You have won the game")
                tok += amount * 2
                print("Your new overall token total: " + str(tok))

            elif res in red:
                print("L, You have lost the game")
                print("Your new overall token total: " + str(tok))
                
            elif res in green:
                print("L, You have lost the game")
                print("Your new overall token total: " + str(tok))
                
                
    if select == '3':
        amount = int(input("How much would you like to bet? "))

        while amount <= 0 or amount > tok:
            amount = int(input("How much would you like to bet? "))

        else:
            tok -= amount

            res = 0

            print('The result is ', res)

            if res in black:
                print("L, You have lost the game")
                print("Your new overall token total: " + str(tok))

            elif res in red:
                print("L, You have lost the game")
                print("Your new overall token total: " + str(tok))
                
            elif res in green:
                print("W, You have won the game")
                tok += amount * 7
                print("Your new overall token total: " + str(tok))
                
    if select == '0':
        sys.exit()
"""


#Slot Machine-----------------------------------------------------------------

"""
def gameOutc():
    x = 0
    poss = ["duran", "cherry", "apple","pear", "crown"]
    
    firstReel = poss[random.randint(0, 4)]
    secReel = poss[random.randint(0, 4)]
    thirdReel = poss[random.randint(0, 4)]

    print("{} {} {}".format(firstReel, secReel, thirdReel))
    if firstReel == secReel and firstReel == thirdReel:
        if firstReel == "Crown":
            x = 0
        else:
            x = 1
            
    elif firstReel == secReel or firstReel == thirdReel or secReel == thirdReel:
        x = 2
    
    else:
        x = 3

    return x
    
print("Two of the same fruit earns 10 tokens")
print("Three of the same fruit earns double tokens")
print("Three of Crown earns quadruple tokens")

def play():
    global tok

    choice = "y"

    while choice == "y":
        choice = input("Do you want to play? (y or n): ").lower()
        
        if choice == "n":
            sys.exit()
        
        amount = int(input("How much would you like to bet? "))

        while amount <= 0 or amount > tok:
            amount = int(input("How much would you like to bet? "))

        else:
            tok -= amount
            
        gameOutc()
        
        if gameOutc() == 0:
            x = amount * 4
        
        elif gameOutc() == 1:
            x = amount * 2
        
        elif gameOutc() == 2:
            x = amount + 10
        
        elif gameOutc() == 3:
            x = 0
        
        print("Your earning is {} tokens".format(x))
        tok += x
        print("Your new overall token total: " + str(tok))

play()
"""
    


#Craps------------------------------------------------------------------------
"""       
amount = int(input("How much would you like to bet? "))

while amount <= 0 or amount > tok:
    amount = int(input("How much would you like to bet? "))

else:
    tok -= amount

print("Winning the game earns you double your bet.")

def rollNum():
    input("Press Enter to play/continue Craps")
      
    firstRoll = random.randrange(1, 7)
    secRoll = random.randrange(1, 7)
    r = firstRoll + secRoll 
    print("Your roll total is " + str(r))
    return firstRoll + secRoll  
  
rollTotal = rollNum()

  
if rollTotal in (7, 11):
    outc = 100
  
elif rollTotal in (2, 3, 12):
    print("L, You have lost the game")
    print("Your new overall token total: " + str(tok))
         
else:  
    pTemp = rollTotal
    print("Your point is ", pTemp)
    outc = 200
  
  
while outc == 200:
    rollTotal = rollNum()
      
    if rollTotal == pTemp:
        outc = 100
          
    elif rollTotal == 7:
        print("L, You have lost the game")
        print("Your new overall token total: " + str(tok))
  
if outc == 100:
    print("W, You have won the game")
    tok += amount * 2
    print("Your new overall token total: " + str(tok))
      
else:
    print("L, You have lost the game")
    print("Your new overall token total: " + str(tok))
"""
#Rock Paper Scissors

#Import Random Module                                             
import random
#Random Integer/Variable for CPU
CPU = random.randint(1,3)

 
#Print Title and Input
print("=============\nRock, Paper, Scissors\n=============")
print("1)Rock\n2)Paper\n3)Scissors")

#player variable
player = int(input("\nPick a number: "))   

#Validate Player Input
if player < 1 or player > 3:
    print("(╯°□°）╯︵ ┻━┻ SELECT A VALID NUMBER")
else:
    print()
    
    #Player Control Flow Statements                                                     
    if player == 1:
        print("You Chose: Rock")
    elif player ==2:
        print("You Chose: Paper")
    elif player ==3:
        print("You Chose: Scissors")
    
    #CPU Control Flow Statements
    if CPU == 1:
        print("CPU Chose: Rock")
    elif CPU == 2:
        print("CPU Chose: Paper")
    elif CPU == 3:
        print("CPU Chose: Scissors")
    else:
        print("Insert Huh cat meme here")                           

    #The Game Begins
    if player == CPU:
        print("It's a Tie!")
    elif player ==1 and CPU ==3 or player ==3 and CPU ==2 or player ==2 and CPU ==1: #This is based of the rules from the Checkpoint Project Instructions
        print("You Win!")
    else:
        print("CPU Wins!")

print(" Welcome To My Quiz Game \n Interesting Game to Play")
Player = input(" Do you want to play the game? yes:no \n" )
if Player.lower() != 'yes':
    print("Good Bye")
    quit()  

name_player = input("Enter Your player Name : ")

print("Let's Start the Game :) ",name_player)

score = 0

answer = input(' What is the abbreviation for Sword art online? \n ')
if answer.lower() == 'sao':
    print("Correct")
    score += 1
else:
    print('Wrong')
 
answer = input(' What is the abbreviation for alfheim online? \n ')
if answer.lower() == 'alo':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' What is the abbreviation for gun gale online? \n ')
if answer.lower() == 'ggo':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' What is the name of the guild that Yuuki is the leader? \n ')
if answer.lower() == 'sleeping knight':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input(' What weapon does Sinon use in GGO? \n ')
if answer.lower() == 'sniper rifle':
    print("Correct")
    score += 1
else:
    print('Wrong')
    
print("You got the " + str(score)+ " correct answers")
print("You got the " + str((score/5) *100)+ " correct answers")

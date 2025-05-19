# Cameron Zorio ICA1
import random

n = 4
n_factorial = n
while n > 1:
    n_factorial *= n-1
    n = n - 1

print(n_factorial)

i = 0
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1


plays = {0: "Rock", 1: "Paper", 2: "Scissors"}
while 1:
    user_input = input("type 'r', 'p', 's', to play rock, paper, scissors. type \"exit\" to quit\n")
    if user_input == 'r':
        user_input = 0
        print("You played: Rock")
    elif user_input == 'p':
        user_input = 1
        print("You played: Paper")
    elif user_input == 's':
        user_input = 2
        print("You played: Scissors")
    elif user_input == "exit":
        break
    else: 
        print("Invalid input")
        continue

    computer_input = random.randrange(0,3)
    print("Computer played: " + plays[computer_input])

    result = user_input - computer_input
    match result:
        case 0:
            print("Tie game")
        case 1 | -2:
            print("You win")
        case -1 | 2:
            print("Computer wins")
            
    


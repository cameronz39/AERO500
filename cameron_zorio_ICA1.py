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
    user_input = input("type 'r', 'p', 's', to play rock, paper, scissors. type \"quit\" to quit\n")
    match user_input:
        case 'r':
            user_input = 0
            print("You played: Rock")
        case 'p':
            user_input = 1
            print("You played Paper")
        case 's':
            user_input = 2
            print("You played Scissors")
        case "quit":
            break
        case _: 
            print("Invalid input")
            continue

    computer_input = random.randrange(0,3)
    print("Computer played: " + plays[computer_input])

    result = user_input - computer_input
    match result:
        case 0:
            print("Tie game")
            
    


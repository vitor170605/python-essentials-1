import random

numero_secreto = random.randint(1, 100)
tentativas_restantes = 7

print("Welcome to the guessing game")
print("Guess a number from 1 to 100. You have 7 chances.\n")

while tentativas_restantes > 0:
    try:
        tentativa = int(input("Type a number: "))
    except ValueError:
        print("Please type a integer number.\n")
        continue

    if tentativa == numero_secreto:
        print("Congratulations, you got it \n")
        break
    elif tentativa < numero_secreto:
        print("Too low.\n")
    else:
        print("Too high.\n")

    tentativas_restantes -= 1
    print(f"Atempts left: {tentativas_restantes}\n")


if tentativas_restantes == 0:
    print(f"You Lost! The number was: {numero_secreto}.\n")

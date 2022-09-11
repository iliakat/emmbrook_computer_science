import random

with open ('words.txt', 'r') as file:
    lines = file.readlines()
    word = random.choice(lines).split()[0]
# word = "helloo"
print(word)

quiz = ['_' for i in range(len(word))]
health = 6
lLeft = len(word)

while health>0 and lLeft>0:
    isGuess = False
    print(f"\t=====================\n\t| You have {health} health |\n\t=====================")
    print(f"\n\t{quiz}")
    letter = str(input("\tType your letter: "))
    for l in range(len(word)):
        if letter == word[l]:
            isGuess = True
            quiz[l] = letter
            lLeft -=1
    if isGuess:
        print("\n\tIt's correct!")
    else:
        print("\n\tSorry maybe another word :(")
        health -= 1
    print(f"\tGuess {lLeft} more to win\n")

if lLeft == 0:
    print("\n\n██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗░█████╗░███╗░░██╗\n╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██╔══██╗████╗░██║\n░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║░░██║██╔██╗██║\n░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║░░██║██║╚████║\n░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░╚█████╔╝██║░╚███║\n░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚══╝")
    print(f"\n\t\tCorrect word: {word}\n")
else:
    print("\n\n██╗░░░██╗░█████╗░██╗░░░██╗  ██╗░░░░░░█████╗░░██████╗███████╗\n╚██╗░██╔╝██╔══██╗██║░░░██║  ██║░░░░░██╔══██╗██╔════╝██╔════╝\n░╚████╔╝░██║░░██║██║░░░██║  ██║░░░░░██║░░██║╚█████╗░█████╗░░\n░░╚██╔╝░░██║░░██║██║░░░██║  ██║░░░░░██║░░██║░╚═══██╗██╔══╝░░\n░░░██║░░░╚█████╔╝╚██████╔╝  ███████╗╚█████╔╝██████╔╝███████╗\n░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚══════╝░╚════╝░╚═════╝░╚══════╝")
    print(f"\n\t\tCorrect word: {word}\n")
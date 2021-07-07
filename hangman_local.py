#Write your code here
import random
print("H A N G M A N")
print ('Type "play" to play the game, "exit" to quit:')
choice = input()


if choice == "play":
    #if choice == "exit":
    #    break
    #elif choice != "play":
    #    continue
    print()
    words =['python', 'java', 'kotlin', 'javascript']

    index = random.randrange(len(words))

    result= words[index]

    result2 = "-"*len(result) 
    print(result2)
    count = 0
    win = False
    letters = []


    while True:
        letter = input("Input a letter: ")

        #validating the letter
        if len(letter) > 1 or letter == "":
            print("You should input a single letter")
            print('\n' +result2)
            continue
        elif letter not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a lowercase English letter")
            print('\n' +result2)
            continue
        elif letter in letters:
            print("You've already guessed this letter")
            print('\n' +result2)
            continue
            
        if letter not in result:
            print("That letter doesn't appear in the word")
            count +=1
            if count == 8:
               break 
        elif letter in result2:
            print("No improvements")
            count +=1
            if count == 8:
               break 
        else:
            result3 = result
            position = 0
            for i in range(result.count(letter)):   
               position = position + result3.find(letter) 
               result2 = result2[:position] + letter + result2[position+1:]
               result3 = result3[position+1:]
               position = position + 1
        if result2 == result:
            win = True
            print("You guessed the word " + result + "!")
            print("You survived!")
            print()
            break
        else:
            print('\n' +result2)
        letters.append(letter)

    if not win:
        print("You lost!")
        print()


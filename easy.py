import random
def hangman():
    list_of_words=["hangman","india","economics","laptop"]
    word=random.choice(list_of_words)
    turns=len(word)
    guessmade=""
    valid_entry=set("abcefghijklmnopqrstuvwxyz")
    while len(word)>0:
        main_word=""
        missed=0
        for letter in word:
            if letter in guessmade:
                main_word+=letter
            else:
                main_word+="_ "
        if main_word==word:
            print(main_word)
            print("you win !")
            break
        print("guess the word",main_word)
        guess=input("=")
        if guess in valid_entry:
            guessmade+=guess
        else:
            print("enter valid character")
            guess=input("=")
        if guess not in word:
            turns-=1
            if turns==len(word)-1:
                print(len(word)-1,"turns are left")
                print("----------")
            if turns==len(word)-2:
                print(len(word)-2,"turns are left")
                print("----------")
                print("    0    ")
            if turns==len(word)-3:
                print(len(word)-3,"turns are left")
                print("-----------")
                print("     O    ")
                print("     |     ")
            if turns==len(word)-4:
                print(len(word)-4,"turns are left")
                print("-----------")
                print("     O     ")
                print("     |     ")
                print("    /      ")
            if turns==len(word)-5:
                print(len(word)-5,"turns are left")
                print("-----------")
                print("     O     ")
                print("     |     ")
                print("    / \    ")
            if turns==len(word)-6:
                print(len(word)-6,"turns are left")
                print("-----------")
                print("    \O    ")
                print("     |     ")
                print("    / \    ")
            if turns==len(word)-7:
                print(len(word)-7,"turns are left")
                print("-----------")
                print("    \O/    ")
                print("     |     ")
                print("    / \    ")
            if turns==len(word)-8:
                print(len(word)-8,"turns are left")
                print("-----------")
                print("    \O/  |  ")
                print("     |     ")
                print("    / \    ")
            if turns==len(word)-9:
                print("only",len(word)-9,"turns left !! Hangman on his last breath")
                print("-----------")
                print("    \O/_|  ")
                print("     |     ")
                print("    / \    ")
            if turns==0:
                print("you loose")
                print("you let a good man die")
                print("-----------")
                print("     O_|  ")
                print("    /|\    ")
                print("    / \    ")
                break        
name=input("enter your name=")
print("Welcome",name,"!")
print("_ _ _ _ _ _ _ _ ")
print("try to guess the word ")
hangman()
#hangman code easy
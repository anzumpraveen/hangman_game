import string
import random
from images import IMAGES
def load_words():
    with open("words.txt","r")as fp:
        data=fp.read().split()
        emp_list=[]
        for list_of_words in data:
            emp_list.append(list_of_words)
        wordlist=emp_list
        secret_word=random.choice(wordlist)
        secret_word=secret_word.lower()
    return secret_word
def choose_word():
    secret=load_words()
    print(secret)
    guessmade=""
    turns=8
    valid_entry=set("abcedfghijklmnopqrstuvwxyz")
    while len(secret)>0:
        main_word=""
        missed=0
        for letter in secret:
            if letter in guessmade:
                main_word+=letter
            else:
                main_word+="_ "
        if main_word==secret:
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
        if guess not in secret:
            turns-=1
            if turns==len(secret)-1:
                print(len(secret)-1,"turns are left")
                print("----------")
                print(IMAGES[0])
            if turns==len(secret)-2:
                print(len(secret)-2,"turns are left")
                print("----------")
                print(IMAGES[1])
            if turns==len(secret)-3:
                print(len(secret)-3,"turns are left")
                print("-----------")
                print(IMAGES[2])
            if turns==len(secret)-4:
                print(len(secret)-4,"turns are left")
                print("-----------")
                print(IMAGES[3])
            if turns==len(secret)-5:
                print(len(secret)-5,"turns are left")
                print("-----------")
                print(IMAGES[4])
            if turns==len(secret)-6:
                print(len(secret)-6,"turns are left")
                print("-----------")
                print(IMAGES[5])
            if turns==len(secret)-7:
                print(len(secret)-7,"turns are left")
                print("-----------")
                print(IMAGES[6])
            if turns==len(secret)-8:
                print(len(secret)-8,"turns are left")
                print("-----------")
                print(IMAGES[7])
                break        
name=input("enter your name=")
print("Welcome",name,"!")
print("_ _ _ _ _ _ _ _ ")
print("try to guess the word ")
choose_word()
# hangman code easy

#     guess=input("guess any word")
#     """
#     word_list (list): list of words (strings)
#     ye function ek word randomly return karega
#     """
#     word_list = load_words()
#     secret_word = random.choice(word_list)
#     secret_word = secret_word.lower()

#     return secret_word
choose_word()
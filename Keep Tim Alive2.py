# -*- coding: utf-8 -*-
"""
@author: Dayra
(Hangman) Keep Tim Alive
"""
import random

categ = [ [], ['apple', 'croissant', 'spinach', 'sandwich', 'watermelon'], 
          ['disgusted','surprised','furious','happy','suspicious'],
          ['motorbike', 'cupboard','paintbrush','lipstick','armchair'] ]

def game():
    #Options
    print("Welcome to Keep Tim Alive! :)")
    print("Please choose a category: ")
    print("1. Food")
    print("2. Emotions")
    print("3. Objects")
    
    n=int(input())
    while n<1 or n>3:
        print("That's not a valid category. Try again.")
        n=int(input())
    
    #Random word from chosen category
    x = random.randint(0,4)
    word = categ[n][x]
    ac=[]  
    
    #Instructions
    print("\nTim has 6 little stars ★★★★★★")
    print("You have to guess the secret word letter by letter")
    print("Every time you make a mistake, Tim loses a star")
    print("If Tim loses his 6 stars, he will die of sadness :( ")
    print("\n")
    
    for i in word:
        ac.append('_')
        print("_ ", end = '')
    print("\n\nIt's time to play! Type a lowercase letter from the english alphabet")
    
    cont=len(word)
    lose=False
    stars=6
    
    while lose==False and cont>0:
        el=str(input())
        guess=False
        for i in range(len(word)):
            if word[i]==el and ac[i]=='_':
                ac[i]=el
                cont-=1
                guess=True
        if guess==True and cont>0:
            for i in ac:
                print(i+" ", end = '')
            print("\nNice! Type another one")
        if guess==False:
            stars-=1
            for i in ac:
                print(i+" ", end = '')
            if stars>0:
                print("\nTim has lost a star :( Type another letter")
                print('★' * stars)
            if stars==0:
                lose=True
                print("\nTim is dead xP")
                print("The secret word was: "+word)
                print("Press 1 to play again")
                print("Press 2 to quit the game")
                y = int(input())
                while y<1 or y>2:
                    print("\nThat's not a valid option. Try again")
                    y = int(input())
                if y==1:
                    game()
                else: 
                    return
    if lose==False and cont==0:
        for i in ac:
            print(i+" ", end = '')
        print("\nTim is safe! :D Congratulations!")
        print("Press 1 to play again")
        print("Press 2 to quit the game")
        y = int(input())
        while y<1 or y>2:
            print("\nThat's not a valid option. Try again")
            y = int(input())
        if y==1:
            game()
        else: 
            return
        
game()         

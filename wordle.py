import random

def word_list()->list:
    l = []
    with open("5_letter_words.txt") as f:
        for line in f:
            l.append(line.strip())
    return l

def random_word(words:list)->str:
    return words[random.randint(0,len(words)-1)]
    
def is_real_word(word:str, l:list)->bool:
    return (word in l) and (len(word) == 5)

def next_guess(words:list)->str:
    while True:
        inpt = input("Please enter a guess:").lower()
        if is_real_word(inpt,words):
            return inpt
        else:
            print("That's not a real word!")

def check_guess(word:str, key:str)->str:
    key2 = list(key)
    s = ""
    for i in range(5):
        if word[i] == key[i]:
            s+="X"
            key2[i] = " "
        elif word[i] in key2:
            key2[key.index(word[i])] = " "
            s+="O"
        else:
            s+="_"
    return s
    
def play()->None:
    words = word_list()
    key = random_word(words)
    guesses = 0
    while guesses <6:
        guess = next_guess(words)
        print(check_guess(guess,key))
        guesses += 1
        if guess == key:
            print("You won!")
            return
    if guesses == 6:
            print("You lost!")
            print(f"The word was: {key}")

play()

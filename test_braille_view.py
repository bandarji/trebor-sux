import random


word_list = [
    "friend",
    "fiends",
    "bottom",
    "abased",
]

word = random.choice(word_list)
guessed = set()  # a set of letters already guessed
tries_remaining = 5


while tries_remaining:
    # This next line can also be written as
    # out = ""
    # for char in word:
    #     if c in guessed:
    #         out += f"{c} "
    #     else:
    #         out += "_ "
    # print(out)
    print(" ".join(c if c in guessed else "_" for c in word))
    guess = input("Guess a letter: ").lower()[0]  # make lowercase and take first letter
    if guess in guessed:
        continue  # restart loop, no loss of tries
    guessed.add(guess)  # add the current guess to the guessed
    if len(guessed)
    if guess in word:
        continue  # restart loop, no loss of tries
    tries_remaining -= 1  # decrement tries counter

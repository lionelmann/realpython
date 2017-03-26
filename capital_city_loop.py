from capitals import capitals_dict
from random import choice

def capital_game(province, capital):
    while True:
        guess = input("What is the capital of {}?".format(province))
        if guess.lower() == capital.lower():
            print("Correct")
            print("The capital of {} is {}".format(province,capital))
            break
        elif guess.lower() == "exit":
            print("Goodbye")
            break
        
province = choice(list(capitals_dict.keys()))
capital  = capitals_dict[province]
print(province, capital)


capital_game(province, capital)
    


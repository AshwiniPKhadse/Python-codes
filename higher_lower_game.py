import random
import game_art
import gamedatabase

print(game_art.game_logo)

def display_accountinfo(account):
    name=account["name"]
    description=account["description"]
    country=account["country"]
    return f"{name},a{description},from{country}"

def check_ans(guess,followers_1,followers_2):
    if followers_1< followers_2:
        if guess==1:
            return False
        else:
            return True
    
    else:
        if guess==1:
            return True
        else:
            return False
        

account1= random.choice(gamedatabase.data)
account2= random.choice(gamedatabase.data)

print(f"compare 1:{display_accountinfo(account1)}")

print(game_art.vs)

print(f"compare 2:{display_accountinfo(account2)}")
guess=int(input("who has more followers? Type 1 or 2: "))
followers_count_1=account1["follower_count"]
followers_count_2=account2["follower_count"]



display_accountinfo(account1)
display_accountinfo(account2)



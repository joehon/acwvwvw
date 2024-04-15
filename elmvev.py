import random

def unique(l):
    if len(l)==len(set(l)):
        print("The List is Unique!")
        return True
    else:
        print("The List is Not Unique!")
        return False


katachi = ['♣', '◆', '♠', '♥']
bango = ['A', '2', '3', '4', '5', '6', '8', '7', '9', '10', 'Jack', 'Queen', 'King']
card = []

for i in bango:
    for j in katachi:
        card.append(i+j)
card.append('BlackJokker')
card.append('ColorJokker')

player = []
cp = []

player.append(random.sample(card, 26))
cp.append(random.sample(card, 26))

print(player, cp)
import itertools
import random

card_suits = {
    "s": "spades",
    "D": "diamonds",
    "H": "heart",
    "C": "clubs"
}
cards = {
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11
}

dec_of_cards = []
# for suits in card_suits:
# for card in cards:
#    dec_of_cards.append((suits,cards))
#print(suits, card)

for i in itertools.product(card_suits,cards):
    dec_of_cards.append(i)
#מגריל 2 מספרים והשמה לmy_cards
my_cards=random.sample(dec_of_cards,2)

#דק-אוף-כרד מחזיק קלפים שלא נמצאים במיי-כרד
dec_of_cards=[card for card in dec_of_cards if card not in my_cards]
#מגריל 2 מספרים והשמה לדיילר
dealer_cards= random.sample(dec_of_cards,2)
dec_of_cards=[card for card in dec_of_cards if card not in dealer_cards]


print("dec_of_cards ",dec_of_cards)
print("my_cards ",my_cards)
print("dealer_cards ",dealer_cards)
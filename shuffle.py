import random
import numpy as np

# make a deck of cards
# deck = list(['Orel','Jeřáb','Sova','Kolibřík','Medvěd','Vlk', 'Liška', 'Rys', 'Myš', 'Had', 'Chameleon', 'Krokodýl', 'Ještěrka', 'Žralok', 'Krab', 'Chobotnice'])
def BalicekKaret ():
	a = np.array(['Orel','Jeřáb','Sova','Kolibřík','Medvěd','Vlk'])
	s = np.array([3, 3, 9, 3, 6, 3]) #kolik má odpovídající typ mít počet v arrayi
	deck = np.repeat(a, s)
	random.shuffle(deck)
	return deck
# shuffle the cards
deck = BalicekKaret()
print (deck)
"""random.shuffle(deck)

# draw five cards
print(deck)
print(z[3:])
	return deck
a = np.array(['Orel','Jeřáb','Sova','Kolibřík','Medvěd','Vlk'])
	s = np.array([3, 3, 9, 3, 6, 3]) #kolik má odpovídající typ mít počet v arrayi
	deck = np.repeat(a, s)"""
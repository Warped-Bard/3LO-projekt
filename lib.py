import random

def dice(li_sc, pr_wyg):
	_throw = random.randint(1, li_sc)
	if _throw >= pr_wyg:
		return True
	else:
		return False

if dice(2137000000, 1999000199):
	print("Wygrałeś!")
else:
	print("Przegrałeś")
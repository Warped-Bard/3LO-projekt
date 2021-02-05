import yaml
import random
import time

def dot(n):                                                                                        # funkcja pisze kropke n kropek i czeka chwile.
	for b in range(0, n):
		print(".")
		time.sleep(1)
		b += 1

def walka(wrog):                                                                                   # funkcja obsługuje walkę z wybranym wrogiem.
	global ty_hp
	global ty_exp
	global ty_lv
	global ty_atak
	wróg_hp = dane_dungeonu[wrog]['hp']
	print(f"Atakuje cię {wrog}")
	dot(1)
	if ty_szybkość >= dane_dungeonu[wrog]['szybkosc']:
		tura_gracza = 2
	else:
		tura_gracza = 3
	obaj_żywi = True
	while obaj_żywi:
		if tura_gracza % 2 == 0: 
			answer = input("Zaczynasz, wykonaj akcję. (atak czy ucieczka?):  ")
			if answer == 'atak':
				critical = float(random.randint(1, 10)) * ty_critical
				if critical > 7.5:
					ty_atak = ty_atak * 2
					wróg_hp -= ty_atak
					dot(1)
					print("Cios krytyczny!")
				else:
					wróg_hp -= ty_atak
				if wróg_hp < 0:
					wróg_hp = 0
				dot(1)
				print(f"Uderzasz {wrog}, zadając mu {ty_atak} życia. ")
				dot(1)
				print(f"Zostało mu {wróg_hp} życia. ")
			elif answer == 'ucieczka':
				dot(1)
				ucieczka(wrog)
			else:
				print("Nie ma takiej opcji. Powtórz wybór. ")
				continue
		else:
			dot(1)
			print("Teraz kolej wroga...")
			dot(2)
			print(f"{wrog} wykonuje Atak.")
			dot(1)
			critical = float(random.randint(1, 10)) * dane_dungeonu[wrog]['critical']
			if critical > 7.5:
				case_atak = dane_dungeonu[wrog]['atak'] * 2
				dot(1)
				print("Cios krytyczny!")
			else:
				case_atak = dane_dungeonu[wrog]['atak']
			print(f"Zadaje ci {case_atak} dmg.")
			dot(1)
			ty_hp -= case_atak
			print(f"Pozostało ci {ty_hp} życia.")
		if ty_hp <= 0:
			print("Zdechłeś.")
			obaj_żywi = False
		if wróg_hp <= 0:
			print(f"Pokonałeś {wrog}a! Gratulacje")
			dot(1)
			print(f"Zdobywasz {dane_dungeonu[wrog]['exp']} punktów doświadczenia.")
			ty_exp += dane_dungeonu[wrog]['exp']
			if ty_exp >= 20:
				ty_exp -= 20
				ty_lv += 1
				print("Zwiększyłeś swój poziom doświadczenia!")
				dot(1)
				print(f"Teraz masz poziom {ty_lv}!")
				dot(1)
				print(f"Do kolejnego poziomu pozostało {20 - ty_exp} punktów doświadczenia.")
				dot(1)
			drop = loot(wrog)
			dot(1)
			print("Grzebiewsz w truchle wroga...")
			dot(2)
			if drop != 'nic':
				print(f"Znalazłeś {drop}! \nZbierasz przedmiot do swojej sakwy.")
				worek.append(drop)
			else:
				dot(1)
				print("Nic nie znalazłeś..")
			obaj_żywi = False
		tura_gracza += 1

def loot(wrogg):
	droplist = dane_dungeonu[wrogg]['drop']
	return random.choice(droplist)

def zobaczsakwe():                                                                                 # jeszcze nie użyta funkcja pozwalająca przejrzeć dotychczas zebrane łupy.
	element = 0
	for element in worek:
		print(element)

def ucieczka(wrog):
	print('Próbujesz uciec...')
	dot(1)
	_run = ty_szybkość / dane_dungeonu[wrog]['szybkosc']
	if _run <= 1.0:
		print("Nie udaje ci się uciec.")
		print("Wróg wykorzystuje chwilę twojej nieuwgi i atakuje!")
		tura_gracza += 1
	elif _run > 1.0 and _run <= 1.5:
		if dice(2,2):
			print("Ledwo udaje ci się uciec.")
			print("Wróg przez chwilę cię goni, poczym sobie odpuszcza...")
			obaj_żywi = False
	else:
		print("Udaje ci się uciec.")
		print("Wróg zdezorientowany stoi przez chwilę w miejscu, po czym dokądś odchodzi...")
		obaj_żywi = False                                                                          # fubkcja obsługująca możliwość ucieczki

def dice(li_sc, pr_wyg):
	_throw = random.randint(1, li_sc)
	if _throw >= pr_wyg:
		return True
	else:
		return False

worek = []                                    
ty_exp = 0
ty_critical = 1.2                                                                                  # Dane gracza
ty_lv = 1
ty_hp = 10
ty_szybkość = 4
ty_atak = 3
lista_dungeonów = ['las','cmentarz','zbocze']
while True:                                                                                        # Wybór dungeonu
	a = input("Wybierz dokąd chcesz się udać (las, cmentarz czy zbocze?):  ")
	if a in lista_dungeonów:
		nazwa_dungeonu = a
		break
	else:
		print("Podałeś złą nazwę dungeonu. Spróbuj ponownie \n") 

dot(1)
plik_dungeonu = open(f'{nazwa_dungeonu}.yml')                                                      # Załadowanie danych w zależnpośći od wybranego dungeonu.
print(f"Wchodzisz do {nazwa_dungeonu}")
dane_dungeonu = yaml.full_load(plik_dungeonu)

dot(3)
wróg = (random.choice(list(dane_dungeonu)))
walka(wróg) 
dot(1)

print(f"Oto co masz teraz w worku: {worek}")
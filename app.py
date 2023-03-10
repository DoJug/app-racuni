import json, os
from funkcije import kreiranje_broja_lokacija, kreiranje_baze, prikaz_baze, prikaz_izbornika, uredenje_postojece_baze, brisanje_baze
#from funkcije import provjera_postojece_baze

def main():

    aktivnost = True
    while aktivnost:
        os.system('cls')
        print('*' * 110)
        print("\n\t\t\tAPLIKACIJA ZA KREIRANJE, PREGLED I UREĐENJE BAZE RAČUNA")
        print("\nZa početak, upišite ime kako bismo provjerili postoji li Vaša baza (upišite 'q' za izlazak iz aplikacije)")
        ime = input("\nVaše ime: ")
        if ime == 'q':
            print("\nZatvaranje aplikacije...")
            aktivnost = False
        else:#provjera_postojeće_baze() ili:
            datoteka = f'{ime}_racuni.json'
            pretraga = os.path.exists(f'{ime}_racuni.json')
            postojanost = lambda pretraga, ime:  f'\nVaša baza postoji, {ime}! Ako želite prikazati Vašu bazu, odaberite opciju broj 2.' if pretraga else f'\nVaša baza ne postoji, {ime}! Kreirajte novu bazu.'
            print(postojanost(pretraga, ime))
            print()
            input("\n\n\t\t\t\tPRITISNITE 'ENTER' ZA NASTAVAK U GLAVNI IZBORNIK!")
            glavni_izbornik = True

            while glavni_izbornik:
                os.system('cls')
                print('*' * 110)
                print("\n\n\t\t\tAPLIKACIJA ZA KREIRANJE, PREGLED I UREĐENJE BAZE RAČUNA")
                #datoteka = f'{ime}_racuni.json'
                prikaz_izbornika(pretraga)
                odabrana_opcija = int(input("\nOdabir: "))

                if odabrana_opcija == 1:
                    os.system('cls')
                    print('*' * 110)
                    print("\n\t\t\tAPLIKACIJA ZA KREIRANJE, PREGLED I UREĐENJE BAZE RAČUNA")
                    broj_lokacija = kreiranje_broja_lokacija()
                    input("\n\n\t\t\t\tPRITISNITE 'ENTER' ZA NASTAVAK!")
                    racuni = kreiranje_baze(broj_lokacija)
                    with open(datoteka, 'w') as dat:
                        json.dump(racuni, dat)

                    pitanje = input("\nŽelite li prikazati kreiranu bazu? (da/ne) ")
                    if pitanje == 'da':
                        os.system('cls')
                        print('*' * 110)
                        print("\n\t\t\tAPLIKACIJA ZA KREIRANJE, PREGLED I UREĐENJE BAZE RAČUNA")
                        with open(datoteka, 'r') as dat:
                            racuni = json.load(dat)
                            prikaz_baze(racuni)
                            print("\n\nNakon prikaza baze, obavezno se ulogirati sa kreiranim računom!")
                            input("\n\n\t\t\t\tPRITISNITE 'ENTER' ZA ODLAZAK NA PRIJAVU!")
                            break
                    elif pitanje == 'ne':
                        print("Zatvaranje aplikacije...")
                        glavni_izbornik = False
                    else:
                        print("\nKrivi unos!")
                        input("\n\n\t\t\t\tPRITISNITE 'ENTER' ZA ODLAZAK NA PRIJAVU!")

                elif odabrana_opcija == 2:
                    os.system('cls')
                    """try:
                        with open(datoteka, 'r') as dat:
                            racuni = json.load(dat)
                    except FileNotFoundError:
                        print("Baza ne postoji. Niste kreirali bazu.")
                    else:
                        prikaz_baze(racuni)""" #ili:
                    if pretraga:
                        with open(datoteka, 'r') as dat:
                            racuni = json.load(dat)
                        prikaz_baze(racuni)
                        input("\n\n\n\t\t\t\tPRITISNITE 'ENTER' ZA ODLAZAK U PRETHODNI IZBORNIK!")
                    else:
                        print('*' * 110)
                        print("\n\t\t\tAPLIKACIJA ZA KREIRANJE, PREGLED I UREĐENJE BAZE RAČUNA")
                        print("\nBaza ne postoji! Niste kreirali bazu!")
                        input("\n\n\t\t\t\tPRITISNITE 'ENTER' ZA ODLAZAK U PRETHODNI IZBORNIK!")

                elif odabrana_opcija == 3:#Uređenje postojeće baze
                    os.system('cls')
                    print('*' * 110)
                    print("\n\t\t\tAPLIKACIJA ZA KREIRANJE, PREGLED I UREĐENJE BAZE RAČUNA")
                    if pretraga:
                        with open(datoteka, 'r') as dat:
                            racuni = json.load(dat)
                        uredenje_postojece_baze(racuni)
                        with open(datoteka, 'w') as dat:
                            json.dump(racuni, dat)
                    else:
                        print("\nVaša baza ne postoji stoga ju ne možete urediti!")
                        input("\n\n\t\t\t\tPRITISNITE 'ENTER' ZA ODLAZAK U PRETHODNI IZBORNIK!")
                    
                elif odabrana_opcija == 4:
                    os.system('cls')
                    print('*' * 110)
                    print("\n\t\t\tAPLIKACIJA ZA KREIRANJE, PREGLED I UREĐENJE BAZE RAČUNA")
                    if pretraga:
                        brisanje_baze(datoteka)
                        glavni_izbornik = False
                    else:
                        print(f"\nBaza pod imenim {datoteka} ne postoji!")
                        input("\n\n\t\t\t\tPRITISNITE 'ENTER' ZA ODLAZAK U PRETHODNI IZBORNIK!")
                    
                elif odabrana_opcija == 5:
                    print("Povratak na početni log-in screen")
                    glavni_izbornik = False

                elif odabrana_opcija == 6:
                    print("Zatvaranje aplikacije...")
                    return
                
                else:
                    print("Krivi unos.")
main()
                





import os
import send2trash

def kreiranje_broja_lokacija():
    broj_lokacija = 'nista'

    while broj_lokacija.isdigit() == False:

        broj_lokacija = input("\nUnesite željeni broj lokacija: ")

        if broj_lokacija.isdigit() == False:
            print("Krivi unos. Koristite brojke za definiranje lokacija. Molim Vas upišite broj.")

    return int(broj_lokacija)
   
def prikaz_izbornika(pretraga):
    if pretraga:
        print()
        print("\nTrenutačno se nalazite u glavnom izborniku. Odaberite redni broj ispred ponuđenih opcija.")
        print("\nIZBORNIK: ")
        print("\t 1. Ažuriranje baze")
        print("\t 2. Prikazivanje baze")
        print("\t 3. Ažuriranje postojeće baze")
        print("\t 4. Brisanje postojeće baze")
        print("\t 5. Povratak na početni log-in screen")
        print("\t 6. Kraj rada")
    else:
        print()
        print("\nTrenutačno se nalazite u glavnom izborniku. Odaberite redni broj ispred ponuđenih opcija.")
        print("\nIZBORNIK: ")
        print("\t 1. Kreiranje baze")
        print("\t 5. Povratak na početni log-in screen")
        print("\t 6. Kraj rada")

def provjera_postojece_baze(naziv_baze, ime):
    import json
    try:
        with open(naziv_baze, 'r') as dat:
            racuni = json.load(dat)
    except FileNotFoundError:
        print("Baza ne postoji. Niste kreirali bazu.")
    else:
        print(f"\nPostoji baza sa vašim imenom {ime}.")
        print(f"Dobrodošli nazad, {ime}!")

def kreiranje_baze(broj_lokacija):#ime, broj lokacija
    os.system('cls')
    print('*' * 110)
    print("\n\t\t\tAPLIKACIJA ZA KREIRANJE, PREGLED I UREĐENJE BAZE RAČUNA")
    racuni = dict()
    #mjeseci = ['Siječanj', 'Veljača', 'Ožujak', 'Travanj', 'Svibanj', 'Lipanj', 'Srpanj', 'Kolovoz', 'Rujan', 'Listopad', 'Studeni', 'Prosinac']
    for broj in range(1, broj_lokacija + 1):
        kljucna_rijec = input(f"\nOdaberite ključnu riječ za lokaciju {broj}:  ")
        mjesec = int(input("Za koji mjesec želite kreirati bazu (unesite broj):  ")) 
            
        naziv_lokacije = f"Lokacija {broj} - {kljucna_rijec.title()} ({mjesec}. mjesec)"
        naziv_mjeseca = f'{mjesec}. mjesec'
            
        racuni[naziv_lokacije] = {naziv_mjeseca: 
                        
            {'plin': False, 'voda': False, 'struja': False, 'komunalije': False, 'dopunsko': False, 'općina/grad': False, 'zgrada': False} 
                
                                }            
        
    return racuni

def prikaz_baze(baza):
    os.system('cls')
    print('*' * 110)
    print("\n\t\t\tAPLIKACIJA ZA KREIRANJE, PREGLED I UREĐENJE BAZE RAČUNA")
    print(('\t\t\t______________________________________________________'))
    print("\t\t\t*Prikaz plaćenih i neplaćenih računa prema lokacijama*")
    print(('\t\t\t______________________________________________________'))
    print()

    for kljuc, vrijednost in baza.items():
        print()
        """if vrijednost == 1:
            vrijednost = 'Siječanj'"""
        print(f"\t\t{kljuc}", end="||\t\t\t")

        for kljuc, vrijednost in vrijednost.items():
            print()
            print()
            print(f"{kljuc}", end='|' )
            print()
            for kljuc, vrijednost in vrijednost.items():
                print()
                if vrijednost == False or vrijednost == 'NEPLAĆENO':
                    vrijednost = 'NEPLAĆENO'
                elif vrijednost == True or vrijednost == 'PLAĆENO':
                    vrijednost = 'PLAĆENO'
                print(f"{kljuc.title()}: {vrijednost}", end='')
        print()


def uredenje_postojece_baze(racuni):
    #print("\nOtvorili ste vašu bazu računa.")

    odabir_lokacije = ''#1. lokacija 1 - grad, itd.
    while odabir_lokacije not in racuni.keys():
        os.system('cls')
        print('*' * 110)
        print("\n\t\t\tAPLIKACIJA ZA KREIRANJE, PREGLED I UREĐENJE BAZE RAČUNA")
        print("\nOdaberite lokaciju koju želite urediti - unesite redni broj ispred lokacije (unesite 'q' za povratak u prethodni izbornik): ")
        brojac = 1
        for kljuc in racuni.keys():
            print(f"\n\t{brojac}. {kljuc}")
            brojac +=1
        lista_lokacija = list(racuni.keys())
        odabir_lokacije = input("\nOdabir lokacije ('q' za izlaz): ")#ako korisnik unese 1, to je zapravo prvi element nule na indeksu 0
        if odabir_lokacije == 'q':
            return
        else:
            odabir_lokacije = int(odabir_lokacije)-1
            if odabir_lokacije not in range(len(lista_lokacija)):
                print(f"\nOdabrali ste redni broj lokacije koja ne postoji. Pokušajte ponovno!")
            else:
                print(f"\nOdabrali ste lokaciju '{lista_lokacija[odabir_lokacije]}'. \n\nIzbornik (unesite broj ispred odabira): \n\t1. Plaćeni \n\t2. Neplaćeni \n\t3. Prikaz plaćenih i neplaćenih\n")

                odabir_plaćeni_neplaćeni = 0
                vrijednosti = racuni[lista_lokacija[odabir_lokacije]]
                while odabir_plaćeni_neplaćeni > 3 or odabir_plaćeni_neplaćeni == 0:
                    odabir_plaćeni_neplaćeni = int(input("\nOdabir:  "))
                    odabir_vrste_racuna(odabir_plaćeni_neplaćeni, vrijednosti)

def funkcija(placeni_ili_neplaceni):
    odabir_racuna = ''
    while odabir_racuna not in placeni_ili_neplaceni.keys():
        print("\n\nSto zelite od navedenog promijeniti? ('q' za povratak u glavni izbornik)")
        odabir_racuna = input("Odabir:  ")
        if odabir_racuna == 'q':
            return
        elif odabir_racuna not in placeni_ili_neplaceni.keys():
            print("Krivi odabir!")
        else:
            print(f"\nTRENUTAČNA VRIJEDNOST {odabir_racuna} je {placeni_ili_neplaceni[odabir_racuna]}.")
            vrijednost = int(input("NOVA VRIJEDNOST: "))
            placeni_ili_neplaceni[odabir_racuna] = vrijednost

def odabir_vrste_racuna(odabir_plaćeni_neplaćeni, vrijednosti):

    if odabir_plaćeni_neplaćeni == 1:
        os.system('cls')
        print('*' * 110)
        print(f"\n\t\t\tISPIS SVIH PLAĆENIH RAČUNA")
        print("\n|PLAĆENI RAČUNI| ")
        for kljuc, vrijednost in vrijednosti.items():
                print(f"\n\n{kljuc}")
                print('________________')
                for kljuc_2, vrijednost_2 in vrijednost.items():
                    if vrijednost_2 == True or vrijednost_2 == 'PLAĆENO':
                        vrijednost_2 = 'PLAĆENO'
                        print(f"\n{kljuc_2}: {vrijednost_2}")
        kljuc_mjesec = list(vrijednosti.keys())
        kljucevi_i_vrijednosti_mjeseca = vrijednosti[kljuc_mjesec[0]]#plin:neplaceni, struja:neplaceni
        #vrijednosti_mjeseca_vrijednosti = vrijednosti.values()    
        odabir_racuna = ''
        while odabir_racuna != ['plin', 'voda', 'struja', 'komunalije', 'dopunsko', 'općina/grad', 'zgrada']:#ili: while odabir_racuna not in plaćeni.keys(), ili not in ['plin'...]
            print("\n\nSto zelite od navedenog promijeniti? ('q' za povratak u glavni izbornik)")
            odabir_racuna = input('ODABIR:  ')
            if odabir_racuna == 'q':
                return
            else:
                if odabir_racuna not in kljucevi_i_vrijednosti_mjeseca.keys():
                    print("Krivi odabir!")
                else:
                    print(f"\nTRENUTAČNA VRIJEDNOST za {odabir_racuna} je PLAĆENO.")
                    vrijednost = input("JESTE LI PLATILI RAČUN (da/ne)?  ")
                    if vrijednost == 'da':
                        kljucevi_i_vrijednosti_mjeseca[odabir_racuna] = 'PLAĆENO'
                        print("\nUSPJEŠAN ZAPIS!")
                    elif vrijednost == 'ne':
                        kljucevi_i_vrijednosti_mjeseca[odabir_racuna] = 'NEPLAĆENO'
                        print("\nUSPJEŠAN ZAPIS!")
                    else:
                        print("KRIVI UNOS!")
        input("\n\t\t\t\tPRITISNITE 'ENTER' ZA ODLAZAK U PRETHODNI IZBORNIK!")
        return

    elif odabir_plaćeni_neplaćeni == 2:
        os.system('cls')
        print('*' * 110)
        print(f"\n\t\t\tISPIS SVIH NEPLAĆENIH RAČUNA")
        print("\n|NEPLAĆENI RAČUNI|")
        for kljuc, vrijednost in vrijednosti.items():
            print(f"\n\n{kljuc}")#mjesec
            print('__________________')
            for kljuc_2, vrijednost_2 in vrijednost.items():
                if vrijednost_2 == False or vrijednost_2 == 'NEPLAĆENI':
                    vrijednost_2 = 'NEPLAĆENI'
                    print(f"\n{kljuc_2}: {vrijednost_2}")#vrsta racuna i string placeni/neplaceni
                
        kljuc_mjesec = list(vrijednosti.keys())
        kljucevi_i_vrijednosti_mjeseca = vrijednosti[kljuc_mjesec[0]]#plin:neplaceni, struja:neplaceni
        #vrijednosti_mjeseca_vrijednosti = vrijednosti.values()
        odabir_racuna = ''
        while odabir_racuna != ['plin', 'voda', 'struja', 'komunalije', 'dopunsko', 'općina/grad', 'zgrada']:#ili: while odabir_racuna not in plaćeni.keys(), ili not in ['plin'...]
            print("\n\nSto zelite od navedenog promijeniti? ('q' za povratak u prethodni izbornik)")
            #mjesec = list(vrijednost.keys())
            odabir_racuna = input("ODABIR: ")
            if odabir_racuna == 'q':
                return
            elif odabir_racuna not in kljucevi_i_vrijednosti_mjeseca.keys():
                print("Krivi odabir!")
            else:
                if kljucevi_i_vrijednosti_mjeseca[odabir_racuna] == False:
                    print(f"\nTRENUTAČNA VRIJEDNOST za {odabir_racuna} je NEPLAĆENO.")
                vrijednost = input("JESTE LI PLATILI RAČUN (da/ne)?  ")
                if vrijednost == 'da':
                    kljucevi_i_vrijednosti_mjeseca[odabir_racuna] = 'PLAĆENO'
                    print("\nUSPJEŠAN ZAPIS!")
                elif vrijednost == 'ne':
                    kljucevi_i_vrijednosti_mjeseca[odabir_racuna] = 'NEPLAĆENO'
                    print("\nUSPJEŠAN ZAPIS!")
                else:
                    print("KRIVI UNOS!")
        input("\n\t\t\t\tPRITISNITE 'ENTER' ZA ODLAZAK U GLAVNI IZBORNIK!")
        return
    
    elif odabir_plaćeni_neplaćeni == 3:
        os.system('cls')
        print('*' * 110)
        print("\n\t\t\tAPLIKACIJA ZA KREIRANJE, PREGLED I UREĐENJE BAZE RAČUNA")
        print(('\t\t\t______________________________________________________'))
        print("\t\t\t*Prikaz placenih i neplacenih racuna prema lokacijama*")
        print(('\t\t\t______________________________________________________'))
        print()
        for kljuc, vrijednost in vrijednosti.items():
            print(f"\t\t{kljuc}", end="||\t\t\t")
            print()
            print()
            for kljuc, vrijednost in vrijednost.items():
                if vrijednost == False:
                    vrijednost = 'NEPLAĆENO'
                elif vrijednost == True:
                    vrijednost = 'PLAĆENO'
                print(f"\n{kljuc.title()}: {vrijednost}")
        input("\n\t\t\t\tPRITISNITE 'ENTER' ZA ODLAZAK U PRETHODNI IZBORNIK!")
        return
    else:
        print("Krivi unos!\n")

def brisanje_baze(datoteka):
    os.system('cls')
    print('*' * 110)
    print("\n\t\t\tAPLIKACIJA ZA KREIRANJE, PREGLED I UREĐENJE BAZE RAČUNA")
    print("\n\nJESTE LI SIGURNI DA ŽELITE OBRISATI VAŠU BAZU SA RAČUNIMA? (da/ne)")
    odabir = ''
    while odabir != ('da' or 'ne'):
        odabir = input("\nOdgovor: ")
        if odabir == 'da':
            send2trash.send2trash(datoteka)
            print("\n\n\tUSPJEŠNO OBRISANA BAZA!")
            input("\n\t\t\t\tPRITISNITE 'ENTER' ZA ODLAZAK U PRETHODNI IZBORNIK!")
        elif odabir == 'ne':
            print("\nODUSTAJANJE...")
            input("\n\t\t\t\tPRITISNITE 'ENTER' ZA ODLAZAK U PRETHODNI IZBORNIK!")
            break
        else:
            print("\nKrivi unos!")
            




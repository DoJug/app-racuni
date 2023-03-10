Pozdrav!
Ovo je moja druga aplikacija nakon aplikacije "app-banka". 

Aplikacija sadržava sljedeće funkcionalnosti:
1. Kreiranje/ažuriranje baze
2. Prikazivanje baze
3. Ažuriranje postojeće baze
4. Brisanje postojeće baze
5. Povratak na početni log-in screen
6. Kraj rada
    
Aplikacija se sastoji od nekoliko dijelova:
- app.py
- funkcije.py
- primjer_baze.py
- user_racuni.json
    
app.py je glavna, main funkcija koja pokreće cijeli kod aplikacije. Prilikom pokretanja aplikacije, aplikacija upita korisnika da unese svoje ime kako bi provjerila postoji li baza računa sa korisnikovim imenom (user_racuni.json predstavlja default bazu racuna sa kojom se korisnik može ulogirati ako želi). Nakon pretrage aplikacija uzvraća povratnu informaciju korisniku. app.py sve funkcije (module) koje obavlja importa iz datoteke funkcije.py

funkcije.py sadržava sve funkcije koje su potrebne za rad aplikacije. 

primjer_baze.py predstavlja moj primjer zamišljene baze.

*NAPOMENA: ZA RAD "BRISANJE POSTOJEĆE BAZE" KORIŠTEN JE "send2trash" MODULE KOJI BRIŠE POSTOJEĆU BAZU I ŠALJE JU U RECYCLE BIN (KOŠ ZA SMEĆE). UKOLIKO U APLIKACIJI DOĐE DO POGREŠKE SA OPISOM "REPORTMISSINGMODULESOURCE" POTREBNO JE INSTALIRATI MODUL PUTEM COMMAND PROMPT-a UZ NAREDBU "pip install Send2Trash".  

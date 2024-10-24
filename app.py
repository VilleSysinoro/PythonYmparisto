# SOVELLUKSEN PÄÄOHJELMA
# ======================

# KIRJASTOT
# ---------

# MODUULIT
# --------

from avtools import sound  # Äänimerkit ja äänitiedostot
from avtools import video  # Videomoduuli
import identityCheck2

# ASETUKSET
# ---------
kameraIndeksi: int = 1  # Ensimmäinen kamera on aina 0

while True:
    userGivenSsn = input('Syötä asiakkaan henkilötunnus: ')
    userGivenSsn = userGivenSsn.upper()  # Varmistetaan, että  tarkiste on isolla

    # TODO: Tee tarkistus siitä, että nimi ei voi olla tyhjä

    # TODO: Rakenna funktio , jolla kysytään nimet ja muutetaan yhdysnimet isoile alkukirjaimille -> reg exp

    ssnToCheck = identityCheck2.NationalSSN(userGivenSsn)
    if ssnToCheck.isValidSsn() == True:
        try:
            dateOfBirth = ssnToCheck.getDateOfBirth()
            ssnToCheck.getGender()
            age = ssnToCheck.calculateAge()
            userGivenLastname = input(
                'Syötä asiakkaan sukunimi: ')  # Pyydetään sukunimeä
            # Korjataan sukunimen ensimäinen kirjain isoksi kirjaimeksi
            userGivenLastname = userGivenLastname.capitalize()
            userGivenFirstname = input(
                'Syötä asiakkaan etunimi: ')  # Pyydetään etunime
            # Korjataan etuimen ensimäinen kirjain isoksi kirjaimeksi
            userGivenFirstname = userGivenFirstname.capitalize()
            print('Asiakas:', userGivenLastname, userGivenFirstname)
            print('Syntymäaika: ', ssnToCheck.dateOfBirth)
            print('Ikä: ', age)
            print('Sukupuoli: ', ssnToCheck.gender)

        except Exception as e:
            print('Syöttämässäsi sosiaaliturvatunniksessa oli virhe', e)

    # Kysytään halutaanko poistua ohjelmasta
        wantAbort = input('Haluatko päättää ohjelman k/E: ')
    # Muutetaan vastaus isoksi kirjaimeksi ja tarkitetaan onko vastaus K
    if wantAbort.upper() == 'K':
        break  # Poistutaan ikuisesta silmukasta

# LUOKKA HENKILÖTUNNUSTEN KÄSITTELYYN
# ===================================

# KIRJASTOT JA MODUULIT
# ---------------------

# LUOKAT
# ------

# Henklötunnuksen käsittely
class NationalSSN:
    """Various methods to access and validate the Finnish Social Security Number properties
    """
    def __init__(self, ssn: str) -> None:
        """Generate a Finnish SSN object

        Args:
            ssn (str): 11 characters SSN to process
        """
        self.ssn = ssn

        # Lasekemalla selviävät ominaisuudet
        self.dateOfBirth = ''
        self.number = 0
        self.gender = ''
        self.checkSum = ''

    # Luokan metodi eri osien laskentaan ja järkevyystarkistuksiin

    # Tarkistetaan, että HeTu:n pituus on 11 merkkiä
    def checkSsnLengthOK(self) -> bool:
        """Checks correct length of SSN

        Returns:
            bool: True if 11 chr othervise False
        """
        ssnLength = len(self.ssn)
        if ssnLength != 11:
            return False
            # TODO: Mieti pitäisikö generoida virheilmoitus (raise)
        else:
            return True

    # Pilkotaan henkilötunnus osiin
    def splitSsn(self) -> dict:
        """Splits the SSN to functional parts ie. birthdate, century, number and the checksum

        Returns:
            dict: parts as strings
        """
        # Tehdään pilkkominen vain jos pituus on oikein
        if self.checkSsnLengthOK(): # Jos True pilkotaan, huom self.metodinNimi
            dayPart = self.ssn[0:2]
            monthPart = self.ssn[2:4]
            yearPart = self.ssn[4:6]
            centuryPart = self.ssn[6]
            birthNumberPart = self.ssn[7:10]
            checksumPart = self.ssn[10]
            return {'days': dayPart,
                    'month': monthPart,
                    'year': yearPart,
                    'century': centuryPart,
                    'birth': birthNumberPart,
                    'checksum': checksumPart
                    }
        else:
            # TODO: Mieti pitäisikö generoida virheilmoitus (raise)
            return{'status' : 'erro'}

    # Muutetaan syntymäaika osa ja vuosisata päivämääräksi
    def getDateOfBirth(self):
        pass

    # Lasketaan ikä nyt täysinä vuosina
    def calculateAge(self, arg):
        pass

    # Selvitetään vamistussumman avulla onko HeTu syötetty oikein
    def isValidSsn(self, arg):
        pass

# MAIN KOKEILUJA VARTEN (Poista kun ei enään tarvita)
# ===================================================
if __name__ == "__main__":
    hetu1 = NationalSSN('130728-478N')
    print('Oikein muodostettu:', hetu1.checkSsnLengthOK())
    print('HeTun osat ovat: ', hetu1.splitSsn())
# LUOKKA HENKILÖTUNNUSTEN KÄSITTELYYN
# ===================================

# KIRJASTOT JA MODUULIT
# ---------------------

# LUOKAT
# ------

# Henklötunnuksen käsittely
class NationalSSN:
    def __init__(self, ssn: str) -> None:
        self.ssn = ssn

        # Lasekemalla selviävät ominaisuudet
        self.dateOfBith = ''
        self.number = 0
        self.gender = ''
        self.checkSum = ''

    # Luokan metodi eri osien laskentaan ja järkevyystarkistuksiin
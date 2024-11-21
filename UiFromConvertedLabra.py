# LABORATORIOETIKETTISOVELLUKSEN PÄÄIKKUNAN
# LUOMINEN Labra_ui.py TIEDOSTON PERUSTEELLA
# =====================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------
import os # Polkumääritykset
import sys # Käynnistysargumentit

from PySide6 import QtWidgets # Qt-vimpaimet
from Labra_ui import Ui_MainWindow # Käännetyn käyttöliittymän luokka

import identityCheck2 # Henkilötunnuksen tarkistukseen liittyvät työkalut
import barcode # Viivakoodin muodostukseen tarvittavat rutiinit
from avtools import sound # Äänitoiminnot

# Määritellään luokka, joka perii QMainWindow- ja Ui_MainWindow-luokan
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """A class for creating main window for the application"""
    
    # Määritellään olionmuodostin ja kutsutaan yliluokkien muodostimia
    def __init__(self):
        super().__init__()

        # Luodaan käyttöliittymä konvertoidun tiedoston perusteella MainWindow:n ui-ominaisuudeksi. Tämä suojaa lopun MainWindow-olion ylikirjoitukselta, kun ui-tiedostoa päivitetään
        self.ui = Ui_MainWindow()

        # Kutsutaan käyttöliittymän muodostusmetodia setupUi
        self.ui.setupUi(self)
        self.ui.printPushButton.setEnabled(False)

        # OHJELMOIDUT SIGNAALIT
        # ---------------------
        
        # Kun poistutaan ssnLineEdit-elementistä suoritetaan barcodeLabel-elementin päivitys
        self.ui.ssnLineEdit.editingFinished.connect(self.updateBarcodeLabel)

        # Siistitään etunimi- ja sukunimielementit poistuttaessa:
        self.ui.firstNameLineEdit.editingFinished.connect(lambda: self.beautifyElement(self.ui.firstNameLineEdit))
        self.ui.lastNameLineEdit.editingFinished.connect(lambda: self.beautifyElement(self.ui.lastNameLineEdit))
        
        # Aktivoidaan tulostupainike sen jälkeen kun etikettien määrä on valittu
        self.ui.amountSpinBox.valueChanged.connect(self.enablePrintButton)
   
    # OHJELMOIDUT SLOTIT
    # ------------------
    #
    # Viivakoodin muodostus ja barcodeLabel:n päivitys
    def updateBarcodeLabel(self):
        """Updates the barcode label and sets ssnLineEdit to upper case
        """
        # Tarkistetaan, että henkilötunnus on oikein muodostettu
        uiSsn = self.ui.ssnLineEdit.text().upper() # Luetaan käyttöliittymästä henkilötunnus
        ssnToCheck = identityCheck2.NationalSSN(uiSsn) # Luodaan henkilötunnusobjekti
        self.ui.ssnLineEdit.setText(uiSsn) # Päivitetään myös syöttökenttä isoihin kirjaimiin

        # Jos se on oikein, luodaan viivakoodi ja päivitetään tilariviä
        if ssnToCheck.isValidSsn():
            barcode128 = barcode.Code128B(uiSsn) # Luodaan viivakoodi-olio
            barCodeToPrint = barcode128.buildBarcode() # Lisätään alku- ja loppumerkki sekä varmistussumma
            self.ui.barcodeLabel.setText(barCodeToPrint) # Päivitetään käyttöliittymän 
            age = ssnToCheck.calculateAge() # Lasketaan ikä
            ssnToCheck.getGender() # kutsutaan sukupuolen selvitys metodia
            gender = ssnToCheck.gender.lower() # Luetaan ikä-ominaisuuden arvo oliosta
            textToShow = f'Asiakas on {age} vuotias {gender}'
            timeToShow = 10000
            self.updateStatusbar(textToShow)
        # Jos se muodostettu väärin näytetään virheilmoitus MessageBox-ikkunassa
        else:
            self.errorTitle = 'Henkilötunnus virheellinen'
            self.errorText = ssnToCheck.errorMessage
            self.openErrorMsgBox(self.errorTitle, self.errorText)
            self.ui.ssnLineEdit.setFocus() # Palautetaan kursori takaisin elementtiin

    # Yleispätevä elementin siistimismetodi, varsinainen metodi, jota interMediateSlot tai lambda kutsuu
    def beautifyElement(self, element):
        """Beautifies contents of an element

        Args:
            element (QtWidget): The element to be beautified
        """
        elementText = element.text() # Luetaan elementin teksti
        elementText = elementText.strip() # Poistetaan välit alusta ja lopusta
        elementText = elementText.title() # Muutetaan isot alkukirjaimet
        element.setText(elementText) # Päivitetään elementin teksti
    
    # Aktivoidaan tulostuspainike
    def enablePrintButton(self):
        """Enables the print button if all inputs are occupied with values
        """
        if self.ui.ssnLineEdit.text != '' or self.ui.firstNameLineEdit.text != '' or self.ui.lastNameLineEdit != '':
            self.ui.printPushButton.setEnabled(True)


    # Virheilmoitusikkuna
    def openErrorMsgBox(self, errorTitle, errorText):
        """Opens a message box alerting about an error

        Args:
            errorTitle (str): Title of the message box
            errorText (str): What kind of an error has occured
        """
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle(errorTitle)
        msgBox.setText(errorText)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()

    # Tilarivinpäivitysrutiini
    def updateStatusbar(self, textToShow, timeToShow = -1):
        """Updates the statusbar

        Args:
            textToShow (str): A text to show on statusbar
            timeToShow (int, optional): duration of message in ms. Defaults to -1.
        """
        self.ui.statusbar.showMessage(textToShow, timeToShow)
    
if __name__ == "__main__":

    # Luodaan sovellus, jossa on käyttöjärjestelmästä riippumaton ulkonäkö (Fusion)
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')

    # Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
    window = MainWindow()
    window.show()

    # Käynnistetään sovellus ja tapahtumienkäsittelijä
    app.exec()

    
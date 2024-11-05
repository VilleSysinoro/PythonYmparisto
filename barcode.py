# MODUULI VIIVAKOODIEN TUOTTAMISEEN
# =================================

# KIRJASTOT
# ---------

# ASETUKSET
# ---------

# FUNKTIOT
# --------

def barCodeValue(character: str) -> int:
    """Calculates a value of character used in Code128B barcode generation

    Args:
        character (str): a single character to convert

    Returns:
        int: Code128B value for calcultaing the checksum
    """
    asciiValue = ord(character)
    code128BValue = asciiValue - 32
    return code128BValue

def calculateCode128BCheksum(text: str) -> int:
    """Calculates a checksum for a given string

    Args:
        text (str): text string to use in a barcode

    Returns:
        int: Modulo 103 checksum of weighted values
    """
    text = text.strip()
    numberOfLetters = len(text)
    weightedSum = 0
    for number in range(numberOfLetters):
        letter = text[number]
        code128BValue = barCodeValue(letter)
        weightedValue = code128BValue * (number + 1)
        weightedSum = weightedSum + weightedValue
    weightedSum = weightedSum + 104
    code128BChecksum = weightedSum % 103
    return code128BChecksum


def createCode128B(text: str) -> str:
    """Creates a complete code128B barcode to be printed using Libre Code128 font

    Args:
        text (str): The text for a barcode without checksum

    Returns:
        str: String containing start, barcode, checksum and stop symbols
    """
    code128BarcodeString = ''
    startChar = chr(204)
    stopChar = chr(206)
    checkSum = calculateCode128BCheksum(text)
    checkSumSymbol = chr(checkSum + 32)
    code128BarcodeString = startChar + text + checkSumSymbol + stopChar
    return code128BarcodeString
# LUOKKA VIIVAKOODEILLE
# =====================

class Viivakoodi:
    pass

if __name__ == "__main__":
    testString = '128B'
    print('painotetut arvot yhteensä:',calculateCode128BCheksum(testString))
import re
message = input("Please enter the sentence to encode: ").upper()

morseDict = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ' : ''
}


def encryption(message):
    myCipher = " "
    for myLetter in message:
        if myLetter != " ":
            myCipher += morseDict[myLetter] + " "
        else:
            myCipher += " "

     #It seems like due to there is one more space here?
    return myCipher


def decryption(message):
    message += ' '
    decipher = ''
    mycitext = ''
    spaceCounter = 0

    for myLetter in message:
        if myLetter != " ":
            spaceCounter = 0
            mycitext += myLetter
        else:
            spaceCounter += 1
            if spaceCounter == 2:
                decipher += ' '
            else:
                decipher += list(morseDict.keys())[list(morseDict.values()).index(mycitext)]
                mycitext = ''
    return decipher


encryp = encryption(message)
decryp = decryption(encryp)
print(encryp + '\n')
print(decryp)

----after installing all dependencies----

from googletrans import Translator

def translate_english_to_french(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest='fr')


    if text == " ":
        print("Please enter a word")
    else:
        pass

    return translation.text
#translate_english_to_french( )
#from googletrans import Translator

def frenchToEnglish(frenchText):
    translator = Translator()
    translation = translator.translate(frenchText, src='fr', dest='en')
    englishText = translation.text
    return englishText


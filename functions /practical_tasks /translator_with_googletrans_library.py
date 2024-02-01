from googletrans import Translator

def translated_text(text: str, from_language: str, to_language: str):
    translator = Translator()
    message = translator.translate(text, src=from_language, dest=to_language)
    return message.text
    

def main():
    from_language = input("Enter the input language('en', 'fr', 'de', 'es', 'bg'): ")
    to_language = input("Enter the output language('en', 'fr', 'de', 'es', 'bg'): ")
    text = input("Enter text to translate: ")
    translation = translated_text(text, from_language, to_language)
    print(f"\nTranslated text: {translation}")


if __name__ == "__main__":
    main()

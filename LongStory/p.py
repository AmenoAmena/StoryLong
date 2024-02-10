from googletrans import Translator

def translate_text(text, target_language='en'):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

# Example usage
text_to_translate = "sen beni bilemedin yüreğimi göremedin kendini bilemedin yamacıma gelemedim amacına varamadın  her yeri karaladın barışı da aldın"
translated_text = translate_text(text_to_translate, target_language='en')
print(f"Original text: {text_to_translate}")
print(f"Translated text: {translated_text}")

from translate import Translator
word = input("Enter the text:")
lang = input("Enter The Word :")
translator = Translator(to_lang="french")
Translations = translator.translate(lang)
x = word.replace(lang, Translations)
print(x)
from googletrans import Translator
def translate(text,language):
	translator = Translator()
	x=translator.translate(text, dest=language)
	print(x)
translate("Hello","japanese")
from wit import Wit
from googletrans import Translator
import json

access_token="ADRPSCFWVJEDDBCIYEP4ZFLY3EREFPYC"
client = Wit(access_token)
# res=client.message('suggest sad movies')
# # print('res is '+str(res))

def check_intent(obj,key,name):
	if key not in obj[0]:
		return None
	if obj[0][key]==name:
		return 1
	else:
		return 0


def first_value(obj, key):
    if key not in obj:
        return None
    val = obj[key][0]['value']
    if not val:
        return None
    return val

def first_entityvalue(obj, key):
    if key not in obj:
        return None
    val = obj[key][0]['body']
    if not val:
        return None
    return val

def translate(text,language):
	try:

		translator = Translator()
		x=translator.translate(text, dest=language)
		return " '{0}' \n This is how you will say {1} in {2} \n & Pronounciation is '{3}'".format(x.text,text,language,x.pronunciation)

	except Exception as e:
		return "I didnt get destination language."
def handle_message(response):
	print(json.dumps(json.loads(json.dumps(response)),indent=2))
	greeting=first_value(response['traits'], 'wit$greetings')
	typeof=first_value(response['entities'], 'type:type')
	bye=first_value(response['traits'], 'wit$bye')

# translate wala
	checktranslate=check_intent(response['intents'],'name','phrase_translate')
	# print(checktranslate)
	tbody=first_value(response['entities'],'wit$phrase_to_translate:phrase_to_translate')
	tlanguage=first_value(response['entities'],'wit$message_subject:message_subject')
	
	if checktranslate:
		return translate(tbody,tlanguage)
	elif typeof!=None:
		 if typeof.lower()=="movie":
		 	return "Movie you can watch"
	elif bye:
		return "Bye see you later"
	elif greeting:
		return "Hi ask me to translate"
	else:
		return "........oooooo"



client.interactive(handle_message=handle_message)
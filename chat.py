from wit import Wit
from googletrans import Translator
import json

access_token="ADRPSCFWVJEDDBCIYEP4ZFLY3EREFPYC"
client = Wit(access_token)
# res=client.message('suggest sad movies')
# # print('res is '+str(res))

def check_intent(obj,key,name):
	if key not in obj:
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
	translator = Translator()
	x=translator.translate(text, dest=language)
	return "{0} \n This is how you will say {1} in {2} ".format(x.text,text,language)

def handle_message(response):
	print(json.dumps(json.loads(json.dumps(response)),indent=2))
	greeting=first_value(response['traits'], 'wit$greetings')
	typeof=first_value(response['entities'], 'type:type')
	bye=first_value(response['traits'], 'wit$bye')

# translate wala
	checktranslate=check_intent(response['intents'],'name','phrase_translate')
	tbody=first_value(response['entities'],'wit$phrase_to_translate:phrase_to_translate')
	tlanguage=first_value(response['entities'],'wit$message_subject:message_subject')
	
	if greeting:
		return "Hi u can ask me to translate anything "
	elif typeof!=None:
		 if typeof.lower()=="movie":
		 	return "Movie you can watch"
	elif bye:
		return "Bye see you later"
	elif checktranslate:
		return translate(tbody,tlanguage)

	else:
		return "........oooooo"
    # traits = response['traits']
    # get_joke = first_value(traits, 'get_recommendation')
    # greetings = first_value(traits, 'wit$greetings')
    # category = first_value(response['entities'], 'category:category')
    # sentiment = first_value(traits, 'wit$sentiment')

    # if get_joke:
    #     return select_joke(category)
    # elif sentiment:
    #     return 'Glad you liked it.' if sentiment == 'positive' else 'Hmm.'
    # elif greetings:
    #     return 'Hey this is joke bot :)'
    # else:
    #     return 'I can tell jokes! Say "tell me a joke about tech"!'



client.interactive(handle_message=handle_message)
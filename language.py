


import nltk_read


def search_languages():


	lang_counter_en = 0
	lang_counter_ger = 0
	lang_counter_nep = 0
	lang_counter_fr = 0
	lang_counter_indo = 0
	lang_counter_slovene = 0
	lang_counter_azer = 0
	lang_counter_dutch = 0
	lang_counter_italian = 0
	lang_counter_spanish = 0
	lang_counter_romanian = 0
	lang_counter_danish = 0
	lang_counter_portuguese = 0
	lang_counter_rus = 0
	lang_counter_arabic = 0
	selvat_twiitit = 0

	language_list = []
	user_list = []


	tweets = pd.read_csv('scraped_tweets_nosmoking_30.csv')


	hashtags = tweets["hashtags"]
	usernames = tweets["username"]
	
	text = tweets["text"]
	length, width = tweets.shape

	for i in range(0, length):
		try:
			
			if usernames[i] not in user_list:
				user_list.append(usernames[i])
				prob, lang = nltk_read.detect_language(text[i])
				if prob > 55:
					print(text[i])
					print(prob, lang)
				if lang not in language_list:
					language_list.insert(0, lang)

				if lang == 'english' and prob > 55:
					lang_counter_en += 1
					selvat_twiitit += 1
				if lang == 'german' and prob > 55:
					lang_counter_ger += 1
					selvat_twiitit += 1
				if lang == 'nepali' and prob > 55:
					lang_counter_nep += 1
					selvat_twiitit += 1
				if lang == 'french' and prob > 55:
					lang_counter_fr += 1
					selvat_twiitit += 1
				if lang == 'indonesian' and prob > 55:
					lang_counter_indo += 1
					selvat_twiitit += 1
				if lang == 'slovene' and prob > 55:
					lang_counter_slovene += 1
					selvat_twiitit += 1
				if lang == 'azerbaijani' and prob > 55:
					lang_counter_nep += 1
					selvat_twiitit += 1
				if lang == 'dutch' and prob > 55:
					lang_counter_dutch += 1
					selvat_twiitit += 1
				if lang == 'italian' and prob > 55:
					lang_counter_italian += 1
					selvat_twiitit += 1
				if lang == 'spanish' and prob > 55:
					lang_counter_spanish += 1
					selvat_twiitit += 1
				if lang == 'romanian' and prob > 55:
					lang_counter_romanian += 1
					selvat_twiitit += 1
				if lang == 'danish' and prob > 55:
					lang_counter_danish += 1
					selvat_twiitit += 1
				if lang == 'portuguese' and prob > 55:
					lang_counter_portuguese += 1
					selvat_twiitit += 1
				if lang == 'russian' and prob > 55:
					lang_counter_rus += 1
					selvat_twiitit += 1
				if lang == 'arabic' and prob > 55:
					lang_counter_arabic += 1
					selvat_twiitit += 1
			else:
				continue
		except ZeroDivisionError:
			pass



	print("English tweets: ", lang_counter_en)
	print("German tweets: ", lang_counter_ger)
	print("French tweets: ", lang_counter_fr)
	print("Nepalese tweets: ", lang_counter_nep)
	print("Indonesian tweets: ", lang_counter_indo)
	print("Slovenian tweets: ", lang_counter_slovene)
	print("Azerbaijanese tweets: ", lang_counter_azer)
	print("Dutch tweets: ", lang_counter_dutch)
	print("Italian tweets: ", lang_counter_italian)
	print("Spanish tweets: ", lang_counter_spanish)
	print("Romanian tweets: ", lang_counter_romanian)
	print("Danish tweets: ", lang_counter_danish)
	print("Portuguese tweets: ", lang_counter_portuguese)
	print("Russian tweets: ", lang_counter_rus)
	print("Arabic tweets: ", lang_counter_arabic)



	print("kaikkien twiittien määrä, epäselvät twiitit: ", length, (length - selvat_twiitit))

	print("kielilista: ", language_list)


search_languages()
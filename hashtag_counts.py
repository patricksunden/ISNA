import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import nltk_read
import numpy as np

smokefree_f = pd.read_csv('scraped_tweets_smokefree_30.csv')
nosmoking_f = pd.read_csv('scraped_tweets_nosmoking_30.csv')
quitsmoking_f = pd.read_csv('scraped_tweets_quitsmoking_30.csv')
quittingsmoking_f =pd.read_csv('scraped_tweets_quittingsmoking_30.csv')
smokingkills_f = pd.read_csv('scraped_tweets_smokingkills_30.csv')
stopsmoking_f = pd.read_csv('scraped_tweets_stopsmoking_30.csv')
tobaccofree_f = pd.read_csv('scraped_tweets_tobaccofree_30.csv')

smokefree = smokefree_f['hashtags']
nosmoking = nosmoking_f['hashtags']
quitsmoking = quitsmoking_f['hashtags']
quittingsmoking = quittingsmoking_f['hashtags']
smokingkills = smokingkills_f['hashtags']
stopsmoking = stopsmoking_f['hashtags']
tobaccofree = tobaccofree_f['hashtags']

smokefree_r = smokefree_f['retweetcount']
nosmoking_r = nosmoking_f['retweetcount']
quitsmoking_r = quitsmoking_f['retweetcount']
quittingsmoking_r = quittingsmoking_f['retweetcount']
smokingkills_r = smokingkills_f['retweetcount']
stopsmoking_r = stopsmoking_f['retweetcount']
tobaccofree_r = tobaccofree_f['retweetcount']


hashtag_list = []
tweet_counter = 0
all_tweet_counter = 0
quitsmoking_count = 0
nosmoking_count = 0
smokingkills_count = 0
tobaccofree_count = 0
smokefree_count = 0
quittingsmoking_count = 0
stopsmoking_count = 0

def hashtag_counts():
	length, width = quitsmoking_f.shape
	for i in range(0, length):
		if len(quitsmoking[i]) > 2:

			if 'quitsmoking' in quitsmoking[i].lower():
				quitsmoking_count +=1
			all_tweet_counter += 1
			hashtag_list.append(quitsmoking[i].lower())
			

	length, width = nosmoking_f.shape		
	for i in range(0, length):
		if len(nosmoking[i]) > 2:

			if 'nosmoking' in nosmoking[i].lower():
				nosmoking_count +=1
			all_tweet_counter += 1
			hashtag_list.append(nosmoking[i].lower())
		

	length, width = stopsmoking_f.shape
	for i in range(0, length):
		if len(stopsmoking[i]) > 2:

			if 'stopsmoking' in stopsmoking[i].lower():
				stopsmoking_count +=1
			all_tweet_counter += 1
			hashtag_list.append(stopsmoking[i].lower())
		

	length, width = smokefree_f.shape
	for i in range(0, length):
		if len(smokefree[i]) > 2:

			all_tweet_counter += 1
			if 'smokefree' in smokefree[i].lower():
				smokefree_count +=1
			hashtag_list.append(smokefree[i].lower())
		

	length, width = smokingkills_f.shape
	for i in range(0, length):
		if len(smokingkills[i]) > 2:

			if 'smokingkills' in smokingkills[i].lower():
				smokingkills_count +=1
			all_tweet_counter += 1
			hashtag_list.append(smokingkills[i].lower())
			

	length, width = quittingsmoking_f.shape
	for i in range(0, length):
		if len(quittingsmoking[i]) > 2:

			if 'quittingsmoking' in quittingsmoking[i].lower():
				quittingsmoking_count +=1
			all_tweet_counter += 1
			hashtag_list.append(quittingsmoking[i].lower())
		

	length, width = tobaccofree_f.shape
	for i in range(0, length):
		if len(tobaccofree[i]) > 2:

			if 'tobaccofree' in tobaccofree[i].lower():
				tobaccofree_count +=1
			all_tweet_counter += 1
			hashtag_list.append(tobaccofree[i].lower())

	print(hashtag_list)
	print(all_tweet_counter)
	length = len(hashtag_list)
		
	smokefree_count_list = 0
	nosmoking_count_list = 0
	quitsmoking_count_list = 0
	quittingsmoking_count_list = 0
	smokingkills_count_list = 0
	stopsmoking_count_list = 0
	tobaccofree_count_list = 0


	for i in range(0, length):

		if 'smokefree' in hashtag_list[i]:
			smokefree_count_list +=1
		if 'nosmoking' in hashtag_list[i]:
			nosmoking_count_list +=1
		if 'quitsmoking' in hashtag_list[i]:
			quitsmoking_count_list +=1
		if 'quittingsmoking' in hashtag_list[i]:
			quittingsmoking_count_list +=1
		if 'smokingkills' in hashtag_list[i]:
			smokingkills_count_list +=1
		if 'stopsmoking' in hashtag_list[i]:
			stopsmoking_count_list +=1
		if 'tobaccofree' in hashtag_list[i]:
			tobaccofree_count_list +=1


	# This is the amount of hashtags found from their own excels, for example the print smokefree line prints
	# how many smokefree-hashtags have been used in smokefree-excel.


	print("smokefree_count", smokefree_count)
	print("nosmoking_count", nosmoking_count)
	print("quitsmoking_count", quitsmoking_count)
	print("quittingsmoking_count", quittingsmoking_count)
	print("smokingkills_count", smokingkills_count)
	print("stopsmoking_count", stopsmoking_count)
	print("tobaccofree_count", tobaccofree_count)

	# This is the amount of hashtags found from all excels alltogether, for example in previous print it only collected smokefree
	# hashtags from smokefree excel, but here it collects smokefree hashtags from all excels.


	print("smokefree_count", smokefree_count_list)
	print("nosmoking_count", nosmoking_count_list)
	print("quitsmoking_count", quitsmoking_count_list)
	print("quittingsmoking_count", quittingsmoking_count_list)
	print("smokingkills_count", smokingkills_count_list)
	print("stopsmoking_count", stopsmoking_count_list)
	print("tobaccofree_count", tobaccofree_count_list)

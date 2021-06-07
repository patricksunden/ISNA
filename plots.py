
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import nltk_read


#THE DATA FOR THESE CHARTS IS HARDCODED

def location_of_users_chart():
	y = [0, 1]
	x = [1595, 598]


	fig, ax = plt.subplots()
	p1 = ax.bar(y, x)
	ax.set_title('Information about location of twitter users')
	ax.set_xticks(y)
	ax.set_xticklabels(['location', 'no location'])
	ax.set_ylabel('Nr of users')

	ax.legend()
	ax.bar_label(p1, label_type = 'center')
	plt.show()


def language_of_tweet_chart():


	labels = 'english', 'german', 'french' , 'nepali', 'indonesian', 'slovenian', 'dutch', 'italian', 'spanish', 'romanian', 'portuguese', 'russian', 'arabic'
	sizes = [1913, 17, 12, 19, 8, 3, 2, 21, 11, 6, 4, 1, 1]
	fig, ax = plt.subplots()
	ax.pie(sizes, labels = labels, autopct = '%1.1f%%')
	ax.axis('equal')

	labels =  'german', 'french' , 'nepali', 'indonesian', 'slovenian', 'dutch', 'italian', 'spanish', 'romanian', 'portuguese', 'russian', 'arabic'
	sizes = [17, 12, 19, 8, 3, 2, 21, 11, 6, 4, 1, 1]
	fig, ax = plt.subplots()
	ax.pie(sizes, labels = labels, autopct = '%1.1f%%')
	ax.axis('equal')

	plt.show()
	
language_of_tweet_chart()

def hashtag_plot():
	y = [0, 1, 2, 3, 4, 5, 6]
	x = [367, 340, 708, 56, 272, 373, 100]

	fig, ax = plt.subplots()
	p1 = ax.bar(y, x, 0.6)

	ax.set_ylabel('NR of hashtags', fontsize = 15)
	ax.set_title('Hashtags related to smoking cessation in 1169 tweets', fontsize = 18)
	ax.set_xticklabels(('smokefree', 'smokefree', 'nosmoking', 'quitsmoking', 'quittingsmoking', 'smokingkills', 'stopsmoking', 'tobaccofree'), fontsize = 18)
	plt.show()

def barplot():
	y = [0, 1, 2, 3, 4, 5, 6]
	x = [214, 160, 256, 20, 119, 149, 42]

	fig, ax = plt.subplots()
	p1 = ax.bar(y, x, 0.8)

	ax.set_ylabel('Twitter users')
	ax.set_title('Distinct twitter users per individual hashtag')
	ax.set_xticklabels(('smokefree' ,'smokefree', 'nosmoking', 'quitsmoking', 'quittingsmoking', 'smokingkills', 'stopsmoking', 'tobaccofree'))
	plt.show()


def botplot():
	#nosmoking, quitsmoking, stopsmoking, smokefree, smokingkills, quittingsmoking, tobaccofree
	bots = [211, 161, 170, 197, 120]  # bot accounts
	notbots = [23, 18, 22, 37, 1]  #human accounts
			        #[9, 12, 11, 14, 9, 341, 6, 5, 9, 20] # accounts skipped

	bots1 = [382, 61, 58, 57, 244]
	notbots1 =  [40, 5, 9, 6, 44]
	labels = ['quitsmoking', 'nosmoking', 'stopsmoking', 'smokefree', 'smokingkills']
	labels1 = ['smoking', 'vape', 'tobaccofree', 'vaping', 'smoke']
	x = np.arange(len(labels))
	width = 0.3  # the width of the bars

	fig, ax = plt.subplots()
	rect1 = ax.bar(x - width/2, bots, width, label = 'bot account')
	rect2 = ax.bar(x + width/2, notbots, width, label = 'human account')
	ax.set_ylabel('Nr of accounts', fontsize = 16)
	ax.set_title('Bots vs human accounts - top 5 hashtags', fontsize = 16)
	ax.set_xticks(x)
	ax.set_xticklabels(labels, fontsize = 15)
	ax.legend()
	ax.bar_label(rect1, padding=3)
	ax.bar_label(rect2, padding=3)

	fig.tight_layout()

	plt.show()

location_of_users_chart()
language_of_tweet_chart()
hashtag_plot()
barplot()
botplot()
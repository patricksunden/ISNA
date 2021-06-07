




#Prints the usernames of the users who have used the wanted hashtag
def userlist(str_hash):

	user_list = []

	
	length = len(quitsmoking)
	for i in range(0, length):
		if str_hash in quitsmoking[i].lower():
			user_list.append((quitsmoking_f["username"][i]))
	

	length = len(nosmoking)
	for i in range(0, length):
		if str_hash in nosmoking[i].lower():
			user_list.append((nosmoking_f["username"][i]))
	

	length = len(stopsmoking)
	for i in range(0, length):
		if str_hash in stopsmoking[i].lower():
			user_list.append((stopsmoking_f["username"][i]))
	
	
	length = len(smokefree)
	for i in range(0, length):
		if str_hash in smokefree[i].lower():
			user_list.append((smokefree_f["username"][i]))
			
	
	length = len(smokingkills)
	for i in range(0, length):
		if str_hash in smokingkills[i].lower():
			user_list.append((smokingkills_f["username"][i]))
	

	length = len(quittingsmoking)
	for i in range(0, length):
		if str_hash in quittingsmoking[i].lower():
			user_list.append((quittingsmoking_f["username"][i]))
	
	
	length = len(tobaccofree)
	for i in range(0, length):
		if str_hash in tobaccofree[i].lower():
			user_list.append((tobaccofree_f["username"][i]))


	print("length of user_list before removing duplicates: ", len(user_list))

	user_list = list(dict.fromkeys(user_list))	
	
	print("length of user_list after removing duplicates: ", len(user_list))
	
	#print(user_list)
	return user_list
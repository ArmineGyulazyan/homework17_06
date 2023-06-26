import string

def word_frequency_count(str_check):

	''' This function takes a string as an argument, clears all the 
	punctuation marks, makes it lowercase, splits into a list and calculates
	the frequences of all the words '''

	str_check = str_check.translate(str.maketrans('','',string.punctuation))
	str_lowCase = str_check.lower()	
	str_list = str_lowCase.split()	
	word_count = {}
	for i in str_list:
		if word_count.get(i) is None:
			word_count[i] = 1
		else:
			word_count[i] = word_count.get(i)+1
	
	for i in word_count:
		print(i,":",word_count[i])

str_input = input("Enter the sentence: ")
word_frequency_count(str_input)

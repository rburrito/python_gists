#!/usr/bin/env python3

import sys

def decode_message(character, modby):
	if not character.isalpha():
		return character
	ascii_enc=ord(character) 
	letter=ascii_enc-ord('a') #to find the position in the alphabet
	output_letter=letter-modby #subtracting modby to depending on which index it is
	output_letter=output_letter%26 #loops around if we exceed the alphabet
	new_character=chr(output_letter+ord('a')) #converting back to ASCII value
#	will only work with less than 26 indexes
#	if ascii_enc-modby >= 97:
#		new_character=chr(ascii_enc-modby)
#	else:
#		new_character=chr(ascii_enc-modby+26)
	return new_character

def split_word(word, index):
	decoded_word=""
	for char in word:
		decoded_word+=decode_message(char, index)
	return decoded_word

def split_line(sentence):
	sentence=sentence.split(' ')
	index=0
	new_sentence=[]
	for word in sentence:
		if index==0:
			new_sentence.append(word)
		else:
			new_word=split_word(word, index)
			new_sentence.append(new_word)
		index+=1
	return ' '.join(new_sentence)


def display_content(filename):
	f=open(filename, 'r')
	content=f.readlines()
	for line in content:
		line=line.rstrip()
		print(split_line(line))

def main():
	display_content(sys.argv[1])

if __name__=="__main__":
	main()

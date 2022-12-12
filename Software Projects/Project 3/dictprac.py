# Kahan Shah 
# Assignment 6.1 Dictionary Practice
# This program  has three fuction one that compares two dictionaries another that counts the number of words and the frequency of the words as well the last one converts a sentence into morse code.
# Acknowledgments: https://www.w3schools.com/python/python_dictionaries.asp, https://docs.python.org/3/tutorial/datastructures.html, https://www.geeksforgeeks.org/python-dictionary/, and my roommate Arin Gadre for helping me figure out what syntax I forgot in the count words function.

def dict_equal(dict1, dict2):
    # checking to see if the number of keys should be same
    if len(dict1)!=len(dict2):
        return False
    for i in dict1:
        # same key should be there in both dictionaries
        if i not in dict2:
            return False
        if dict1[i]!=dict2[i]:#value should be same
            return False
    return True

def count_words(sentence):
    #split by space
    words=sentence.split()
    freq={}
    for word in words:
        word=word.strip(", .")
        freq[word.lower()]=freq.get(word.lower(),0)+1
    return freq

def morse(sentence):
    MORSE_DICT = { 'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.',
                       'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-','L':'.-..', 'M':'--', 'N':'-.',
                       'O':'---', 'P':'.--.', 'Q':'--.-','R':'.-.', 'S':'...', 'T':'-',
                       'U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..'}
    words=[]
    word=[]
    for i in sentence:
        #if we encounter a space, it means the old word is completed
        if i==" ":
            #add it to words, joining by a space
            words.append(" ".join(word))
            #empty the list for new word
            word=[]
        else:
            #otherwise add the morse letter
            word.append(MORSE_DICT[i.upper()])
        #add the last word in sentence  
    if word:
        words.append(" ".join(word))
    #join the words by  / and return the sentence
    return " / ".join(words)

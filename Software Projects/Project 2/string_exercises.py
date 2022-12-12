# Kahan Shah
# The assigment is Assignment 5.2: String Exercises 
# string_exercises.py
# This program performs a variety of string fuctions
# Acknowledgements : https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/#:~:text=In%20Python%2C%20upper()%20is,it%20returns%20the%20original%20string.
# https://www.kite.com/python/answers/how-to-replace-characters-in-a-string-in-python, https://www.geeksforgeeks.org/python-program-to-print-even-length-words-in-a-string/#:~:text=Approach%3A%20Split%20the%20string%20using,even%2C%20then%20print%20the%20word.


# This fuction censors the word the user chooses
def censor(message,word):
    # Storing the length of the word to be censored and the number of stars for the censored word
    n=len(word) 
    star='*'*n 
    # Replacing censored word with the stars
    res=message.replace(word,star) 
    # returning the result
    return res 

# This function takes user input for the fuction censor
def run_censor():
    x = input("Write the message ")
    y = input("Write the word you want to censor ")
    print(censor(x,y))

# This fuction fixes the title of books movies and articles.
def fix_title(input_str):
    # Convert the input string to lower case and split to type and title
    input_str=input_str.lower() 
    type,title=input_str.split(":") 
    # If type is trash return the title which is already in lower case
    if(type=="trash"):  
        return title # 
    #If type is article convertithe title to upper case and return that 
    elif(type=="article"): 
        return title.upper() 
    else: 
        # If type is book split the title string into words and capitalize the first letter of each words 
        l=title.split(" ")  
        for i in range(len(l)): 
            l[i]=l[i].capitalize()
        # Joining all the words into a sentence and returning it
        return(" ".join(l)) 
# This fuction takes user input for the fix title fuction
def run_fix_title():
    str1 = input("What is the incorrectly formatted title ")
    print(fix_title(str1))

def get_longest_word(sentence):
    # Split the sentence into words 
    words=sentence.split(" ") 
    wrd=""
    for word in words: 
        # Checking for the longest length word
        if(len(word)>len(wrd)): 
            wrd=word 
    # Returning the word with longest length
    return wrd 
# This function takes input for the longest word
def run_get_longest_word():
    x = input("Write a sentence to find the longest word in it ")
    print(get_longest_word(x))

# This function puts a frame around the users message
def frame(sentence):
# Splitting the sentence into words and storing them in a list
    words=sentence.split(" ") # Splitting the sentence into words and storing them in a list
    n = 0 
# Iterating through all the words in the sentence  
    for word in words: 
        n=max(n,len(word)) 
    # creating the output string
    res="*"*(n+2)+"\n" 
    # Iterating through all the words in the sentence to find the lenght of the words
    for word in words:  
        l=len(word) 
        res=res+"*"+word+(n-l)*" "+"*"+"\n" 
    res=res+"*"*(n+2)
    return res 
# This function takes user input for the message
def run_frame():
    x = input("Enter a series a words spearate by a space and they will be framed ")
    print(frame(x))

# This runs the fuctions and allows the user to pick one
def main():
    # Show the options the user has
    print("Type 1 for censor ")
    print("Type 2 for  fix title ")
    print("Type 3 for get longest word ")
    print("Type 4 for fram")
    # Ask for operation option
    op1  = int(input(" What operation would you like to do "))
    # This directs the user to each function
    if op1 == 1:
        run_censor()
    if op1 == 2:
        run_fix_title()
    if op1 == 3:
        run_get_longest_word()
    if op1 == 4:
        run_frame()

    

# Run the main fuction
main()


#Create a program that asks the user to input a sentence, and display:
# 1 Count total words in the sentence.
# 2 Find the longest word in the sentence.
# 3 Display the sentence in uppercase.
# 4 Display the sentence in lowercase.
# 5 Display the sentence in Title Case (first letter of each word capitalized).
# 6 Display the sentence in reverse order.
# Student Name: Prashant Rijal
# Student Id: 397152
# Assignment: 1 
# Group: DAN/EXT 14

# Here, Def tells the python that we are defining a function called sentence_analysis that takes one parameter called sentence. 
def sentence_analysis(sentence):
    
    while True:
    # Here, this line prompts the user to enter a sentence and stores it in the variable text.
     text = input ("Please Enter a sentence: ") 
    
    # Here, this line checks if the input text is empty or contains only whitespace characters.
     if not text.strip(): 
         break
     else:
         print("Please enter a valid sentence.")
        
        # If the input is empty, this line prints a message indicating that no sentence was entered.
       # print("No sentence was entered.") 
       # return # This line exits the function early if no sentence was entered.
    
    # This line splits the input text into a list of words using whitespace as the delimiter and stores it in the variable words.
    words = text.split() 
    
    total_words = len(words) # This line calculates the total number of words in the list   
    
    # This line finds the longest word in the list of words using the max function with the key parameter set to len, which returns the length of each word.
    if words:
        longest_word = max(words, key=len)
        longest_word_len=len(longest_word)
    else:
        longest_word = "None"
        longest_word_len=0
    
    print(f"Total words: {total_words}") # This line prints the total number of words in the sentence.
    print(f"Longest word: {longest_word} ({len(longest_word)} Letters)") # This line prints the longest word along with its length in letters.
    print(f"Uppercase: {text.upper()}") # This line prints the sentence in uppercase using the upper() method.
    print(f"Lowercase: {text.lower()}") # This line prints the sentence in lowercase using the lower() method.
    print(f"Title Case: {text.title()}") # This line prints the sentence in title case using the title() method.    
    print(f"Reversed:{text[::-1]}") # This line prints the sentence in reverse order using slicing with a step of -1.

# This line checks if the script is being run directly (not imported as a module).
if __name__ == "__main__": 
    # If the script is run directly, this line calls the sentence_analysis function with an empty string as an argument.
        sentence_analysis("") 